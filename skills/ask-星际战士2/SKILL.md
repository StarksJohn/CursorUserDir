---
name: ask-星际战士2
description: >-
  《战锤40K：星际战士2》（Space Marine 2）与 PS5 联网游戏加速入口。用于 CSF、错误代码 140/142 等联网报错，
  PS5 联机延迟高或掉线，PS5 经 Mac + Clash Verge 节点加速（替代 UU 加速器），查看/固定加速节点，
  抓包定位网关数据包风暴，停用或恢复 PS5 网关，以及每次 PS5 加速任务结束后把事实沉淀到文档。
  用户执行 /ask-星际战士2、@ask-星际战士2，或提到 星际战士2、Space Marine 2、PS5 加速、PS5 延迟、CSF 时使用。
---

# ask-星际战士2

## Purpose

用 Mac 上的独立 mihomo 网关给 PS5 的所有联网游戏加速，替代 UU 加速器；本技能负责排障、看节点、换节点、改配置，并把每次任务的事实沉淀下来。

## 项目路径

- Windows：`D:\work\星际战士2`
- Mac 基线文档（详细事实）：`/Users/stark/Desktop/work/MAC/MAC系统相关配置.md`，「PS5 联网游戏网关（替代 UU）」一节
- 本技能（稳定结论、流程、事件索引）：`/Users/stark/.cursor/skills/ask-星际战士2/SKILL.md`

## 输入格式

在 Cursor 输入 `/ask-星际战士2` 或 `@ask-星际战士2`，后面可附带当前问题或截图。有截图时先按精确路径读图再判断。

## 沉淀规则（每次 PS5 加速任务结束前必做）

适用：排障、测速、抓包、改节点、改 pf 或脚本或配置、重启服务、核对状态，以及用户反馈延迟数字或错误代码。

1. 把本次事实同时写进两个文件：
   - Mac 基线文档：详细数据、测量方法、时间线，写在「PS5 联网游戏网关」一节下对应的小节；没有合适小节就新增一个带日期的小节。
   - 本技能：只写稳定结论，以及「事件索引」里的一行摘要；如果「当前方案」「工作流」「边界」受影响，同步改这些章节。
2. 每条事实写清：日期和时间、现象（含用户给出的延迟数字、错误代码、截图内容）、检查结果（关键命令和数值）、结论，并标明「实测」「推断」「未验证」，改动了什么（文件、规则、生效时间、是否重启后失效）、遗留项。
3. 新事实推翻旧结论时，直接修改旧条目并注明「更正」，不要让两条矛盾的结论并存；纯查看状态且没有新事实时，可以不写，但要在回复里说明。
4. 不写入：订阅里的节点密码、`secret` 内容、任何令牌；不记录队友的公网 IP，服务器和机房地址可以写。
5. 不新建零散的 Markdown 文件；长数据放基线文档，不堆在本技能里。
6. 回复末尾说明更新了哪两个文件的哪些章节，并给出下一步建议。

## 已确认结论（稳定事实）

