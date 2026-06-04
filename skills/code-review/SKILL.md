---
name: code-review
description: 按团队标准审查代码质量、安全性与可维护性，覆盖 React、React Native、Vue 2、Vue 3、TypeScript、JavaScript、HTML、CSS、微信小程序、Flutter、iOS、Android、Node.js 全栈。适用于审查 pull request、代码变更、Bitbucket/GitHub PR，或用户请求 code review / 审查代码 时。
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

## 输入格式说明

在 Cursor 中输入 **`@code-review`**（不是 `/code-review\SKILL.md`），可附带参数：

| 输入示例 | 说明 |
|----------|------|
| `@code-review` | 最小输入，自动推断目标分支 |
| `@code-review 目标 1.1.8` | 指定目标分支为 1.1.8 |
| `@code-review 目标 1.1.8 PR 445` | 指定目标 + PR 号，**只审查该 PR 的变更**（不区分是否已 merge） |

## 指定 PR 号模式（目标 X PR Y）

当用户输入 `@code-review 目标 1.1.8 PR 445` 时，**只审查 PR 445 引入的变更**，不区分该 PR 是否已 merge。

**执行逻辑：**
1. 执行 `git fetch origin` 确保有最新提交
2. 在目标分支上查找 PR 的 merge 提交：`git log origin/1.1.8 --oneline --merges -50 --grep="445"`
3. **若找到 merge 提交**：使用 `git show <merge-commit>` 获取该 PR 的精确变更并审查
4. **若未找到**（PR 未 merge）：假定当前分支为 PR 源分支，使用 `git diff origin/1.1.8...HEAD` 获取变更并审查（需先 checkout 到 PR 源分支并 `git pull`）

**用户操作**：先 `git fetch origin`，再在 Cursor 输入 `@code-review 目标 1.1.8 PR 445` 即可。

## 分支说明（使用前须知）
- **当前分支**：通常为 PR 的**源分支**（如 `1.1.8-ivan-dev`）。未指定 PR 号时，用当前分支与目标分支的 diff。
- **目标分支**：PR 要合并进去的分支。可由用户指定（如 `目标 1.1.8`），否则按推断规则选择。

## 最小输入模式（推荐）
当用户**仅输入** `@code-review`、未提供其他说明时，按以下流程自动执行，无需用户额外输入：
1. 获取当前分支（源分支）：`git branch --show-current`
2. 确定目标分支：若用户已指定则使用该分支；否则依次尝试 `origin/main`、`origin/master`、`origin/develop`，或与当前分支同前缀的版本分支（如当前为 `1.1.8-ivan-dev` 则尝试 `origin/1.1.8`）
3. 获取 diff：`git diff origin/<目标分支>...HEAD --name-only` 和 `git diff origin/<目标分支>...HEAD`
4. 按审查清单对变更进行审查
用户只需在本地 `git pull` 或 `git checkout <源分支名>` 后，在 Cursor 输入框输入 `@code-review`（可附加目标分支）并发送即可。

## 使用场景
- 用户仅输入 `@code-review`（最小输入模式）
- 用户指定 PR 号（如 `@code-review 目标 1.1.8 PR 445`，只审查该 PR 变更，不区分是否已 merge）
- 用户提供 Bitbucket/GitHub PR 链接
- 用户请求审查暂存变更或某个分支

## 快速开始
1. 在本地获取 PR 的 diff（见下方「Bitbucket PR 工作流」）
2. 确定变更文件
3. 按审查清单逐项检查
4. 按要求格式输出反馈

