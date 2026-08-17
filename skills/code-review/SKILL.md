---
name: code-review
description: 只审查当前 chat 明确给出的 PR/commit，或当前分支最新 PR/commit 的已提交精确 diff，并追踪该 diff 对已提交历史调用者、实现与测试的影响；仅输出由该 diff 直接引入或扩大、且合并前必须修复的 Critical。若本次修改导致历史代码出错，必须在同一 Critical 中列出本次修改位置及所有受影响历史代码位置。适用于 pull request、GitHub/Bitbucket PR、最新提交或 code review；覆盖 React、React Native、Vue 2/3、TypeScript、JavaScript、HTML/CSS、微信小程序、Flutter、iOS、Android 与 Node.js。不审查未提交代码、未指定且非最新的 PR/commit，或与精确 diff 无因果关系的旧问题；不输出 Suggestions、Nice to have 或 PR 外备注。
---

# Code Review

## 默认执行策略
- 默认目标：一次性完成可长期复用的 code review 工作流优化，而不是每次只做最小补丁。
- 当用户要求“补规则 / 优化 skill / 完善 review 模板”时，默认直接修改并完善当前 skill，不反复追问“是否还要继续优化”。
- 只有在以下情况才额外提问：
  - 用户目标彼此冲突
  - 需要删除用户现有规则或大幅改变原有输出风格
  - 无法判断应优先保留哪套团队规范
- 若发现当前 skill 还有明显结构缺口，应在同次编辑中顺手补齐相关默认规则、模板或边界，避免多轮来回修补。

## 核心边界（硬门禁）

以当前 chat 明确给出的 PR/commit，或最新 PR/commit 的已提交精确 diff 作为问题根因范围；同时必须检查该 diff 对已提交历史调用者、实现、类型使用方和测试的直接影响。不得包含其他 PR/commit、未提交代码或与本次 diff 无因果关系的旧问题；不得输出 Suggestions、Nice to have、顺带发现或 PR 外备注。

### 审查目标选择（唯一范围）

按优先级选择**唯一**审查目标，选定后不得混入其他范围：

1. **当前 chat 已发送的 PR 或 commit**：用户在当前 chat 任意一条消息中给出的 PR 号、PR 链接、commit SHA，或明确说“审查这个 PR / 这个 commit”。
2. **否则用最新 PR**：当前分支对应的 open / most recently updated PR。
3. **否则用最新 commit**：`HEAD^..HEAD`；若 HEAD 是 merge commit，使用 `HEAD^1..HEAD`。

“最新 PR”只指当前分支对应的 PR，不要选仓库里与当前分支无关的其他 PR。用户未在当前 chat 发送、且也不是上述最新 PR / 最新 commit 的变更，一律不审。

当前 chat 同时出现多个 PR/commit 时，只选用户最后一次明确要求审查的那一个；只有用户明确要求批量审查时才能分别审查，且不得合并成一份混合 diff。

先建立该目标的**已提交精确 diff**，再读必要上下文。后续每个 finding 的根因必须能回查到这份 diff 的 changed files 与 hunks；受影响历史代码可以位于 changed files 外，但必须证明由该根因直接触发。

### 精确 diff 建立规则

- PR 优先使用平台返回的 base SHA / head SHA、PR patch，或可验证的 PR refs；以这两个端点生成 changed files 与 hunks。
- 只有确认本地 `HEAD` 与 PR head SHA 完全相同时，才能用 `git diff origin/<base>...HEAD` 代表该 PR；不得把 PR 外的本地已提交 commit 混入审查。
- commit 使用指定 SHA 的精确父子范围：普通 commit 为 `<sha>^..<sha>`，merge commit 为 `<sha>^1..<sha>`。
- 建立范围记录：目标类型与标识、base/head 或 commit range、changed files、diff hunks。结果中的每条 Critical 根因必须与该记录匹配；其受影响历史位置另按因果证据记录。
- 若用户已指定 PR/commit，但无法取得或证明其精确 diff，明确报告范围阻塞；不得悄然改审其他 PR、最新 commit 或工作区代码。

### Critical 范围硬门禁

报告 `[Critical]` 前，必须同时满足：

1. 问题由本次审查目标（当前 chat 的 PR/commit，或最新 PR/commit）的新增、修改或删除直接引入，或该 diff 明确扩大了原有问题的影响面。
2. finding 的根因能锚定到该 diff 的行或 hunk。若该 diff 使未修改的历史代码发生类型错误、构建错误、运行时错误或行为回归，还必须在同一 Critical 中列出这些受影响历史代码的具体位置。
3. 问题会影响正确性、安全性、数据、类型契约、跨平台行为、资源释放或合并后的关键流程，且必须在合并前修复。
4. 历史代码位置与本次 diff 之间有可验证的直接因果关系，例如父提交通过而当前提交新增诊断，或修改后的签名、DTO、返回值、配置、状态结构直接破坏既有调用者。

