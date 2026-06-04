---
name: ask-amber-medical-app-rn
description: >-
  Cursor：Amber Medical / Heals Pass React Native 应用（amber-medical-app-rn）的项目会话入口；
  name 为 ask-amber-medical-app-rn，口令 /ask-amber-medical-app-rn。用于恢复项目上下文、收敛任务范围、
  读取项目规则，并路由 RN/i18n/API/导航/Agora/原生构建/代码审查/BMAD 等专项 skills。Use when the user
  works on amber-medical-app-rn, Amber Medical App, Heals Pass, invokes /ask-amber-medical-app-rn, or the
  workspace is Windows D:\work\RN\amber-medical-app-rn / macOS
  /Users/<你的用户名>/Desktop/work/RN/amber-medical-app-rn.
---

# ask-amber-medical-app-rn（Cursor）

## 与 Codex 入口（可选对照）

| 客户端 | `SKILL.md` | `name` | 口令 |
|--------|------------|--------|------|
| Cursor（本文件） | **Windows** `%USERPROFILE%\.cursor\skills\ask-amber-medical-app-rn\SKILL.md` / **macOS** `/Users/<你的用户名>/.cursor/skills/ask-amber-medical-app-rn/SKILL.md` | `ask-amber-medical-app-rn` | `/ask-amber-medical-app-rn` |
| Codex（若已安装） | **Windows** `%USERPROFILE%\.codex\skills\amber-medical-app-rn\SKILL.md` / **macOS** `/Users/<你的用户名>/.codex/skills/amber-medical-app-rn/SKILL.md` | `amber-medical-app-rn` | `/amber-medical-app-rn` |

两处不要求逐句同步，但工作区、必读顺序、路由、上下文门禁与输出约定应保持一致。若 Codex 侧 skill 未安装，使用 Cursor 入口时仍应按本文件的双平台路径与子 skill 门禁执行。

## 目的

本 skill 是 **`amber-medical-app-rn`（Amber Medical App / Heals Pass）** 的默认分析入口，用于在新会话或跨工具切换时，把任务拉回到项目事实与最小必要上下文上。

- **恢复项目事实**：先读项目规则、依赖与直接相关源码，避免只凭历史记忆或旧摘要行动。
- **收敛任务范围**：区分「需求澄清 / 架构讨论 / 实现 / 排障 / 审查 / i18n / 原生构建」，按任务读取最小文件集合。
- **路由专项能力**：将 React Native、TypeScript、API、导航、Figma、BMAD、代码审查等任务指向对应 skills 或项目规则。
- **保证上下文完整**：若入口 skill 又指向其它 skill、ask、command、BMAD 工作流或同目录资源，先补读其依赖文件，再执行。
- **沉淀项目结论**：需要长期保留的项目事实优先更新 `{workspace}/.cursor/rules/project-context.mdc` 或既有文档，不把阶段性结论塞进通用 skill。

**非目标**：不在本文件维护易过期的版本号清单、接口字段清单、临时 TODO 或一次性需求结论；不把 README 中的账号、证书、密钥写入本 skill。

## 何时使用

- 用户显式 `@ask-amber-medical-app-rn`、`/ask-amber-medical-app-rn` 或自然语言提及本 skill 名。
- 用户提到 `amber-medical-app-rn`、Amber Medical、Heals Pass、健康护照、远程问诊、预约、会员计划、账单、家属账户等本仓库相关任务。
- 当前工作区根目录为 **Windows** `D:\work\RN\amber-medical-app-rn` 或 **macOS** `/Users/<你的用户名>/Desktop/work/RN/amber-medical-app-rn`（当前 Mac：`/Users/stark/Desktop/work/RN/amber-medical-app-rn`），且需要项目级引导。
- 需求涉及多模块（导航、Auth、API、i18n、Agora 视频、钱包 Pass、原生构建、推送）且需先定范围。
- 用户未指定文件，但明显在本仓库内工作时，优先按本 skill 的加载顺序取上下文。

