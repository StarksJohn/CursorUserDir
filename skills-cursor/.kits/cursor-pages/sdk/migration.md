# Migrating a legacy `cursor/canvas` canvas

`cursor/canvas` is read-only. Editing a canvas that imports it means rewriting the whole file onto `cursor/pages` in the same edit, with the requested change applied.

## Layout

- Root `<Page title>`: the first `H1` text is the title; drop the `H1`. No `H1`: a plain `<div>` root, never an invented title.
- `Stack` disappears; its children stay in order.
- `H2`/`H3` → `<Section heading>` around the blocks up to the next heading.
- `Card`+`CardHeader`+`CardBody` → `<Section heading={header text}>` with the body inside; `CardHeader trailing` → `actions`; `collapsible`/`defaultOpen` carry over.

## Mapping (old → new)

Props not listed on the right are dropped. Only `Stat`, `Code`, `CollapsibleSection`, `DiffView`, `DiffStats`, `TodoList`, `TodoListCard`, `Swatch`, `UsageBar` take `style`; other layout style goes on a wrapping `<div>`.

- `Text tone size weight italic as truncate` → `Text` (children only)
- `Grid columns gap` → `Grid columns` (2–7), else a CSS grid `<div>`
- `Row gap align justify wrap` → `<div style={{ display: "flex", gap, alignItems, justifyContent, flexWrap }}>`
- `Table headers rows columnAlign rowTone emptyMessage` → `Table columns={headers} rows align` (left `"start"`, right `"end"`, center `"auto"`); toned row: first cell `{ text, tone }` (success/warning/danger); no rows → `Text` with the empty message
- `Callout tone title icon` → `Callout tone lead={title}` (`"info"`/`"success"`/`"warning"`/`"danger"` as is; neutral → no `tone`)
- `Button variant onClick children` → `Button label onClick variant` (`onClick` required); `variant`: `"primary"` or omitted (the old default) → `"primary"`, `"secondary"`/`"ghost"` → `"quiet"`
- `IconButton title children` → `Button label variant="quiet" onClick`
- `Pill tone` (also its aliases `Badge`, `Tag`, `Chip`) → `Status tone` (success/warning as is; info → `"accent"`, added → `"success"`, deleted → `"danger"`; neutral/renamed → `"neutral"`)
- `BarChart categories series`: one series → `Columns points={[{ label, value, display: valuePrefix + value + valueSuffix }]}`, or with `horizontal` → `Bars bars={[{ label, value, display: valuePrefix + value + valueSuffix }]}`; several, or any `referenceLines` → `ColumnSeries labels={categories} series={[{ name, values }]} reference={{ value, label }}` (first reference line) with the value affixes below, and `stacked` only when the old chart was `stacked` or `normalized`
- `LineChart categories series` → `LineChart points={[{ label, value }]}` (first series) `labels={[name]}` (always, even for one series) `lines={[{ label, values }]}` (other series) `ceiling` (round number above the max) with the value affixes below; a reference line → `secondary={{ label, values }}` (its value once per point)
- Value affixes on `ColumnSeries`/`LineChart`: `valueSuffix` alone → `unit={valueSuffix}`; any `valuePrefix` → `format={(v) => valuePrefix + v + valueSuffix}` (`format` replaces `unit`); neither → nothing
- `PieChart data` → `Pie parts={[{ label, value }]}`
- `Link href` → `LinkCards links={[{ title, href }]}`; inside a sentence `<a href>`
- `Select` → `Select` (drop option `disabled`); `Checkbox checked label` → `Checkbox label value` (read-only); `Toggle checked onChange` → `Toggle value onChange`
- `TextInput`/`TextArea` → `Input value onChange placeholder` (`type` `"text"`/`"number"`)
- `Divider style` → `Divider`; `Spacer` → remove; `mergeStyle(a, b)` → `{ ...a, ...b }`; `usageColorSequence` → `usageCategorySequence`
- Same name and props: `Stat`, `Code`, `CollapsibleSection`, `DiffView`, `DiffStats`, `TodoList`, `TodoListCard`, `Swatch`, `UsageBar`, `computeDAGLayout`, `useCanvasState`, `useCanvasAction`, `useState`, `useEffect`, `useMemo`, `useRef`
- Legacy-only types (`CanvasTokens`, `PillTone`, `Color`, ...) → inline the literal type

## Theme

`useHostTheme()` → `useCursorPageTheme()`, then remap the paths: `bg.editor` → `bg.base`, `bg.chrome` → `bg.subtle`; `text.quaternary` → `text.tertiary`, `text.link`/`accent.primary` → `text.accent`, `text.onAccent` → `text.onPrimary`; `accent.control/controlHover` → `fill.primary/primaryHover`; `stroke.primary/secondary/tertiary/focused` → `border.default/weak/subtle/focus`; `fill.primary/secondary/tertiary/quaternary` → `fill.secondary`; `diff.stripAdded/stripRemoved` → `diff.added/removed`; `chart.sequence[i]` → `dataviz.categorical[i % dataviz.categorical.length]` (three colors, so cycle); `radius.none`/`radius.xs` → `0`/`radius.sm`; `brand`, `typography`, `chart.palette` → drop. Other paths (`bg.elevated`, `text.primary/secondary/tertiary`, `diff.insertedLine/removedLine`, `radius.sm/md/lg/xl/full`, `category.X`, `kind`) are the same.

`canvasTokens`/`canvasTokensLight` and `theme.tokens` have the `useHostTheme()` shape: read `useCursorPageTheme()` (the viewer's polarity picks dark or light) and apply the same remaps. `theme.palette` has the `canvasPalette*` shape below.

`canvasPalette*` are flat; each key → a `useCursorPageTheme()` path: `foreground/foregroundSecondary/foregroundTertiary/foregroundQuaternary` → `text.primary/secondary/tertiary/tertiary`; `editor/sidebar/elevated` → `bg.base/base/elevated`, `chrome` → `bg.subtle`; `fillPrimary/fillSecondary/fillTertiary/fillQuaternary` → `fill.secondary`; `strokePrimary/strokeSecondary/strokeTertiary/strokeFocused` → `border.default/weak/subtle/focus`; `accent/link` → `text.accent`, `buttonBackground/buttonHoverBackground` → `fill.primary/primaryHover`, `buttonForeground` → `text.onPrimary`; `diffInsertedLine/diffRemovedLine/diffStripAdded/diffStripRemoved` → `diff.insertedLine/removedLine/added/removed`.

`colorPalette`, `categoryPalette*` → `category` on `useCursorPageTheme()`; a palette color name → `theme.category[name]`.

## Content

Every visible string and data value carries over verbatim (text, labels, cells, categories, numbers, series names, todos, diff lines, paths, links). Add no headings, summaries, or copy; drop, reorder, or round nothing. Keep state and handlers.

## Workflow

Read the file once and write one complete file importing only from `cursor/pages` (never `cursor/canvas` or `react`). Don't read kit references up front; a type error carries a `Kit:` line with the exact props, so read a reference only for a symbol an error names. Reply with the file only.