不得作为本次 `[Critical]`：

- 目标分支已有、本次审查目标未修改、未触发且未扩大影响面的旧问题。
- 与本次 diff 没有直接因果关系的历史代码、历史 `any`、历史 TODO 或既有风格问题。
- 工作区里的 staged、unstaged、untracked 代码，以及不属于本次审查目标的其他分支、其他 PR 或旧 commit 改动。
- 仅因审查时顺带发现、但本次审查目标不改变其执行路径或风险的问题。

未修改的已提交历史代码既可作为上下文，也必须作为本次修改的影响证据进行检查。finding 仍以 diff 行作为根因锚点；如果本次 diff 导致历史调用者或实现出错，则在同一 Critical 的“受影响历史代码”中逐个列出其文件、准确行号和具体错误。不得把这些位置拆成无因果关系的旧问题，也不得因其不在 changed files 中而省略。

若问题完全位于本次审查目标外，不列入审查结果。需要审查其他范围时，必须由用户另行明确指定，不能混入本次 Critical。

### 未提交代码排除规则

- `git status` / 工作区 diff **只用于识别并排除**未提交代码，不得把 staged / unstaged / untracked 纳入审查。
- 即使同一文件既有已提交变更又有本地未提交修改，也只审已提交 hunk；不得按磁盘上的工作区版本报问题。
- 保留用户已有脏工作区，不 checkout、reset、clean、stash 或覆盖无关改动。
- 不要把本地未提交 diff 与本次 PR/commit diff 合并后再审查。

### 只输出 Critical

默认只输出 `[Critical]`。不输出 `Suggestions` 或 `Nice to have`，也不把非阻塞问题塞进 Critical。若问题达不到合并前必须修复的级别，忽略它；若没有 Critical，明确报告“无”。

## 输入格式说明

在 Cursor 中输入 **`@code-review`**（不是 `/code-review\SKILL.md`），可附带参数：

| 输入示例                         | 说明                                                           |
| -------------------------------- | -------------------------------------------------------------- |
| `@code-review`                   | 未在当前 chat 指定 PR/commit 时：审查当前分支最新 PR；无法确定 PR 时审查最新 commit |
| `@code-review 目标 1.1.8`        | 指定目标分支为 1.1.8；范围仍是当前分支最新 PR，否则最新 commit |
| `@code-review 目标 1.1.8 PR 445` | 当前 chat 指定 PR 445，**只审查该 PR 已提交的变更**（不区分是否已 merge） |
| `@code-review commit abc1234`    | 当前 chat 指定该 commit，只审查该 commit 已提交的变更          |

若用户在当前 chat 粘贴了 PR 链接、PR 号或 commit SHA，即使没有写成上表格式，也视为已指定审查目标，优先于“最新 PR / 最新 commit”。

## 指定 PR 号模式（目标 X PR Y）

当用户输入 `@code-review 目标 1.1.8 PR 445`，或在当前 chat 发送了等价的 PR 号 / PR 链接时，**只审查该 PR 已提交的变更**，不区分该 PR 是否已 merge，也不审查工作区未提交代码。

**执行逻辑：**
1. 执行 `git fetch origin` 确保有最新提交（需联网时先确认任务允许联网）
2. 用 `git status --short` 识别 staged / unstaged / untracked，仅用于排除，不纳入 diff
3. 在目标分支上查找 PR 的 merge 提交：`git log origin/1.1.8 --oneline --merges -50 --grep="445"`
4. **若找到 merge 提交**：使用 `git diff <merge-commit>^1 <merge-commit>` 获取该 PR 相对第一父提交的净变化并审查
5. **若未找到**（PR 未 merge）：使用平台提供的 base/head SHA、PR patch 或 PR refs。只有确认本地 `HEAD` 等于 PR head SHA 时才能使用 `git diff origin/1.1.8...HEAD`。squash/rebase merge 优先平台 patch 或精确 commit range，不能只靠 merge commit grep 猜测
6. 先记录该 PR 的 changed files 和 diff hunks；后续每个 finding 的根因必须回查到该集合，受影响历史位置则必须回查到由该根因新增的错误

**用户操作**：先 `git fetch origin`，再在 Cursor 输入 `@code-review 目标 1.1.8 PR 445` 即可。

## 分支说明（使用前须知）
- **当前分支**：通常为 PR 的**源分支**（如 `1.1.8-ivan-dev`）。未指定 PR 号时，用当前分支与目标分支的已提交 diff，或最新 commit。
- **目标分支**：PR 要合并进去的分支。可由用户指定（如 `目标 1.1.8`），否则按推断规则选择。

