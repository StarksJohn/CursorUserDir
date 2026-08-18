---
name: ask-csx-web
description: >-
  Cursor：csx-web / ClinicSolution Web Vue 2 前端项目入口。用于在用户输入
  /ask-csx-web、当前工作区为 csx-web，或任务明确属于旧 Vue 系统时恢复路径、
  读取项目规则、收敛范围，并按需路由到关联 React 项目和专项 skills。用户只调用
  入口而没有另给具体任务时，自动解析并继续执行“最新待继续问题”中未被注释的任务。
---

# ask-csx-web

## 路径与事实源

- 项目根：Windows `D:\work\csx-web`；macOS `/Users/<你的用户名>/Desktop/work/csx-web`，当前 Mac 为 `/Users/stark/Desktop/work/csx-web`。
- Codex 对照入口：Windows `%USERPROFILE%\.codex\skills\csx-web\SKILL.md`；macOS `/Users/<你的用户名>/.codex/skills/csx-web/SKILL.md`。
- 关联 React 项目：Windows `D:\work\csx-web-react`；macOS `/Users/<你的用户名>/Desktop/work/csx-web-react`，对应 Cursor Skill 为 `ask-csx-web-react`。
- 业务逻辑、字段绑定、API 映射、组件交互和错误处理：以当前源码、真实页面、Network 和测试为准。
- 技术栈、命令、环境、构建与部署：以 `package.json`、项目配置、`README.md` 和仓库规则为准。
- 本 Skill 只保存入口、加载门禁、跨仓路由和无法从仓库恢复的最小状态，不充当业务事实档案。

发生冲突时，当前代码和真实运行证据优先于历史文档；外部 contract 与产品范围以负责人最新确认优先。

## 最小读取顺序

1. 完整读取本 `SKILL.md`。
2. 确认实际工作区、分支和未提交改动，保留用户已有修改。
3. 读取实际存在且与任务相关的项目规则：`AGENTS.md`、`.cursor/rules/project-context.mdc`、`.cursor/rules/*`。
4. 读取当前任务直接相关的源码与测试；需要命令或环境信息时再读 `package.json`、`README.md` 和对应配置。
5. 仅在需要对齐 Codex 工作流或恢复其未注释活跃需求时读取 Codex 对照入口。
6. 修改关联 React 仓库或处理 TECH-8458、显示屏配置、公开大屏时，先读取 `ask-csx-web-react` Skill，并由它决定后续上下文。
7. 路由到 BMAD、Figma 或其它 Skill 时，先读取对应入口及其要求的依赖文件。

普通代码修复、UI 调整、校验规则或 API 映射问题不从本 Skill 恢复业务细节，直接从代码和真实页面取证。

## 活跃任务解析与自动续做门禁

把“最新待继续问题（不要修改这部分的子内容）”视为用户维护的活跃任务队列，不得只当作背景资料。

1. 解析该区块时完全忽略 `<!-- ... -->` 内的内容，不从注释恢复任务或约束。
2. 将未注释内容分类后再执行：
   - 工作目录、代码风格、工具顺序和禁止事项属于执行约束，对后续相关任务持续生效。
   - 含有“帮我”“先”“实现”“修改”“检查”“启动”“访问”“确保”“调研”等动作要求的条目属于可执行任务。
   - 只有标题或分类名称、且其下没有未注释动作要求的条目只用于组织上下文，不单独视为任务。
3. 用户在调用入口的同一条消息中给出具体任务时，优先执行该任务，并应用与它相关的未注释约束；不要自动展开无关的队列任务。
4. 用户只调用 `/ask-csx-web`、只附上本 Skill、只提供 Skill 路径，或仅要求“继续”但没有另给具体任务时：
   - 立即按文档顺序执行所有尚未由当前真实证据证明完成的未注释可执行任务。
   - 先用简短进度说明识别出的任务队列和执行顺序，然后直接开始，不得停在“上下文已加载”“已就绪”，也不得反问用户下一步做什么。
   - 已有历史摘要只能帮助定位，不能替代对当前代码、Git、进程、页面、Network 或测试的实时核验。
   - 某项受外部权限或人工操作阻塞时，明确记录阻塞，继续处理不依赖该阻塞的其它队列任务。
