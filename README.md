# Cursor User Dir

远程git仓库: https://github.com/StarksJohn/CursorUserDir

Cursor 用户级命令、技能、MCP 主目录:
- Win11: `C:\Users\Stark8964911\.cursor`
- Mac: `~/.cursor`

## 跨机器同步

在 Mac 上 `git pull` 即可将 Win11 的配置同步到 Mac。

## 目录结构

```
~/.cursor  (或 C:\Users\Stark8964911\.cursor)
├── config/                     # Cursor 全局配置备份
│   ├── settings.json          # 全局设置
│   ├── keybindings.json       # 快捷键
│   ├── .prettierrc            # Prettier 配置
│   ├── snippets/              # 代码片段
│   ├── SwapCtrlAlt.ahk        # Windows: Ctrl/Alt 交换脚本
│   └── extensions-list.txt    # 已安装扩展列表
├── sync-cursor-config.ps1     # Windows: 配置备份/恢复脚本
├── commands/                  # 自定义 slash 命令
├── skills-cursor/             # 内置技能
├── skills/                    # 个人技能
├── rules/                     # 用户规则
└── projects/                  # 项目级数据
```

## 使用方式

### Windows: 备份配置到 Git

```powershell
cd C:\Users\Stark8964911\.cursor   # 或 cd ~/.cursor (若已迁移)
.\sync-cursor-config.ps1 -Action backup

git add .
git commit -m "Update Cursor configuration"
git push
```

### Windows: 从 Git 恢复配置

```powershell
cd C:\Users\Stark8964911\.cursor
git pull
.\sync-cursor-config.ps1 -Action restore
# 重启 Cursor 使配置生效
```

### 检查同步状态

```powershell
.\sync-cursor-config.ps1 -Action status
```

## 配置路径

| 项目 | Windows | Mac |
|------|---------|-----|
| Cursor 配置 | `%APPDATA%\Cursor\User\` | `~/Library/Application Support/Cursor/User/` |
| 扩展 | `%USERPROFILE%\.cursor\extensions\` | `~/.cursor/extensions/` |
| AHK 脚本 | `%APPDATA%\...\Startup\SwapCtrlAlt.ahk` | (仅 Windows) |

## 说明

- **sync-cursor-config.ps1**: 仅 Windows 可用; Mac 上可手动复制 `config/` 内容到 Cursor 配置目录
- **SwapCtrlAlt.ahk**: Windows 专用, 用于模拟 Mac 键位
- **config/**: 作为配置源, 通过脚本恢复到 Cursor 实际配置目录