## 最小输入模式（推荐）
当用户**仅输入** `@code-review`、未提供其他说明时，按以下流程自动执行，无需用户额外输入：
1. 获取当前分支（源分支）：`git branch --show-current`
2. 只读检查工作区：`git status --short`，识别并排除未提交代码
3. 若当前 chat 已发送 PR 或 commit，使用该目标；否则查找当前分支对应的最新 PR；再否则审查最新 commit `HEAD^..HEAD`（merge commit 用 `HEAD^1..HEAD`）
4. 确定目标分支：若用户已指定则使用该分支；否则依次尝试与当前分支同前缀的版本分支（如当前为 `1.1.8-ivan-dev` 则尝试 `origin/1.1.8`），再尝试 `origin/main`、`origin/master`、`origin/develop`
5. 获取已提交精确 diff（不要把工作区 diff 合并进来）：
   - 最新 PR：先获取 PR base/head SHA 或 PR patch；只有 `HEAD` 等于 PR head SHA 时才可用 `git diff origin/<目标分支>...HEAD`
   - 最新 commit：普通 commit 使用 `git diff HEAD^ HEAD`；merge commit 使用 `git diff HEAD^1 HEAD`；两者都先用同一范围加 `--name-only` 记录 changed files
6. 按审查清单审查该已提交 diff 及其对已提交历史代码的直接影响；只输出 Critical
用户只需在 Cursor 输入框输入 `@code-review`（可附加目标分支、PR 号或 commit）并发送即可。审查时优先 fetch 并直接使用远端 ref / SHA，不要为了审查切换用户当前工作区。

无法唯一确定目标分支，且选择会显著改变审查结果时，先说明候选及依据再向用户确认。

## 使用场景
- 用户仅输入 `@code-review`（最小输入模式：最新 PR，否则最新 commit）
- 用户在当前 chat 指定 PR 号 / PR 链接 / commit（如 `@code-review 目标 1.1.8 PR 445`，只审查该已提交变更）
- 用户提供 Bitbucket/GitHub PR 链接
- 用户请求审查某个已提交分支上的最新 PR 或最新 commit（不是暂存区、不是未提交工作区）

## 快速开始
1. 确定审查目标：当前 chat 发送的 PR/commit，否则最新 PR，否则最新 commit
2. 在本地获取该目标的**已提交** diff（见下方「Bitbucket PR 工作流」），并用 `git status` 排除未提交代码
3. 记录 changed files 与 diff hunks
4. 按审查清单逐项检查，只对以 diff 内改动为根因的问题报 Critical，并列出其直接破坏的历史代码位置
5. 输出前做范围复核；按要求格式只输出 Critical

## Bitbucket PR 工作流
Cursor 无法直接通过 Bitbucket URL 获取 PR 内容时，先在本地拉取 PR 远端 ref，不切换工作区。
**步骤 1：拉取 PR 远端 ref**
从 PR 页面（例如 `https://bitbucket.org/healshealthcare/csx-mobile/pull-requests/437/overview`）获取源分支名和目标分支名，然后执行：
```bash
git fetch origin <源分支名>:refs/remotes/origin/<源分支名> <目标分支名>:refs/remotes/origin/<目标分支名>
```
**步骤 2：获取已提交 diff**
```bash
git status --short
# 优先使用 Bitbucket 提供的 PR base/head SHA，不要叠加工作区 diff
git diff <base-sha>...<head-sha> --name-only
git diff <base-sha>...<head-sha>
```
只有确认 `HEAD` 就是该 PR 的 head SHA 时，才可将 `<head-sha>` 替换为 `HEAD`。
**步骤 3：在 Cursor Chat 中**
用户可说：「用 @code-review 审查此 PR，源分支 xxx，目标 main」，并发送 PR 链接 / PR 号。不要依赖工作区未提交文件，也不要把未提交 diff 粘贴进来当作审查范围。

## 关联历史代码影响追踪（强制）

- 对 diff 中修改的函数签名、DTO/interface、返回值、导出、配置、状态结构、公共 helper、API schema 和持久化结构，搜索仓库内所有已提交引用，不只阅读 changed files。
- 用 `rg`、语言服务、调用层级、类型检查或测试定位调用者、实现、覆盖/重载和相关测试；工作区存在未提交内容时，以目标 commit 的文件内容和行号为准。
- 对类型、构建、lint 或测试问题尽量比较父提交/base 与当前提交/head。只把当前提交新增或扩大的诊断归因于本次修改，排除基线已有错误。
- 若同一根因导致多个历史位置失败，可合并为一条 Critical，但必须列出每个已确认位置及其错误代码/失败条件；不得只写“有 16 个错误”、只列代表性位置或只列 DTO 定义。
- 历史位置是本次 Critical 的影响范围和修复位置，不代表允许进行全仓库旧问题审计。

## 审查清单
审查根因始终是本次审查目标的已提交 diff；审查影响必须覆盖该 diff 直接破坏的已提交历史代码，但不得使用工作区未提交版本或扩展到无因果关系的旧问题。

