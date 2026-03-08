# /init - Initialize Project Context for Cursor

Execute the following steps in order:

1. **Analyze current workspace**
   - Read `package.json` (or equivalent for non-JS projects)
   - Read `README.md` if exists
   - Scan project structure (src/, lib/, app/, etc.)
   - Identify tech stack, frameworks, build tools

2. **Create project rule file**
   - Create `.cursor/rules/` directory in workspace root if not exists
   - Create `.cursor/rules/project-context.mdc` with content similar to CLAUDE.md

3. **project-context.mdc structure (required)**
   - YAML frontmatter: `description: "Project context"`, `alwaysApply: true`
   - Project Overview (brief description)
   - Tech Stack (frameworks, languages, key libraries)
   - Development Commands (npm/yarn scripts, run instructions)
   - Node/Runtime version if applicable
   - Directory Structure (main folders and purpose)
   - Architecture notes (entry point, routing, state management)
   - Build/Deploy notes if relevant
   - Code style or conventions if discoverable

4. **Output**
   - Confirm the file was created
   - Summarize what context was captured

Do not ask for confirmation. Create the file directly. Use English for comments in the generated content.
