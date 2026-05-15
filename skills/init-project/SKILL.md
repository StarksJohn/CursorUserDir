---
name: init-project
description: >-
  Cursor: initialize or refresh a repository's project context by analyzing the
  current workspace and writing .cursor/rules/project-context.mdc. Use when
  opening a new project, after major structure changes, or when the user invokes
  /init-project. Codex counterpart: /initProject.
---

# init-project（Cursor 项目上下文初始化）

## Cursor 侧说明

- **路径（本文件，Cursor Agent Skill）**：**Windows** `%USERPROFILE%\.cursor\skills\init-project\SKILL.md`（本机示例：`C:\Users\Stark8964911\.cursor\skills\init-project\SKILL.md`）；**macOS** `/Users/<你的用户名>/.cursor/skills/init-project/SKILL.md`（本机示例：`/Users/stark/.cursor/skills/init-project/SKILL.md`）。
- **对照（Codex）**：**Windows** `%USERPROFILE%\.codex\skills\initProject\SKILL.md`（本机示例：`C:\Users\Stark8964911\.codex\skills\initProject\SKILL.md`）；**macOS** `/Users/<你的用户名>/.codex/skills/initProject/SKILL.md`（本机示例：`/Users/stark/.codex/skills/initProject/SKILL.md`，`name: initProject`，口令 `/initProject`）。
- **执行等价**：在 Cursor 输入框执行 **`/init-project`**，应与在 Cursor 的 Codex 插件输入框发送 **`/initProject`** 达到同一结果：读取同一类项目锚点文件，按同一顺序分析工作区，并创建或刷新同一份 `{workspace}/.cursor/rules/project-context.mdc`。
- **Cursor / Codex 目录分工**：Cursor Agent Skills 位于 **Windows** `%USERPROFILE%\.cursor\skills` / **macOS** `/Users/<你的用户名>/.cursor/skills`；Cursor 应用配置与用户数据位于 **Windows** `%APPDATA%\Cursor` / **macOS** `~/Library/Application Support/Cursor`；Codex 配置、规则和 skills 位于 **Windows** `%USERPROFILE%\.codex` / **macOS** `/Users/<你的用户名>/.codex`。

## 目的

本 skill 用于为当前项目生成稳定、可复用的 Cursor 项目规则文件：

- 识别项目技术栈、运行脚本、目录结构与架构入口
- 将长期稳定事实写入 `{workspace}/.cursor/rules/project-context.mdc`
- 让后续 Cursor Agent、Cursor 内 Codex 插件或 Codex CLI 在进入该仓库时先读项目事实

**非目标**：不写临时 TODO、会话结论、路线图、账号密码、token、Cookie、私钥、证书密码等敏感信息；不新建与初始化无关的文档或脚本。

## 何时使用

- 用户显式执行 `/init-project`、`@init-project`，或要求初始化 / 刷新项目上下文。
- 打开新仓库，且缺少 `{workspace}/.cursor/rules/project-context.mdc`。
- 项目结构、技术栈、构建脚本或主要架构发生较大变化，需要刷新项目规则。
- 其它入口 skill 发现项目规则缺失，并路由到 `init-project`。

## 工作区定位

- 默认 `{workspace}` 为当前打开的项目根目录，不是用户配置目录。
- 若当前目录是配置仓（例如 **Windows** `%USERPROFILE%\.cursor` / `%USERPROFILE%\.codex`，或 **macOS** `/Users/<你的用户名>/.cursor` / `/Users/<你的用户名>/.codex`），但用户明确给了业务仓库路径，以用户指定路径为 `{workspace}`。
- 若同时存在多层项目标志文件，优先选择包含用户当前任务文件、`package.json` / `pyproject.toml` / `pom.xml` 等 manifest、`.git/` 的最近公共根。

## 新会话必读顺序

在创建或刷新规则文件前，按顺序读取最小必要上下文；已在当前 chat 实际加载的文件可不重复读取，但不得只凭历史摘要继续。