### 通用（所有技术栈）
- [ ] 逻辑正确且处理边界情况
- [ ] 无安全问题（注入、XSS、敏感数据暴露、不安全反序列化、SSRF）
- [ ] 代码符合项目约定
- [ ] 函数职责单一、体量适中
- [ ] 错误处理充分（异步必有 try-catch / catch / error 边界）
- [ ] 测试覆盖变更（如适用）
- [ ] 无硬编码密钥、token、凭证或私有 URL
- [ ] 无明显性能陷阱（循环内 DOM/网络、N+1 查询、未释放的监听/定时器）

### 按技术栈触发（命中对应文件类型时才查）
- [ ] **TypeScript（.ts/.tsx/lang="ts"）**：见「**TypeScript 专项**」，必须扫描 diff 中新增 / 扩大的 `any`
- [ ] **JavaScript（.js/.jsx 无 TS）**：见「**JavaScript 专项**」，重点防隐式类型错误、`==`、未声明变量
- [ ] **React**：effect 依赖数组、key、不必要 re-render、状态更新闭包陷阱
- [ ] **React Native**：Platform.OS 分支、键盘、内存泄漏、双端字段差异、列表性能
- [ ] **Vue 2**：见「**Vue 专项**」，Options API / mixins、`this` 响应式、`v-for` 有 key
- [ ] **Vue 3**：见「**Vue 专项**」，Composition API、`ref/reactive` 误用、`<script setup>`
- [ ] **微信小程序**：页面生命周期、`setData` 性能、分包与体积、授权流程
- [ ] **Flutter**：见「**Flutter 专项**」，Widget 重建、`setState` 范围、`dispose`、`BuildContext` 跨异步
- [ ] **Node.js**：见「**Node.js 专项**」，异步错误、阻塞事件循环、输入校验、依赖与配置安全
- [ ] **iOS 原生（.swift/.m/.mm）**：见「**原生 iOS/Android 专项**」，retain cycle、主线程 UI、可选解包
- [ ] **Android 原生（.kt/.java）**：见「**原生 iOS/Android 专项**」，生命周期、空安全、主线程阻塞
- [ ] **HTML/CSS**：见「**HTML/CSS 专项**」，语义化、可访问性、布局健壮性、无 `!important` 滥用

未达到合并前必须修复的问题直接忽略，不输出 Suggestions。

## TypeScript 专项
**适用范围**：本次已提交 diff 中涉及 `.ts`、`.tsx`，以及 Vue SFC 中带 `lang="ts"` 的 `<script>`。与本次 diff 无因果关系的历史类型问题不报；本次修改新触发的历史调用点类型错误必须报告并列出准确位置。

**必查项（缺失一律报 [Critical]）**  
对本次审查目标 diff 范围内 **新增或修改** 的以下内容，须具备 **显式类型**：
- **参数**：每个形参均有类型注解（禁止依赖隐式 `any`；禁止裸 `any` 作为“逃避注释”，除非项目已有明确豁免条款且本 PR/commit 未扩大使用面）。
- **返回值**：函数/方法/async 函数须有显式返回类型（`async` 须写 `Promise<...>` 或等价明确形式）。
- **新增 / 扩大的 `any` 使用面**：本次 diff 中新增、复制、移动到新代码路径、或把原本更窄类型放宽为 `any` 的位置，必须逐项检查；不能只因为项目历史已有 `any` 就跳过。历史 `any` 未被本次审查目标修改或扩大时，不得报 Critical。

**审查对象包括**：导出的函数/方法、组件外的命名函数、类方法、`const fn = (...) => ...` 等独立声明；class 字段上的方法签名同等要求。以上均须位于本次已提交 diff 的新增或修改行。

### `any` 使用审查规则

**扫描要求**：
- Review 本次已提交 diff 时必须主动扫描新增行中的 `any`，包括但不限于：`props: any`、`item: any`、`e: any`、`data: any[]`、`useRef<any>`、`useState<any>`、`Record<string, any>`、回调参数类型、API 响应类型、组件 props 类型、列表 item 类型。
- 若 `any` 来自未改动旧代码，或只存在于工作区未提交内容中，默认不单独报；但如果本次审查目标修改了该函数签名、复制旧写法到新函数、或扩大调用面，按新增 / 扩大使用处理。
- 如果同一文件出现多处同类 `any`，可以合并成一条 finding，但必须列出代表性位置和建议替代类型。

**严重级别**：
- **[Critical]**：新增 / 扩大的 `any` 出现在公共接口、组件 props、API DTO / response、导航参数、全局状态、表单 payload、业务核心函数入参 / 返回值、或会掩盖运行时字段差异的位置。
- **[Critical]**：使用 `any` 导致 review 无法确认字段是否存在、平台差异是否被处理、或错误 payload 是否会进入 API / navigation / storage。
- 新增 `any` 只限于局部 UI 回调 / 第三方库事件，且可用现有类型、轻量 interface、`unknown` + type guard、或泛型很容易收紧时：**不输出 finding**。
- 历史遗留 `any` 未被本次审查目标扩大：不报，也不输出 Suggestions。

