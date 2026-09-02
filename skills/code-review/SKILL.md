---
name: code-review
description: 审查当前 chat 指定的 PR/commit/range，或当前本地分支相对目标基线的完整变更；本地分支范围包含 committed、staged、unstaged 与未忽略的 untracked 文件，并对范围内 merge 的相关父提交执行目标分支保留审计，防止端点净 diff 漏掉合入后删除或覆盖的目标分支既有代码；同时追踪对历史调用者、类型、配置和测试的直接影响，只报告合并前必须修复的 Critical。适用于 GitHub/Bitbucket PR、commit、commit range、目标分支与 code review，重点覆盖用户 9 个项目中的 Next.js、React、React Native、Vue 2、TypeScript、Node.js、Prisma、原生 iOS/Android，同时兼容 Vue 3、Flutter、微信小程序和 HTML/CSS；排除基线旧问题、Suggestions 和 PR 外备注。
---

# Code Review

## 结果契约

- 把 code review 作为只读任务；除非用户明确要求，否则不修改业务代码、不提交、不推送、不发布，也不在 PR 平台发评论。
- 只审查一个明确目标。当前本地分支是目标或待合入对象时，审查相对基线的完整工作树快照，必须包含 committed、staged、unstaged 和 `git ls-files --others --exclude-standard` 返回的 untracked 文件。
- 端点净 diff 不是唯一证据：只要精确范围内含 merge commit，或当前分支曾合入目标分支，必须检查目标侧父提交和后续删除历史。目标代码“先合入、后删除或覆盖”即使在基线到 head 的净 diff 中抵消，也不得漏审。
- 明确指定 PR、commit 或 commit range 时，默认只审查其不可变精确 diff；只有用户同时明确要求本地改动时才叠加当前工作树，避免把无关工作区污染混入远端或历史目标。
- 只输出由当前精确范围直接引入或扩大、且合并前必须修复的 `[Critical]`。不输出 Suggestions、Nice to have、风格偏好、顺带发现或无因果关系的旧问题。
- 以端点 diff，或同一精确范围内的父提交到 merge 结果、后续 commit、staged/unstaged 删除 hunk 作为 finding 的根因锚点；若根因破坏了未修改的历史代码，在同一 Critical 中列出所有已确认的受影响位置。

## 读取项目规则

先确认仓库身份、根目录和当前分支，再读取项目规则。已登记项目不得寻找已删除的仓库根 `AGENTS.md`；按下表读取唯一规则源：

| 仓库身份或常见目录名 | 唯一项目规则 |
| --- | --- |
| `csx-web-react` | `$HOME/.codex/skills/csx-web-react/AGENTS.md` |
| `csx-web` | `$HOME/.codex/skills/csx-web/AGENTS.md` |
| `MyStartupProject1` | `$HOME/.codex/skills/MyStartupProject1/AGENTS.md` |
| `circleapp` / `CircleAppNew` | `$HOME/.codex/skills/CircleAppNew/AGENTS.md` |
| `amber-medical-app-rn` | `$HOME/.codex/skills/amber-medical-app-rn/AGENTS.md` |
| `csx-mobile` / `csx-mobile-upgrade` | `$HOME/.codex/skills/csx-mobile-upgrade/AGENTS.md` |
| `heals-app-rn` | `$HOME/.codex/skills/heals-app-rn/AGENTS.md` |
| `newtownapp` | `$HOME/.codex/skills/newtownapp/AGENTS.md` |
| `react-native-advanced-flatlist` | `$HOME/.codex/skills/react-native-advanced-flatlist/AGENTS.md` |

- Windows 将 `$HOME/.codex/skills` 解析为 `%USERPROFILE%\.codex\skills`。
- 用仓库根目录名、manifest 和 remote URL 交叉确认身份；不因相似命名套用另一个项目规则。
- 未登记仓库读取实际存在的仓库 `AGENTS.md`。规则缺失或身份不唯一时报告精确阻塞，不猜测创建。
- 从项目规则和当前 manifest 动态提取框架、项目边界、验证命令、隐私/医疗、发布、跨仓库和平台约束；当前源码与 manifest 高于过期说明。
- Review 保持只读。若发现唯一项目规则与仓库存在重大结构冲突，按当前源码审查并说明规则漂移风险；不要在 review 中执行 `init-project` 或更新外部规则。

