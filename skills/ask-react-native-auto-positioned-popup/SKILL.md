---
name: ask-react-native-auto-positioned-popup
description: >-
  React Native 组件库 react-native-auto-positioned-popup 的会话入口：在新 chat 中恢复任务上下文、对齐仓库事实、收敛需求并路由到 RN/TS/发布等专项 skills。适用于用户提及该包名、工作区为 D:/work/RN/react-native-auto-positioned-popup、或显式执行 /ask-react-native-auto-positioned-popup、@ 本 skill 时。
---

# ask-react-native-auto-positioned-popup

## 目的

本 skill 是 **`react-native-auto-positioned-popup`**（npm 包与 Git 仓库同名）的默认入口，用于：

- **在新会话中恢复与本仓库相关的历史任务上下文**（见下文「会话恢复」）
- 用最少读取对齐技术栈、构建、目录与集成约束（RootView、peer deps 等）
- 区分需求澄清、实现、排障、审查与发布流程，避免无目标整仓搜索
- 将任务路由到合适的仓库规则或专项 skill

## 何时使用

满足以下任一情况时启用本 skill：

- 用户显式输入 `/ask-react-native-auto-positioned-popup` 或 @ 本 skill
- 对话围绕 **`react-native-auto-positioned-popup`**、`AutoPositionedPopup`、本仓库 issue/PR、或 npm 发布
- 工作区为 **`D:\work\RN\react-native-auto-positioned-popup`**（Mac 上以用户本机路径为准）且需要**项目级**引导

## 与全局 ask 模板的关系（可选、只读）

若你的工作流要求在「新开 chat」时同步全局约束，可 **读取一次**（不要修改）：

- Windows: `C:\Users\Stark8964911\.claude\ask\ask.md`
- Mac: `/Users/stark/.claude/ask/ask.md`

该文件含路径约定与文件保护说明。涉及其中图片引用时，按用户规则：图片与引用它的 `.md` **同目录**，优先在同目录做精确路径读取。

**禁止**修改 `ask.md` 及任何其他已声明受保护的 ask 文件。

**主维护入口**：本文件 `SKILL.md`；长期、可复查的任务与结论**优先落在仓库内**文档（见「会话恢复」），避免仅存在于 chat 或仅改 skill 正文。

## 工作区路径

| 平台 | 路径 |
|------|------|
| Windows | `D:\work\RN\react-native-auto-positioned-popup` |
| Mac | 以用户本机为准（示例：`~/work/RN/react-native-auto-positioned-popup`） |

下文 `{workspace}` 表示本表中的仓库根目录。

## 本 skill 文件路径

| 平台 | 路径 |
|------|------|
| Windows | `C:\Users\Stark8964911\.cursor\skills\ask-react-native-auto-positioned-popup\SKILL.md` |
| Mac | `~/.cursor/skills/ask-react-native-auto-positioned-popup/SKILL.md` |

---

## 会话恢复（新 chat 必读顺序）

目标：执行本 skill 后，助手应能拼回「最近在这个仓库里做过什么、还有什么没做完」，而不仅依赖模型训练记忆。

### 1. 仓库内滚动上下文文件（任务记忆主来源）

**路径（固定）**：`{workspace}/ACTIVE_CONTEXT.md`

**新开 chat 且用户已 @ 本 skill 或明确在本仓库工作时**：

1. 若 `ACTIVE_CONTEXT.md` **存在**：**必须先读**该文件（可与 `package.json` 并行读取，但不得在未读的情况下宣称「没有历史上下文」）。
2. 若 **不存在**：在本轮对话中**创建**该文件，使用下文「ACTIVE_CONTEXT.md 模板」初始化；并把当前用户问题记入「Open items」。
3. 读完後，再结合下面「最小上下文来源」表补齐稳定事实。

**本轮对话结束或完成阶段性任务后（维护义务）**：

用**简练、可复查**的要点更新 `ACTIVE_CONTEXT.md`（同意用户规则：不要把整段聊天粘贴进文件）：

- **Recent sessions**：日期（YYYY-MM-DD）、1～5 条 bullets：做了什么、涉及文件/PR、是否已 `npm run build` / `lint`
- **Open items**：未关闭的决策、待发布版本、已知 bug、待补测试
- **Constraints / decisions**：本轮确认过的行为约定（例如 breaking change、props 语义）
- **Consumer notes**：若涉及宿主 App 联调，记**包版本、集成方式**（RootViewProvider、babel alias 等），避免秘钥与隐私数据

若信息与 `project-context.mdc` 冲突，**以仓库内源码与 `package.json` 为准**，并应顺带修正规则文件或本文件中的过时句。

### 2. ACTIVE_CONTEXT.md 模板（创建或重置时使用）

将以下内容写入 `{workspace}/ACTIVE_CONTEXT.md` 的初始体；后续只增量更新，不删历史时可把旧条目移到 `Archive` 小节。

```markdown
# ACTIVE_CONTEXT — react-native-auto-positioned-popup

Rolling task memory for Cursor chats. Keep entries short; source of truth is still git history.

## Recent sessions

- YYYY-MM-DD: ...

## Open items

- ...

## Decisions / constraints

- ...

## Release / integration notes

- Package version (last touched): ...
- ...
```

### 3. 稳定事实 vs 滚动任务

