#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path
from typing import Optional, Tuple

try:
    from PIL import Image, ImageChops, ImageEnhance, ImageStat
except ImportError:
    print(
        "Pillow is required. Install it with: python3 -m pip install Pillow",
        file=sys.stderr,
    )
    raise SystemExit(2)


CropBox = Tuple[int, int, int, int]


def parse_crop(value: str) -> CropBox:
    try:
        x, y, width, height = (int(part) for part in value.split(","))
    except (TypeError, ValueError):
        raise argparse.ArgumentTypeError("crop must use x,y,width,height") from None

    if min(x, y) < 0 or width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError(
            "crop coordinates must be non-negative and dimensions positive"
        )

    return x, y, x + width, y + height


def load_image(path: Path, crop: Optional[CropBox]) -> Image.Image:
    if not path.is_file():
        raise ValueError(f"image does not exist: {path}")

    with Image.open(path) as source:
        image = source.convert("RGB")

    if crop is None:
        return image

    left, top, right, bottom = crop
    if right > image.width or bottom > image.height:
        raise ValueError(
            f"crop {crop} exceeds image size {image.width}x{image.height}: {path}"
        )

    return image.crop(crop)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare two rendered UI images and emit measurable differences."
    )
    parser.add_argument("expected", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--output", type=Path, help="Path for an amplified diff image")
    parser.add_argument(
        "--crop",
        type=parse_crop,
        help="Compare the same x,y,width,height region in both images",
    )
    parser.add_argument(
        "--channel-threshold",
        type=int,
        default=0,
        help="Count a pixel when any RGB channel exceeds this 0-255 difference",
    )
    parser.add_argument(
        "--max-diff-ratio",
        type=float,
        help="Fail when the different-pixel ratio exceeds this 0-1 value",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    if not 0 <= args.channel_threshold <= 255:
        print("--channel-threshold must be between 0 and 255", file=sys.stderr)
        return 2
    if args.max_diff_ratio is not None and not 0 <= args.max_diff_ratio <= 1:
        print("--max-diff-ratio must be between 0 and 1", file=sys.stderr)
        return 2

    try:
        expected = load_image(args.expected, args.crop)
        actual = load_image(args.actual, args.crop)
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 2

    if expected.size != actual.size:
        print(
            (
                "image sizes differ: "
                f"expected={expected.width}x{expected.height}, "
                f"actual={actual.width}x{actual.height}"
            ),
            file=sys.stderr,
        )
        return 2

    difference = ImageChops.difference(expected, actual)
    pixels = difference.getdata()
    different_pixels = sum(
        1 for red, green, blue in pixels if max(red, green, blue) > args.channel_threshold
    )
    total_pixels = expected.width * expected.height
    diff_ratio = different_pixels / total_pixels if total_pixels else 0.0
    channel_mean = ImageStat.Stat(difference).mean

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        ImageEnhance.Contrast(difference).enhance(4).save(args.output)

    result = {
        "expected": str(args.expected),
        "actual": str(args.actual),
        "size": {"width": expected.width, "height": expected.height},
        "crop": args.crop,
        "channelThreshold": args.channel_threshold,
        "differentPixels": different_pixels,
        "totalPixels": total_pixels,
        "diffRatio": round(diff_ratio, 8),
        "meanAbsoluteChannelDifference": {
            "red": round(channel_mean[0], 4),
            "green": round(channel_mean[1], 4),
            "blue": round(channel_mean[2], 4),
        },
        "differenceBounds": difference.getbbox(),
        "diffImage": str(args.output) if args.output else None,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

    if args.max_diff_ratio is not None and diff_ratio > args.max_diff_ratio:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