5. 只有在该区块没有未注释可执行任务、所有任务均已由当前证据确认完成，或用户明确要求“只加载上下文、不执行待继续项”时，才停在等待用户输入的状态。
6. 不修改该区块的子内容；任务是否完成通过当前事实判断，不通过自动注释、删除或改写原条目表示。

## 实施工作流

1. 先读用户附件、真实 DOM、Network 和直接相关代码，确定当前事实。
2. API contract 可由真实页面触发时，先读取实际请求与响应；无法触发或受登录、权限阻塞时，再查 Swagger / OpenAPI 或后端文档。
3. 代码任务依次完成业务实现、定向测试，再处理项目目录外的 Skill、ask 或恢复文档。
4. 修改保持最小范围，遵循仓库现有 Vue 2、Options API、Element UI、Vuex、Vue Router、i18n 和 Axios 封装。
5. 开发阶段优先运行相关文件检查、单用例或单页面验证；阶段收尾再按风险扩大范围。
6. 未运行的构建、测试、浏览器验证或外部页面读取必须明确说明。

## 工程与跨仓边界

- 一般代码任务不复制精确版本、脚本和代理配置；用户明确要求归档的跨团队部署恢复事实可保留最小命令，并将版本、地址和进程状态标记为易变信息。
- 不新增零散 Axios 实例；使用项目现有 API 封装。
- 新增用户可见文案时复用现有 i18n key，必要时同步相关语言包。
- 非必要不新增依赖、不升级旧构建链、不做无关重构。
- 旧 Vue 与 React 分仓修改；未获授权不改另一仓库的依赖、构建或 pipeline。
- 不写入或输出 token、Cookie、密码、私钥、证书和部署凭证。

### Git 分支方向硬门禁

1. 需求分支（例如 `TECH-8713`）必须以最新 `master` 为基线；需求分支需要更新公共代码时，只允许先同步本地 `master` 与 `origin/master`，再执行“最新 `master` -> 需求分支”。需求分支不得以 `dev` 为基线，也不得与最新 `dev` 保持整树一致。
2. 禁止把本地 `dev` 或远程 `origin/dev` merge、rebase、整树覆盖到需求分支、`master` 或任何其它分支，不得通过改变命令形式规避该限制。唯一允许的 `dev` 来源合并是“`origin/dev` -> 本地 `dev`”的同分支同步；这不属于把 `dev` 带入其它分支。
3. 发 POC 前必须执行“需求分支 -> 最新 `dev`”：先切换到本地 `dev`，确认工作区干净并同步 `origin/dev`；再把需求分支 merge 到本地 `dev`。确认无冲突、合并方向与文件差异正确并完成必要测试后，才能 push 本地 `dev`。若 push 前远程 `dev` 又有更新，必须先把 `origin/dev` 同步到本地 `dev` 并重新验证；不得反向把更新后的 `dev` merge 回需求分支。
4. 发 Prod 前必须执行“最新 `master` -> 需求分支 -> 本地 `master`”：先同步本地 `master` 与 `origin/master`，再把最新 `master` merge 到需求分支；确认无冲突并完成必要测试后，把需求分支 merge 到本地 `master`，再次核验后才能 push 本地 `master`。整个 Prod 流程不得使用 `dev` 作为中间基线。
5. 任何跨分支操作前，必须核对当前分支、工作区状态、本地与远程 source/target SHA、merge-base 和提交拓扑；操作后必须核对 merge commit 父节点、实际文件差异、目标分支远端 SHA 和构建/测试结果。方向不清、远端并发更新或差异超出任务范围时立即停止，不得直接 push。
6. 如果修改误做在 `dev` 上，而用户明确要求只转移指定文件或 commit，可以使用定向 patch 或 cherry-pick，但不得 merge `dev`；转移后必须证明需求分支仍以 `master` 为基线，且没有带入 `dev` 的其它提交或文件差异。

