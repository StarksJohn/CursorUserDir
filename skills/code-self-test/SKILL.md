---
name: code-self-test
description: 审查当前本地分支相对基线的完整工作树（committed、staged、unstaged 与未忽略 untracked），通过静态检查、定向测试和失败路径自测优先发现代码 BUG，并为每个 BUG 提供怎么解决的说明；未发现 BUG 时提出可优化内容以及怎么优化，目标是提升项目性能和用户体验。适用于 /code-self-test、@code-self-test、当前分支自测、找 bug、代码自测、性能优化、体验优化。不要替代 /code-review 的 Critical-only 合入审查。
---

# Code Self Test

## Purpose

审查代码。默认检查当前分支的代码（含未提交改动），通过 skill 进行自测并可以发现代码 BUG，还可以发现代码里可优化内容。

优先发现 BUG，再发现可优化的内容：

- 如果发现 BUG，必须提供怎么解决这个 BUG 的说明。
- 如果没有发现 BUG，则需要提出可优化的内容以及怎么优化。

最终目标是提升使用这个 skill 的项目的性能和用户体验。除非用户明确要求落地修复，否则只读、不改业务代码。

## When to Use

- 用户输入 `/code-self-test`、`@code-self-test`。
- 用户要求对当前分支做自测、找 bug、代码自测、性能优化或体验优化。
- 需要先证明有没有 BUG，再决定优化项时。

不要在用户只要 Critical 合入审查，或明确使用 `/code-review` 时激活本 skill。不要加载 `code-review` 来完成本任务。

## Inputs / Context

1. 确认 Git 根、当前分支、remote，以及用户是否指定了 PR/commit/range；未指定时审查当前 checkout 相对基线的完整本地快照。
2. 读取唯一项目规则后再审查。已登记项目不得寻找已删除的仓库根 `AGENTS.md`：

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
- 当前源码与 manifest 高于过期说明。发现规则漂移时按当前源码审查并说明风险；不要执行 `init-project`。

3. 命中具体技术栈后读取 [reference.md](reference.md) 对应章节，不要通读无关清单。
4. React Native 且必须用真机/模拟器证明用户可见 BUG 时，再读取 `react-native-ui-verification`；纯逻辑自测不必加载。

## Workflow

按顺序执行，不得跳过自测直接给结论。

### 1. 建立当前分支范围

只读检查：`git rev-parse --show-toplevel`、`git status --short`、`git branch --show-current`、`git remote -v`。

默认范围是当前本地分支相对基线的完整工作树：

1. 基线优先用当前分支 PR 的 base；没有 PR 时用 `origin/main` 或 `origin/master` 与 `HEAD` 的 merge-base；都不可用时用最新 commit 的真实父提交。
2. 分别记录 committed 端点 diff、`git diff HEAD --` 的 staged/unstaged，以及 `git ls-files --others --exclude-standard` 的 untracked。
3. 同一文件既有 committed 又有未提交修改时，审查磁盘上的最终文件，不得退回 `git show HEAD:path`。
4. 范围内有 merge commit 时，不能只看端点净 diff；检查合入后删除或覆盖是否造成运行失败。

用户明确指定 PR/commit/range 时，审查该精确 diff；只有用户同时要求本地改动时才叠加工作树。

不得为了审查执行 `checkout`、`reset`、`clean`、`stash`，不得安装依赖或修改 lockfile。

### 2. 建立影响图

从精确范围列出：

- 变更符号：函数、组件、Hook、props、DTO、导出、路由、状态、schema、配置。
- 用户路径：打开、提交、返回、刷新、登录、权限、空态、错误态、弱网。
- 性能/体验面：列表、图片、键盘、启动、导航、重复请求、主线程工作、加载反馈。

在最终工作树中搜索直接调用者，不只阅读 changed files。基线已有且当前范围未扩大的问题不报。

### 3. 执行 skill 自测（强制）

未执行本协议前，不得宣称无 BUG。自测本身就是找 BUG 的手段，不是写完报告后的附录。

**L1 静态自测**

- 只运行项目 manifest 和唯一 `AGENTS.md` 已声明的最小类型检查、lint 或静态命令；不发明平行命令。
- 范围内每个新增或修改的 `.ts` / `.tsx` 必须纳入类型覆盖。Gradle、Metro、Babel、ESLint、Jest 成功都不能替代 TypeScript 编译检查。
- 全仓基线噪音很大时，把完整诊断与范围内文件求交；禁止只看退出码或只抽查熟悉文件。
- 无法覆盖某个 changed TypeScript 文件时，在自测记录标记「类型覆盖阻塞」，不得据此写「无 BUG」的完整结论。

**L2 定向测试自测**

- 找到覆盖变更符号的现有测试，用项目已有命令运行最小相关集合。
- 测试失败时用相同命令对比基线与当前快照；只把当前范围新引入或扩大的失败记为 BUG。
- 没有现成测试时，不擅自新增测试文件；改为构造可复现输入，并在自测记录写明「无定向测试、已做路径自测」。

**L3 失败路径自测**

对每个变更函数/组件走一遍可到达路径，至少覆盖：空值、空列表、加载中、请求失败、超时、重复点击、异步返回时已卸载、权限拒绝、另一端 `Platform.OS`。有具体失败结果的记为 BUG；仅「可能」且走不通的删除。

**L4 运行时自测**

只有 BUG 或用户路径依赖真实页面、设备或后端，且环境可用时才扩展。不把「未运行」写成「通过」。Web UI 在已配置可用的浏览器工具下做最小路径验证；React Native 区分 Android 与 iOS，缺一端就标未验证。