**允许豁免但必须说明原因**：
- 第三方库类型缺失且短期无法安装 / 引入类型定义。
- 动态 JSON、埋点、兼容旧接口等场景确实无法在当前 PR 内完整建模。
- 临时桥接代码已经用局部注释说明原因，并且未流入公共接口、API payload、navigation params 或持久化数据。

**推荐替代方式**：
- 组件 props：新增或复用 `Props` interface。
- 列表 item：为 `FlatList`、`renderItem`、`keyExtractor` 使用明确 item interface。
- 事件参数：使用 RN / React / 第三方库导出的事件类型；没有类型时优先 `unknown` 后窄化。
- API / DTO：补充 DTO / response interface，或使用已有 `@api/api-types.ts` 类型。
- 动态对象：优先 `Record<string, unknown>`，读取字段前做类型收窄。

**不强制本条的情况**（本条不适用时不因类型报 Critical）：
- 纯 `.js` / `.jsx` 或未启用 TS 的脚本
- 第三方类型声明文件（`.d.ts`）中以声明语句体现的签名
- 仅作临时桥接、且文件顶行或区块已有 `eslint-disable`/`@ts-expect-error` 且与团队规范一致的一次性改动（须在 PR 中可说明原因；否则仍报 Critical）
- 未出现在本次审查目标已提交 diff 中的代码

**报告写法**：
- 显式类型缺失：`[文件:行号] 函数/方法名：缺少参数类型 / 缺少返回值类型（或隐式 any）`
- `any` 使用：`[文件:行号] 新增 / 扩大的 any 使用：当前位置为什么会掩盖字段风险；建议改成的具体 interface / unknown / 泛型`
- 若多项缺失可合并为一条 Critical，但必须列出位置、影响范围和至少一个可落地的替代类型示例。
- 修改函数参数、返回值、DTO、泛型或公共 interface 后，必须对父提交/base 与当前提交/head 做差异化类型诊断；在 `受影响历史代码` 下逐个列出本次新增的调用点文件、行号、`TSxxxx` 和失败表达式，不得只写诊断总数。

**手动自测（类型类 Critical）**：至少执行项目约定的静态检查（如 `yarn lint`、`tsc --noEmit` 或 CI 等价步骤），说明当前是否失败；修复后同一命令应通过。无法本地跑命令时写明「暂无稳定手测路径」及原因。

## 反馈格式
只使用以下标签（按规则不使用 emoji）：
- **[Critical]**: 合并前必须修复

不输出 **[Suggestion]**，不输出 **[Nice to have]**。非阻塞问题直接省略，不能人为提高严重级别。不要把“可能有问题”“建议确认”直接升级为 finding；先证明具体失败路径、契约冲突或可复现风险。若证据不足，明确说明不确定性，且不得写成 Critical。

## Critical 修复输出要求
- 每个 Critical 必须区分：
  - `本次修改位置`：位于精确 diff 中的根因文件和行号。
  - `受影响历史代码`：被本次修改直接触发失败的已提交历史位置。逐个列出文件、准确行号、错误代码/失败条件和受影响表达式；没有时写“无”。
- 同一根因可以合并多个历史错误位置，但不能只给数量、模糊范围或代表性示例。修复说明必须同时覆盖根因位置和需要同步调整的历史调用位置。
- 对每个 **[Critical]**，默认必须额外给出一段 **“修改建议”**，明确告诉开发者应如何把代码改正确。这是 Critical 的修复说明，不是 Suggestions 分区。
- `修改建议` 不能只写抽象方向（如“补一下判空”“修正依赖”）；必须尽量给到**可直接落地的代码级改法**，至少满足以下其一：
  - 指出应修改的具体语句、依赖数组、类型签名、条件分支、返回值或调用位置
  - 给出 1 段最小必要的替换后代码示例
  - 给出明确的 before / after 说明，让开发者能直接按说明改
- 若根据当前 diff 和上下文，已经可以 reasonably 推断出正确写法，则**直接写出推荐代码**，不要只停留在“建议检查/建议确认”。
- 若无法安全确定唯一正确实现，必须明确写出 **“为什么当前上下文不足以给出唯一正确代码”**，并同时提供：
  - 最可能的修复方向
  - 需要补充确认的上下文
  - 一份尽可能接近可用的代码骨架 / 伪补丁
- 对 **TypeScript 类 Critical**，优先直接补出缺失的参数类型、返回值类型、泛型或接口定义示例。
- 对 **`any` 类 Critical**，必须明确写出推荐替代类型；若无法确定唯一类型，必须给出 `unknown` + type guard 或最小 interface 骨架，不能只写“避免 any”。
- 对 **React / React Native 类 Critical**，优先直接补出依赖数组、状态更新写法、判空分支、平台分支、清理逻辑或 JSX 改法示例。
- 对 **配置 / 接口 / 平台差异 类 Critical**，优先写出应改成的字段名、配置项、fallback 逻辑或 `Platform.OS` 分支示例。
- 若一个 Critical 同时涉及“问题原因”和“修复代码”，输出顺序固定为：
  - 问题
  - 修改建议
  - 手动自测