## 文档维护规则

- 不把可从源码或测试读取的业务规则、API 字段清单、默认值、修复过程、测试数量和验收流水写入本 Skill。
- 普通代码任务结束不强制更新本 Skill；只有入口、加载门禁、跨仓边界、外部阻塞或无法从代码恢复的下一步发生实质变化时才更新。
- 稳定工程事实通常写入仓库既有规则、`README.md` 或 `docs/`；用户明确要求归档的跨团队部署恢复事实、私有流程和外部协调状态可保留在项目外 Skill。
- 禁止按日期或 chat 追加流水；更新时直接替换过期结论并去重。
- “最新待继续问题（不要修改这部分的子内容）”由用户维护，除非用户明确授权修改，否则保持原文。

## 旧 csx dev（29 内网站点及其 Dev Tunnel 外网入口）部署恢复事实

### 环境关系与访问入口

- 实际部署站点是 29 内网环境 `http://192.168.99.29:8083`；`https://lj3cs48f-8083.jpe1.devtunnels.ms` 只是该站点的 Dev Tunnel 外网入口，不是另一套独立 dev 环境，也不使用另一份前后端部署产物。
- 内网旧 Vue 入口为 `http://192.168.99.29:8083/ui/index.html#/login`；外网入口为 `https://lj3cs48f-8083.jpe1.devtunnels.ms/ui/index.html#/login`。页面、静态文件和同源 `/api/**` 最终都来自 29 对应的同一个旧 CSX 站点。
- Nina 在 29 重新构建和部署后，Dev Tunnel 页面同步更新，可用于验证同一次 29 部署；但 Dev Tunnel 地址、版本号和进程状态可能变化，每次部署或排障仍要实时复核。

### `csx-web` 合并与交接门禁

- `/ui/**` 由旧 Vue 仓库 `csx-web` 提供。若只更新 `http://192.168.99.29:8083/ui/index.html#/` 下的前端页面，任务分支必须先 merge 到 `dev`；未进入 `dev` 的代码不能视为 29 环境的发布源码，也不需要同时构建 `csx-web-react`。
- 从代码输入范围看，这类变更只涉及 `csx-web@dev`；从实际部署动作看，当前不能简化为“前端只重新部署 `csx-web`”。除非 release owner 明确提供可独立替换 `/ui/**` 静态文件的 job，否则继续按已确认的 29 流程：Nina 在 29 Jenkins 构建 `csx-web` 前端包，后端或 release owner 把所需后端代码同步到 29，构建旧 CSX 前后端合包并部署。
- 若本次只有 Vue 前端改动，后端不需要为业务代码另做修改，但仍需负责合包和部署；若同时包含 API 或后端改动，则先把对应后端 commit 纳入同一次合包。
- 前端人员不需要另外手工构建 `dist/`、合包或操作服务器；交接内容是最新 `dev` merge commit，部署完成后再通过 29 内网入口或 Dev Tunnel 做页面冒烟验收。
- 此处目标分支是 `dev`，不要套用旧 csx POC 发布前必须先 merge 到 `master` 的规则。

### 已确认的旧 CSX 前后端合包机制