## Bitbucket PR 工作流
Cursor 无法直接通过 Bitbucket URL 获取 PR 内容，需用户先在本地拉取分支。
**步骤 1：拉取 PR 分支**
从 PR 页面（例如 `https://bitbucket.org/healshealthcare/csx-mobile/pull-requests/437/overview`）获取源分支名，然后执行：
```bash
git fetch origin
git checkout <源分支名>
# 或创建临时分支: git checkout -b pr-437 origin/<源分支名>
```
**步骤 2：获取 diff**
```bash
# 与目标分支对比（如 main、develop）
git diff origin/<目标分支>...HEAD --name-only
git diff origin/<目标分支>...HEAD
```
**步骤 3：在 Cursor Chat 中**
用户可说：「用 @code-review 审查此 PR，源分支 xxx，目标 main」，并 @ 变更文件，或粘贴 `git diff` 输出。

## 审查清单
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

## TypeScript 专项
**适用范围**：本次 diff 中涉及 `.ts`、`.tsx`，以及 Vue SFC 中带 `lang="ts"` 的 `<script>`。

**必查项（缺失一律报 [Critical]）**  
对变更范围内 **新增或修改** 的以下内容，须具备 **显式类型**：
- **参数**：每个形参均有类型注解（禁止依赖隐式 `any`；禁止裸 `any` 作为“逃避注释”，除非项目已有明确豁免条款且本 PR 未扩大使用面）。
- **返回值**：函数/方法/async 函数须有显式返回类型（`async` 须写 `Promise<...>` 或等价明确形式）。
- **新增 / 扩大的 `any` 使用面**：本次 diff 中新增、复制、移动到新代码路径、或把原本更窄类型放宽为 `any` 的位置，必须逐项检查并报告；不能只因为项目历史已有 `any` 就跳过。

**审查对象包括**：导出的函数/方法、组件外的命名函数、类方法、`const fn = (...) => ...` 等独立声明；class 字段上的方法签名同等要求。

### `any` 使用审查规则

**扫描要求**：
- Review diff 时必须主动扫描新增行中的 `any`，包括但不限于：`props: any`、`item: any`、`e: any`、`data: any[]`、`useRef<any>`、`useState<any>`、`Record<string, any>`、回调参数类型、API 响应类型、组件 props 类型、列表 item 类型。
- 若 `any` 来自未改动旧代码，默认不单独报；但如果本 PR 修改了该函数签名、复制旧写法到新函数、或扩大调用面，按新增 / 扩大使用处理。
- 如果同一文件出现多处同类 `any`，可以合并成一条 finding，但必须列出代表性位置和建议替代类型。

**严重级别**：
- **[Critical]**：新增 / 扩大的 `any` 出现在公共接口、组件 props、API DTO / response、导航参数、全局状态、表单 payload、业务核心函数入参 / 返回值、或会掩盖运行时字段差异的位置。
- **[Critical]**：使用 `any` 导致 review 无法确认字段是否存在、平台差异是否被处理、或错误 payload 是否会进入 API / navigation / storage。
- **[Suggestion]**：新增 `any` 只限于局部 UI 回调 / 第三方库事件，且可用现有类型、轻量 interface、`unknown` + type guard、或泛型很容易收紧。
- **[Nice to have]**：历史遗留 `any` 未被本 PR 扩大，但当前变更附近已有清晰替代类型；可建议后续收敛，不阻塞本 PR。

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

**报告写法**：
- 显式类型缺失：`[文件:行号] 函数/方法名：缺少参数类型 / 缺少返回值类型（或隐式 any）`
- `any` 使用：`[文件:行号] 新增 / 扩大的 any 使用：当前位置为什么会掩盖字段风险；建议改成的具体 interface / unknown / 泛型`
- 若多项缺失可合并为一条 Critical，但必须列出位置、影响范围和至少一个可落地的替代类型示例。

**手动自测（类型类 Critical）**：至少执行项目约定的静态检查（如 `yarn lint`、`tsc --noEmit` 或 CI 等价步骤），说明当前是否失败；修复后同一命令应通过。无法本地跑命令时写明「暂无稳定手测路径」及原因。

## 反馈格式
使用以下标签（按规则不使用 emoji）：
- **[Critical]**: 合并前必须修复
- **[Suggestion]**: 建议改进
- **[Nice to have]**: 可选优化

