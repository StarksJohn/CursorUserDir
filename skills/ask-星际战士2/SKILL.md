---
name: ask-星际战士2
description: >-
  《战锤40K：星际战士2》（Space Marine 2）与 PS5 联网游戏加速入口。用于 CSF 等联网报错、
  PS5 经 Mac + Clash Verge 节点加速（替代 UU 加速器）、查看/切换加速节点、停用或恢复 PS5 网关。
  用户执行 /ask-星际战士2、@ask-星际战士2，或提到 星际战士2、Space Marine 2、PS5 加速、CSF 时使用。
---

# ask-星际战士2

## 项目路径

- Windows：`D:\work\星际战士2`
- Mac 基线文档：`/Users/stark/Desktop/work/MAC/MAC系统相关配置.md`（「PS5 联网游戏网关」一节）

## 输入格式

在 Cursor 输入 `/ask-星际战士2` 或 `@ask-星际战士2`，后面可附带当前问题或截图。有截图时先按精确路径读图再判断。

## 已确认结论（2026-10-01）

- UU 加速《星际战士2》会报 CSF：香港、新加坡、欧洲、北美节点，以及 UU 的其它游戏配置都一样；直连能进但延迟高。原因在 UU 对这款游戏的转发方式，本机改不了，UU 客服未回复。
- 替代方案已验证可用：PS5 以 Mac 为网关，只把 PS5 的流量送进一个独立的 mihomo 内核，节点来自 Clash Verge 当前订阅，自动选最快可用节点。《星际战士2》能进，游戏内延迟约 70ms（香港C7）。
- 该方案适用于 PS5 上所有联网游戏，不再需要 UU 加速器。

## 当前方案

| 项 | 值 |
| --- | --- |
| 常驻服务 | LaunchDaemon `com.stark.ps5-clash-gateway`（`/Library/LaunchDaemons/com.stark.ps5-clash-gateway.plist`），开机自启，以 root 运行，不依赖 Cursor |
| 目录 | `/usr/local/ps5-clash-gateway/`：`ps5-gateway.sh`、`config.yaml`、`pf.conf`、`verge-mihomo`（Clash Verge 内核副本）、`secret`、`gateway.log`、`mihomo.log` |
| 节点来源 | `/Users/stark/Library/Application Support/io.github.clash-verge-rev.clash-verge-rev/profiles/RuG18m6w29Or.yaml`（Clash Verge 当前订阅「辐射网络」），每小时重读 |
| 选节点 | `PS5` = fallback[`HK`, `JP`, `TW`, `US`]，各组为 url-test（每 5 分钟测 `gstatic generate_204`，容差 80ms）；优先香港最快可用节点 |
| 转发 | `en0` 别名 `172.22.1.4/16`；pf 锚点 `com.apple/ps5-clash` 只把源地址 `172.22.2.4` 的包 `route-to utun233`；IP 转发开启 |
| DNS | PS5 的 DNS 请求被网关劫持，经所选节点走 `1.1.1.1` / `8.8.8.8` DoH |
| 本机端口 | 控制接口 `127.0.0.1:9098`（密钥在 `secret`）、测试用 mixed `127.0.0.1:7898`、DNS `127.0.0.1:1054` |

PS5 网络设置（与原 UU 设置相同，不用改）：Wi-Fi `CMCC-W6mj-5G`，IP 手动 `172.22.2.4`，掩码 `255.255.0.0`，网关 `172.22.1.4`，首选 DNS `6.6.6.6`，备用 DNS `0.0.0.0`，代理不使用，MTU 自动。

## 日常使用（无需执行本技能）

- 网关随 Mac 开机自动运行。PS5 用下面的手动设置后，任意联网游戏（《星际战士2》、GTA5 Online 等）都会自动走 Clash 订阅节点，不需要先执行 `/ask-星际战士2`，也不需要打开 Cursor 或 UU。
- 本技能只在需要排障、看节点、换节点、停用、恢复或改配置时使用。
- P2P 游戏（如 GTA5 Online 战局）的 NAT 类型取决于节点的 UDP 支持，首次使用要实测；异常时先看 `mihomo.log` 里的 UDP 报错。
- Mac 不会空闲休眠（`pmset` sleep=0）。手动睡眠，或没接外接显示器和电源时合盖，会让 PS5 断网。