## 修改建议写法要求
- 优先使用以下标题：`修改建议：`
- 若需要代码片段，默认用 fenced code block 展示，语言标签与项目一致（如 `ts`、`tsx`、`js`、`swift`、`kotlin`）。
- 代码片段应尽量是**最小必要修改**，避免把整文件大段搬出来。
- 如果修复依赖于“把 A 改成 B”，应显式写出：
  - 现在的问题代码是什么
  - 应改成什么
  - 改完后为什么正确
- 如果问题本质上不是“缺代码”，而是“逻辑位置错了 / 生命周期错了 / 调用时机错了”，也必须给出推荐的重构落点，而不是只描述风险。

## 手动自测流程要求
- 对每个 **[Critical]** 都应补充一段**手动自测流程**，用于帮助提 review 的人或开发者自行复现、验证或回归确认。不给 Suggestions，因此也不为非 Critical 写手测。
- 手动自测流程优先服务于**真实设备/真实页面/真实交互**；只有当问题难以通过真实路径稳定触发时，才说明需要**临时插桩 / mock / 日志辅助**。
- 若问题**可以稳定手测**，至少给出以下信息：
  - **前置条件**：账号、权限、页面入口、测试数据、开关状态
  - **操作步骤**：按时间顺序的点击、跳转、切后台、切权限、刷新等动作
  - **预期结果**：当前错误表现、修复后应看到的表现，必要时区分“当前实际结果 / 正确结果”
- 若问题**不容易直接手测**，需要明确说明原因，并给出最小可行的模拟方案，例如：
  - 临时 mock 接口成功 / 失败
  - 临时让函数固定 return false / throw error
  - 临时打印关键日志或放宽页面过滤条件
- 若某个问题确实**无法合理设计手测流程**，要明确写出“暂无稳定手测路径”，并说明为什么。

## React Native 差异化手测要求
- 对 React Native 项目的 **[Critical]**，默认优先补充 **Android** 与 **iOS** 的差异化手测步骤或差异化结论。
- 若问题只在单平台成立，要明确写出：
  - **Android**：如何触发、预期现象、是否稳定复现
  - **iOS**：如何触发、预期现象、是否同样受影响；若未验证要明确说明“未验证”
- 若问题与以下因素相关，手测步骤中应优先体现平台差异：
  - 系统权限（相机、相册、日历、通知、定位、蓝牙等）
  - 前后台切换 / 冷启动 / 热启动 / 系统回收进程
  - 键盘弹起、Safe Area、状态栏、刘海屏、沉浸式导航
  - 原生组件行为差异、第三方 RN 库在双平台返回字段不一致
- 若 Android 与 iOS 结论一致，也应明确写成：
  - **Android / iOS**：按同一流程验证，预期一致
- 若当前 review 无法完成双平台验证，不要假设一致，必须标注：
  - **Android**：已验证 / 未验证
  - **iOS**：已验证 / 未验证

## 输出前范围复核

输出前逐条检查，任一 Critical 未通过就删除；不得降级成 Suggestions，也不得放进“PR 外备注 / 顺带发现”：

- 根因路径是否在本次审查目标（当前 chat 的 PR/commit，或最新 PR/commit）的 changed files 中；根因行号或 hunk 是否由该已提交 diff 修改。
- 列出的历史代码位置是否确实被该 diff 影响；若撤销本次改动或使用父提交契约后错误仍存在，则不得列入。
- 是否已列出同一根因下所有已确认的受影响位置，而不是只给数量、模糊范围或代表性示例。
- 问题是否在目标分支上本来就存在，且本次 diff 并未引入或扩大风险。
- 严重级别是否达到合并前必须修复；达不到则删除，不改写成 Suggestions。

## 输出模板
```markdown
# Code Review: [PR/分支名或 commit]

## 摘要
[审查范围：当前 chat 指定的 PR/commit，或最新 PR / 最新 commit；base/head 或 commit range；changed files 数；总体结论]

## Critical
- [Critical] [问题描述]
  本次修改位置：[文件:行号]
  受影响历史代码：

    - [文件:行号] [错误代码或具体失败条件]
    - [文件:行号] [错误代码或具体失败条件]

  问题：[触发条件与影响]
  修改建议：
  ```tsx
  // put the minimal correct fix here
  ```
  手动自测：
  前置条件：[...]
  步骤：
  1. ...
  2. ...
  预期结果：修复前 [...]；修复后 [...]
  平台差异（React Native 适用时）：
  Android：[...]
  iOS：[...]

## 验证边界
- 已执行：[静态检查、测试或只读验证]
- 未执行：[未运行项及原因]
```

