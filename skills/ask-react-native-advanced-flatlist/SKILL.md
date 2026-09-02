---
name: ask-react-native-advanced-flatlist
description: >-
  React Native 组件库 react-native-advanced-flatlist 的私有恢复与专项路由入口。仅在用户显式使用
  /ask-react-native-advanced-flatlist 或 @ask-react-native-advanced-flatlist，或明确要求继续受保护待办、
  恢复跨会话状态、处理该库源码/类型/示例/npm 发布时使用。每个新 chat 先调用本入口；随后强制
  读取 Codex 对口 Skill 同目录 AGENTS.md 作为共享仓库规则。
---

# ask-react-native-advanced-flatlist（Cursor）

## 调用策略

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取 `$HOME/.codex/skills/react-native-advanced-flatlist/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\react-native-advanced-flatlist\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得跳过。
- 每个新 chat 先显式调用本入口，再从共享 `AGENTS.md` 与当前源码开始普通实现、排障、审查、测试和发布；项目根不维护第二份 `AGENTS.md`。
- 本 chat 首次激活时，在主任务前执行共享 `AGENTS.md` 的 “First-chat structural drift gate”；发现重大冲突时立即完整读取并执行 macOS `$HOME/.cursor/skills/init-project/SKILL.md` / Windows `%USERPROFILE%\.cursor\skills\init-project\SKILL.md`，刷新后重新读取共享 `AGENTS.md` 并继续原任务，不要求用户再次输入 `/init-project`。
- 本 Skill 只处理私有恢复状态、受保护待办、专项路由和 npm/GitHub 发布上下文。
- 用户给出具体任务时，该任务优先；只有仅调用入口或明确要求“继续”时，才解析未注释待办。

## 路径与事实源

- 项目根：Windows `D:\work\RN\react-native-advanced-flatlist`；macOS `/Users/<你的用户名>/Desktop/work/RN/react-native-advanced-flatlist`，当前 Mac 为 `/Users/stark/Desktop/work/RN/react-native-advanced-flatlist`。
- Cursor 入口：Windows `%USERPROFILE%\.cursor\skills\ask-react-native-advanced-flatlist\SKILL.md`；macOS `/Users/<你的用户名>/.cursor/skills/ask-react-native-advanced-flatlist/SKILL.md`。
- Codex 对照入口：Windows `%USERPROFILE%\.codex\skills\react-native-advanced-flatlist\SKILL.md`；macOS `/Users/<你的用户名>/.codex/skills/react-native-advanced-flatlist/SKILL.md`。
- 公共 API、分页、刷新、选中和渲染行为：以当前 `src/` 和 `__tests__/` 为准。
- 稳定工程约束只维护在 Codex 对口目录的 `AGENTS.md`；不创建仓库根 `AGENTS.md` 或 `.cursor/rules/project-context.mdc`。
- 技术栈、脚本、peer/dev 依赖、发布字段：以 `package.json`、`tsconfig.json` 和项目配置为准。
- 使用方式与 API 说明以 `README.md` 为准；发布步骤以 `NPM_PUBLISH_GUIDE.md` 为准，且不得把其中的过期命令盖过当前 `package.json` scripts。
- 当前任务、npm/GitHub 外部状态和最小下一步：以用户本轮消息、受保护的“当前活跃需求”和实时证据为准，不在入口正文复制状态流水。
- 不在本 Skill、对话或仓库文档中写入或复述 npm token、密码、邮箱验证码或 Git 凭据。

发生冲突时，当前源码、Git、`npm view`、真实构建产物和 registry 实时结果优先于历史摘要。

## 与 Codex 入口对齐

- 两份入口分别维护，但事实源优先级、最小读取顺序、上下文门禁、授权边界、实施流程和输出约定保持一致。
- 在 Cursor 的 Codex 插件中输入 `/react-native-advanced-flatlist`，应与 Cursor 输入框中执行 `/ask-react-native-advanced-flatlist` 对同一明确任务达到相同推进效果。
- 两份“当前活跃需求”由用户分别维护，不自动同步或改写；用户本轮明确任务始终优先。

## 启用与最小读取顺序

1. 完整读取本 `SKILL.md`；已在当前 chat 实际加载且未变化的文件不重复读取。
2. 确认 Codex 对口 Skill 同目录 `AGENTS.md` 已读取；不要读取或创建 `project-context.mdc`。
3. 读取任务直接相关的源码、测试和配置；需要脚本、依赖、发布或示例事实时，再读取 `package.json`、`README.md`、`NPM_PUBLISH_GUIDE.md`、`CHANGELOG.md`、`CLAUDE.md`、`example/` 中实际存在者。
4. 普通实现、排障和审查不默认读取 Codex 对照入口；仅在用户调用 `/react-native-advanced-flatlist`、两份入口需要对齐，或任务事实只存在于对照入口时读取。
5. 用户只有入口口令而没有新任务时，执行本文件“当前活跃需求”中第一个未注释且可行动的事项；已有明确新任务时，不自动展开无关活跃项。
6. 路由到其它 Skill、ask、command 或 `bmad-*` 前，先完整读取对应 `SKILL.md` 及其明确要求的 `workflow.md`、`checklist.md`、`reference.md`。
7. 当前任务涉及 Markdown 图片引用时，先按引用文件同目录精确读取全部相关图片；读取失败后再搜索，不得用文字摘要代替图片事实。

不要默认通读仓库、全部 README 或另一客户端入口，也不要把历史摘要当成已加载的当前事实。

## 实施工作流

1. 确认实际工作区、Git 分支、工作树和任务授权边界；保留用户已有改动，不扩大到无关重构、提交、push 或 npm publish。
2. 按实现、排障、类型、列表现性能、审查或发布分类，只读取能决定下一步的高价值文件。
3. 代码任务依次完成真实库实现、同项目内测试/构建；确认无需继续改代码后，再更新项目文档或项目外入口资料。
4. 公共 API 变更必须保持运行时兼容，或在 `CHANGELOG.md` 中明确标为 breaking 并使用对应 semver。
5. 开发阶段优先单文件、单用例验证；发布前至少跑通 `npm test` 与 `npm run build`。未运行的测试、构建或 registry 核对必须明确说明。
6. 不因普通代码改动更新本 Skill；只有入口、事实源、跨客户端对齐、长期门禁或受保护活跃需求由用户授权变更时才更新。

## 项目工程约束

- 本仓库是 React Native **组件库**，不是完整 App；主入口以当前 `package.json` 的 `main`/`types` 为准，源码在 `src/`，构建产物在 `lib/`。
- React / React Native 只作为 peer dependency；不要把宿主 App 的导航、主题、i18n 或业务 DTO 写进本库。
- 新增用户可见默认文案时保持英文默认值，并允许调用方覆盖；库本身不内置 i18n。
- 跨平台逻辑优先使用 FlatList 公共字段；若使用标记为 `iOS ONLY` / `ANDROID ONLY` 的 API，必须 `Platform.OS` 分支并为另一端提供 fallback。
- 非必要不新增运行时依赖；保持可发布包尽量小。
- 不输出或写入 token、Cookie、密码、私钥和 npm 登录凭据。发布只使用当前已登录的 npm 会话或用户明确提供的非交互 token 环境变量，且不得把凭据写入 Skill 或仓库。

## 用户已有日志保护硬门禁

- 当前源码中的 `console.log`、`console.info`、`console.warn`、`console.error`、自定义 logger、debugger、trace 和诊断 Hook 均视为用户已有代码。除非用户在本轮明确要求删除、注释、降级、脱敏、替换或重构某一条具体日志，否则必须逐条保留。
- 本库面向 npm 发布。若现有日志明显是调试残留，且用户本轮明确要求优化/发布，可在收尾 diff 中逐项报告后移除调试日志；不得借机删除调用方可能依赖的错误上报。
- 发现日志可能包含敏感数据时，只收集最小必要证据且不在回复复述敏感值；等待用户授权后再改。

## 运行、发布与外部系统门禁

- 本库默认验证是 `npm test` 和 `npm run build`，以及必要时 `npm pack --dry-run` / `npm view`。没有可运行的宿主 App 时，不得为了验证去创建新的 RN 工程或安装模拟器。
- Git/release 任务：先检查远端 refs、工作树、提交差异和最终树；“方向看起来安全”不等于授权 merge、push 或 npm publish。
- npm publish、`npm version`、打 tag 和 push 分别需要用户明确授权。用户要求“发布新版本到 npm”时，才可在构建和测试通过后执行 publish；同时把对应 git tag 推到 GitHub，避免 registry 与仓库版本分叉。
- 发布前核对 `package.json` 的 `name`、`version`、`files`、`repository`、`publishConfig.access` 与 npm 上已发布版本；不得覆盖已存在的版本号。
- 浏览器和 npm/GitHub 页面任务：使用当前已授权的真实会话并验证完整数据。

## 文档维护规则

- 若本次任务改变稳定架构、命令工作流或仓库边界，在代码与定向验证稳定后自动最小更新 Codex 对口目录 `AGENTS.md`；否则不全仓扫描。
- `README.md` 保存公共 API 与使用说明；`CHANGELOG.md` 保存面向用户的版本变化；`NPM_PUBLISH_GUIDE.md` 只保存无秘密的发布方法。
- 不把字段清单、默认值、单次分支/commit、构建结果、测试数量、当前阻塞或聊天流水写入入口 Skill。
- “当前活跃需求（不要修改这部分的子内容）”由用户维护；除非用户明确授权，否则保持其子内容原文。
- 最终回复默认只报告产出、验证、风险和必要下一步。

## 输出与边界

- 对用户使用简体中文；代码与代码注释使用英文；引用真实文件时给出路径和必要行号。
- 诚实区分已验证、部分验证、外部阻塞和未执行；不把本地 build 成功写成 npm 已发布。
- 不混入 Heals / 其它宿主 App 的假设，不创建无关文档或脚本。

## 当前活跃需求(不要修改这部分的子内容)
<!-- /ask-react-native-advanced-flatlist -->