1. `csx-pipeline` 与 `csx-pipeline-dev` 提供手动触发的 `Build CSX Install Package` 流水线，输入包括前端、后端和工具仓库的 branch 或 commit，以及构建环境和版本号。
2. Windows self-hosted runner 自行 checkout 指定的 `csx-web` commit，执行 `npm install`、`npm run build` 生成 `dist/`；同时 checkout `csx` commit 并执行 `dotnet publish` 生成 API。
3. 合包阶段把 API publish 结果与前端 `dist/` 内容移动到同一个 `CSX.V<version>` 站点目录，写入包含各仓库 ref 和 commit 的 `release.txt`，最后生成 `CSX.V<version>.<environment>.InstallationPackages.zip`。
4. 后端静态文件中间件把 ASP.NET content root 映射到 `/UI`，因此同一站点目录既通过 `/api/` 提供后端，又通过 `/ui/index.html` 和 `/ui/static/` 提供前端。当前 Dev Tunnel 的同源 Network 结果与该目录结构一致。
5. 这条标准合包链路由 release pipeline 构建前后端，不要求前端人员先手工生成 `dist/`；但两个合包仓库最后一次可见运行停留在 2024 年，不能据此断言 2026 年当前 Dev Tunnel 实例仍由同一个 job 构建和部署。

### 当前环境的可追溯证据

- 旧 Dev 的 `csx-currversion` 会随部署变化，短 hash 可回查后端 commit；2026-07-22 同日先后观察到 `fccb0be29` 与 `7783adf9f`，因此每次排障都必须重新读取响应头，不能沿用本 Skill 中的历史版本值。
- 线上 bundle 内的前端构建时间为 `2026-07-22 14:31:21`；其代码包含 `csx-web` commit `f8fa4e256` 的变更，源码 tree 与随后合入 `dev` 的 `c50e9f56c` 完全一致。`dev` 合并发生在构建前 2 分 25 秒，因此前端内容可追溯到 `dev@c50e9f56c` 对应的源码 tree；由于功能分支 tip 与该 merge commit 的 tree 相同，单凭产物不能证明 job 参数填写的是 `dev` 还是该 commit。
- `csx-web` 自身的 `deploy-to-dev` 历史运行全部属于 `csx-k8` 分支，目标是 S3/CloudFront；它不是旧 csx Dev Tunnel 合包或部署的证据。
- 当前页面能证明前后端已被部署到同一个 ASP.NET 站点，并由 8083 对应的 Dev Tunnel 暴露；不能仅凭页面反推出实际触发人、job 名、IIS 物理目录、部署命令或回滚方式。

### `csx-web-react` 独立 artifact 与 29 Web root 注入事实

- Nina 在 29 环境重新构建并部署旧 `csx` 后端与 `csx-web` 前端包后，Dev Tunnel 的 `/ui/index.html#/Appointment/ClinicOpenAndClose` 同步显示最新页面。这证明当前 Dev Tunnel 暴露的是 29 对应的旧 CSX 站点；但旧 CSX 的“前后端合包”不等于自动包含独立仓库 `csx-web-react` 的静态产物。
- `csx-web-react` Pipeline `#124` 从 `main@2fe90de57f96c67da77d336c92f7dcb22def8d45` 成功执行旧 csx POC build，并上传 `csx-web-react-old-poc-main-124-2fe90de57f96c67da77d336c92f7dcb22def8d45.zip` 与 `csx-web-react-old-poc-main-latest.zip`，两者当时均为 `740.7 KB`。该旧 csx step 只负责构建和上传 Downloads；同一 Pipeline 中明确存在的 Deploy step 只发布到 `csx-k8 dev`，不会把 React artifact 自动部署到 29。
- 2026-07-23 实页对照显示：最新 `/ui/index.html` 的 `Last-Modified` 为 `08:38:53 GMT`，而已有 React HTML 的 `Last-Modified` 为 `00:33:54 GMT`，早于 Pipeline `#124`。因此当次 29 合包更新了旧 Vue/后端站点，但没有把 Pipeline `#124` 的最新 `display-screen-config/**` 注入 Web root。
- React static export 的物理文件已经存在于站点：`/display-screen-config/management-settings/program-settings/display-screen-config/index.html`、`login/index.html` 和 `new/index.html` 均返回 `200`，管理页面带 `index.html` 时可以正常渲染并读取数据；对应的不带 `index.html` 目录 URL 均返回 `404`。
- `/display-screen-config/tvScreenNew/` 与 `/display-screen-config/tvScreenNew/index.html` 均返回 `200`，响应体 SHA-256 完全相同；这证明旧 CSX 已为 `tvScreenNew/` 提供目录入口映射，但没有为其它 `display-screen-config` static-export 路由提供通用 default document / rewrite。
- 完整交付需要两个独立步骤：release owner / Jenkins 下载并校验指定的版本化 React zip，把包内 `display-screen-config/**` 注入 29 Web root；旧 CSX 后端或静态宿主再为所有 `/display-screen-config/**/` 目录请求返回对应的 `index.html`，可使用 `UseDefaultFiles` + `UseStaticFiles`、`UseFileServer` 或等效 rewrite。只重新运行 `csx-web-react` Pipeline 或只重建旧 CSX 前后端包，都不能单独完成这两步。
- 带 `index.html` 的管理页只能作为诊断和临时访问入口，不能作为最终发布方案；否则管理列表、新增、编辑等页面直接访问或刷新仍会 `404`。

