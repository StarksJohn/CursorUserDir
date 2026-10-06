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
- 该方案适用于 PS5 上所有联网游戏，不再需要 UU 加速器。UU `2.8.11` 仍安装着，01:53 已退出。
- 开机后只需打开 Clash Verge：它负责 Cursor、Codex 的 `4782 -> 7897` 链路和订阅自动更新（每 1440 分钟）。PS5 网关本身不依赖 Clash Verge 进程，没开时继续用上次保存的订阅文件。
- 在 Clash Verge 里切换 `辐射网络` 的节点（如 `美国B1`），只影响经 `7897` 的流量（Cursor、Codex、Git、终端、浏览器等走系统代理的应用），不影响 PS5 网关。两边只共用订阅，节点本身故障时恰好在用它的一方才受影响。
- 实测节点：`02:18–02:48` 每轮测速里 `香港C7` 都最快（124–139ms），`香港C3/C4/C6` 约 220–310ms。`01:59` 时只有 `香港C7` 能通，香港A1/A2、日本A1/A5、台湾A1、美国A1 连不上服务器，说明节点可用性会变，要靠自动测速。
- 约 `02:44` 出现一次「连接丢失（错误代码 140）」，重启游戏后恢复。当时订阅文件没更新（mtime `2026-09-30 16:00:47`），节点没切换，网关没有报错，另一条游戏连接一直存活。判断为单条会话瞬断（线路抖动或 Saber 服务端断开），不是本方案的配置问题。

- 2026-10-02 `19:26:56` 网关日志的 `stopping` 是 Mac 正常重启（`kern.boottime` 19:27:14，`ShutdownCause: 1: Normal warm reset`，无 panic 报告），launchd 关机时发 SIGTERM，脚本按设计清理后退出；不是 Clash Verge 杀的，也不是网关崩溃。重启期间 PS5 断网，游戏会掉线。
- 同日 `19:28` Clash Verge 报 `process verge-mihomo remains after IPC failure; refusing a second core`、没有节点，原因是网关内核当时也叫 `verge-mihomo`；已改名 `ps5-mihomo`，之后两个内核并存无报错。Clash Verge 二进制里没有按名字批量 kill 的逻辑。

- 2026-10-06 组队时游戏延迟超过 200ms：（1）发现网关数据包风暴，`ps5-mihomo` 空载 CPU 约 150%，`utun233` 每秒约 40 万包进、20 万包出；root 抓包显示全是 PS5 的 mDNS 组播（`172.22.2.4:5353 > 224.0.0.251:5353`）在网关里循环。原因是 pf 规则 `to ! 172.22.0.0/16` 也把组播和广播送进了 TUN。已在 `pf.conf` 首行放行 `224.0.0.0/4` 和 `255.255.255.255`（不 route-to），并在 `ps5-gateway.sh` 加了风暴看门狗（10 秒内增量超 150 万包且连续两次就重启 mihomo）。PS5 离线，修复效果未实测。（2）物理路径：经 HK 出口到欧洲约 200ms、美国约 270ms（估算），到亚洲约 30–80ms。队友或房主在欧美时延迟本来就会超过 200ms。详见 Mac 基线文档「组队延迟超过 200ms 排查」。

- 2026-10-06 `18:35` 风暴复发并导致错误代码 142：看门狗检测到进包数异常后重启 mihomo，PS5 到 `prismray.io` 的 TCP 连接被一起断开，那一局结束后弹出「连接丢失（错误代码：142）」。风暴前 4 秒 PS5 发出一条 UDP 到队友私网地址 `192.168.137.1:48895`（命中 `192.168.0.0/16 DIRECT`），说明只排除组播不够。已在 `pf.conf` 增加 `block drop` 丢弃 PS5 发往 `10/8`、`192.168/16`、`169.254/16`、`100.64/10` 的 UDP（推断的触发路径，未证实）；看门狗首次异常时会把抓包和连接列表存到 `/usr/local/ps5-clash-gateway/storm-*.txt` 和 `.connections.json`（保留 5 份）。再次遇到 142 或风暴，先读这些文件和 `gateway.log` 里的 `high packet rate`、`packet storm`。同日更正：不要仅凭 whois 国家和 ping 断定对局服务器位置，要核对游戏内显示的延迟。