## 工作流

1. **先复核现场**（不改任何东西）：

```bash
B=/usr/local/ps5-clash-gateway; SECRET=$(cat $B/secret)
launchctl print system/com.stark.ps5-clash-gateway | grep -E 'state =|pid =' | head -n 2
tail -n 5 $B/gateway.log
ifconfig en0 | grep 172.22.1.4; ifconfig utun233 | grep inet
for g in PS5 HK JP TW US; do curl -s -H "Authorization: Bearer $SECRET" http://127.0.0.1:9098/proxies/$g | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d["name"],"->",d.get("now"))'; done
curl -s -H "Authorization: Bearer $SECRET" http://127.0.0.1:9098/connections | python3 -c 'import sys,json,collections;cs=json.load(sys.stdin).get("connections") or [];print(collections.Counter(tuple(c["chains"]) for c in cs if c["metadata"].get("sourceIP")=="172.22.2.4"))'
```

2. **PS5 连不上网**：确认 UU 未在加速、`172.22.1.4` 在 `en0` 上、`mihomo.log` 里是否有 `dial ... timed out`。节点整体不通时手动测速刷新：`curl -s -H "Authorization: Bearer $SECRET" "http://127.0.0.1:9098/group/HK/delay?timeout=3000&url=https%3A%2F%2Fwww.gstatic.com%2Fgenerate_204"`。
3. **临时固定某个节点**（重启服务后恢复自动）：`curl -X PUT -H "Authorization: Bearer $SECRET" -H 'Content-Type: application/json' -d '{"name":"香港C7"}' http://127.0.0.1:9098/proxies/HK`。
4. **需要 root 的操作**用 `osascript -e 'do shell script "..." with administrator privileges'`，让用户在密码框里输入：
   - 重启：`launchctl kickstart -k system/com.stark.ps5-clash-gateway`
   - 停用：`launchctl bootout system/com.stark.ps5-clash-gateway`（脚本会移除别名和 pf 规则）
   - 恢复：`launchctl bootstrap system /Library/LaunchDaemons/com.stark.ps5-clash-gateway.plist`
   - 改配置：先在临时目录改副本并用 `SAFE_PATHS=<profiles 目录> verge-mihomo -t -d <临时目录> -f <config>` 校验，再 `install -o root -g wheel -m 600` 覆盖并 kickstart。
5. **Clash Verge 更新后**内核副本不会自动更新；需要时用 `install -o root -g wheel -m 755 "/Applications/Clash Verge.app/Contents/MacOS/verge-mihomo" /usr/local/ps5-clash-gateway/verge-mihomo` 后 kickstart。
6. **Clash Verge 换了订阅配置**（profiles.yaml 的 `current` 不再是 `RuG18m6w29Or`）：更新 `config.yaml` 里 provider 的 `path`，否则网关仍读旧文件。

## 边界

- 不改 Cursor、Codex、Git、终端的 `127.0.0.1:4782`，不改 Clash Verge 的 `7897`、系统代理、`verge.yaml`。网关规则只匹配 PS5 源地址。
- 网关运行时不要在 UU 里点加速（两者都占用 `172.22.1.4`）；不要打开 Clash Verge 的 TUN 模式（地址段 `198.18.0.0/15` 重叠）。
- Mac 必须开机、不休眠、连在同一 Wi-Fi；Mac 休眠或关机时 PS5 无法联网，此时把 PS5 改回自动获取 IP/DNS 即可直连。
- 订阅到期或节点全挂时加速不可用；「辐射网络」套餐到期日见节点名（2026-10-11）。
- 不把 `*.playstation.net`、`*.prismray.io` 写进全局 bypass 或 `NO_PROXY`。
- 长期结论写回 Mac 基线文档对应小节，不新建零散 Markdown。