## 选择唯一审查目标

按以下优先级选定一次，随后不混入其它范围：

1. 当前 chat 最后一次明确要求审查的 PR 号、PR 链接、commit SHA 或 commit range。
2. 用户明确说“当前分支”“本地分支”，或把某分支写成目标/合并基线时，审查当前 checkout 相对该基线的完整本地快照；命名目标分支是 base，不是要孤立审查的 head。
3. 用户只点名另一分支并明确要求审查该分支本身时，审查该 ref 的已提交内容，不叠加当前 checkout 的工作树。
4. 未明确目标且当前工作树有改动时，审查当前本地分支完整快照：优先使用当前分支 PR 的 base；没有 PR 时以最新 commit 的真实父提交为基线，把最新 commit 与工作树改动一起纳入。
5. 未明确目标且工作树干净时，优先审查当前分支对应的 open 或最近更新 PR；无法确定 PR 时审查最新 commit，普通 commit 使用 `HEAD^..HEAD`，merge commit 使用 `HEAD^1..HEAD`。

- 当前 chat 同时出现多个目标时，只取最后一次明确目标；仅当用户明确要求批量审查时分别建立范围并分别输出。
- “最新 PR”只指当前分支对应的 PR，不得选择仓库中无关的最新 PR。
- “目标 `<branch>`”“准备合入 `<branch>`”默认表示以该分支为 base 审查当前 checkout；“审查 `<branch>` 分支本身”才表示该分支是不可变 head。
- 用户指定目标后若无法取得精确范围，报告范围阻塞；不得悄然改审另一个 PR、分支或 commit。
- Cursor 当前推荐用 `/code-review` 激活；已有客户端若仍以 `@code-review` 选择同一 Skill，执行语义保持一致。可附加 PR、commit、range 或目标分支。

## 建立精确审查范围

1. 执行只读检查：`git rev-parse --show-toplevel`、`git status --short`、`git branch --show-current`、`git remote -v`。
2. PR 优先使用平台返回的 PR 标识、base SHA、head SHA、changed files 和 patch。需要当前远端状态时 fetch 对应 refs，但不 checkout 用户分支。
3. 只有证明本地 `HEAD` 等于 PR head SHA，且目标 ref 对应该 PR base 时，才允许用 `git diff origin/base...HEAD` 代替平台范围。
4. 指定 commit 使用其真实父提交：普通 commit 为 `sha^..sha`。merge commit 用 `sha^1..sha` 建立第一父提交变更，但必须先用 `git show -s --format=%P <sha>` 列出全部父提交，再对每个相关非第一父提交检查 `<sha>^N..<sha>`；不得只看 `^1`。Squash/rebase merge 优先平台 patch 或用户提供的精确 range。
5. 当前本地分支模式先解析精确 target tip 和 `git merge-base --all <target-tip> HEAD`，再分别记录 committed 端点 diff、`git diff HEAD --` 的 staged/unstaged tracked diff，以及 `git ls-files --others --exclude-standard` 的 untracked 文件。只有一个 merge-base 时，用它到 `HEAD`/工作树建立主 diff；返回多个时逐一记录并优先使用平台精确 patch，无法唯一化时标记范围阻塞，不任意挑选其一。把每个 untracked 文件视为完整新增内容；不得只审查其中一层。
6. 记录范围账本：目标模式和标识、base/head 或 commit range、target tip、全部 merge-base、范围内 merge commit 及其父提交、committed/staged/unstaged/untracked 各层 changed files、最终去重文件集、端点与目标保留 hunks、内容不可用项。
7. 不可变 PR/commit/range 以目标 head tree 读取和标注行号；当前本地分支模式以磁盘工作树的最终快照读取和标注行号。后者遇到同一文件既有 committed 又有未提交修改时，必须审查合并后的当前文件，不得退回 `git show HEAD:path` 覆盖本地状态。已删除代码无最终行号时，标注删除侧的 `path:line`、根因 commit 或 working-tree 层级和 hunk，不得因最终文件中已无该行而丢弃 finding。

