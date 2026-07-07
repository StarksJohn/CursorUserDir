---
name: ask-csx-web
description: >-
  Cursor：csx-web / ClinicSolution Web Vue 2 前端项目入口；name 为
  ask-csx-web，口令 /ask-csx-web。用于恢复项目上下文、收敛任务范围、读取项目规则，
  并路由 Vue、webpack、API、i18n、Element UI、WebOffice、telemedicine、代码审查、
  BMAD 等专项 skills。Use when the user works on csx-web, invokes
  /ask-csx-web, or the workspace is Windows D:\work\csx-web / macOS
  /Users/<你的用户名>/Desktop/work/csx-web.
---

# ask-csx-web（Cursor）

## 与 Codex 入口（可选对照）

| 客户端 | `SKILL.md` | `name` | 口令 |
|--------|------------|--------|------|
| Cursor（本文件） | **Windows** `%USERPROFILE%\.cursor\skills\ask-csx-web\SKILL.md` / **macOS** `/Users/<你的用户名>/.cursor/skills/ask-csx-web/SKILL.md`（当前 Mac：`/Users/stark/.cursor/skills/ask-csx-web/SKILL.md`） | `ask-csx-web` | `/ask-csx-web` |
| Codex（对照） | **Windows** `%USERPROFILE%\.codex\skills\csx-web\SKILL.md` / **macOS** `/Users/<你的用户名>/.codex/skills/csx-web/SKILL.md`（当前 Mac：`/Users/stark/.codex/skills/csx-web/SKILL.md`） | `csx-web` | `/csx-web` |

两侧不要求逐句同步，但工作区、必读顺序、路由、上下文门禁、当前活跃需求解释与输出约定应保持一致。若 Codex 侧 skill 未安装，使用 Cursor 入口时仍应按本文件的双平台路径与子 skill 门禁执行。

## 目的

本 skill 是 **`csx-web`（ClinicSolution / CSX Web）** 的默认分析入口，用于在新会话或跨工具切换时，把任务拉回到项目事实与最小必要上下文上。

- **恢复项目事实**：先读项目规则、依赖与直接相关源码，避免只凭历史记忆或旧摘要行动。
- **收敛任务范围**：区分「需求澄清 / 架构讨论 / 实现 / 排障 / 审查 / i18n / 构建部署」，按任务读取最小文件集合。
- **路由专项能力**：将 Vue 2、webpack、API、路由、Vuex、i18n、Element UI、WebOffice、telemedicine、代码审查、BMAD 等任务指向对应 skills 或项目规则。
- **保证上下文完整**：若入口 skill 又指向其它 skill、ask、command、BMAD 工作流或同目录资源，先补读其依赖文件，再执行。
- **沉淀项目结论**：长期稳定项目事实优先更新 `{workspace}/.cursor/rules/project-context.mdc` 或既有文档，不把阶段性结论塞进通用 skill。

**非目标**：不在本文件维护易过期的接口字段清单、临时 TODO 或一次性需求结论；不写真实账号、密码、token、Cookie、私钥、证书密码等敏感信息。

## 何时使用

- 用户显式 `@ask-csx-web`、`/ask-csx-web` 或自然语言提及本 skill 名。
- 用户提到 `csx-web`、ClinicSolution Web、CSX Web、诊所 Web、Vue 2 旧前端、WebOffice、telemedicine、Element UI、webpack 3 等本仓相关任务。
- 当前工作区根目录为 **Windows** `D:\work\csx-web` 或 **macOS** `/Users/<你的用户名>/Desktop/work/csx-web`（当前 Mac：`/Users/stark/Desktop/work/csx-web`），且需要项目级引导。
- 用户未指定文件，但明显在本仓库内工作时，优先按本 skill 的加载顺序取上下文。

## 工作区与路径

| 用途 | Windows | macOS |
|------|---------|--------|
| 工作区根（默认） | `D:\work\csx-web` | `/Users/<你的用户名>/Desktop/work/csx-web`（当前 Mac：`/Users/stark/Desktop/work/csx-web`） |
| 本 Cursor skill | `%USERPROFILE%\.cursor\skills\ask-csx-web\SKILL.md` | `/Users/<你的用户名>/.cursor/skills/ask-csx-web/SKILL.md` |
| Codex 对照 skill | `%USERPROFILE%\.codex\skills\csx-web\SKILL.md` | `/Users/<你的用户名>/.codex/skills/csx-web/SKILL.md` |
| 项目规则 | `{workspace}/.cursor/rules/project-context.mdc` | 同上 |
| Cursor skills 根 | `%USERPROFILE%\.cursor\skills` | `/Users/<你的用户名>/.cursor/skills` |
| Cursor 应用配置与用户数据 | `%APPDATA%\Cursor` | `~/Library/Application Support/Cursor` |
| Codex skills 根 | `%USERPROFILE%\.codex\skills` | `/Users/<你的用户名>/.codex/skills` |
| Codex 全局规则 | `%USERPROFILE%\.codex\AGENTS.md` | `/Users/<你的用户名>/.codex/AGENTS.md` |