- UU 加速《星际战士2》会报 CSF：香港、新加坡、欧洲、北美节点以及 UU 的其它游戏配置都一样；直连能进但延迟高。原因在 UU 的转发方式，本机改不了，UU 客服未回复。
- 替代方案：PS5 以 Mac 为网关，只把 PS5 的流量送进独立的 mihomo 内核，节点来自 Clash Verge 当前订阅，自动选最快可用节点。适用于 PS5 上所有联网游戏，不再需要 UU（`2.8.11` 仍安装着，未使用）。
- 两个内核各管各的：在 Clash Verge 里切换 `辐射网络` 的节点只影响经 `7897` 的流量（Cursor、Codex、Git、终端、浏览器），不影响 PS5 网关；两边只共用订阅文件。
- 网关不依赖 Clash Verge 进程：provider 是 `File` 类型，日志里没有 `7897` 或 `clash-verge`。唯一联系是订阅文件，它只在 Clash Verge 运行时更新，建议每天开一次。
- 开机自启：LaunchDaemon 开机即启动，不依赖登录、Cursor、Clash Verge、UU；联网后立即触发节点测速。
- 节点可用性会变：`01:59` 时只有 `香港C7` 能通；晚高峰时所有香港节点都有 400–1900ms 尖峰。节点测速值（200–900ms）不是路径往返延迟，不能直接拿来判断游戏延迟。
- 延迟的物理下限：经香港出口到亚洲约 30–80ms，到欧洲约 200ms，到美国约 270ms（估算）。无法保证任何地区的队友都低于 70ms。不要只凭 whois 国家和 ping 断定对局服务器位置，要核对游戏内显示的延迟。
- 路径质量随时段变化：空闲时经 C7 访问香港目标的 TLS 完成时间约 67–71ms；晚高峰（`2026-10-08 00:20–00:41`）中位数 116–118ms，原因是中国移动国际网关（CMI，`223.120.3.185`、`223.118.6.114`）丢包约 5%。UDP 经 AnyTLS 以 UDP over TCP 转发，丢包会触发重传卡顿。
- mihomo 的连接一旦建立就固定在当时的节点上，换节点只影响新连接；UDP 对局换节点会改变出口源地址，可能掉线，不要在对局中强行断开。

## 事件索引（一行一事，详情见基线文档）

| 日期              | 现象                                  | 结论                                                                                                              | 状态                   |
| ----------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------- |
| 10-01             | UU 加速报 CSF                         | 改用网关，进游戏约 70ms（香港C7）                                                                                 | 已解决                 |
| 10-01 02:44       | 错误代码 140                          | 单条会话瞬断，订阅和节点都没变                                                                                    | 无需处理               |
| 10-02 19:26       | 网关日志 `stopping`                   | Mac 正常重启（`Normal warm reset`），不是 Clash 或崩溃                                                            | 无需处理               |
| 10-02 19:28       | Clash Verge 无节点、内核报错          | 网关内核名 `verge-mihomo` 与 Clash Verge 重名，已改为 `ps5-mihomo`                                                | 已解决                 |
| 10-02 19:41       | 开机后节点要等 5 分钟                 | 开机无网时测速全失败，已加联网检测并立即测速                                                                      | 已解决                 |
| 10-06 18:00       | 组队延迟超过 200ms，网关空载 CPU 150% | `utun233` 数据包风暴（PS5 的 mDNS 组播在网关里循环）；pf 放行组播，加看门狗                                       | 已处理                 |
| 10-06 18:35       | 错误代码 142                          | 风暴复发，看门狗重启 mihomo 断开了连接；风暴前 4 秒有 UDP 到队友私网地址；pf 丢弃私网 UDP，并在首次异常时保存证据 | 已处理，触发路径是推断 |
| 10-06 18:49–19:23 | 修复后验证                            | 一局稳定约 50ms，无风暴，CPU 0.0%                                                                                 | 已验证                 |
| 10-08 00:02       | 联机延迟高                            | 对局连接在 `香港D6` 上，D 系列抖动大；HK 组临时固定到 `香港C7`                                                    | 临时，重启后恢复自动   |
| 10-08 00:20–00:41 | 换到 C7 后仍高，用户实测 PVE 约 100ms | 全部节点都有尖峰，CMI 国际网关丢包 5%，是运营商晚高峰拥堵                                                         | 网关侧无可调           |

## 未验证与遗留

- 重启后在登录界面（未登录）时 Wi-Fi 是否已联网：FileVault 关闭、没有设置自动登录，未实测。
- 重启后完全不开 Clash Verge 玩一局：未实测。
- 风暴的触发路径是否只有组播和私网 UDP：`18:49` 之后一局无复发，但触发包没有抓到，下次出现看 `storm-*.txt`。
- HK 组长期选节点方案（调大 `tolerance` 或只用 C 系列）：需要改 `config.yaml`，要先问用户；晚高峰所有节点都抖动，收益有限。
- 订阅「辐射网络」套餐 `2026-10-11` 到期，到期后加速不可用。
- 截至 `2026-10-08 00:41`，HK 组固定在 `香港C7`，重启服务或开机后恢复自动选择。