### 更新 29 的 `/display-screen-config/**` 完整发布链路

1. 在 29 验收并获得合并许可后，把 `csx-web-react` 任务分支 merge 到 `main`，记录 merge commit、Bitbucket build number 和 Pipeline 结果。
2. `main` Pipeline 会执行旧 CSX POC 构建，把 Next.js static export 打包为顶层含 `display-screen-config/**` 的 zip，并上传到 Bitbucket Downloads；它只完成构建和上传，不会自动部署到 29。交接时优先使用带 build number 和 commit 的版本化 artifact，不依赖会被覆盖的 `main-latest`。
3. release owner / Jenkins 下载指定版本化 zip 并校验包内至少包含管理列表、`new/`、`edit/`、`login/`、`tvScreenNew/`、`_next/` 等所需文件，再把整个 `display-screen-config/**` 注入 29 的旧 CSX Web root 或最终安装包。
4. 注入时先备份旧目录，并采用可回滚的原子替换或等效方式清理旧 `_next` 哈希资源；不得覆盖或删除同站点的 `/ui/**`、`/api/**` 及其它目录。
5. 首次补齐深层目录访问时，还必须配置 `/display-screen-config/**/ -> 对应 index.html` 的通用 default document / rewrite。若规则写在旧 CSX 后端代码中，需要合并后端修改、重新构建旧 CSX 包并部署；若由 IIS 或其它静态宿主配置完成，则做一次服务器配置和 reload 即可，不必为了该配置重建业务后端。
6. 部署后验证管理列表、`new/`、`edit/`、`login/` 和 `tvScreenNew/` 的无 `index.html` URL 均返回 `200`，HTML 引用的 `_next` 静态资源均为 `200`，页面 API 仍请求 29 同源 `/api/**`，同时确认 `/ui/**` 与 `/api/**` 未受影响。
7. 通用目录映射和 React artifact 注入 job 稳定后，后续纯 `csx-web-react` 页面更新不需要重新构建 `csx-web` 或业务后端，但仍必须执行“下载版本化 artifact -> 注入 Web root -> 发布验收”；若 29 当前只能发布完整旧 CSX 安装包，则由 release owner 把该 React artifact 纳入同一次完整包再部署。

### 待后端或 release owner 确认

1. 当前 29 Jenkins / release job 应由哪个步骤下载指定的 `csx-web-react` 版本化 zip、校验目录并把 `display-screen-config/**` 注入最终 Web root？请提供 job 名、目标物理目录和本次实际使用的 artifact 文件名。
2. 请在旧 CSX 后端或静态宿主中补齐 `/display-screen-config/**/ -> 对应 index.html` 的通用 default document / rewrite，并同时验证管理列表、`new/`、`edit/`、`login/` 和 `tvScreenNew/` 的无 `index.html` URL。
3. React 目录更新时是否会清理旧 `_next` 哈希资源，如何备份、原子替换和回滚 `display-screen-config/**`，以及如何避免影响 `/ui/**`、`/api/**` 和其它站点内容？
4. 8083 Dev Tunnel 由谁维护，机器或服务重启后如何恢复；SignalR/WebSocket 路径是否需要额外 Tunnel 或宿主配置？