### 4. 判定与输出优先级

1. 先关闭 BUG 列表。通过证据门禁的全部输出，每条都必须带怎么解决这个 BUG 的说明。
2. 再找可优化内容。只保留能提升性能或用户体验、且能说明怎么优化的项。
3. 有 BUG 时：BUG 段必出；高价值优化可随后列出，不得用优化段替代修 BUG。
4. 没有发现 BUG 时：必须提出可优化的内容以及怎么优化；摘要写明「未发现当前范围引入的 BUG」。
5. 不得为了填满报告编造 BUG，也不得把命名/格式偏好当成优化。范围内确实没有可验证的性能或体验收益时，写已检查维度和「无落地优化」，并给出下一步测量方法，不要用风格建议充数。

## BUG 证据门禁

报告 BUG 前必须全部满足：

1. 根因位于当前精确范围的新增、修改或删除。
2. 当前范围新引入或明确扩大，不是基线旧问题。
3. 有具体触发路径、期望结果和实际结果；自测记录能指向命令输出、失败路径上的 `文件:行号`，或已执行的运行时证据。
4. 影响正确性、安全性、数据、隐私、关键可用性、跨平台行为、资源泄漏，或用户无法完成主路径。
5. 怎么解决覆盖根因和所有需同步位置，而不是只写「检查一下」。

未通过任一条件就删除该条。

## 优化证据门禁

只在 BUG 狩猎完成后处理。报告优化前必须全部满足：

1. 能指出当前性能成本或体验摩擦（多余渲染、卡顿、重复请求、阻塞主线程、键盘遮挡、错误态缺失、列表/图片内存、启动或导航变慢等）。
2. 优化后用户可感知，或有明确测量方式。
3. 给出怎么优化：改哪里、最小做法、如何验证收益、主要风险。
4. 不是风格、命名、抽象偏好，也不是与性能/体验无关的重构。

## Output Contract

默认只读。不提交、不推送、不在 PR 平台发评论。密钥、Cookie、Authorization、签名材料和完整敏感响应不得出现在输出。

Chat 会把同一个 `-` 列表项里的续行折成一段。每条 finding 必须用 `###` 独立标题；下列标签必须独占一行，且标签前必须有一个空行：

- `位置：`
- `自测证据：`
- `问题：`
- `怎么解决：`（BUG 必填）
- `怎么优化：`（优化必填）
- `修复后自测：` 或 `优化后验证：`
- `平台差异（React Native 适用）：`

禁止把整条 finding 写进一个 bullet。

````markdown
# Code Self Test: [当前分支或指定范围]

## 摘要

- 范围：[local branch snapshot 或 PR/commit]
- 端点：[base] -> [HEAD 或 working tree]
- Changed files：[总数；committed/staged/unstaged/untracked 分层计数]
- 结论：BUG [n]；优化 [n]
- 优先级结果：[发现 BUG，已给出怎么解决 / 未发现 BUG，已给出可优化内容以及怎么优化]

## 自测记录

- L1 静态：[命令、覆盖文件、新失败/无新失败]
- L2 定向测试：[命令、结果，或无现成测试]
- L3 失败路径：[走过的路径；命中或未命中]
- L4 运行时：[已执行/未执行及原因]
- 阻塞：[类型覆盖阻塞/测试环境不可用/无]

## BUG

### [BUG] [标题]

位置：

- [path:line]（committed/staged/unstaged/untracked）

自测证据：

[命令输出摘要，或失败路径上的具体表达式]

问题：

[触发条件、实际结果、对用户或数据的影响]

怎么解决：

```tsx
// Minimal fix covering the root cause
```

同步修改：

- [path:line 或「无」]

修复后自测：

前置条件：[...]

1. [...]
2. [...]

预期：修复前 [...]；修复后 [...]

平台差异（React Native 适用）：

- Android：[已验证 / 未验证]
- iOS：[已验证 / 未验证]

## 优化

### [优化] [标题]

位置：

- [path:line]

当前成本：

[卡顿、多余请求、缺失反馈等，以及它如何影响性能或体验]

怎么优化：

```tsx
// Minimal optimization
```

优化后验证：

[如何证明变快或更好用；不要只写「感觉好一些」]

风险：

[行为变化或过早优化风险]
````

没有 BUG 时，`## BUG` 写「无」，并明确「未发现当前范围引入的 BUG」。此时 `## 优化` 不得省略。没有可落地优化时，`## 优化` 写已检查的性能/体验维度和「无落地优化」。

## Boundaries

- 不替代 `/code-review`；本 skill 允许优化项，且必须做自测。
- 不修改业务代码、不提交、不推送，除非用户明确要求落地修复。
- 不把基线旧问题、风格偏好、无关文件写成当前分支 BUG。
- 不把 lint/类型/测试「未运行」写成通过。
- 不安装依赖、不改 lockfile、不为审查切换分支或丢弃用户改动。
- React Native finding 必须区分 Android 与 iOS。
- 详细技术栈检查见 [reference.md](reference.md)。

## 输出前复核

- 是否已对当前分支完整快照做 L1–L3，L4 未跑是否已记录原因。
- 有 BUG 的每条是否都有怎么解决，且修复说明覆盖根因。
- 没有 BUG 时是否已提出可优化内容以及怎么优化，或诚实写无落地优化。
- 优化是否都指向性能或用户体验，而不是风格。
- 是否泄露密钥或完整敏感响应。
- 每条 finding 是否用 `###` 标题，标签是否都从新行开始。