若用户明确给出 fork、分支工作区或临时路径，以用户指定路径为准；不要把用户目录下的 skill 路径误当成业务仓库根。后续 `{workspace}` 均指当前实际工作区根。

## 新会话必读顺序（恢复上下文）

新 chat 或首次进入本仓库任务时，按以下顺序读取；已有上下文中已实际加载的文件可不重复读，但不能只凭文件名或历史摘要假设已加载。

1. **本 skill 文件**：确认入口目标、路径规则、路由规则与「当前活跃需求」。
2. **项目规则文件**（按实际存在读取）
   - `{workspace}/AGENTS.md`
   - `{workspace}/.cursor/rules/project-context.mdc`
   - `{workspace}/.cursor/rules/*` 中与当前任务直接相关的规则
3. **项目锚点文件**（按实际存在读取）
   - `{workspace}/README.md`
   - `{workspace}/package.json`
   - `{workspace}/package-lock.json`（只在依赖版本、安装或锁文件问题相关时读取）
4. **项目说明与约定**（按任务相关性选读）
   - `{workspace}/docs/项目结构.md`
   - `{workspace}/docs/多语言使用规范.md`
   - `{workspace}/docs/Git规范.md`
5. **任务直接相关文件**（按主题选读，勿通读整棵 `src/`）

| 主题 | 常见位置 |
|------|----------|
| SPA 入口 / 全局注册 | `src/main.js`、`src/App.vue`、`src/Layout.vue` |
| 路由 | `src/router/index.js`、`src/router/*.js` |
| Vuex 状态 | `src/store/index.js`、`src/store/modules/` |
| API / Axios | `src/api/_axios.js`、`src/api/dataSource/` |
| 权限 / 登录态 | `src/utils/permission.js`、`src/api/_axios.js`、登录相关组件 |
| i18n | `src/language/`、`src/language/locales/` |
| Element UI / 主题 | `src/element-variables.scss`、`src/components/Theme/`、`static/theme/` |
| WebOffice | `src/weboffice/`、`build/webpack.base.conf.js` |
| telemedicine | `src/components/Telemedicine/`、`library/telemedicine/` |
| 打印 / Lodop | `src/utils/*print*`、`src/components/Print/`、`static/lodop/` |
| 构建配置 | `build/`、`config/`、`.babelrc`、`.eslintrc.json`、`bitbucket-pipelines.yml` |
| 业务页面 | `src/components/` 下对应模块；项目历史原因导致页面与组件混放 |

若 `project-context.mdc`、README、docs 与 `package.json` 或源码冲突，**以当前仓库文件为准**，并在答复中说明取舍。

## 稳定背景（摘要；详情以仓库规则为准）

- **业务**：ClinicSolution / CSX 诊所管理 Web 前端，覆盖登录、预约、诊症、账单、报告、仓库/药库、支出、病人信息、通知、打印、视频诊症与 WebOffice 文档编辑。
- **技术**：Vue 2 + Vue Router 3 + Vuex 3 + Axios + Element UI + vue-i18n；webpack 3 多入口构建；npm + `package-lock.json`。
- **入口**：`src/main.js` 为主 SPA 入口；`src/weboffice/main.js` 与 `library/telemedicine` 作为额外 webpack entry。
- **API**：统一优先使用 `src/api/_axios.js` 导出的请求封装，鉴权 token、locale、loading、取消请求、导出响应与登出逻辑集中在该文件。
- **环境**：README 指定 Node `v14.17.5`；Bitbucket Pipeline 使用 Node 14 构建。
- **事实源**：`{workspace}/.cursor/rules/project-context.mdc`；缺失或过期时用 `init-project` / Codex 侧 `initProject` 重建或刷新。

面向用户的医疗健康文案应避免确诊式、替代医嘱式、保证疗效式表述。

## 子 skill / 子任务上下文完整性门禁

当本入口、用户请求、项目规则或「当前活跃需求」指向其它 skill、ask、command、BMAD 工作流或专项子任务时，必须先完成以下检查，再开始实现、审查、改代码或按模板产出。

1. **建立加载账本**：列出当前 chat 已实际读取的入口 skill、项目规则、锚点文件、任务文件、图片及已路由的子 skill。
2. **识别触发源**：用户输入、本文件「当前活跃需求」、项目规则、BMAD 模板/图片引用。
3. **确认是否已读**：必须已实际读取对应 `SKILL.md` 及 `workflow.md` / `checklist.md` / `reference.md` 等依赖；不能只凭摘要继续。
4. **缺什么补什么**：已知路径直接读取；失败则说明精确路径读取失败，再搜索或请用户 `@` 附上文件。
5. **BMAD 硬门禁**：执行任意 `bmad-*` 前，先读 **Windows** `%USERPROFILE%\.cursor\skills\<bmad-identifier>\SKILL.md` / **macOS** `/Users/<你的用户名>/.cursor/skills/<bmad-identifier>/SKILL.md`（及要求的 workflow/checklist/reference）。
6. **图片门禁**：`![img_xxx.png](img_xxx.png)` 按引用源 `.md` 同目录拼接文件名精确读取；读取失败后再搜索，并明确区分「精确路径读取失败」与「搜索未命中」。
7. **执行前复核**：一句话确认上下文是否足够；不足则先补读。
8. **记录加载事实**：最终回复列出「当前 chat 已加载的关键文件」与「本轮新增读取/加载的文件」。