## 工作区与本 skill 路径

| 用途 | Windows | macOS |
|------|---------|--------|
| 工作区根 | `D:\work\RN\amber-medical-app-rn` | `/Users/<你的用户名>/Desktop/work/RN/amber-medical-app-rn`（当前 Mac：`/Users/stark/Desktop/work/RN/amber-medical-app-rn`） |
| 本 skill 文件 | `%USERPROFILE%\.cursor\skills\ask-amber-medical-app-rn\SKILL.md` | `/Users/<你的用户名>/.cursor/skills/ask-amber-medical-app-rn/SKILL.md` |
| 项目规则 | `{workspace}/.cursor/rules/project-context.mdc` | 同上 |
| Cursor skills 根 | `%USERPROFILE%\.cursor\skills` | `/Users/<你的用户名>/.cursor/skills` |
| Cursor 应用配置与用户数据 | `%APPDATA%\Cursor` | `~/Library/Application Support/Cursor` |
| Codex skills 根 | `%USERPROFILE%\.codex\skills` | `/Users/<你的用户名>/.codex/skills` |
| Codex 全局规则 | `%USERPROFILE%\.codex\AGENTS.md` | `/Users/<你的用户名>/.codex/AGENTS.md` |

若用户明确给出 fork、分支工作区或临时路径，以用户指定路径为准；不要把用户目录下的 skill 路径误当成业务仓库根。

后续步骤中的 `{workspace}` 均指当前实际工作区根。

## 新会话必读顺序（恢复上下文）

新 chat 或首次进入本仓库任务时，按以下顺序读取；已有上下文中已实际加载的文件可不重复读，但不能只凭文件名或历史摘要假设已加载。

1. **本 skill 文件**：确认入口目标、路径规则、路由规则与「当前活跃需求」。
2. **项目规则文件**（按实际存在读取）
   - `{workspace}/AGENTS.md`
   - `{workspace}/.cursor/rules/project-context.mdc`
   - `{workspace}/.cursor/rules/*` 中与当前任务直接相关的规则
3. **项目锚点文件**（按实际存在读取）
   - `{workspace}/README.md`
   - `{workspace}/CLAUDE.md`
   - `{workspace}/package.json`
4. **任务直接相关文件**（按主题选读，勿通读 `src/`）

| 主题 | 常见位置 |
|------|----------|
| 入口 / 启动 | `App.tsx`, `index.js` |
| 导航 | `src/navigation/main-stack.tsx`, `main-tab/`, `route-names.ts`, `global-navigation.ts` |
| 全局状态 | `src/store/AppContext.tsx` |
| API | `src/api/api.ts`, `api-client.ts`, `urls.ts`, `dto/` |
| 配置 | `src/config/`, `.env.development`, `.env.production` |
| i18n | `src/i18n/i18n.ts`, `src/i18n/locale/` |
| Auth | `src/screens/auth-screen/` |
| 首页 / Pass | `src/screens/main-screen/home-screen/`, `pass-screen/` |
| 预约 / 医生 | `src/screens/doctor-*`, `my-appointment-*`, `product-waiting-room/` |
| 视频问诊 | `src/screens/teleconsult-screen/` |
| 会员 / 计划 | `src/screens/my-plans-screen/`, `heals-plan-membership/`, `profile/plans/` |
| 个人资料 | `src/screens/profile/`, `src/screens/main-screen/profile-screen/` |
| 推送 | `src/services/firebase/` |
| 共享 UI | `src/components/` |
| 原生构建 | `android/app/build.gradle`, `ios/Podfile`, schemes `AmberMedicalAppDev` / `AmberMedicalAppProd` |