## 当前方案

| 项       | 值                                                                                                                                                                                                                                                                                                                                  |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 常驻服务 | LaunchDaemon `com.stark.ps5-clash-gateway`（`/Library/LaunchDaemons/com.stark.ps5-clash-gateway.plist`），开机自启，以 root 运行，不依赖 Cursor                                                                                                                                                                                     |
| 目录     | `/usr/local/ps5-clash-gateway/`：`ps5-gateway.sh`、`config.yaml`、`pf.conf`、`ps5-mihomo`（Clash Verge 内核副本）、`secret`、`gateway.log`、`mihomo.log`、`storm-*.txt` 与 `storm-*.connections.json`（风暴证据，保留 5 份）                                                                                                        |
| 节点来源 | `/Users/stark/Library/Application Support/io.github.clash-verge-rev.clash-verge-rev/profiles/RuG18m6w29Or.yaml`（Clash Verge 当前订阅「辐射网络」），每小时重读                                                                                                                                                                     |
| 选节点   | `PS5` = fallback[`HK`, `JP`, `TW`, `US`]，各组为 url-test（每 5 分钟测 `gstatic generate_204`，容差 80ms，只看最近一次测速）。provider 必须开 health-check（`enable: true`、`interval: 300`、`lazy: false`），否则不会测速                                                                                                          |
| 内核     | `/usr/local/ps5-clash-gateway/ps5-mihomo`，Mihomo `v1.19.31` 副本；日志级别 `warning`。进程名不能是 `verge-mihomo`，否则 Clash Verge 会把它当成残留内核并拒绝启动                                                                                                                                                                   |
| 转发     | `en0` 别名 `172.22.1.4/16`；IP 转发开启；pf 锚点 `com.apple/ps5-clash`（`pf.conf`）三条规则：1) 源 `172.22.2.4` 发往 `224.0.0.0/4`、`255.255.255.255` 的包 `pass`，不进 TUN；2) 发往 `10.0.0.0/8`、`192.168.0.0/16`、`169.254.0.0/16`、`100.64.0.0/10` 的 UDP `block drop`；3) 其余发往 `172.22.0.0/16` 以外的包 `route-to utun233` |
| 看门狗   | `ps5-gateway.sh` 每 10 秒读 `utun233` 输入包数，增量超过 150 万且连续两次就重启 mihomo，首次异常先保存抓包和连接列表；日志关键字 `high packet rate`、`packet storm`、`storm capture saved`。联网检测日志关键字 `network up`、`node refresh done`                                                                                    |
| DNS      | PS5 的 DNS 请求被网关劫持，经所选节点走 `1.1.1.1` / `8.8.8.8` DoH                                                                                                                                                                                                                                                                   |
| 本机端口 | 控制接口 `127.0.0.1:9098`（密钥在 `secret`）、测试用 mixed `127.0.0.1:7898`、DNS `127.0.0.1:1054`                                                                                                                                                                                                                                   |

PS5 网络设置（与原 UU 设置相同，不用改）：Wi-Fi `CMCC-W6mj-5G`，IP 手动 `172.22.2.4`，掩码 `255.255.0.0`，网关 `172.22.1.4`，首选 DNS `6.6.6.6`，备用 DNS `0.0.0.0`，代理不使用，MTU 自动。

## 日常使用（无需执行本技能）

- 网关随 Mac 开机自动运行。PS5 用上面的手动设置后，任意联网游戏（《星际战士2》、GTA5 Online 等）都会自动走订阅节点，不需要先执行 `/ask-星际战士2`，也不需要打开 Cursor 或 UU。
- 本技能只在排障、看节点、换节点、停用、恢复或改配置时使用。
- P2P 游戏的 NAT 类型取决于节点的 UDP 支持，首次使用要实测；异常先看 `mihomo.log` 里的 UDP 报错。
- Mac 不会空闲休眠（`pmset` sleep=0）。手动睡眠，或没接外接显示器和电源时合盖，会让 PS5 断网。
- 重启后看 `gateway.log` 应有 `alias ... added`、`pf anchor loaded`、`network up`、`node refresh done`。