不得为了审查执行 `checkout`、`reset`、`clean`、`stash` 或覆盖用户文件。浅克隆、LFS、submodule、权限或网络导致目标内容不完整时，明确写入验证边界。

## 目标分支保留审计

此审计补充端点 diff，只检查精确目标内对目标分支既有内容的删除或语义覆盖，不得借此混入无关分支或工作树。
只有当精确范围含 merge commit，或已确认当前分支合入过指定目标分支时才触发；不含 merge 且没有目标分支语义的普通 commit/range 标记为“不适用”。

1. 对范围内每个 merge commit，用 `git rev-list --parents --merges <range>` 和 `git show -s --format=%P <merge-sha>` 列出父提交；根据拓扑和目标 ref 识别 target-side parent，不盲猜它一定是 `^2`。
2. 对每个已确认的 target-side parent `P` 与 merge 结果 `M`，检查 `git diff --find-renames P M --` 的全文，包括整文件删除、行级删除、rename 后内容丢失、export/config/test 移除和用旧实现覆盖新逻辑。这一 parent-to-merge hunk 属于 merge commit 的精确审查范围。
3. 找出当前 head 实际已合入的最新目标快照 `I`：若 target tip 是 `HEAD` 祖先则使用 target tip；否则使用拓扑证据确认的最新 target-side parent 或 merge-base。比较 `I` 到 `HEAD` 及最终工作树，再沿合入后的 commit、staged 和 unstaged hunks 定位具体删除或覆盖根因；不得只看最终文件列表。
4. 若当前 target tip 比 `I` 更新，“target tip 有、head 没有”只是候选差异。只有找到当前范围内的主动删除/覆盖 hunk，或只读 merge 模拟证明合并结果会丢失该内容时，才能归因于当前分支；不得把尚未合入的 target-only 新代码误报为删除。
5. 删除本身不自动构成 Critical。先从 `P`/`I` 恢复被删符号和契约，再检查最终快照中的调用者、导出、路由、配置、migration、测试与运行路径；只在达到 Critical 证据门禁时报告。
6. 无法取得 target-side parent、相关对象或可信拓扑时，写明“目标分支保留审计阻塞”和缺失证据；不得宣称该维度“无 Critical”。

## 追踪直接影响

从当前精确范围构建变更符号和契约清单，至少覆盖：

- 函数/方法签名、组件 props、Hook、DTO/interface、泛型、返回值、导出和公共 helper。
- API schema、鉴权、导航参数、全局状态、缓存、持久化、数据库 schema/migration 和序列化格式。
- 环境变量、构建/打包、静态导出/base path、原生 scheme/flavor、权限、通知、签名和发布配置。
- manifest、lockfile、patch-package、Gradle/CocoaPods、CI 脚本、i18n key 和生成物边界。

对每项变更：

1. 不可变目标在 head tree 中搜索调用者；当前本地分支目标在最终工作树快照中搜索调用者，并同时覆盖未跟踪的新文件，不只阅读 changed files。
2. 目标保留候选必须同时读取 target-side parent/已合入快照和最终快照，逐个追踪被删或被覆盖的符号、契约及直接使用者。端点净 diff 没有该文件不是跳过理由。
3. 证明因果关系：若恢复 base 契约或撤销根因 hunk 后错误仍存在，则它是基线问题，不得报告。
4. 对类型、构建、lint 或测试诊断尽量做基线与目标快照的同命令差分，只保留目标新增或扩大的失败；本地分支模式的目标快照必须保留工作树改动。
5. 同一根因造成多个历史位置失败时合并为一条 Critical，但逐个列出文件、对应目标快照行号、错误代码/失败条件和表达式；不得只给数量或代表性样例。
6. 不扩展到无因果关系的全仓旧问题。只有当前范围改变了明确的跨仓接口且另一仓库被用户纳入范围时，才检查跨仓影响。

