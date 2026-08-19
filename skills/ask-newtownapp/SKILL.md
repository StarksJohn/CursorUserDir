---
name: ask-newtownapp
description: >-
  New Town Medical 私有恢复与专项路由入口。仅在用户显式使用
  /ask-newtownapp 或 @ask-newtownapp，或明确要求继续受保护待办、恢复跨会话状态、
  处理外部构建发布阻塞时使用。每个新 chat 先调用本入口；随后强制读取 Codex
  对口 Skill 同目录 AGENTS.md 作为共享仓库规则。
---

# ask-newtownapp（Cursor）

## 调用策略

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取 `$HOME/.codex/skills/newtownapp/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\newtownapp\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得跳过。
- 每个新 chat 先显式调用本入口，再从共享 `AGENTS.md` 与当前源码开始普通实现、排障、审查和测试；项目根不维护第二份 `AGENTS.md`。
- 本 Skill 只处理私有恢复状态、受保护待办、跨客户端对齐和外部构建/发布上下文。
- 用户给出具体任务时，该任务优先；只有仅调用入口或明确要求“继续”时，才解析未注释待办。

## 与 Codex 入口（分别维护）

| 客户端 | `SKILL.md` | `name` | 口令 |
|--------|------------|--------|------|
| Cursor（本文件） | **Windows** `%USERPROFILE%\.cursor\skills\ask-newtownapp\SKILL.md`（本机示例：`C:\Users\Stark8964911\.cursor\skills\ask-newtownapp\SKILL.md`） / **macOS** `/Users/<你的用户名>/.cursor/skills/ask-newtownapp/SKILL.md`（当前 Mac：`/Users/stark/.cursor/skills/ask-newtownapp/SKILL.md`） | `ask-newtownapp` | `/ask-newtownapp` |
| Codex（对口入口） | **Windows** `%USERPROFILE%\.codex\skills\newtownapp\SKILL.md` / **macOS** `/Users/<你的用户名>/.codex/skills/newtownapp/SKILL.md`（当前 Mac：`/Users/stark/.codex/skills/newtownapp/SKILL.md`） | `newtownapp` | `/newtownapp` |

两份文件分别维护，但入口、必读顺序、上下文门禁、路由规则与任务验收口径必须保持一致。通过 Cursor 输入框执行 `/ask-newtownapp`，或在 Codex / Cursor 内 Codex 插件输入 `/newtownapp`，应获得同一任务执行效果。

## 目的

本 skill 是 **newtownapp / New Town Medical**（`package.json` 中 `name: new-town-medical`，`app.json` 中 `name: newTownMedical`）的默认分析入口，用于在新会话或跨工具切换时把任务拉回项目事实与最小必要上下文。

- **恢复项目事实**：先读项目规则、依赖脚本与直接相关源码，避免只凭历史记忆或旧摘要行动。
- **收敛任务范围**：区分「需求澄清 / 架构讨论 / 实现 / 排障 / 审查 / i18n / 原生构建与发布」，按任务读取最小文件集合。
- **路由专项能力**：将 React Native、TypeScript、Figma、BMAD、代码审查、翻译、Android/iOS 构建等任务指向对应 skills 或项目规则。
- **保证上下文完整**：若入口 skill 又指向其它 skill、BMAD 工作流、同目录图片或项目文档，须先按门禁补读其依赖文件，再执行。
- **合并待办来源**：除用户输入框外，本文件「当前活跃需求」及 Codex 对照入口中的未注释条目，均视为本轮须覆盖的验收范围；用户明确裁剪范围时以用户裁剪为准。
- **沉淀项目结论**：需要长期保留的事实优先更新仓库内规则或既有文档，不把结论只留在对话里。

## 何时使用

- 用户显式使用 `/ask-newtownapp` 或 `@ask-newtownapp`。
- 用户明确要求继续受保护待办、恢复私有跨会话状态，或处理外部构建/发布上下文。
- 项目名、路径、工作区或普通仓库任务本身不触发本 Skill。

## 工作区与本 skill 路径

| 用途 | Windows | macOS |
|------|---------|--------|
| 工作区根（默认） | `D:\work\RN\newtownapp` | `/Users/<你的用户名>/Desktop/work/RN/newtownapp`（当前 Mac：`/Users/stark/Desktop/work/RN/newtownapp`） |
| 本 Cursor skill | `%USERPROFILE%\.cursor\skills\ask-newtownapp\SKILL.md` | `/Users/<你的用户名>/.cursor/skills/ask-newtownapp/SKILL.md` |
| Codex 对照 skill | `%USERPROFILE%\.codex\skills\newtownapp\SKILL.md` | `/Users/<你的用户名>/.codex/skills/newtownapp/SKILL.md` |
| Cursor skills 根 | `%USERPROFILE%\.cursor\skills` | `/Users/<你的用户名>/.cursor/skills`（当前 Mac：`/Users/stark/.cursor/skills`） |
| Cursor 应用数据 | `%APPDATA%\Cursor` | `~/Library/Application Support/Cursor` |
| Codex 配置与 skills 根 | `%USERPROFILE%\.codex` | `/Users/<你的用户名>/.codex`（当前 Mac：`/Users/stark/.codex`） |
| Codex 全局规则 | `%USERPROFILE%\.codex\AGENTS.md` | `/Users/<你的用户名>/.codex/AGENTS.md`（当前 Mac：`/Users/stark/.codex/AGENTS.md`） |

若用户明确给出 fork、分支工作区或临时路径，以用户指定路径为准；否则按上表定位。

正文与文档中需要双平台表达业务仓库根时，统一写作：

- **Windows** `D:\work\RN\newtownapp`
- **macOS** `/Users/<你的用户名>/Desktop/work/RN/newtownapp`（当前 Mac：`/Users/stark/Desktop/work/RN/newtownapp`）

下文 `{workspace}` 均指当前 IDE 实际打开的业务仓库根；不要把用户目录下的 `.cursor` 或 `.codex` 路径误当成业务仓库根。

## 图片资源路径

本文中的 `![img_xxx.png](img_xxx.png)` 视为与本文件同目录：**Windows** `%USERPROFILE%\.cursor\skills\ask-newtownapp\`；**macOS** `/Users/<你的用户名>/.cursor/skills/ask-newtownapp/`（当前 Mac：`/Users/stark/.cursor/skills/ask-newtownapp/`）。读取图片时须按引用源 `.md` 所在目录精确拼接文件名。

## 新会话必读顺序（恢复上下文）

新 chat 或首次进入本仓库任务时，按以下顺序读取；已在当前 chat 实际 Read 成功的文件可不重复读，但不能只凭文件名、打开标签页或历史摘要假设已加载。

1. **本 skill**：入口目标、路径规则、路由、上下文门禁与「当前活跃需求」。
2. **Codex 对照 skill（存在则读）**：**Windows** `%USERPROFILE%\.codex\skills\newtownapp\SKILL.md` / **macOS** `/Users/<你的用户名>/.codex/skills/newtownapp/SKILL.md`，用于核对 `/newtownapp` 与 `/ask-newtownapp` 的必读顺序、上下文门禁与活跃需求解释是否一致。
3. **项目规则与锚点**（存在则读）
   - `{workspace}/.cursorrules`
   - Codex 对口 Skill 同目录 `AGENTS.md`
   - `{workspace}/package.json`
   - `{workspace}/README.md`、`{workspace}/CLAUDE.md`（与任务相关时）
   - `{workspace}/app.json`、`{workspace}/babel.config.js`、`{workspace}/tsconfig.json`（与入口名、别名、TS 或构建问题相关时）
4. **任务直接相关文件**：仅与用户问题或「当前活跃需求」对应的 `src/`、`android/`、`ios/`、根目录配置或指南类 `.md`。

| 优先级 | 来源 | 用途 |
|--------|------|------|
| 1 | 本 skill + Codex 对口 Skill 同目录 `AGENTS.md` | 入口、长期规则、加载门禁 |
| 2 | `package.json`、`app.json`、README、CLAUDE | 脚本、依赖、环境和发布说明 |
| 3 | 具体代码与配置 | 实现、排障、审查 |

不要默认通读整棵 `src/`；先定位 1 至 3 个高价值文件，再决定是否扩大范围。

## 当前 chat 上下文加载门禁（必读）

- **入口恢复自检**：通过 `/ask-newtownapp` 进入后，执行任务前须已实际读取本 `SKILL.md`、Codex 对照 `SKILL.md`（若存在）、Codex 对口目录 `AGENTS.md`、`{workspace}/package.json` 以及任务相关项目规则；不要读取或创建 `project-context.mdc`。
- **双入口一致性自检**：若 `/ask-newtownapp` 与 `/newtownapp` 的路径表、必读顺序、路由或活跃需求解释出现冲突，以更具体、更新且更贴近当前工作区的条目为准，并在最终回复说明取舍。
- **任务相关文件自检**：列出本步必须依赖的文件（设计、API、目标 screen、Gradle、Podfile、环境说明、测试文件等），逐项判断是否已在当前 chat 读取；未读则先 `ReadFile`。
- **子 skill 自检**：下一步若执行任意其它 skill（含 `bmad-*`、`react-native-patterns`、`typescript-strict`、`code-review` 等），须判断当前 chat 是否已读取该 skill 的 `SKILL.md` 及其要求的 `workflow.md` / `checklist.md` / `reference.md` 等；缺一则按 **Windows** `%USERPROFILE%\.cursor\skills\<id>\` / **macOS** `/Users/<你的用户名>/.cursor/skills/<id>/` 补读后再执行。
- **BMAD 硬门禁**：执行任意 `bmad-<identifier>` 前，必须先 `ReadFile` 对应 `SKILL.md` 及同目录依赖文件。
- **图片门禁**：任务引用 skill、ask、command、rule 或项目文档中的图片时，先精确路径读图，再推理；读取失败后再搜索，并明确区分「精确路径读取失败」与「搜索未命中」。
- **双 skill 待办**：若用户同时挂载或点名多个入口 skill，各文件中「当前活跃需求」未注释项均须纳入本轮完成标准（除非用户明确排除）。
- **任务结束汇报**：最终回复须列出「当前 chat 已加载的关键文件」与「本轮新增读取/加载的文件」；只列对判断、修改或验证有实际影响的项。

## 稳定项目事实（摘要）

本节为记忆锚点；以 Codex 对口目录 `AGENTS.md`、仓库 `package.json`、源码和原生工程为准。

- **产品**：`new-town-medical` / `newTownMedical` 是新都医疗患者侧 React Native app，覆盖登录、Health Pass / membership、预约、视频问诊、账单、Profile、通知与 wallet pass 相关能力。
- **技术栈**：React Native `0.76.3`、React `18.3.1`、TypeScript strict、React Navigation v7、axios、`i18n-js`、`react-native-extended-stylesheet`。
- **状态与启动**：`index.js` 注册 `App`；`App.tsx` 组合 `ToastProvider`、`AppProvider`、`ErrorBoundary`、`MainStack`、BootSplash、Keychain / Biometrics、Firebase push permission 与版本检查。
- **API / 配置**：`src/api/api-client.ts` 通过 axios 注入 Bearer、语言和 client header；`react-native-config` 使用 `.env.development` / `.env.production`。
- **导航与状态**：`src/navigation/` 管理 stack / tabs；全局状态在 `src/store/AppContext.tsx`，通过 `useAppState()` / `getGlobalAppState()` 使用。
- **原生与构建**：Android `applicationId` 为 `com.newTownMedical`，flavor 为 `dev` / `prod`；iOS workspace 为 `ios/newTownMedical.xcworkspace`，脚本 scheme 为 `newTownMedicalAppDev` / `newTownMedicalAppProd`。
- **补丁与资源**：`patch-package` 当前包含 `react-native-snap-carousel+3.9.1.patch`；SVG 通过 `react-native-svg-transformer`；BootSplash 资源在根 `assets/`。
- **文档取舍**：README 中可能包含历史 Amber 命名和敏感账号/令牌示例；实现与命令优先以 `package.json`、源码和原生工程现状为准，回复时不要复述真实凭据。

医疗健康类用户可见文案避免确诊式、替代医嘱式措辞。

## 常用命令锚点

| 场景 | 命令 |
|------|------|
| 安装依赖 | `npm i` |
| Metro | `npm run start` |
| Android dev | `npm run android:dev` |
| Android prod debug | `npm run android:prod` |
| iOS dev / prod | `npm run ios:dev` / `npm run ios:prod` |
| Test | `npm test` |
| Release APK（macOS） | `npm run build:mac` |
| Release APK（Windows） | `npm run build:win` |
| AAB（Windows 脚本） | `npm run android_aab:dev` / `npm run android_aab:prod` |
| iOS offline bundle | `npm run ios-bundle` |

## 最小上下文来源（按主题）

| 主题 | 常见位置 |
|------|----------|
| 根入口 / Provider | `App.tsx`、`index.js`、`app.json` |
| 导航与路由名 | `src/navigation/` |
| API / DTO | `src/api/` |
| 全局状态 | `src/store/AppContext.tsx` |
| 页面 | `src/screens/` |
| 组件与样式 | `src/components/`、`src/style/` |
| i18n | `src/i18n/`、`src/i18n/locale/` |
| 常量 | `src/constants/` |
| 配置 | `src/config/`、`.env.development`、`.env.production` |
| Firebase Push | `src/services/firebase/`、`android/app/src/*/google-services.json`、`ios/GoogleService-Info.plist` |
| Teleconsult / Agora | `src/screens/teleconsult-screen/`、与 Agora 相关 API / env |
| 缓存 / 持久化 | `src/cache/`、AsyncStorage、Keychain |
| 补丁 | `patches/` |
| 原生构建 / 发布 | `android/`、`ios/`、README、Gradle、Podfile |

## 路由规则（关联 skills）

名称与 **Windows** `%USERPROFILE%\.cursor\skills` / **macOS** `/Users/<你的用户名>/.cursor/skills` 下目录一致。路由到某 skill 后，必须按上文「子 skill 自检」补读该 skill 全文及依赖后再执行。

| 场景 | Skill |
|------|--------|
| 唯一 `AGENTS.md` 缺失或重大结构刷新 | `/init-project` |
| RN 实现与体验 | `react-native-patterns` |
| 类型安全 | `typescript-strict` |
| 代码审查 | `code-review` / `bmad-code-review` |
| 国际化与文案 | `chinese-english-translation` |
| Figma 到 RN | `ask-figma-to-rn-toolkit`；写入 Figma 配合 `figma-use` |
| 快速交付 | `bmad-quick-dev`；有 story 时 `bmad-dev-story` |
| 架构 | `architecture-review` / `bmad-agent-architect` |
| Cursor / MCP / Rules | `ask-cursor` |

默认优先级：澄清事实 -> 读最小相关代码切片 -> 再实现。需求仍模糊时，不要盲目使用 `bmad-quick-dev`。

## 执行工作流

1. 确认工作区为本仓库（或用户声明的 fork），并确认双平台路径表中哪一侧对应当前机器。
2. 按「新会话必读顺序」与「上下文加载门禁」拉取最小有用上下文；若唯一 `AGENTS.md` 缺失，使用 `/init-project`，不得创建仓库内规则副本。
3. 识别请求形态，并合并用户输入与「当前活跃需求」中未注释条目为验收清单。
4. 扩大范围前，先指向最相关的文件或 skill；需子 skill 时先补读子 skill。
5. 实现类任务优先最小改动，遵循项目现有 RN / TS / 原生工程约定。
6. 若本次任务改变稳定架构、命令工作流或仓库边界，在代码与定向验证稳定后自动最小更新 Codex 对口目录 `AGENTS.md`；否则不全仓扫描。外部合并造成的大规模变化使用 `/init-project` 刷新。
7. 运行、构建和发布事实继续维护在现有仓库文档，而非仅留在对话中。

## 输出约定

- 对用户：简体中文（除非用户要求其他语言）。
- 代码与代码注释：英文。
- 引用仓库代码：使用当前客户端兼容的文件/代码引用方式。
- 不向 skill、README 或对话写入真实密钥；敏感配置用占位符。
- 任务结束必须包含「当前 chat 已加载的关键文件」与「本轮新增读取/加载的文件」。

## 边界

- 不把医学表述写成确诊或处方替代。
- 不擅自扩大范围做无关重构。
- 不假设 Heals、CS Mobile、CircleApp、Amber 或其它仓库与本仓库路径/模块/约定相同。
- 除非用户明确要求，默认不运行应用、不做真机测试。
- 不以陈旧笔记或单独 README 片段覆盖当前仓库文件。
- 不在回复中复述 README、env、plist、keystore、Jenkins、Apple、Google Play 等位置的真实账号、密码、token 或证书内容。

## 当前活跃需求(不要修改这部分的子内容)

- 当前无固定活跃需求。执行 `/ask-newtownapp` 时，将用户输入框中的任务与 Codex 对照入口 `/newtownapp` 的「当前活跃需求」未注释条目合并为本轮验收范围。
