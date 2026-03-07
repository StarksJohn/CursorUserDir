; ===== TeamViewer Mac 远程特殊处理 =====
; 检测 TeamViewer 窗口，使用 Windows 键映射为 Mac 的 Command 键
#IfWinActive ahk_class TV_CClientWindowClass
    ; Alt+C 映射为 Win+C (Mac的Cmd+C复制)
    !c::Send {LWin down}c{LWin up}
    ; Alt+V 映射为 Win+V (Mac的Cmd+V粘贴)
    !v::Send {LWin down}v{LWin up}
    ; Alt+X 映射为 Win+X (Mac的Cmd+X剪切)
    !x::Send {LWin down}x{LWin up}
    ; Alt+A 映射为 Win+A (Mac的Cmd+A全选)
    !a::Send {LWin down}a{LWin up}
    ; Alt+Z 映射为 Win+Z (Mac的Cmd+Z撤销)
    !z::Send {LWin down}z{LWin up}
    ; Alt+S 映射为 Win+S (Mac的Cmd+S保存)
    !s::Send {LWin down}s{LWin up}
    ; Alt+F 映射为 Win+F (Mac的Cmd+F查找)
    !f::Send {LWin down}f{LWin up}
    ; Alt+W 映射为 Win+W (Mac的Cmd+W关闭)
    !w::Send {LWin down}w{LWin up}
    ; Alt+Tab 映射为 Win+Tab (Mac的Cmd+Tab切换)
    !Tab::Send {LWin down}{Tab}{LWin up}
    ; Alt+` 映射为 Win+` (Mac的Cmd+`窗口切换)
    !`::Send {LWin down}``{LWin up}
#IfWinActive
; ===== TeamViewer 特殊处理结束 =====

; 交换 Ctrl 和 Alt 键
LCtrl::Alt
LAlt::Ctrl

; 保持 Alt 键的原有功能
LAlt & Tab::AltTab
LAlt & Esc::Send {Alt down}{Esc}{Alt up}
LAlt & F4::Send {Alt down}{F4}{Alt up}
LAlt & Space::Send {Alt down}{Space}{Alt up}
LAlt & Enter::Send {Alt down}{Enter}{Alt up}
LAlt & Shift::Send {Alt down}{Shift down}
LAlt & Shift up::Send {Alt up}{Shift up}

; 定义 Alt 组合键
!a::Send ^a
!c::Send ^c
!v::Send ^v
!x::Send ^x
!z::Send ^z
!s::Send ^s
!f::Send ^f
!w::Send ^w

; 保持其他常见 Ctrl 键的原有功能
LCtrl & C::Send ^c
LCtrl & V::Send ^v
LCtrl & X::Send ^x
LCtrl & Z::Send ^z
LCtrl & A::Send ^a
LCtrl & S::Send ^s
LCtrl & F::Send ^f

; 在魔兽世界中定义 Alt + W 发送 Ctrl + W
#IfWinActive ahk_class waApplication Window
!w::Send ^w
#IfWinActive

; 在印象笔记中映射 Alt + 组合键为 Ctrl + 组合键
#IfWinActive ahk_class Qt5152QWindowIcon
!c::Send ^c
!v::Send ^v
!x::Send ^x
!z::Send ^z
!s::Send ^s
!a::Send ^a
LAlt::return
#IfWinActive


!r:: ; Alt+R
    Send, {F5}
    return

!`:: ; Alt+`
    ; 获取当前活动窗口的应用程序名称
    WinGet, CurrentApp, ProcessName, A

    ; 获取该应用程序的所有窗口ID
    WinGet, AppWindows, List, ahk_exe %CurrentApp%

    ; 如果有多个窗口，切换到下一个窗口
    if (AppWindows > 1) {
        ; 获取当前活动窗口的ID
        WinGet, CurrentWindowID, ID, A

        ; 找到当前活动窗口的位置
        Loop, %AppWindows% {
            if (AppWindows%A_Index% = CurrentWindowID) {
                NextIndex := A_Index + 1
                break
            }
        }

        ; 如果下一个窗口ID超出范围，循环回到第一个窗口
        if (NextIndex > AppWindows) {
            NextIndex := 1
        }

        ; 激活下一个窗口
        NextWindowID := AppWindows%NextIndex%
        WinActivate, ahk_id %NextWindowID%
    }

    return


; 在记事本中交换 Ctrl 和 Alt 键
#IfWinActive ahk_class Notepad
LCtrl::Alt
LAlt::Ctrl
#IfWinActive


; 在 Figma 网站中交换 Ctrl 和 Alt 键
#IfWinActive ahk_class Chrome_WidgetWin_1 ; 假设你在 Chrome 浏览器中使用 Figma  
GroupAdd, FigmaGroup, ahk_class Chrome_WidgetWin_1 ; 添加 Figma 到分组
LCtrl::Alt
LAlt::Ctrl
#IfWinActive




; 在Cursor IDE中特殊处理
#IfWinActive ahk_exe Cursor.exe
    ; 全局Ctrl/Alt交换
    LCtrl::LAlt
    LAlt::LCtrl

    ; 添加注释快捷键映射 (Alt+/ -> Ctrl+/)
    !/::Send ^/

    ; Alt+D (physical Ctrl+D) -> Send Ctrl+D to Cursor for deleting selected lines
    ; This supports multi-line deletion via Cursor's native editor.action.deleteLines
    !d::Send ^d

    ; Alt+Q (physical Ctrl+Q) -> Send Ctrl+Q to Cursor for copying file absolute path
    !q::Send ^q

    ; Alt+V (physical Ctrl+V) -> Let Cursor handle it directly
    ; In Markdown files: triggers Paste Image plugin (via keybindings.json)
    ; In other files: triggers normal paste (via keybindings.json)
    ; The ~ prefix allows the keystroke to pass through to the application
    ~!v::return

; 使用Alt+Backspace作为删除行的快捷键
!Backspace::
    Send {Home}
    Send +{End}
    Send {Delete}
    Send {Delete}
return

    ; 快速打开文件 (Alt+E -> Ctrl+P)
    !e::Send ^p

    ; 导航返回 (Alt+1 -> Alt+Left)
    !1::Send !{Left}

    ; 跳转到文件顶部 (Alt+2 -> Ctrl+Home)
    !2::Send ^{Home}

    ; 跳转到文件底部 (Alt+3 -> Ctrl+End)
    !3::Send ^{End}

 ; 折叠所有代码 (Alt+4 -> 通过命令面板)
!4::
    Send ^+p                     ; 打开命令面板
    Sleep 100
    Send Fold All                ; 输入折叠命令
    Sleep 100
    Send {Enter}                 ; 执行
return

    ; 展开所有代码 (Alt+Shift++ -> Ctrl+K Ctrl+J)
    !+=::Send ^k^j

    ; 折叠到定义 (Alt+M -> Ctrl+M O) - Visual Studio Outlining插件
    !m::
        Send ^m
        Sleep 50
        Send o
    return

    ; Alt+Click转为F12 (转到定义)
    LAlt & LButton::
        Send {LButton}  ; 先点击选中符号
        Sleep 50        ; 短暂等待选中生效
        Send {F12}      ; 发送转到定义快捷键
    return

#IfWinActive


; 在 Claude Code 中 Alt+1 映射为 Ctrl+O (显示/隐藏 Thinking 内容)
#IfWinActive ahk_exe claude.exe
!1::^o  ; Alt+1 映射为 Ctrl+O
#IfWinActive