## Critical 证据门禁

报告 finding 前必须全部满足：

1. 根因位于当前精确范围的新增、修改或删除 hunk；包含范围内 merge commit 相对目标侧父提交的结果 hunk，以及本地分支的 committed、staged、unstaged 和未忽略 untracked 内容。
2. 问题是当前范围新引入或明确扩大的，不是目标基线已有问题。
3. 存在具体失败路径、契约冲突、可复现风险或差异化诊断，不以“可能”“建议确认”代替证据。
4. 影响正确性、安全性、数据、隐私、类型契约、跨平台行为、资源生命周期、关键可用性或构建/发布，达到合并前必须修复。
5. 所有列出的历史位置都与根因有直接可验证的因果关系。
6. 目标分支保留 finding 还必须证明内容确实存在于已确认的 target-side parent/已合入快照，且当前范围的根因 hunk 使最终结果丢失代码或语义；不能只以两个 tree 不同作为证据。

未通过任一条件就删除 finding；不得降级成 Suggestion 或放入 PR 外备注。

## 按改动路由审查

只执行命中当前精确范围和项目规则的检查，不机械扫描所有技术栈。

### TypeScript、React 与 Next.js

- 对新增或修改的命名函数、组件、Hook、方法和模块 helper，执行用户的显式类型契约：参数和返回值明确，async 使用 `Promise<...>`；禁止新增或扩大 `any`。该契约是当前用户的合并硬门禁，当前范围违反时按 Critical；安全可推断的内联回调不因缺少冗余注解单独报错。
- 对新增或修改的 import、属性、调用签名和第三方符号，检查目标版本类型声明中的 `@deprecated` 及 TypeScript suggestion 诊断。当前范围新增 TS6385、TS6387 或等价弃用诊断时按 Critical；不得因 `tsc` CLI 默认不显示 suggestion diagnostics、构建成功或 API 仍可运行而漏报。
- 对公共接口、props、API DTO、导航、全局状态、表单、持久化或平台字段中的 `any`，若掩盖真实契约或违反项目硬规则，报 Critical 并给出具体 interface、泛型或 `unknown` + type guard。
- 检查 Hook 依赖、旧闭包、函数式 state 更新、稳定 key、渲染期副作用、监听/定时器清理和异步竞态。
- Next.js 项目按实际路由模式检查 server/client 边界、hydration、导航与鉴权、缓存、静态导出/base path、资源路径及 public/server 环境变量泄漏。
- UI 变更只有在造成不可操作、溢出、关键断点回归或无障碍阻塞时才报 Critical；可选 memo、样式偏好和一般语义优化不报。

### Vue 2 / Vue 3 与 JavaScript

- 先从 manifest 和 SFC 写法确定版本。Vue 2 检查新增属性响应式、`this`、Vuex/Router/i18n 契约、稳定 key 和生命周期清理；不得用 Vue 3 假设审查旧项目。
- Vue 3 检查 `ref/reactive`、解构丢响应式、只读 props、watch 清理、computed 副作用和生命周期。
- JavaScript 检查会改变行为的弱比较、隐式全局、漏 `await`、未处理 Promise、`forEach(async)`、可空链路和共享引用；纯 JSDoc 或现代化偏好不报。

### React Native 与原生平台

- 核对第三方库、本地类型和必要的对应版本官方文档中的 `iOS ONLY`、`ANDROID ONLY`、deprecated、experimental 标记。共享逻辑使用单端字段时要求 `Platform.OS` 分支和另一端 fallback。
- 检查导航与状态恢复、权限、前后台/冷热启动、系统回收、键盘/Safe Area、监听/定时器/订阅清理、长列表/图片内存和原生桥接契约。
- 从项目规则决定 Redux Toolkit、Context、FCM/HMS、patch-package、flavor/scheme 和发布边界，不把一个 RN 项目的路径或行为套到另一个。
- 原生 iOS 检查 retain cycle、主线程 UI、强制解包和通知生命周期；Android 检查 Activity/Fragment 生命周期、协程取消、空安全、主线程 IO 和资源关闭。
- finding 和手测必须区分 Android 与 iOS；未执行设备验证就分别标注未验证，不能假设一致。