- 2026-10-06 `18:49` 修复后的验证：到 `19:23` 共 34 分钟，联机一局稳定约 50ms，无风暴日志、无 `storm-*` 证据文件，`ps5-mihomo` CPU 为 0.0%。重启后不开 Clash Verge 网关照样加速（provider 是 `File` 类型，日志里没有 `7897` 或 `clash-verge`；未实测过完全不开 Clash Verge 玩一局）。唯一联系是订阅文件：它只在 Clash Verge 运行时更新，建议每天开一次；套餐 `2026-10-11` 到期。延迟水平由对局服务器和房主位置决定，约 50ms 说明对手在香港或华南一带（推断）；无法保证任何地区队友都低于 70ms。详见 Mac 基线文档「PS5 组队延迟高与错误代码 142 排查」。

## 当前方案

| 项 | 值 |
| --- | --- |
| 常驻服务 | LaunchDaemon `com.stark.ps5-clash-gateway`（`/Library/LaunchDaemons/com.stark.ps5-clash-gateway.plist`），开机自启，以 root 运行，不依赖 Cursor |
| 目录 | `/usr/local/ps5-clash-gateway/`：`ps5-gateway.sh`、`config.yaml`、`pf.conf`、`ps5-mihomo`（Clash Verge 内核副本）、`secret`、`gateway.log`、`mihomo.log` |
| 节点来源 | `/Users/stark/Library/Application Support/io.github.clash-verge-rev.clash-verge-rev/profiles/RuG18m6w29Or.yaml`（Clash Verge 当前订阅「辐射网络」），每小时重读 |
| 选节点 | `PS5` = fallback[`HK`, `JP`, `TW`, `US`]，各组为 url-test（每 5 分钟测 `gstatic generate_204`，容差 80ms）；优先香港最快可用节点。provider 必须开 health-check（`enable: true`、`interval: 300`、`lazy: false`），否则不会测速、只停在第一个节点。换节点时已建立的连接留在原节点 |
| 内核 | `/usr/local/ps5-clash-gateway/ps5-mihomo`，即 Mihomo `v1.19.31` 副本；日志级别 `warning`。进程名不能是 `verge-mihomo`，否则 Clash Verge 会把它当成自己的残留内核并拒绝启动 |
| 转发 | `en0` 别名 `172.22.1.4/16`；pf 锚点 `com.apple/ps5-clash` 只把源地址 `172.22.2.4` 的单播包 `route-to utun233`（发往 `224.0.0.0/4`、`255.255.255.255` 的组播广播包先 `pass`，不进 TUN）；IP 转发开启 |
| DNS | PS5 的 DNS 请求被网关劫持，经所选节点走 `1.1.1.1` / `8.8.8.8` DoH |
| 本机端口 | 控制接口 `127.0.0.1:9098`（密钥在 `secret`）、测试用 mixed `127.0.0.1:7898`、DNS `127.0.0.1:1054` |

PS5 网络设置（与原 UU 设置相同，不用改）：Wi-Fi `CMCC-W6mj-5G`，IP 手动 `172.22.2.4`，掩码 `255.255.0.0`，网关 `172.22.1.4`，首选 DNS `6.6.6.6`，备用 DNS `0.0.0.0`，代理不使用，MTU 自动。

## 日常使用（无需执行本技能）