## Critical 修复输出要求
- 对每个 **[Critical]**，默认必须额外给出一段 **“修改建议”**，明确告诉开发者应如何把代码改正确。
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
- 对 **`any` 类 Critical / Suggestion**，必须明确写出推荐替代类型；若无法确定唯一类型，必须给出 `unknown` + type guard 或最小 interface 骨架，不能只写“避免 any”。
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
- 对每个 **[Critical]** 和 **[Suggestion]**，默认都应补充一段**手动自测流程**，用于帮助提 review 的人或开发者自行复现、验证或回归确认。
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
- `Nice to have` 默认**不强制**附带手动自测流程，除非该建议本身带有明显的行为风险。

## React Native 差异化手测要求
- 对 React Native 项目的 **[Critical]** 和 **[Suggestion]**，默认优先补充 **Android** 与 **iOS** 的差异化手测步骤或差异化结论。
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

## 输出模板
```markdown
# Code Review: [PR/分支名]
## 摘要
[1–2 句概述]
## Critical
- [文件:行号] [问题描述]
  修改建议：
  ```tsx
  // put the minimal correct fix here
  ```
  手动自测：
  前置条件：[...]
  步骤：
  1. ...
  2. ...
  预期结果：[...]
  平台差异（React Native 适用时）：
  Android：[...]
  iOS：[...]
## Suggestions
- [文件:行号] [建议]
  手动自测：
  前置条件：[...]
  步骤：
  1. ...
  2. ...
  预期结果：[...]
  平台差异（React Native 适用时）：
  Android：[...]
  iOS：[...]
## Nice to have
- [可选改进]
```

## JavaScript 专项
**适用范围**：本次 diff 中涉及未启用 TS 的 `.js` / `.jsx` / `.mjs`、Vue SFC 中无 `lang="ts"` 的 `<script>`。
**必查项（命中报 [Critical] 或 [Suggestion]）**：
- **隐式类型 / 弱比较**：新增 `==` / `!=` 应改为 `===` / `!==`（除与 `null` 宽松判空可豁免，但需一致）。
- **未声明 / 提升陷阱**：禁用隐式全局变量；优先 `const`，需要重赋值才用 `let`，禁止新增 `var`。
- **异步**：`Promise` 必须有 `.catch` 或外层 `try-catch`；禁止漏 `await` 导致的“伪同步”；禁止 `forEach` 中写 `await`（应用 `for...of` 或 `Promise.all`）。
- **可选链 / 判空**：访问可能为 `undefined` 的链路用 `?.` 与 `??`，避免 `Cannot read properties of undefined`。
- **相等性与拷贝**：注意对象 / 数组浅拷贝、引用共享导致的状态污染。
- **建议**：缺少类型保护的公共函数可建议补 JSDoc（`@param` / `@returns`），便于编辑器推断，不阻塞合并。

## React 专项
- **effect 依赖**：`useEffect` / `useMemo` / `useCallback` 依赖数组必须完整；遗漏依赖或滥用空数组导致闭包旧值 → [Critical]。
- **key**：列表 `key` 必须稳定唯一，禁止用 index 作为可重排列表的 key。
- **状态更新**：基于旧 state 的更新用函数式 `setX(prev => ...)`；避免在渲染期间 setState。
- **清理**：订阅 / 定时器 / 事件监听必须在 effect return 中清理。
- **性能**：识别可被 `memo` / `useMemo` / `useCallback` 优化的高频重渲染，但不为优化而过度包裹。

## React Native 专项
- **平台差异**：使用第三方库 / 原生桥接字段前核对 `iOS ONLY` / `ANDROID ONLY` / `deprecated` 标记；共享逻辑里出现单端字段必须有 `Platform.OS` 分支与另一端 fallback → [Critical]。
- **样式**：优先 `StyleSheet.create()`；注意 Safe Area、状态栏、刘海屏、键盘遮挡（`KeyboardAvoidingView`）。
- **列表与图片**：长列表用 `FlatList` / `SectionList` 并设 `keyExtractor`；大图优先 `FastImage`，警惕内存泄漏。
- **内存 / 生命周期**：监听器、计时器、订阅在卸载时清理；前后台切换、冷热启动、进程回收的边界。
- **手测**：默认按「React Native 差异化手测要求」给出 Android / iOS 分别结论。

