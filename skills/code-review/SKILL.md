---
name: code-review
description: 按团队标准审查代码质量、安全性与可维护性。适用于审查 pull request、代码变更、Bitbucket/GitHub PR，或用户请求 code review 时。
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
- [ ] 逻辑正确且处理边界情况
- [ ] 无安全问题（注入、XSS、敏感数据暴露）
- [ ] 代码符合项目约定
- [ ] 函数职责单一、体量适中
- [ ] 错误处理充分
- [ ] 测试覆盖变更（如适用）
- [ ] TypeScript：见下方「**TypeScript 专项**」
- [ ] React Native：检查 Platform.OS、键盘、内存
- [ ] Vue：v-for 有 key、Composition API 使用
- [ ] 无硬编码密钥或凭证

## TypeScript 专项
**适用范围**：本次 diff 中涉及 `.ts`、`.tsx`，以及 Vue SFC 中带 `lang="ts"` 的 `<script>`。

**必查项（缺失一律报 [Critical]）**  
对变更范围内 **新增或修改** 的以下内容，须具备 **显式类型**：
- **参数**：每个形参均有类型注解（禁止依赖隐式 `any`；禁止裸 `any` 作为“逃避注释”，除非项目已有明确豁免条款且本 PR 未扩大使用面）。
- **返回值**：函数/方法/async 函数须有显式返回类型（`async` 须写 `Promise<...>` 或等价明确形式）。

**审查对象包括**：导出的函数/方法、组件外的命名函数、类方法、`const fn = (...) => ...` 等独立声明；class 字段上的方法签名同等要求。

**不强制本条的情况**（本条不适用时不因类型报 Critical）：
- 纯 `.js` / `.jsx` 或未启用 TS 的脚本
- 第三方类型声明文件（`.d.ts`）中以声明语句体现的签名
- 仅作临时桥接、且文件顶行或区块已有 `eslint-disable`/`@ts-expect-error` 且与团队规范一致的一次性改动（须在 PR 中可说明原因；否则仍报 Critical）

**报告写法**：`[文件:行号] 函数/方法名：缺少参数类型 / 缺少返回值类型（或隐式 any）`；若多项缺失可合并为一条 Critical 并列出位置。

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

## 项目类型
审查 React Native、React、Vue、iOS、Android 或微信小程序时，需关注：
- **React Native**: Hooks 顺序、StyleSheet、Platform.OS、FastImage、KeyboardAvoidingView
- **React**: Memoization、effect 依赖、key 属性
- **Vue**: Composition API、v-for 的 key、响应式
- **微信小程序**: 页面生命周期、数据绑定、WXML 语法
