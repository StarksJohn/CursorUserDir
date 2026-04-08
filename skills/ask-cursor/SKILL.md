---
name: ask-cursor
description: 迁移并执行 ask_cursor 工作流，处理 Cursor IDE 配置优化、Claude Code 到 Cursor 的 Rules、Commands、Skills、MCP 迁移，以及相关使用指南更新。Use when the user mentions ask_cursor, Cursor 配置优化, 模型能力发挥, or migrating Claude Code workflows into Cursor.
---

# Ask Cursor

## 目标

把旧的 `claude code` `ask_cursor` 工作流，收敛成一个可在 Cursor 中稳定复用的个人 Skill。


## 配置信息
- Windows11系统全局配置数据目录(User 设置、工作区存储、UI 状态等，类似 VS Code):
  - win:`C:\Users\Stark8964911\AppData\Roaming\Cursor`
  - mac:`~/Library/Application Support/Cursor`
- Cursor 用户级命令、技能、MCP 主目录: `C:\Users\Stark8964911\.cursor`（Win11）或 `~/.cursor`（Mac）: 
- cursor提问目录: `C:\Users\Stark8964911\.cursor`（Win11）或 `~/.cursor`（Mac）
- cursor 常打开的项目类型: React Native, React, Vue, iOS, Android, 微信小程序

## 当前 ask_cursor 场景的推荐主入口

- Windows: `C:/Users/Stark8964911/.cursor/skills/ask-cursor/SKILL.md`
- Mac: `~/.cursor/skills/ask-cursor/SKILL.md`

<!-- 这份 Skill 是主入口；旧的 `~/.claude/commands/ask_cursor.md` 只作为历史来源或兼容参考，不再作为长期主维护点。 -->

## 当前活跃需求
<!-- - 我当前是`cursor Pro+ Annual $48/mo.` 计划的用户, 目前有如图![img_010515.png](img_010515.png)![img_011234.png](img_011234.png) 2个计费池,一个是使用高级API的计费池,一个是`Auto + Composer`的计费池, 每月24日15:00点重置 -->
- 当前Win11系统已经安装了`cursor IDE`
  <!-- - 刚刚cursor 更新到了最新版本, 给我说下这次更新新增了哪些功能? -->
  <!-- - 我需要最大化发挥出 ![img_182707.png](img_182707.png) 这几个模型解决编码和架构问题的能力, 还需要进行哪些全局配置优化或者创建哪些 skills 或者 Subagents? -->
  <!-- - 我想在每次cursor 执行完毕任务后, 用户可以选择点击 一个按钮,然后 cursor 把 任务内容朗读出来
    - 我在 cursor 的扩展里没找到 **Read Aloud**、**Speech** -->
- 当前 `MacBook Pro` 电脑也下载安装了cursor,已经有了  `/Users/stark/.cursor` 和 `~/Library/Application Support/Cursor` 目录
  - 你帮我解决 `/Users/stark/Library/Application Support/Cursor/Cursor_使用指南与Token优化.md` 里的 ![img_201253.png](img_201253.png)
    <!-- - 你借鉴 `C:\Users\Stark8964911\AppData\Roaming\Cursor`和 `~/Library/Application Support/Cursor`目录 的同步方式,修改 "C:\Users\Stark8964911\.cursor\.gitignore", 让 `C:\Users\Stark8964911\.cursor`这个本地git仓库也只追踪可移植到 `MacBook Pro` 系统的 `/Users/stark/.cursor` 目录里的文件和子目录, 然后 push 到 远程仓库 -->
    <!-- - 目前我已经把 `C:\Users\Stark8964911\AppData\Roaming\Cursor` 下可移植项同步到 `~/Library/Application Support/Cursor`，把 `C:\Users\Stark8964911\.cursor` 可移植项同步到 `/Users/stark/.cursor`；Win 上其余能力哪些常仍未在 Mac 对齐？见指南 **§2.1a 问题 17**。 -->
- 把以上问题你的解答总结更新到 
  - win:`C:\Users\Stark8964911\AppData\Roaming\Cursor\Cursor_使用指南与Token优化.md`
  - mac : `/Users/stark/Library/Application Support/Cursor/Cursor_使用指南与Token优化.md`
