import { type JSX } from "react";
import { type SequenceProps } from "./sequence-layout.js";
export type { SequenceActor, SequenceMessage, SequenceNote, SequenceProps, SequenceRow, } from "./sequence-layout.js";
/**
 * A sequence diagram: actors as columns, each a header box over a dashed
 * lifeline, and messages as rows down them, top to bottom. A message is a
 * solid arrow in the first data color; a `reply` is a dashed arrow in the
 * gray `other`; a message from an actor to itself loops out to the right
 * and back, its label beside the loop. Labels sit above their arrows in the
 * small neutral type, wrapping to two lines between the lifelines. A `note`
 * row is a tinted box over one actor or across them all. Draws its own
 * chart card.
 *
 * The columns share the block's width; on a block too narrow for every
 * column at its least width, the diagram keeps that width and scrolls
 * sideways, fading at the edge with more beyond it, as a `Diagram` does.
 * It is never scaled down.
 *
 * @example
 * ```tsx
 * <Sequence
 *   actors={[{ id: "app", label: "App" }, { id: "api", label: "API" }]}
 *   messages={[
 *     { from: "app", to: "api", label: "GET /orders" },
 *     { from: "api", to: "api", label: "check token" },
 *     { from: "api", to: "app", label: "200 OK", reply: true },
 *   ]}
 * />
 * ```
 */
export declare function Sequence(props: SequenceProps): JSX.Element | null;
