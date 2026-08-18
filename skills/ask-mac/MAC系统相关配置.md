# Mac 系统当前配置与验证基线

> 最后核验：2026-08-18。本文只记录当前 Mac 上仍存在且已复核的事实。进程 PID、`utun` 编号、Clash 节点、VPN 连接状态和公网出口属于运行时状态，使用时应重新检查。

## 硬件、系统与显示器

- 设备：MacBook Pro `MacBookPro16,1`，8-Core Intel Core i9，8 个物理核心、16 个逻辑 CPU，16GB 内存。
- 系统：macOS `26.4.1 (25E253)`，Darwin `25.4.0`。
- 内屏：`3072 x 1920` Retina。
- 外接屏：ViewSonic `VG2481-4K`，当前为 `3840 x 2160`，HiDPI `looks like 1920 x 1080 @ 60Hz`，通过 DVI/HDMI 类型链路连接，并设为主显示器。
- 当前开启镜像显示；内屏和外接屏均在线。
- `pmset -g therm` 当前无 thermal warning 或 performance warning，CPU 调度、可用 CPU 和速度限制均为 `100%`。
- macOS 已启用减少动态效果和降低透明度：`AppleReduceMotion = 1`、`reduceMotion = 1`、`reduceTransparency = 1`。

## 网络、双 VPN 与代理分层

### 持久拓扑

| 层 | 当前端点 | 已验证职责 |
| --- | --- | --- |
| 应用统一入口 | `127.0.0.1:4782` | Cursor、Cursor 内 Codex、终端和 Git 的稳定 HTTP/HTTPS 代理入口 |
| 本地路由器 | `cursor-vpn-proxy-router.py` | 首选 Clash；Clash 不可用时回退到当前 macOS 系统路由 |
| Clash Verge | mixed proxy `127.0.0.1:7897` | 提供应用层海外代理出口 |
| UUBooster | 透明 TUN | 接管当前公网系统路由，不提供可填写到 Cursor 的 HTTP 代理端口 |
| 深圳办公室 VPN | PPP/L2TP | 提供深圳内网路由，访问 `192.168.99.0/24` |

当前公网模型请求链路：

```text
Cursor / Codex / Terminal / Git
  -> 127.0.0.1:4782
  -> Clash 127.0.0.1:7897
  -> UUBooster TUN
  -> physical network
```

当前深圳内网链路：

```text
192.168.99.29
  -> gateway 192.168.100.1
  -> ppp0
  -> 深圳办公室 VPN
```

### 持久配置

- 路由器脚本：`/Users/stark/.local/libexec/cursor-vpn-proxy-router.py`。
  - 监听 `127.0.0.1:4782`。
  - primary 为 `clash://127.0.0.1:7897`。
  - HTTPS 只有在 Clash `CONNECT` 成功后才使用该隧道，否则建立 `route=system` 连接。
  - 普通 HTTP 连接 Clash 失败时同样回退到系统路由。
- LaunchAgent：`/Users/stark/Library/LaunchAgents/com.stark.cursor-vpn-proxy-router.plist`。
  - label 为 `com.stark.cursor-vpn-proxy-router`。
  - `RunAtLoad = true`、`KeepAlive = true`。
  - 当前已加载。
- GUI 代理环境任务 `com.stark.proxy-env` 当前已加载。
- Clash Verge 配置 `/Users/stark/Library/Application Support/io.github.clash-verge-rev.clash-verge-rev/verge.yaml` 中 `enable_system_proxy: false`。
- `Wi-Fi` 与“深圳办公室 VPN”网络服务当前均为：
  - HTTP proxy：启用，`127.0.0.1:4782`。
  - HTTPS proxy：启用，`127.0.0.1:4782`。
  - SOCKS proxy：关闭。
  - bypass 包含 `127.0.0.1`、`localhost`、`*.local`、`192.168.0.0/16`、`10.0.0.0/8`、`172.16.0.0/12`。