### API、Node.js、数据库、安全与隐私

- 检查输入校验、认证与授权、注入、XSS、SSRF、路径穿越、开放重定向、敏感响应、日志泄密和不安全反序列化。
- 检查未处理 rejection、同步阻塞、超时/重试、事务、连接/流/文件句柄释放，以及重复请求或幂等性。
- Prisma/schema/migration 变更检查向前/向后兼容、数据丢失、部署顺序和回滚边界；不要执行数据库写入或 migration。
- 遵循项目 `AGENTS.md` 的医疗文案、隐私分析、环境隔离、生产写入和发布授权规则。密钥、Cookie、Authorization、签名材料和完整敏感响应不得出现在输出。

### Flutter、微信小程序、HTML/CSS 与配置

- Flutter 检查 controller/subscription dispose、await 后 `mounted`、空安全和 loading/error/empty 状态。
- 微信小程序检查生命周期、`setData`、`wx:key`、授权、分包和请求域名。
- HTML/CSS 检查关键语义/键盘/label/alt/ARIA、长文本与响应式溢出、覆盖冲突和目标 WebView/浏览器兼容。
- 依赖、构建、CI、环境或原生配置变更检查目标污染、秘密泄漏、脚本副作用、锁文件一致性和实际产物边界。

## 验证策略

- 优先运行项目 manifest 和唯一 `AGENTS.md` 声明的最小相关静态检查或测试；不发明平行命令，不安装依赖，不修改 lockfile。
- 对范围内每个新增或修改的 `.ts` / `.tsx` 文件建立“文件 -> 编译覆盖 -> 诊断归属”账本，并使用项目本地 TypeScript、当前 `tsconfig` 及项目命令完成编译覆盖。Gradle、Metro、Babel、ESLint、Jest 或运行成功都不能替代 TypeScript 编译检查。
- 普通 `tsc` 诊断之外，必须使用项目本地 TypeScript Compiler API 的 `Program.getSuggestionDiagnostics(sourceFile)`、Language Service 的等价能力或可证明覆盖相同诊断的 IDE 接口，对每个 changed `.ts` / `.tsx` 获取 suggestion diagnostics，并与目标版本声明中的 `@deprecated` 交叉核对。若该层无法执行，必须标记“弃用诊断覆盖阻塞”，不得把未显示 TS6385/TS6387 写成已通过。
- TypeScript 命令被配置级错误提前阻断，或全仓基线错误很多时，不得停在首个错误、只看进程退出码或只抽查熟悉文件。先读取当前 `tsconfig` 和 scripts，使用不改变项目语义的最小兼容参数让编译器继续产出诊断，再把完整诊断路径与精确范围内全部 `.ts` / `.tsx`（含 untracked）逐一求交；禁止因为无关错误很多而漏掉 changed-file 诊断，也禁止直接用脱离项目 `tsconfig` 的单文件 `tsc file.ts` 制造假结论。
- 新增或 untracked TypeScript 文件没有基线版本，其目标诊断直接属于当前范围；修改文件的诊断使用相同编译器、配置和命令比较 base 与 target。若没有任何可行命令能覆盖某个 changed TypeScript 文件，验证边界必须标记“类型覆盖阻塞”，不得给出“无 Critical”的完整结论。
- 对疑似新增诊断，使用完全相同的命令、环境和范围比较基线与目标快照；无法隔离时不得把基线失败归因于当前范围。
- 先做类型/静态/定向测试，只有 finding 依赖真实页面、设备或后端契约且环境可用时才扩展运行验证。
- 对可由真实页面触发的 API 契约，Network 实际请求/响应优先于 Swagger 推断；不得泄露认证信息。
- 不把 lint、类型检查、构建、测试、浏览器或设备验证“未运行”写成“通过”。完整测试未运行不自动构成 Critical。

## Finding 格式

按根因位置排序，每条使用：

