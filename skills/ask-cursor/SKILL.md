---
name: ask-cursor
description: 迁移并执行 ask_cursor 工作流，处理 Cursor IDE 配置优化、Claude Code 到 Cursor 的 Rules、Commands、Skills、MCP 迁移，以及相关使用指南更新。Use when the user mentions ask_cursor, Cursor 配置优化, 模型能力发挥, or migrating Claude Code workflows into Cursor.
---

# Ask Cursor

## 目标

把旧的 `claude code` `ask_cursor` 工作流，收敛成一个可在 Cursor 中稳定复用的个人 Skill。

## 通用执行规范

<!-- Skill 执行规范已合并到 User Rules（`Cursor AI 规则.md` 第 9 条），每个会话自动生效，无需单独加载。 -->

## 配置信息
- Windows11系统全局配置数据目录(User 设置、工作区存储、UI 状态等，类似 VS Code):`C:\Users\Stark8964911\AppData\Roaming\Cursor`
- Cursor 用户级命令、技能、MCP 主目录: `C:\Users\Stark8964911\.cursor`（Win11）或 `~/.cursor`（Mac）: 
- cursor提问目录: `C:\Users\Stark8964911\.cursor`（Win11）或 `~/.cursor`（Mac）
- cursor 常打开的项目类型: React Native, React, Vue, iOS, Android, 微信小程序

## 默认迁移策略

- 常驻偏好放 `User Rules`
- 项目长期规则放 `.cursor/rules/*.mdc`
- 按需多步流程放 `~/.cursor/skills/`
- 显式 slash 命令兼容入口放 `~/.cursor/commands/`
- 本地 MCP 配置放 `~/.cursor/mcp.json`

## 当前 ask_cursor 场景的推荐主入口

- Windows: `C:/Users/Stark8964911/.cursor/skills/ask-cursor/SKILL.md`
- Mac: `~/.cursor/skills/ask-cursor/SKILL.md`

<!-- 这份 Skill 是主入口；旧的 `~/.claude/commands/ask_cursor.md` 只作为历史来源或兼容参考，不再作为长期主维护点。 -->

## 当前活跃需求
<!-- - 我当前是`cursor Pro+ Annual $48/mo.` 计划的用户, 目前有如图![img_010515.png](img_010515.png)![img_011234.png](img_011234.png) 2个计费池,一个是使用高级API的计费池,一个是`Auto + Composer`的计费池, 每月24日15:00点重置 -->
- 当前Win11系统已经安装了`cursor IDE`
  <!-- - 我需要最大化发挥出 ![img_182707.png](img_182707.png) 这几个模型解决编码和架构问题的能力, 还需要进行哪些全局配置优化或者创建哪些 skills 或者 Subagents? -->
  - 我之前在 当前Win11系统 里使用了 `Claude code`+`BMad`,现在能否在 cursor 里使用 BMad ? 如果可以,更新当前win11系统里全局安装的 BMad
  - 把以上问题你的解答总结更新到 `C:\Users\Stark8964911\AppData\Roaming\Cursor\Cursor_使用指南与Token优化.md`