| 类型 | 存放位置 |
|------|----------|
| 技术栈、脚本、目录、架构摘要 | `{workspace}/.cursor/rules/project-context.mdc`（缺失则用 `init-project` 生成） |
| 近期任务、未完成项、联调笔记 | `{workspace}/ACTIVE_CONTEXT.md` |
| 发布流程细节 | `{workspace}/NPM_PUBLISH_GUIDE.md`、`{workspace}/CLAUDE.md`（与版本冲突时以 `package.json` / `project-context.mdc` 为准） |

### 4. 可选：Cursor Agent transcripts

用户本地可能存在历史父级会话导出（仅作人工追溯）；**不要**依赖在 skill 中硬编码 transcript 路径。若用户主动粘贴 transcript 摘要，将有效结论合并进 `ACTIVE_CONTEXT.md`。

---

## 最小上下文来源

按优先级 **按需** 读取；不要默认通读 `src/` 全文。

| 优先级 | 来源 | 用途 |
|--------|------|------|
| 1 | `{workspace}/ACTIVE_CONTEXT.md` | **历史任务与未完成项** |
| 2 | `{workspace}/.cursor/rules/project-context.mdc` | 技术栈、脚本、目录、架构 |
| 3 | `{workspace}/package.json` | version、scripts、peerDependencies、files 字段 |
| 4 | `{workspace}/CLAUDE.md` | 命令与架构补充（与 2、3 冲突时以仓库最新事实为准） |
| 5 | `{workspace}/README.md` 或 `README_zh.md` | 集成、babel alias、使用示例 |
| 6 | `{workspace}/NPM_PUBLISH_GUIDE.md` | 发布 checklist（与发布相关任务时） |
| 7 | 具体源码文件 | 仅与用户问题直接相关的 1～3 个文件 |

### 按主题的默认切入（按需打开）

| 主题 | 常见路径 |
|------|----------|
| 主组件与定位/列表逻辑 | `src/AutoPositionedPopup.tsx` |
| 对外 API 与类型 | `src/AutoPositionedPopupProps.ts` |
| 样式与主题 | `src/AutoPositionedPopup.style.ts` |
| RootView 挂载 | `src/RootViewContext.tsx` |
| 键盘相关 | `src/KeyboardManager.tsx` |
| 事件名常量 | `src/constants.ts` |
| 包入口导出 | `src/index.ts` |
| 第三方类型补丁 | `src/types/react-native-advanced-flatlist.d.ts` |

---

## 稳定项目事实（摘要）

本节仅为**记忆锚点**；**以 `project-context.mdc`、源码与 `package.json` 为准**。

- **产品形态**：React Native **库**（非完整 App），主入口 `lib/index.js`，源码在 `src/`。
- **集成**：宿主需 `RootViewProvider`；列表依赖 `react-native-advanced-flatlist`。
- **构建**：`npm run build` → `lib/`，含 `strip-console` 后处理；发布前通常 `prepublishOnly` 含 lint。

---

## 路由规则（关联 skills）

### 规则缺失或过期

- 生成或刷新 `{workspace}/.cursor/rules/project-context.mdc`：`init-project`

### React Native 实现与体验

- Hooks、跨端差异、列表、键盘：`react-native-patterns`

### 类型安全

- 收紧 props / 公共 API 类型：`typescript-strict`

### 代码审查

- 常规：`code-review`；偏对抗：`bmad-code-review`

### 以交付为目标的实现

- 需求已清、偏执行：`bmad-quick-dev`；若有 story 文件：`bmad-dev-story`

### 架构与模块边界

- `architecture-review` 或 `bmad-agent-architect`

### Cursor / Skills 机制（与库开发并行时）

- Rules、Skills、MCP：`ask-cursor`

**默认优先级**：读 `ACTIVE_CONTEXT.md` + 稳定规则 → 小范围读代码 → 再改；需求模糊时不要直接大范围重构。

---

## 执行工作流

1. 确认工作区为本仓库（或用户声明的 fork），`package.json` 的 `name` 为 `react-native-auto-positioned-popup`。
2. **读取** `ACTIVE_CONTEXT.md`（无则按模板创建）。
3. 读取 `project-context.mdc`、`package.json`；其余文件按问题按需加载。
4. 归类：需求 / 实现 / 缺陷 / 审查 / 发布 / 文档。
5. 给出下一步或调用专项 skill；实现类任务指明可能涉及的 `src/` 路径。
6. **更新** `ACTIVE_CONTEXT.md`：记录本轮结论与仍开放的项。

---

## 输出约定

- 对用户说明：**简体中文**（除非用户要求其他语言）
- **代码与代码注释**：英文
- 引用仓库代码时使用带路径与起止行的代码引用块
- 不在 skill、`ACTIVE_CONTEXT.md` 或对话中写入真实密钥；npm token、git 凭据等用占位符

---

## 边界

- 不假设消费端 App 的导航、状态管理与本仓库相同
- 不擅自扩大范围（无关重构、用户未要求的文档）；**例外**：为维护会话连续性而创建/更新 `ACTIVE_CONTEXT.md` 属于本 skill 范围
- 除非用户明确要求，默认不替用户执行 `npm publish` 或链接真实 npm 账号操作
- 不以陈旧 chat 记忆覆盖当前仓库文件；冲突时以 git 与磁盘为准

---

## 当前活跃需求

<!-- 可选：仅放 1～3 条「跨会话仍需提醒」的极短线索；细节与长背景写入 {workspace}/ACTIVE_CONTEXT.md，避免本 skill 无限膨胀。 -->
- （暂无；请优先维护仓库内 `ACTIVE_CONTEXT.md`）
- 你帮我全自动发布一个当前项目的新版本到NPM;我的NPM登录密码是 `Zc111111`,你帮我在命令行里登录NPM
