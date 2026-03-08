---
name: code-review
description: 按团队标准审查代码质量、安全性与可维护性。适用于审查 pull request、代码变更、Bitbucket/GitHub PR，或用户请求 code review 时。
---

# Code Review

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
- [ ] React Native：检查 Platform.OS、键盘、内存
- [ ] Vue：v-for 有 key、Composition API 使用
- [ ] 无硬编码密钥或凭证

## 反馈格式
使用以下标签（按规则不使用 emoji）：
- **[Critical]**: 合并前必须修复
- **[Suggestion]**: 建议改进
- **[Nice to have]**: 可选优化

## 输出模板
```markdown
# Code Review: [PR/分支名]
## 摘要
[1–2 句概述]
## Critical
- [文件:行号] [问题描述]
## Suggestions
- [文件:行号] [建议]
## Nice to have
- [可选改进]
```

## 项目类型
审查 React Native、React、Vue、iOS、Android 或微信小程序时，需关注：
- **React Native**: Hooks 顺序、StyleSheet、Platform.OS、FastImage、KeyboardAvoidingView
- **React**: Memoization、effect 依赖、key 属性
- **Vue**: Composition API、v-for 的 key、响应式
- **微信小程序**: 页面生命周期、数据绑定、WXML 语法