| 优先级 | 来源 | 用途 |
|--------|------|------|
| 1 | 本 skill + `project-context.mdc` | 入口、长期项目事实、约束 |
| 2 | `package.json`, README, CLAUDE | 脚本、依赖、团队约定 |
| 3 | 任务直接相关源码/配置 | 实现、排障、审查 |
| 4 | 官方文档或第三方类型定义 | 平台差异、弃用/实验 API |

若 `project-context.mdc` 与 `package.json` 冲突，**以当前仓库文件为准**，并在答复中说明。

## 稳定背景（摘要；详情以仓库规则为准）

- **业务**：Heals Pass / 健康护照、会员计划（365 Basic/Gold/Platinum）、医生预约、eQueue/eBook、Agora 远程问诊、账单、家属、Apple/Google 钱包 Pass；配套 H5 见 `heals-monorepo/apps/heals/health-passport`。
- **技术**：React Native + TypeScript strict；React Navigation v7；单例 `AppContext`；axios 多后端（`API_URL`、`API_URL1`、`baseURL`）；`i18n-js`（活跃 locale：`en`、`zh-Hans`、`zh-Hant`）。
- **环境**：`npm run android:dev` / `ios:dev` 使用 `.env.development`；prod 使用 `.env.production`；Android dev 包名后缀 `.dev`。
- **关联仓库**：`heals-app-rn`（Android release keystore 等可从该仓复制，见 README）；勿把 heals-app-rn 的模块路径或约定默认套用到本仓。
- **事实源**：`{workspace}/.cursor/rules/project-context.mdc`（缺失时用 `init-project` 重建）。

面向用户的医疗健康文案：避免确诊式、替代医嘱式、保证疗效式表述。

## 子 skill / 子任务上下文完整性门禁

当本入口、用户请求、项目规则或「当前活跃需求」指向其它 skill、ask、command、BMAD 工作流或专项子任务时，必须先完成以下检查，再开始实现、审查、改代码或按模板产出。

1. **建立加载账本**：列出当前 chat 已实际读取的入口 skill、项目规则、锚点文件、任务文件、图片及已路由的子 skill。
2. **识别触发源**：用户输入、本文件「当前活跃需求」、项目规则、BMAD 模板/图片引用。
3. **确认是否已读**：必须已实际读取对应 `SKILL.md` 及 `workflow.md` / `checklist.md` / `reference.md` 等依赖；不能只凭摘要继续。
4. **缺什么补什么**：已知路径直接 `Read`；失败则说明精确路径读取失败，再搜索或请用户 `@` 附上文件。
5. **BMAD 硬门禁**：执行任意 `bmad-*` 前，先读 **Windows** `%USERPROFILE%\.cursor\skills\<bmad-identifier>\SKILL.md` / **macOS** `/Users/<你的用户名>/.cursor/skills/<bmad-identifier>/SKILL.md`（及要求的 workflow/checklist/reference）。
6. **图片门禁**：`![img_xxx.png](img_xxx.png)` 按引用源 `.md` 同目录拼接文件名精确读取。
7. **执行前复核**：一句话确认上下文是否足够；不足则先补读。
8. **记录加载事实**：最终回复列出「当前 chat 已加载的关键文件」与「本轮新增读取/加载的文件」。

## 路由规则（关联 skills）

按任务类型选用专项能力（**Windows** `%USERPROFILE%\.cursor\skills\<name>\SKILL.md`；**macOS** `/Users/<你的用户名>/.cursor/skills/<name>/SKILL.md`）。路由后须完成上一节门禁。

### 1. 初始化或规则缺失

- 生成/刷新 `project-context.mdc`：`init-project`

### 2. React Native 实现与体验

- Hooks、跨端差异、列表性能、键盘与图片：`react-native-patterns`

### 3. 类型与接口

- 收紧类型、减少 `any`、API/DTO 边界：`typescript-strict`

### 4. 代码审查

- PR/变更质量与安全：`code-review` 或 `bmad-code-review`

### 5. 国际化与中英文案