- `~/.zprofile`、`~/.zshrc`、`~/.profile`、`~/.bashrc` 均配置 `HTTP_PROXY` / `HTTPS_PROXY = http://127.0.0.1:4782`。
- 登录 zsh 当前继承：
  - `HTTP_PROXY` / `HTTPS_PROXY = http://127.0.0.1:4782`。
  - `ALL_PROXY` 为空。
  - `NO_PROXY` 包含 `192.168.99.29`、本机地址和私网网段。
- Git 全局 `http.proxy = http://127.0.0.1:4782`。

### 当前运行态

- UUBooster `2.8.11`、Clash Verge `2.5.2`、`cursor-vpn-proxy-router.py` 当前均在运行。
- `4782` 由路由器监听，`7897` 由 Clash core 监听。
- 深圳办公室 VPN 当前为 `Connected`，类型为 PPP/L2TP。
- 当前公网默认路由为 `gateway 192.0.0.1 -> utun4`；Clash 外连 socket 的本地源地址也是 `192.0.0.1`，证明 Clash 当前位于 UU TUN 之上。
- Clash 组 `辐射网络` 当前选择 `[anytls]美国A2`。
- 当前出口对照：
  - 经 `4782` / Clash：美国 California / Los Angeles，`AS63150 BAGE CLOUD LLC`。
  - 绕过代理、只经 UU 系统路由：中国 Shanghai，`AS24400 Shanghai Mobile Communications Co.,Ltd.`。
- `http://192.168.99.29:8083/ui/index.html#/` 经 `4782` 和显式直连均返回 HTTP `200`，远端地址均为 `192.168.99.29`。

### 使用边界

- 不要打开 Clash Verge 的 System Proxy；否则它会把系统代理从统一入口 `4782` 改回 `7897`。
- 不要把 UU 的 TUN 地址或动态端口写入 Cursor `http.proxy`。UU 是透明网络层，不是应用 HTTP 代理。
- UU 启停不要求修改 Cursor、Codex 或 Git 的 `4782` 配置。
- Clash 不可用时，`4782` 会回退到系统路由；当前 UU 开启时，该系统路由仍是 UU 的中国出口，受区域限制的模型可能因此不可用。
- 深圳内网必须继续由 bypass 和 `ppp0` 路由处理，不能把 `192.168.99.29` 强制送往 Clash 海外节点。

## Cursor 与 Codex

### 当前版本与安装组合

- Cursor：`3.16.17`。
- Codex CLI：`0.147.0-alpha.1.2`，路径为 `/Applications/Codex.app/Contents/Resources/codex`。
- OpenAI Codex 扩展：`openai.chatgpt@26.715.31925`，扩展注册状态为 `pinned = true`、`updated = false`。
- 本地兼容扩展：`stark-local.codex-cursor-compat@1.0.0`，目录为 `/Users/stark/.cursor/extensions/stark-local.codex-cursor-compat-1.0.0`。
- Cursor 启动参数 `/Users/stark/.cursor/argv.json` 当前包含 `enable-proposed-api = ["openai.chatgpt"]`。
- 不兼容扩展备份仍存在于 `/Users/stark/.cursor/extension-backups/openai.chatgpt-26.803.41515-darwin-x64.incompatible-with-cursor-3.15.6`。

### 当前关键设置

配置文件：`/Users/stark/Library/Application Support/Cursor/User/settings.json`。

```jsonc
"http.proxy": "http://127.0.0.1:4782",
"http.proxySupport": "override",
"http.proxyStrictSSL": false,
"cursor.general.disableHttp2": true,
"chatgpt.cliExecutable": "/Applications/Codex.app/Contents/Resources/codex",
"chatgpt.openOnStartup": false,
"typescript.tsserver.maxTsServerMemory": 4096,
"gitlens.currentLine.enabled": true,
"gitlens.codeLens.enabled": false,
"gitlens.hovers.enabled": false,
"gitlens.blame.highlight.enabled": false,
"extensions.autoCheckUpdates": false,
"extensions.autoUpdate": false
```