## 旧 csx POC 部署恢复事实

旧 csx POC 入口为 `https://poc.demo.clinicsolution.hk/ui/index.html#/login`；不要与 csx-k8 POC `https://csx-poc.clinicsolution.hk/#/login` 混用。版本、分支 tip 和域名状态都可能变化，部署前重新核对。

### 已确认的前端合并门禁

- 当前分支方向统一遵循“Git 分支方向硬门禁”：发 POC 使用“需求分支 -> 最新 `dev`”，发 Prod 使用“最新 `master` -> 需求分支 -> 本地 `master`”；不得再把下面的历史发布链路当作当前合并方向。
- 2026-07-22 上一次旧 csx POC 发布采用的实际链路是：任务分支先通过 PR 合入 `master`，随后把最新 `master` 合入当次 POC 发布分支 `dev-1.9.14-TECH-7667`，再从合并后的源码 tree 构建前端包。该条只保留为历史发布证据，`dev-1.9.14-TECH-7667` 也不是以后永久固定使用的分支。
- 前端负责按当前硬门禁完成对应目标分支的合并、验证与 merge commit 交接；发布分支选择、构建、合包和部署仍由 release owner 负责，前端在部署完成后做页面冒烟验收。

### 当前 POC 前端包

- 2026-07-22 实页响应为 `csx-currversion: 1.9.14.260722`，`installationId` 为 `poc.demo.clinicsolution.hk`；`/ui/` 静态资源与 `/api/` 由同一 origin 提供。
- 已部署 app bundle 的 `buildVersion` 为 `2026-07-22 14:14:11`，文件更新时间约为 14:17；bundle 中的 npm 元数据记录构建工作目录为 `D:\CsxRelease\csx-web`。
- 部署内容对应 `csx-web` 分支 `dev-1.9.14-TECH-7667` 在构建时的 tip `8f09e2f2885de0cbc2b57b2eaf75a608c47030c8`：页面含该分支独有的 Botpress 入口与 Chatbot 代码，同时保留该 tip 从 `master` 合入的页面实现。若其它 ref 指向相同 tree，仅凭 bundle 仍无法区分实际 checkout 参数。
- 前端采用 `ENV=dev` 构建；仓库内对应的标准命令是 `npm run build:dev`，即 `SYSTEM=csx ENV=dev node build/build.js`。证据是部署 chunk 已把相关环境分支编译成 `checkin-dev.heals.asia`、`heals-patient-gateway-dev.heals.asia` 和 `health-passport-dev.heals.asia`。
- `csx-web` 当天可见的 Bitbucket Pipeline 是 `csx-k8` 的 S3/CloudFront 部署，与旧 POC 无关；`csx-pipeline` / `csx-pipeline-dev` 的合包运行记录停在 2024 年，也不是本次 POC 构建记录。

### 前后端构建与合包边界