## 路由规则（关联 skills）

按任务类型选用专项能力（**Windows** `%USERPROFILE%\.cursor\skills\<name>\SKILL.md`；**macOS** `/Users/<你的用户名>/.cursor/skills/<name>/SKILL.md`）。路由后须完成上一节门禁。

| 场景 | Skill |
|------|-------|
| 规则缺失或刷新 `project-context.mdc` | `init-project` / Codex 侧 `initProject` |
| Vue / 前端实现 | 优先项目规则 + 直接相关源码；若有本机 Vue 专项 skill，再按门禁读取 |
| TypeScript / JS 类型与边界 | `typescript-strict`（仅当任务涉及 TS 或类型收紧） |
| 代码审查 | `code-review` 或 `bmad-code-review` |
| 国际化与中英文案 | `chinese-english-translation`；代码中新增用户可见文案需同步相关 locale 文件 |
| 架构讨论 | `architecture-review` 或 `bmad-agent-architect` |
| 快速交付 / Story 实现 | 规格已清时 `bmad-quick-dev`；有 story 文件时 `bmad-dev-story` |
| 文档化当前项目 | `bmad-document-project` 或 `init-project`，取决于目标是项目规则还是完整文档 |
| Cursor / MCP / Rules | `ask-cursor` |

**默认优先级**：事实澄清 → 小步读代码 → 再改；产品范围未清时不要盲目 `bmad-quick-dev`。

## 执行工作流（默认）

1. 确认工作区是否为 `csx-web`（或用户指定路径）。
2. 按「新会话必读顺序」读取最小上下文。
3. 合并用户输入框与本文件「当前活跃需求」未注释项，形成验收范围；用户明确裁剪时以用户裁剪为准。
4. 分类任务：需求 / 架构 / 实现 / 排障 / i18n / 构建部署 / 审查。
5. 若需要专项 skill、BMAD、图片或模板，先完成上下文门禁。
6. 实现类任务先定位直接相关 route/component/store/api/config；修改前说明文件与意图。
7. 完成后给出验证方式；未运行应用、构建或测试时明确说明。
8. 长期结论写入 `project-context.mdc` 或 README/docs 既有章节；不新建无关 `.md` 或脚本。

## 任务类型补充

- **Vue 2**：优先遵循现有 Options API、mixins、Element UI、Vue Router 3、Vuex 3 写法；不要主动引入 Vue 3/Composition API 风格。
- **API**：优先使用 `src/api/_axios.js` 封装，不在页面中散落新的 Axios 实例或临时 URL 拼接。
- **i18n**：语言包在 `src/language/locales/`；新增 key 使用 lower camelCase English，并同步每个必要语言包。
- **构建**：webpack 3 / Babel 6 / node-sass 4 对 Node 版本敏感；涉及安装、构建或 CI 时优先核对 Node 14 约束。
- **WebOffice / telemedicine**：它们是多入口或本地依赖边界；改动前读取对应 entry 与构建配置，避免误伤主 SPA。
- **依赖**：先查 `package.json` 与 `package-lock.json`；非必要不新增依赖。

## 输出约定

- 对用户说明：**简体中文**（除非用户要求其他语言）。
- **代码与代码注释**：英文。
- 引用仓库代码时使用路径与行号。
- 不向 skill、项目文档或对话写入真实密钥；敏感配置用占位符。
- 未运行应用、构建或测试时必须明确说明。
- 完成任务后必须说明：
  - 当前 chat 已加载的关键文件
  - 本轮新增读取/加载的文件

## 边界

- 不把医学建议写成确诊或处方替代。
- 不擅自扩大需求范围（无关重构、额外文档）。
- 默认不替用户运行应用/浏览器测试；用户明确要求或任务含验证时再执行并说明结果。
- 不把 React Native、Heals、CS Mobile 或其它仓库的路径与模块假设混入本仓。
- 不把 token、密码、Cookie、私钥、证书密码、运维账号写入 skill 或规则文件。

## 当前活跃需求（不要修改这部分的子内容）

<!-- 在此追加跨会话任务；路径写双平台：Windows D:\work\csx-web / macOS /Users/<你的用户名>/Desktop/work/csx-web（当前 Mac：/Users/stark/Desktop/work/csx-web） -->