1. `[Critical] 标题`
2. `本次修改位置：` 至少一个精确范围内的 `文件:行号`；本地分支模式标明 committed/staged/unstaged/untracked 来源。已删除代码标注删除侧行号、根因 commit/工作树层级和 hunk
3. `目标分支来源：` 目标保留 finding 列出 target ref、target-side parent 或已合入快照 SHA，以及被删内容原 `文件:行号`；其他 finding 省略
4. `受影响历史代码：` 逐个列出 `文件:行号`、错误代码/失败条件和表达式；没有时写“无”
5. `问题：` 触发条件、错误结果和影响
6. `证据：` 端点 diff、parent-to-merge/后续删除 hunk、base/head 差分、类型/测试/运行时或契约依据
7. `修改建议：` 覆盖根因及所有需同步位置的最小可落地代码、before/after 或伪补丁
8. `手动自测：` 前置条件、步骤、修复前/后预期；无稳定路径时说明原因并给最小 mock/插桩
9. React Native finding 追加 Android 与 iOS 的已验证/未验证结论

无法安全确定唯一修复时，说明缺失上下文，给出最可能方向、待确认事实和尽可能接近可用的代码骨架。修复说明属于 Critical，不是 Suggestions。

## 输出模板

````markdown
# Code Review: [PR/commit/local branch]

## 摘要

- 范围：[PR 标识、commit range 或 local branch snapshot]
- 端点：[base/parent] -> [head 或 working tree]
- Changed files：[总数；本地模式列出 committed/staged/unstaged/untracked 分层计数]
- 目标分支保留审计：[target tip/已合入快照、范围内 merge commit 数、完成/阻塞/不适用]
- 结论：[Critical 数量或无]

## Critical

- [Critical] [标题]
  本次修改位置：[path:line]
  目标分支来源（适用时）：[target ref、parent/snapshot SHA、path:line]
  受影响历史代码：

    - [path:line] [错误代码/失败条件与表达式]

  问题：[触发条件与影响]
  证据：[差异化诊断或具体契约]
  修改建议：

  ```tsx
  // Minimal fix
  ```

  手动自测：
  前置条件：[...]
  步骤：
  1. [...]
  2. [...]
  预期结果：修复前 [...]；修复后 [...]
  平台差异（React Native 适用）：
  Android：[已验证 / 未验证及结论]
  iOS：[已验证 / 未验证及结论]

## 验证边界

- 已执行：[命令或只读证据]
- 未执行：[项目及原因]
````

没有 Critical 时写“无”，并明确“未发现当前精确范围引入的合并阻塞问题”。仍需列出验证边界，不补充 Suggestions。

## 输出前复核

- 范围账本、各层 changed files、hunks 和行号来源是否一致。
- 是否检查了范围内全部 merge commit 的父提交，而非只看端点 diff 或 `^1`；已合入目标代码的后续删除/覆盖是否已定位到具体 hunk。
- 是否把 target tip 比已合入快照更新所产生的 target-only 差异误当删除；目标保留审计阻塞时是否避免宣称该维度已通过。
- 每个 changed `.ts` / `.tsx`（尤其 untracked 新文件）是否都已与完整 TypeScript 诊断逐一核对；是否错误地用构建、lint、测试通过或全仓基线噪音替代了编译覆盖。
- 每个 changed `.ts` / `.tsx` 是否都已读取 suggestion diagnostics 并核对 `@deprecated` 声明；是否因普通 `tsc` 未显示 TS6385/TS6387 而把覆盖误写为通过。
- 每条根因是否位于当前精确范围，历史位置是否全部由该根因直接影响。
- 基线已有问题是否已排除；本地分支模式是否确实纳入 staged、unstaged、未忽略 untracked，且不可变 PR/commit/range 是否未混入未授权工作区。
- 项目唯一 `AGENTS.md` 的技术栈、跨平台、隐私、发布和验证边界是否已应用。
- 每条是否真正阻塞合并；证据不足或仅为偏好者是否已删除。
- 是否只输出 Critical、摘要与验证边界，没有 Suggestions 或 PR 外备注。