1. 当前仓库可见的 `csx/BuildCsxPackage.ps1` 中，前端 checkout、`npm i` 与 `npm run build` 均已注释；脚本只消费已有 `dist/`，再把前端文件与 `dotnet publish` 的 API 输出移入同一个站点目录。因此不能把当前 POC 前端描述成“由该后端脚本直接构建”，前端 `dist/` 是独立的前置产物。
2. 历史标准 `Build CSX Install Package` Pipeline 会在 Windows runner 上 checkout 输入的前后端 ref，执行前端 `npm install && npm run build`、后端 `dotnet publish`，再把 `dist/*` 与 `api/*` 合并进 `CSX.V<version>`，写 `release.txt` 并压缩成 `CSX.V<version>.<environment>.InstallationPackages.zip`。
3. 当前 POC 前端明确是 `npm run build:dev`，而上述历史 Pipeline 写的是 `npm run build`，且没有 2026 年运行记录；它只能作为合包格式的历史依据，不能当作当前 POC 的实际执行流水线。
4. 后端 `Startup.cs` 把 ASP.NET content root 映射为 `/UI`，与实页同源的 `/ui/` 和 `/api/` 结构一致；这能证明最终部署是前后端同站点合包形态，但不能证明使用了哪个外部 job、脚本或人工复制步骤。
5. POC bundle 的 `D:\CsxRelease\csx-web` 不是旧 Dev bundle 中的 Jenkins 工作目录 `E:\Jenkins\.jenkins\workspace\CSX\CSX-WEB-DEV`。现有证据只能确认 POC 前端被单独构建，尚不能判断 `D:\CsxRelease` 是人工工作区、Jenkins custom workspace，还是未入库的 release 脚本目录。

### 待后端或 release owner 确认

1. 2026-07-22 这次 POC 发布实际由哪个 Jenkins job、PowerShell 脚本或人工流程触发？请提供 job URL、构建日志或未过期 artifact。
2. `D:\CsxRelease\csx-web` 中是谁或哪个自动化执行 `git checkout`、依赖安装与 `npm run build:dev`；实际 ref 是否为 `dev-1.9.14-TECH-7667@8f09e2f288`？
3. 当次后端 `csx` 输入 ref/commit 和 `dotnet publish` 参数是什么？当前 POC 版本头不含 commit hash，且公开 `release.txt` 路径返回 404，无法从页面精确回查。
4. 当前合包是否仍生成 `CSX.V<version>.<environment>.InstallationPackages.zip`；若是，请提供包内 `release.txt`。若不是，请给出 `dist/` 与 API publish 目录的实际合并命令。
5. 合包如何发布到 POC 的 IIS/ASP.NET physical path，是否使用 `app_offline.htm`、是否清理旧哈希资源，以及服务重启、原子替换和回滚命令是什么？

## 最小恢复状态

- 旧 csx dev 的旧 Vue/后端合包与 `csx-web-react` 静态 artifact 是两条独立交付链路；Bitbucket build/upload 成功不代表 React 文件已经进入 29。当前仍需由 release owner / Jenkins 完成版本化 zip 的 Web root 注入，并由后端或静态宿主补齐所有 static-export 深层目录的 `index.html` 映射。
- 旧 csx POC 当前可确认前端 source tree、`npm run build:dev` 和独立构建目录；未取得 release job 日志或安装包 `release.txt` 前，不把历史 Pipeline 写成当前 POC 的实际合包或发布执行器，也不把“人工构建”写成已确认事实。
- 本地服务、代理目标、登录态、Git 状态和接口响应均属于易变信息，每次任务实时检查。
- 仅调用入口且没有另给具体任务时，按“活跃任务解析与自动续做门禁”执行未注释队列；队列没有可执行项时再等待用户输入。涉及独立 React 新系统时路由到 `ask-csx-web-react`。

## 输出与边界

- 回复使用简体中文；代码与代码注释使用英文。
- 默认只说明产出、验证、风险和下一步，不列完整文件加载清单；用户要求、审查、排障、上下文降级或慢任务复盘时再列。
- 不把医疗健康文案写成确诊、处方替代或疗效保证。
- 不擅自扩大任务范围，也不把其它仓库的路径、模块或约定套用到本项目。

## 最新待继续问题（不要修改这部分的子内容）

<!-- 在此追加跨会话任务；路径写双平台：Windows D:\work\csx-web / macOS /Users/<你的用户名>/Desktop/work/csx-web（当前 Mac：/Users/stark/Desktop/work/csx-web） -->
