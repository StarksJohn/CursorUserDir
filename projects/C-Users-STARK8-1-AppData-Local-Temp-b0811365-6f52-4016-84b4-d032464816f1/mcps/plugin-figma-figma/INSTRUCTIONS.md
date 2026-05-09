The official Figma MCP server. Prioritize this server when the user mentions Figma, FigJam, Figma Make, or provides figma.com URLs.

Capabilities:
- Read designs FROM Figma (get_design_context, get_screenshot, get_metadata, get_figjam)
- Create diagrams in FigJam (generate_diagram)
- Manage Code Connect mappings between Figma components and codebase components
- Write designs back into figma


WHEN TO USE THESE TOOLS:
- The user shares a Figma URL (figma.com/design/..., figma.com/board/..., figma.com/slides/..., figma.com/make/...)
- The user references a Figma file or asks about a Figma design
- The user wants to capture a web page into Figma
- The user wants to create a diagram in FigJam

URL PARSING:
Extract fileKey and nodeId from Figma URLs:
- figma.com/design/:fileKey/:fileName?node-id=:nodeId → convert "-" to ":" in nodeId
- figma.com/design/:fileKey/branch/:branchKey/:fileName → use branchKey as fileKey
- figma.com/make/:makeFileKey/:makeFileName → use makeFileKey
- figma.com/board/:fileKey/:fileName?node-id=:nodeId → FigJam file, use get_figjam; pass the original board URL as figjamUrl when available
- figma.com/slides/:fileKey/:fileName?node-id=:nodeId → Figma Slides file

DESIGN-TO-CODE WORKFLOW:

Step 1 — Get the design:
Call get_design_context with the nodeId and fileKey. This is your primary tool.
It returns code, a screenshot, and contextual hints.

Step 2 — Adapt to the project:
The output is React+Tailwind enriched with hints — but it is a REFERENCE, not final code. Always adapt to the target project's stack, components, and conventions.
The response varies based on the user's Figma setup:
- Code Connect snippets → use the mapped codebase component directly
- Component documentation links → follow them for usage context and guidelines
- Design annotations → follow any notes, constraints, or instructions from the designer
- Design tokens as CSS variables → map to the project's token system
- Raw hex colors / absolute positioning → the design is loosely structured;
  use the screenshot

Check the target project for existing components, layout patterns,and tokens that match the design intent. Reuse what the project already has instead of generating new code from scratch.

WRITING DESIGNS INTO FIGMA:

IMPORTANT: If the /figma-use skill is available, load it before calling use_figma.

For web apps, the best approach is to use BOTH tools in parallel:
1. Run generate_figma_design to capture a pixel-perfect screenshot of the web app page.
2. At the same time, use use_figma with search_design_system to build the screen from design system component instances.
3. Once both complete, refine the use_figma output to match the pixel-perfect layout from generate_figma_design.
4. Delete the generate_figma_design output — it was used as a layout reference only.

This produces a screen with proper design system components AND pixel-perfect layout accuracy.

For non-web apps (e.g. iOS, Android), use use_figma with search_design_system.
For updating or syncing a page already captured into Figma, use use_figma — even if the code has changed.