## Vue 专项
**先判断 Vue 2 还是 Vue 3**（看 SFC 写法、`package.json` 版本或 API 形态），按版本套规则。
**Vue 2（Options API / mixins）**：
- 响应式：新增对象属性需 `Vue.set` / `this.$set`；数组按索引赋值 / 改 `length` 不触发更新 → [Critical]。
- `v-for` 必须有稳定 `key`；`v-if` 与 `v-for` 不应同层混用。
- 逻辑复用用 mixins 时注意命名冲突与来源不清。
- `this` 上下文：避免在回调中丢失 `this`（箭头函数 vs 普通函数）。
**Vue 3（Composition API）**：
- `ref` vs `reactive` 误用：`reactive` 解构会丢响应式（用 `toRefs`）；模板外访问 `ref` 漏 `.value` → [Critical/Suggestion]。
- `<script setup>` 下 `defineProps` / `defineEmits` 类型与默认值；props 只读不可直接改。
- `watch` / `watchEffect` 的依赖与清理（`onCleanup`）、`computed` 不应有副作用。
- 生命周期钩子（`onMounted` / `onUnmounted`）中注册的监听需对应清理。
- `v-for` 必须有稳定 `key`。

## 微信小程序专项
- **生命周期**：`onLoad` / `onShow` / `onReady` / `onUnload` 使用正确；页面与组件生命周期不混淆。
- **`setData` 性能**：避免一次 `setData` 大对象 / 高频调用；只传变化字段，长列表慎用全量刷新 → [Critical/Suggestion]。
- **数据绑定与 WXML**：`wx:for` 必须有 `wx:key`；事件传参用 `data-*` + `e.currentTarget.dataset`。
- **包体积与分包**：主包体积、分包加载、按需注入；图片 / 资源是否走 CDN。
- **授权 / API**：`wx.login` / `getUserProfile` / 权限申请流程合规；网络请求域名白名单、超时与失败处理。

## Flutter 专项
**适用范围**：`.dart` 文件。
- **Widget 重建**：`build` 内避免创建昂贵对象 / 发起请求；尽量 `const` 构造；`setState` 范围尽量小，必要时拆分 Widget 或用局部状态。
- **资源释放**：`AnimationController`、`TextEditingController`、`StreamSubscription`、`ScrollController` 等必须在 `dispose` 中释放 → [Critical]。
- **异步与 BuildContext**：`await` 之后使用 `context` 前必须检查 `if (!mounted) return;` → [Critical]。
- **异步 UI**：`FutureBuilder` / `StreamBuilder` 须处理 loading / error / empty 三态。
- **空安全**：避免滥用 `!`（强制解包）；优先 `?.`、`??`、`late` 的合理使用。
- **状态管理**：与项目既有方案（Provider / Riverpod / Bloc / GetX）一致，不引入混用。
- **性能**：长列表用 `ListView.builder`；避免不必要的 `Opacity` / `ClipRRect` 嵌套。

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
- **语义化与可访问性**：使用语义标签；交互元素有可聚焦性、`aria-*`、`alt`、label 关联 → [Suggestion]，关键无障碍缺失可 [Critical]。
- **布局健壮性**：优先 Flex / Grid；避免写死宽高导致溢出；考虑长文本、空数据、不同视口。
- **CSS 维护性**：避免 `!important` 滥用与高特异性选择器；类名遵循项目约定（BEM / 模块化 / scoped）。
- **性能**：避免会触发重排 / 重绘的高频属性动画；优先 `transform` / `opacity`；图片设尺寸与懒加载。
- **兼容性**：用到较新特性时确认目标浏览器 / WebView 支持，必要时降级。