没有 Critical 时写“无”，并明确写“未发现本次审查目标引入的合并阻塞问题”。不要为了填满模板编造问题，也不要补充 Suggestions 或 Nice to have。

## JavaScript 专项
**适用范围**：本次已提交 diff 中涉及未启用 TS 的 `.js` / `.jsx` / `.mjs`、Vue SFC 中无 `lang="ts"` 的 `<script>`。
**必查项（仅达到合并阻塞时报 [Critical]，否则忽略）**：
- **隐式类型 / 弱比较**：新增 `==` / `!=` 应改为 `===` / `!==`（除与 `null` 宽松判空可豁免，但需一致）。只有会改变业务判断结果时才报 Critical。
- **未声明 / 提升陷阱**：禁用隐式全局变量；优先 `const`，需要重赋值才用 `let`，禁止新增 `var`。
- **异步**：`Promise` 必须有 `.catch` 或外层 `try-catch`；禁止漏 `await` 导致的“伪同步”；禁止 `forEach` 中写 `await`（应用 `for...of` 或 `Promise.all`）。
- **可选链 / 判空**：访问可能为 `undefined` 的链路用 `?.` 与 `??`，避免 `Cannot read properties of undefined`。
- **相等性与拷贝**：注意对象 / 数组浅拷贝、引用共享导致的状态污染。
- 缺少 JSDoc 等纯风格偏好不报，也不输出 Suggestions。

## React 专项
- **effect 依赖**：`useEffect` / `useMemo` / `useCallback` 依赖数组必须完整；遗漏依赖或滥用空数组导致闭包旧值 → [Critical]。
- **key**：列表 `key` 必须稳定唯一，禁止用 index 作为可重排列表的 key。
- **状态更新**：基于旧 state 的更新用函数式 `setX(prev => ...)`；避免在渲染期间 setState。
- **清理**：订阅 / 定时器 / 事件监听必须在 effect return 中清理。
- **性能**：仅当本次 diff 引入真实重渲染或资源风险时才报 Critical；不为可选 `memo` / `useMemo` / `useCallback` 输出 Suggestions。

## React Native 专项
- **平台差异**：使用第三方库 / 原生桥接字段前核对 `iOS ONLY` / `ANDROID ONLY` / `deprecated` 标记；共享逻辑里出现单端字段必须有 `Platform.OS` 分支与另一端 fallback → [Critical]。
- **样式**：优先 `StyleSheet.create()`；注意 Safe Area、状态栏、刘海屏、键盘遮挡（`KeyboardAvoidingView`）。仅当本次 diff 引入明显错位 / 遮挡 / 不可用时才报 Critical。
- **列表与图片**：长列表用 `FlatList` / `SectionList` 并设 `keyExtractor`；大图优先 `FastImage`，警惕内存泄漏。
- **内存 / 生命周期**：监听器、计时器、订阅在卸载时清理；前后台切换、冷热启动、进程回收的边界。
- **手测**：默认按「React Native 差异化手测要求」给出 Android / iOS 分别结论。

## Vue 专项
**先判断 Vue 2 还是 Vue 3**（看 SFC 写法、`package.json` 版本或 API 形态），按版本套规则。
**Vue 2（Options API / mixins）**：
- 响应式：新增对象属性需 `Vue.set` / `this.$set`；数组按索引赋值 / 改 `length` 不触发更新 → [Critical]。
- `v-for` 必须有稳定 `key`；`v-if` 与 `v-for` 不应同层混用。
- 逻辑复用用 mixins 时注意命名冲突与来源不清。仅当本次 diff 引入冲突并会造成错误行为时才报 Critical。
- `this` 上下文：避免在回调中丢失 `this`（箭头函数 vs 普通函数）。
**Vue 3（Composition API）**：
- `ref` vs `reactive` 误用：`reactive` 解构会丢响应式（用 `toRefs`）；模板外访问 `ref` 漏 `.value`。会造成错误数据或静默失效时 → [Critical]；仅风格问题则忽略。
- `<script setup>` 下 `defineProps` / `defineEmits` 类型与默认值；props 只读不可直接改。
- `watch` / `watchEffect` 的依赖与清理（`onCleanup`）、`computed` 不应有副作用。
- 生命周期钩子（`onMounted` / `onUnmounted`）中注册的监听需对应清理。
- `v-for` 必须有稳定 `key`。

## 微信小程序专项
- **生命周期**：`onLoad` / `onShow` / `onReady` / `onUnload` 使用正确；页面与组件生命周期不混淆。
- **`setData` 性能**：避免一次 `setData` 大对象 / 高频调用；只传变化字段，长列表慎用全量刷新。会造成卡顿、丢更新或错误渲染时 → [Critical]；一般性能偏好忽略。
- **数据绑定与 WXML**：`wx:for` 必须有 `wx:key`；事件传参用 `data-*` + `e.currentTarget.dataset`。
- **包体积与分包**：主包体积、分包加载、按需注入；图片 / 资源是否走 CDN。仅当本次 diff 明显引入体积或加载阻塞时才报 Critical。
- **授权 / API**：`wx.login` / `getUserProfile` / 权限申请流程合规；网络请求域名白名单、超时与失败处理。