1. **本 skill 文件**：确认目标、输出位置与路径规则。
2. **现有项目规则**（若存在）
   - `{workspace}/AGENTS.md`
   - `{workspace}/.cursor/rules/project-context.mdc`
   - `{workspace}/.cursor/rules/*` 中与项目级事实直接相关的文件
3. **项目 manifest**（按实际存在读取 1-3 个高价值文件）
   - JavaScript / TypeScript：`package.json`、`pnpm-lock.yaml`、`yarn.lock`、`package-lock.json`
   - Python：`pyproject.toml`、`requirements.txt`、`Pipfile`
   - Java / Kotlin：`pom.xml`、`build.gradle`、`settings.gradle`
   - Rust：`Cargo.toml`
   - Flutter / Dart：`pubspec.yaml`
   - Go：`go.mod`
4. **项目说明与环境文件**（若存在）
   - `README.md`、`README.*`
   - `.nvmrc`、`.node-version`、`.tool-versions`
   - `.env.example`、`.env.template`（只记录变量名与用途，不记录真实密钥）
5. **目录结构**：用 `rg --files`、`find` 或等价工具查看顶层与关键目录，例如 `src/`、`app/`、`lib/`、`components/`、`pages/`、`server/`、`ios/`、`android/`、`docs/`、`tests/`。
6. **配置与风格文件**（若存在且与判断相关）：ESLint、Prettier、TypeScript、Vite、Next、Metro、Babel、Jest、Vitest、Playwright、Docker、CI 配置等。

不要默认通读整仓；先获取足够判断项目事实的最小文件集合。

## 执行流程

1. 确认 `{workspace}` 和项目类型。
2. 按「新会话必读顺序」读取上下文。
3. 识别技术栈、框架、包管理器、运行脚本、测试脚本、构建方式、主要目录和架构入口。
4. 若 `{workspace}/.cursor/rules/` 不存在，创建该目录。
5. 创建或刷新 `{workspace}/.cursor/rules/project-context.mdc`。
6. 若已有 `project-context.mdc`，保留仍然准确的长期事实，更新过期内容；不要把旧文件整段盲目丢弃。
7. 完成后简要说明捕获了哪些上下文、写入了哪个文件，以及是否有未能确认的风险点。

## project-context.mdc 模板

必须使用以下 frontmatter：

```yaml
---
description: "Project context"
alwaysApply: true
---
```

正文必须包含以下章节；无法确认的内容写「未在当前读取范围内确认」，不要编造。

| Section | Content |
|---------|---------|
| Project Overview | 项目简介、业务域或工具用途 |
| Tech Stack | 语言、框架、核心依赖、包管理器 |
| Development Commands | 运行、测试、构建、lint 等脚本 |
| Node/Runtime version | `.nvmrc`、`engines`、`.tool-versions` 或等价来源 |
| Directory Structure | 主要目录及用途 |
| Architecture notes | 入口、路由、状态管理、API 层、数据流 |
| Build/Deploy notes | 构建、发布、平台差异、CI/CD |
| Code style or conventions | 可发现的 lint、format、命名、测试约定 |

## 输出约定

- 面向用户用**简体中文**；生成文件中的注释使用 **English**。
- 路径、命令、标识符保持原文。
- 只把长期稳定、可复查的项目事实写入 `project-context.mdc`。
- 若信息来自推断，需在文件或答复中标明「根据文件结构推断」。
- 最终回复说明：
  - 已创建或更新的文件
  - 捕获到的关键项目事实
  - 未验证或未确认的部分

## 边界

- 不写真实密钥或私人账号信息。
- 不把一次性任务状态写进项目规则。
- 不主动运行项目、安装依赖或大规模测试，除非用户明确要求或初始化需要轻量验证。
- 不擅自改业务代码；本 skill 的默认写入目标仅为 `{workspace}/.cursor/rules/project-context.mdc`。