- `cursor.general.disableHttp2 = true` 是当前原生 Agent 代理链路的必要配置。Cursor 的 `always-local` HTTP/2 路径曾绕过 `http.proxy`，使受区域限制模型看到 UU 的中国出口。
- 写入上述代理或 HTTP/2 设置后，必须用 `Cursor -> Quit Cursor` 或 `Cmd+Q` 完整退出并重新打开；关闭窗口或 Reload Window 不能作为冷启动验收。
- 冷启动后的 Cursor 原生 Agent 已使用 `gpt-5.6-sol` 完成两次真实请求，`rpc.run` 均正常结束且没有 `error=true`；用户界面也已确认 `GPT-5.6 Sol Extra High` 恢复可用。
- Cursor 网络进程当前存在多条到 `127.0.0.1:4782` 的已建立连接，Cursor 内 Codex 当前可用。
- 当前仍能观察到 `always-local` 对 `api3.cursor.sh` 的后台直连。验收目标是模型请求可用，不应把现状描述成“Cursor 所有 socket 都经过 4782”。
- `com.stark.cursor-relaunch-once-20260817` 当前不存在，`chatgpt.openOnStartup = false`。

### 当前完整性边界

- `/Applications/Cursor.app` 当前通过 `codesign --verify --deep --strict`，并被 `spctl` 接受为 Notarized Developer ID。
- `/Applications/Codex.app` 当前的 `codesign` 与 `spctl` 验证失败，错误指向 `Sparkle.framework` 的 sealed resource missing or invalid；该事实不等同于当前 Codex 插件或 CLI 不可用。

## 开发环境与 MCP

- 登录 zsh 当前默认 Node.js 为 `v20.20.2`。
- Cursor MCP 配置 `/Users/stark/.cursor/mcp.json` 当前只启用 `chrome-devtools`。
- Codex 当前启用的 MCP：`chrome_devtools`、`context7`、`node_repl`、`figma`。
- Codex 当前禁用 `computer-use`、`everything`、`fetch`、`filesystem`、`git`、`github`、`memory`、`npm`、`playwright`、`puppeteer`、`sequential_thinking`、`sqlite`、`taskmaster_ai`。
- 当前可用的核心开发扩展包括 ESLint `3.0.24`、Prettier `12.4.0`、GitLens `18.3.0`、React Native `1.13.0`、React Native Directory `1.6.2`、Volar `3.3.6`、Vetur `0.37.3` 和 Markdown Preview Enhanced `0.8.30`。

## 快速复核

检查持久代理：

```bash
networksetup -getwebproxy 'Wi-Fi'
networksetup -getsecurewebproxy 'Wi-Fi'
networksetup -getsocksfirewallproxy 'Wi-Fi'
networksetup -getwebproxy '深圳办公室 VPN'
networksetup -getsecurewebproxy '深圳办公室 VPN'
networksetup -getsocksfirewallproxy '深圳办公室 VPN'
```

检查监听与运行时路由：

```bash
lsof -nP -iTCP:4782 -sTCP:LISTEN
lsof -nP -iTCP:7897 -sTCP:LISTEN
route -n get 1.1.1.1
route -n get 192.168.99.29
```

检查 Cursor 代理设置与真实连接：

```bash
rg -n 'http.proxy|disableHttp2|chatgpt.cliExecutable' \
  '/Users/stark/Library/Application Support/Cursor/User/settings.json'
lsof -nP -iTCP@127.0.0.1:4782 -sTCP:ESTABLISHED
```

检查深圳内网：

```bash
curl --proxy http://127.0.0.1:4782 --max-time 15 \
  -o /dev/null -w '%{http_code}\n' \
  'http://192.168.99.29:8083/ui/index.html#/'
```

验收标准：系统 HTTP/HTTPS proxy 指向 `4782`、SOCKS 关闭、`4782` 与 `7897` 均监听、深圳内网路由为 `ppp0`、29 页面返回 `200`、Cursor 原生 Agent 与 Cursor 内 Codex 均能完成真实模型请求。