## Flutter 专项
**适用范围**：本次已提交 diff 中的 `.dart` 文件。
- **Widget 重建**：`build` 内避免创建昂贵对象 / 发起请求；尽量 `const` 构造；`setState` 范围尽量小，必要时拆分 Widget 或用局部状态。
- **资源释放**：`AnimationController`、`TextEditingController`、`StreamSubscription`、`ScrollController` 等必须在 `dispose` 中释放 → [Critical]。
- **异步与 BuildContext**：`await` 之后使用 `context` 前必须检查 `if (!mounted) return;` → [Critical]。
- **异步 UI**：`FutureBuilder` / `StreamBuilder` 须处理 loading / error / empty 三态。
- **空安全**：避免滥用 `!`（强制解包）；优先 `?.`、`??`、`late` 的合理使用。
- **状态管理**：与项目既有方案（Provider / Riverpod / Bloc / GetX）一致，不引入混用。
- **性能**：长列表用 `ListView.builder`；避免不必要的 `Opacity` / `ClipRRect` 嵌套。仅当本次 diff 引入真实卡顿或泄漏时才报 Critical。

## Node.js 专项
- **异步错误**：`async` 函数必有 `try-catch` 或在调用处兜底；未处理的 `Promise` rejection、回调风格漏处理 `err` → [Critical]。
- **事件循环**：避免在请求路径中做同步阻塞（大文件同步 IO、`JSON.parse` 超大体、`crypto` 同步、长 CPU 循环）；CPU 密集任务考虑 worker / 队列。
- **输入校验与安全**：所有外部入参（body / query / params / header）做校验与转义；防注入（SQL / NoSQL / 命令）、路径穿越、SSRF；`dotenv` 管理密钥，禁止硬编码。
- **HTTP / 中间件**：中间件顺序正确；错误统一处理（error-handling middleware）；超时、重试、连接池配置；响应不泄漏堆栈 / 内部细节。
- **资源管理**：数据库连接、文件句柄、流正确关闭；监听器避免泄漏（`removeListener`）。
- **日志**：关键路径有结构化日志（如 Winston），不在日志中打印敏感信息。

## 原生 iOS / Android 专项
**iOS（Swift / Objective-C）**：
- **内存**：闭包 / delegate 的 retain cycle，必要时 `[weak self]` / `weak` delegate → [Critical]。
- **线程**：所有 UI 更新必须在主线程（`DispatchQueue.main`）；耗时操作放后台队列。
- **可选值**：避免强制解包 `!` / `as!`，优先 `if let` / `guard let` / `??`。
- **生命周期**：`viewDidLoad` / `viewWillAppear` 等职责正确，避免重复注册通知。
**Android（Kotlin / Java）**：
- **生命周期**：`Activity` / `Fragment` 生命周期内注册的监听 / 协程在对应回调取消（`onDestroy` / `viewLifecycleScope`）→ [Critical]。
- **空安全（Kotlin）**：避免滥用 `!!`；合理用 `?.`、`?:`、`lateinit`。
- **线程**：主线程不做网络 / 磁盘 IO；用协程 / `WorkManager` / 线程池；UI 更新回主线程。
- **资源**：`Cursor`、`InputStream`、监听器及时关闭 / 注销，防泄漏。

## HTML/CSS 专项
- **语义化与可访问性**：使用语义标签；交互元素有可聚焦性、`aria-*`、`alt`、label 关联。关键无障碍缺失且由本次 diff 引入、会导致不可用时 → [Critical]；一般语义偏好忽略，不输出 Suggestions。
- **布局健壮性**：优先 Flex / Grid；避免写死宽高导致溢出；考虑长文本、空数据、不同视口。
- **CSS 维护性**：避免 `!important` 滥用与高特异性选择器；类名遵循项目约定（BEM / 模块化 / scoped）。仅当本次 diff 造成明显覆盖错误或不可维护回归时才报 Critical。
- **性能**：避免会触发重排 / 重绘的高频属性动画；优先 `transform` / `opacity`；图片设尺寸与懒加载。
- **兼容性**：用到较新特性时确认目标浏览器 / WebView 支持，必要时降级。

## 行为边界
- Code review 默认是只读任务；不修改业务代码、提交、推送或在 PR 平台发评论，除非用户明确要求。
- 不把 lint、类型检查或测试未运行写成已经通过。
- 不泄露 token、Cookie、Authorization、私有凭证或完整敏感响应。
- 必须追踪本次 diff 对已提交历史代码的直接影响，但不扩展为无因果关系的全仓库旧问题审计；不把未提交代码纳入审查，不输出 Suggestions。