- 文案翻译、术语、命名旁注：`chinese-english-translation`
- **代码要求**：新增用户可见文案需同步 `en`、`zh-Hans`、`zh-Hant`（以 `src/i18n/i18n.ts` 为准）

### 6. 设计还原（Figma → RN）

- 工具链：`ask-figma-to-rn-toolkit`；本仓亦依赖 `figma-to-rn-toolkit` npm 包
- Figma 设计稿（Heals Pass）：README 中的 Figma 链接

### 7. 快速交付 / Story 实现

- 规格已清、偏执行：`bmad-quick-dev` 或 `bmad-dev-story`（有 story 文件时）

### 8. 架构级讨论

- 模块边界与演进：`architecture-review` 或 `bmad-agent-architect`

### 9. 与 heals-app-rn 对照

- 仅当用户明确要求对比 Heals App 实现或共享原生配置时，再打开 `heals-app-rn` 工作区或 `ask-heals-app-rn`；默认以本仓源码为准。

**默认优先级**：事实澄清 → 小步读代码 → 再改；产品范围未清时不要盲目 `bmad-quick-dev`。

## 执行工作流（默认）

1. 确认工作区是否为 `amber-medical-app-rn`（或用户指定路径）。
2. 按「新会话必读顺序」读取最小上下文。
3. 分类任务：需求 / 架构 / 实现 / 排障 / i18n / 构建 / 审查。
4. 若需要专项 skill 或 BMAD，先完成上下文门禁。
5. 实现类任务先定位直接相关 screen/component；修改前说明文件与意图。
6. 完成后给出验证方式；未运行应用或测试时明确说明。
7. 长期结论写入 `project-context.mdc` 或 README 既有章节；不新建无关 `.md` 或脚本。

## 任务类型补充

- **React Native 跨平台**：公共字段优先；`iOS ONLY` / `ANDROID ONLY` / deprecated 须查类型定义或官方文档后再写共享逻辑。
- **API**：使用 `constants.$api` 与既有 axios 封装；避免在 screen 内散落临时 URL 拼接。
- **导航**：改路由前核对 `main-stack.tsx` 注册、`route-names.ts`、参数类型与 `global-navigation` 调用点。
- **Agora**：视频问诊相关见 README Agora 章节；频道/Token 为运行时配置，勿写入 skill。
- **Android 16KB**：本仓仅 `arm64-v8a`；勿随意恢复 x86 ABI（见 `android/app/build.gradle` 注释）。
- **Env / 签名**：`.env*`、`release.keystore`、Apple 证书等仅用占位符讨论；真实值留在本地安全配置。
- **依赖**：先查 `package.json` 与 `patches/`；非必要不新增依赖；`patch-package` 在 `postinstall` 执行。

## 输出约定

- 对用户说明：**简体中文**（除非用户要求其他语言）
- **代码与代码注释**：英文
- 引用仓库代码时使用路径与行号（Cursor 代码引用格式）
- 完成任务后必须说明：
  - 当前 chat 已加载的关键文件
  - 本轮新增读取/加载的文件

## 边界

- 不把医学建议写成确诊或处方替代
- 不擅自扩大需求范围（无关重构、额外文档）
- 默认不替用户运行应用/真机测试；用户明确要求或任务含验证时再执行并说明结果
- 不把 `heals-app-rn`、`csx-mobile-upgrade` 等其他 Heals 仓的路径与模块假设混入本仓
- 不把 token、密码、Cookie、私钥、keystore 密码、README 内运维账号写入 skill 或规则文件

## 当前活跃需求（不要修改这部分的子内容）

<!-- 在此追加跨会话任务；路径写双平台：Windows D:\work\RN\amber-medical-app-rn / macOS /Users/<你的用户名>/Desktop/work/RN/amber-medical-app-rn（当前 Mac：/Users/stark/Desktop/work/RN/amber-medical-app-rn） -->