## 工作流

1. **先复核现场**（不改任何东西）：

```bash
B=/usr/local/ps5-clash-gateway; SECRET=$(cat $B/secret)
launchctl print system/com.stark.ps5-clash-gateway | grep -E 'state =|pid =' | head -n 2
tail -n 8 $B/gateway.log; ls $B | grep storm
ps -o pcpu=,etime= -p $(pgrep -f 'ps5-mihomo -d')
ifconfig en0 | grep 172.22.1.4; ifconfig utun233 | grep inet; netstat -I utun233 -b
for g in PS5 HK JP TW US; do curl -s -H "Authorization: Bearer $SECRET" http://127.0.0.1:9098/proxies/$g | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d["name"],"->",d.get("now"),d.get("fixed"))'; done
curl -s -H "Authorization: Bearer $SECRET" http://127.0.0.1:9098/connections | python3 -c 'import sys,json;cs=json.load(sys.stdin).get("connections") or [];[print(c["metadata"]["network"],c["metadata"].get("host") or "-",c["metadata"].get("destinationIP"),c["metadata"].get("destinationPort"),c["chains"][:1],c["upload"],c["download"],c["start"][11:19]) for c in cs if c["metadata"].get("sourceIP")=="172.22.2.4"]'
```

   Shell 的当前目录被删除后命令会报 `spawn /bin/zsh ENOENT`，每次调用都指定 `working_directory`。

2. **PS5 连不上网**：确认 UU 未在加速、`172.22.1.4` 在 `en0` 上、`mihomo.log` 里是否有 `dial ... timed out`。节点整体不通时手动测速刷新：`curl -s -H "Authorization: Bearer $SECRET" "http://127.0.0.1:9098/group/HK/delay?timeout=3000&url=https%3A%2F%2Fwww.gstatic.com%2Fgenerate_204"`。
3. **游戏中途掉线（如错误代码 140、142）**：先查 `gateway.log` 有没有 `packet storm`（有就是看门狗重启造成的 142，读 `storm-*.txt` 和 `.connections.json` 定位触发包）；再查订阅文件 mtime（`stat -f '%Sm' <订阅文件>`）、`/providers/proxies/sub` 里节点 `history` 有没有失败或切换、`/connections` 里 PS5 的连接从哪个时间点重建。都正常就按瞬断处理，重启游戏即可。频繁复现时，经用户同意把 `config.yaml` 的 `log-level` 改为 `info`，定位后改回 `warning`。
4. **游戏延迟高**：先分段排查，再决定要不要换节点。
   - 网关侧：`ps -o pcpu=` 是否空载仍有高 CPU；`netstat -I utun233 -b` 隔几秒看输入包数（正常远低于每秒 5 万，每秒数十万是风暴，重启服务可解除；root 抓包用 `tcpdump -i utun233 -n -c 40`）。
   - 本地链路：`ping` 路由器和 `223.5.5.5`，各 30 次看抖动和丢包。
   - 国内骨干和国际出口：`traceroute -n -m 12 -w 1 -q 1 <目标>`，再对 CMI 的几跳各 `ping -c 40 -i 0.25`，看丢包。
   - 节点路径：经 `7898` 测量 `curl -x http://127.0.0.1:7898 -w '%{time_appconnect}' https://s3.ap-east-1.amazonaws.com/`（香港目标，TLS 完成时间约等于两个往返），连续 20–60 次看 p50、p90、最大值；对比空闲时的 67–71ms。
   - 单个 provider 节点的测速用 `GET /providers/proxies/sub/<节点名URL编码>/healthcheck?timeout=4000&url=...`；`/proxies/<节点名>/delay` 对 provider 节点返回 404。多节点对比要在同一时间窗口内交替测，并丢掉冷启动的第一次。
   - `/connections` 里 `sourceIP=172.22.2.4` 的 UDP 连接就是对局流量，记录目标地址、节点、字节数；对局服务器位置用游戏内延迟核对，不要只看 whois。
   - 判断：本地链路干净、网关正常、全部节点都有尖峰，就是运营商国际出口拥堵，网关侧无可调，建议避开晚高峰或换不经 CMI 的宽带。