- 网关随 Mac 开机自动运行。PS5 用下面的手动设置后，任意联网游戏（《星际战士2》、GTA5 Online 等）都会自动走 Clash 订阅节点，不需要先执行 `/ask-星际战士2`，也不需要打开 Cursor 或 UU。
- 本技能只在需要排障、看节点、换节点、停用、恢复或改配置时使用。
- P2P 游戏（如 GTA5 Online 战局）的 NAT 类型取决于节点的 UDP 支持，首次使用要实测；异常时先看 `mihomo.log` 里的 UDP 报错。
- Mac 不会空闲休眠（`pmset` sleep=0）。手动睡眠，或没接外接显示器和电源时合盖，会让 PS5 断网。
- 开机全自动：LaunchDaemon 开机即启动，不依赖登录、Cursor、Clash Verge、UU。脚本检测到默认路由走 `en0` 且 `223.5.5.5` 可达（日志 `network up`）后，立即对 `HK/JP/TW/US` 触发测速，并在 30 秒、90 秒后各再测一次，避免开机瞬间无网时测速全失败、节点要等 5 分钟才恢复。重启后看 `gateway.log` 应有 `alias ... added`、`pf anchor loaded`、`network up`、`node refresh done`。
- 未验证：重启后登录界面（未登录）时 Wi-Fi 是否已联网。FileVault 关闭、没有设置自动登录。若重启后不登录 PS5 上不了网，就登录一次，或让用户决定是否开启自动登录。

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
3. **游戏中途掉线（如错误代码 140）**：先查三件事，都正常就按瞬断处理，重启游戏即可。一是订阅文件的 mtime 有没有变（`stat -f '%Sm' <订阅文件>`）；二是 `/providers/proxies/sub` 里各节点 `history` 有没有失败或切换；三是 `/connections` 里 PS5 的连接从哪个时间点开始重建。频繁复现时，经用户同意把 `config.yaml` 的 `log-level` 改为 `info`，记录每条连接，定位后再改回 `warning`。
3a. **游戏延迟高（如组队超过 200ms）**：PS5 在线时先看三项。一是 `ps -o pcpu= -p $(pgrep -f 'ps5-mihomo -d')` 是否空载仍有高 CPU；二是 `netstat -I utun233 -b` 隔几秒看输入包数增长（正常远低于每秒 5 万；每秒数十万是风暴，重启服务可解除，抓包需要 root：`tcpdump -i utun233 -n -c 40`）；三是 `/connections` 里 `sourceIP=172.22.2.4` 的目标地址和链路。节点测速值（200–900ms）不是路径往返延迟，不要拿它判断游戏延迟，需要路径估算时用 `curl -x http://127.0.0.1:7898 -w '%{time_appconnect}' https://s3.<区域>.amazonaws.com/`，往返约为结果的一半。
4. **临时固定某个节点**（重启服务后恢复自动）：`curl -X PUT -H "Authorization: Bearer $SECRET" -H 'Content-Type: application/json' -d '{"name":"香港C7"}' http://127.0.0.1:9098/proxies/HK`。
5. **需要 root 的操作**用 `osascript -e 'do shell script "..." with administrator privileges'`，让用户在密码框里输入：
   - 重启：`launchctl kickstart -k system/com.stark.ps5-clash-gateway`
   - 停用：`launchctl bootout system/com.stark.ps5-clash-gateway`（脚本会移除别名和 pf 规则）
   - 恢复：`launchctl bootstrap system /Library/LaunchDaemons/com.stark.ps5-clash-gateway.plist`
   - 改配置：先在临时目录改副本并用 `SAFE_PATHS=<profiles 目录> verge-mihomo -t -d <临时目录> -f <config>` 校验，再 `install -o root -g wheel -m 600` 覆盖并 kickstart。
6. **Clash Verge 更新后**内核副本不会自动更新；需要时用 `install -o root -g wheel -m 755 "/Applications/Clash Verge.app/Contents/MacOS/verge-mihomo" /usr/local/ps5-clash-gateway/ps5-mihomo` 后 kickstart。目标文件名必须是 `ps5-mihomo`。
7. **Clash Verge 换了订阅配置**（profiles.yaml 的 `current` 不再是 `RuG18m6w29Or`）：更新 `config.yaml` 里 provider 的 `path`，否则网关仍读旧文件。

## 边界

- 不改 Cursor、Codex、Git、终端的 `127.0.0.1:4782`，不改 Clash Verge 的 `7897`、系统代理、`verge.yaml`。网关规则只匹配 PS5 源地址。
- 网关运行时不要在 UU 里点加速（两者都占用 `172.22.1.4`）；不要打开 Clash Verge 的 TUN 模式（地址段 `198.18.0.0/15` 重叠）。
- Mac 必须开机、不休眠、连在同一 Wi-Fi；Mac 休眠或关机时 PS5 无法联网，此时把 PS5 改回自动获取 IP/DNS 即可直连。
- 订阅到期或节点全挂时加速不可用；「辐射网络」套餐到期日见节点名（2026-10-11）。
- 两个内核互不干扰的规则：网关内核文件名永远是 `ps5-mihomo`；端口（网关 `7898/9098/1054`，Clash Verge `7897`）、TUN（`utun233`，Clash TUN 关闭）、配置目录都不重叠；不要让 Clash Verge 管理或重启网关；改脚本或升级内核后确认 `pgrep -lf mihomo` 里同时有 `verge-mihomo` 和 `ps5-mihomo`。
- 不把 `*.playstation.net`、`*.prismray.io` 写进全局 bypass 或 `NO_PROXY`。
- 长期结论写回 Mac 基线文档对应小节，不新建零散 Markdown。