5. **临时固定某个节点**（重启服务后恢复自动，只影响新建连接）：`curl -X PUT -H "Authorization: Bearer $SECRET" -H 'Content-Type: application/json' -d '{"name":"香港C7"}' http://127.0.0.1:9098/proxies/HK`。固定后确认 `/proxies/HK` 的 `now` 和 `fixed`。
6. **需要 root 的操作**用 `osascript -e 'do shell script "..." with administrator privileges'`，让用户在密码框里输入；被自动审查拦下时，用 `request_smart_mode_approval` 原样重试。先把改动文件放到 `/tmp` 下的临时目录，`bash -n` 或 `pfctl -n -f` 校验，再安装，最后删除临时目录：
   - 重启（会让 PS5 断线十几秒，对局中不要做）：`launchctl kickstart -k system/com.stark.ps5-clash-gateway`
   - 停用：`launchctl bootout system/com.stark.ps5-clash-gateway`（脚本会移除别名和 pf 规则）
   - 恢复：`launchctl bootstrap system /Library/LaunchDaemons/com.stark.ps5-clash-gateway.plist`
   - 改脚本或 pf：`install -o root -g wheel -m 755 <脚本>`、`install -o root -g wheel -m 644 <pf.conf>` 后 kickstart；pf 可单独热加载：`pfctl -a com.apple/ps5-clash -f /usr/local/ps5-clash-gateway/pf.conf`，但已存在的风暴要重启服务才会停。
   - 改配置：先在临时目录改副本并用 `SAFE_PATHS=<profiles 目录> ps5-mihomo -t -d <临时目录> -f <config>` 校验，再 `install -o root -g wheel -m 600` 覆盖并 kickstart。
7. **Clash Verge 更新后**内核副本不会自动更新；需要时用 `install -o root -g wheel -m 755 "/Applications/Clash Verge.app/Contents/MacOS/verge-mihomo" /usr/local/ps5-clash-gateway/ps5-mihomo` 后 kickstart。目标文件名必须是 `ps5-mihomo`。
8. **Clash Verge 换了订阅配置**（`profiles.yaml` 的 `current` 不再是 `RuG18m6w29Or`）：更新 `config.yaml` 里 provider 的 `path`，否则网关仍读旧文件。
9. **任务结束**：按「沉淀规则」更新两个文件，并在回复里说明更新了哪些章节。

## 边界

- 不改 Cursor、Codex、Git、终端的 `127.0.0.1:4782`，不改 Clash Verge 的 `7897`、系统代理、`verge.yaml`。网关规则只匹配 PS5 源地址。
- 网关运行时不要在 UU 里点加速（两者都占用 `172.22.1.4`）；不要打开 Clash Verge 的 TUN 模式（地址段 `198.18.0.0/15` 重叠）。
- Mac 必须开机、不休眠、连在同一 Wi-Fi；Mac 休眠或关机时 PS5 无法联网，此时把 PS5 改回自动获取 IP/DNS 即可直连。
- 订阅到期或节点全挂时加速不可用。
- 两个内核互不干扰：网关内核文件名永远是 `ps5-mihomo`；端口（网关 `7898/9098/1054`，Clash Verge `7897`）、TUN（`utun233`，Clash TUN 关闭）、配置目录都不重叠；不要让 Clash Verge 管理或重启网关；改脚本或升级内核后确认 `pgrep -lf mihomo` 里同时有 `verge-mihomo` 和 `ps5-mihomo`。
- 不把 `*.playstation.net`、`*.prismray.io` 写进全局 bypass 或 `NO_PROXY`。
- 在对局中不要重启网关或强行关闭 UDP 连接；改动前先确认 PS5 没有进行中的对局。
- 不对用户保证队友在任何地区的延迟都低于某个数；只报告实测值和物理下限。

<!-- ## 我现在正在玩<战锤40K 星际战士 2>PVE 联机模式,延迟突然很高,超过 200+,帮我优化; -->