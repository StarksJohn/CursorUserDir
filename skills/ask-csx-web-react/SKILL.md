---
name: ask-csx-web-react
description: >-
  csx-web-react 的 Cursor 私有恢复与专项路由入口。仅在用户显式使用
  /ask-csx-web-react 或 @ask-csx-web-react，或明确要求继续受保护待办、恢复私有需求/
  Figma/ClickUp 索引、估时、外部阻塞与旧 csx-web 跨仓协作时使用。每个新 chat 先调用
  本入口；随后强制读取 Codex 对口 Skill 同目录 AGENTS.md 作为共享仓库规则。
---

# ask-csx-web-react private recovery

## 调用策略与边界

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取 `$HOME/.codex/skills/csx-web-react/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\csx-web-react\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得跳过。
- 每个新 chat 先显式调用本入口，再从共享 `AGENTS.md`、当前源码与聚焦测试开始普通实现、排障、审查和测试；项目根不维护第二份 `AGENTS.md`。
- 本 chat 首次激活时，在主任务前执行共享 `AGENTS.md` 的 “First-chat structural drift gate”；发现重大冲突时立即完整读取并执行 macOS `$HOME/.cursor/skills/init-project/SKILL.md` / Windows `%USERPROFILE%\.cursor\skills\init-project\SKILL.md`，刷新后重新读取共享 `AGENTS.md` 并继续原任务，不要求用户再次输入 `/init-project`。
- 本 Skill 只补充无法安全放进仓库的受保护待办、私有需求索引、外部阻塞和跨仓路由。
- 用户给出具体任务时，该任务优先；只有仅调用入口或明确要求“继续”时，才解析未注释待办。
- 普通一次性任务优先在新 chat 第一条消息中同时写 `/ask-csx-web-react` 和任务正文；只有需要跨 chat、跨设备或长周期恢复时，才把任务放入本文件受保护区后仅输入入口词继续。
- Cursor 入口 `/ask-csx-web-react` 与 Codex 显式入口 `$csx-web-react` 保持事实优先级和授权边界一致，但不复制客户端专属说明。

## 路径与事实优先级

- 项目根：macOS `$HOME/Desktop/work/csx-web-react`；Windows `D:\work\csx-web-react`。
- 旧 Vue 仓库：macOS `$HOME/Desktop/work/csx-web`；Windows `D:\work\csx-web`。
- Codex 对照入口：macOS `$HOME/.codex/skills/csx-web-react/SKILL.md`；Windows `%USERPROFILE%\.codex\skills\csx-web-react\SKILL.md`。
- 私有需求与外部问题：Codex 对照目录中的 `CSX顯示屏配置技术文档.md`。
- 私有阶段与阻塞：仅在继续待办或阶段判断时读取 Codex 对照目录中的 `references/recovery-state.md`。

冲突按以下优先级处理：

1. 当前源码、聚焦测试、真实 DOM / Network / API 响应和当前 Git 状态。
2. Codex 对口 Skill 同目录 `AGENTS.md`、`package.json`、`next.config.ts` 与相关 `README.md` 章节。
3. 用户本轮需求来源或负责人最新确认。
4. 按需读取的私有技术文档与恢复快照。
5. 本文件受保护区块中的历史兼容待办。

## 执行工作流

1. 先判断本轮是具体任务还是“继续项目”类恢复请求；具体任务不得被无关待办覆盖。
2. 读取 Codex 对口 Skill 同目录 `AGENTS.md` 和任务直接相关文件；不要通读 README、私有技术文档或历史附件。
3. 仅在任务依赖 ClickUp / PRD / Figma 索引、范围、估时、负责人回复或外部问题草稿时读取私有技术文档。
4. 仅在继续待办、判断当前阶段或处理外部阻塞时读取恢复快照或 Codex 对照入口。
5. 修改旧 Vue 仓库前读取 `ask-csx-web`；执行 BMAD 或其它专项 Skill 前完整读取其入口与必需依赖。
6. Figma 节点任务先用 Figma MCP 读取节点事实；API 可由真实页面触发时先读 Network 实际请求与响应。
7. 代码任务依次完成仓库实现、聚焦测试，再更新项目目录外的材料；若本次任务改变稳定架构、命令工作流或仓库边界，最后自动最小更新 Codex 对口目录 `AGENTS.md`，否则不全仓扫描或改写规则。
8. 最终明确区分静态校验、本地运行证据、部署结果和外部负责人确认，不扩大成功范围。

## 文档维护

- Codex 对口 Skill 同目录 `AGENTS.md` 保存稳定项目约束；`package.json` 和 README 保存工程、命令、构建与部署事实。
- 别人合并进来的大规模结构变化使用 Cursor `/init-project` 做一次完整刷新；不得创建仓库根 `AGENTS.md` 或 `.cursor/rules/project-context.mdc`。
- `references/recovery-state.md` 只保存不能从源码恢复的当前阶段、外部阻塞和最小下一步；实质变化时直接替换，不按 chat 追加流水。
- 私有技术文档只保存需求来源、设计索引、范围/估时边界和外部问题；没有这些变化时不更新。
- 不把可从源码、测试或 Git 恢复的业务规则、字段、默认值、测试数量和修复过程复制进私有材料。
- “最新待继续问题（不要修改这部分的子内容）”由用户维护，除非用户明确授权，否则保持标题、位置和子内容原文。

## 最新待继续问题（不要修改这部分的子内容）
<!-- - 借鉴`/Users/stark/.codex/skills/csx-web-react/SKILL.md`和当前项目状态,更新当前skill -->
<!-- - 新 chat 执行 `/csx-web-react` 后，先执行用户输入框里的具体任务；没有具体任务时，根据项目配置和源码恢复最小必要上下文 -->
<!-- - 为什么 skill里还有类似如图这种带日期的聊天流水内容? 把 skill 和技术文档以及`/Users/stark/Desktop/work/csx-web-react/README.md`里 的 和 `2026` 相关的带日期的聊天流水内容沉淀成 既定事实,以后不要再新增 对话流水内容 -->
<!-- - 我负责 当前项目的前端开发,不负责 后端API 和 部署运维的开发; -->
<!-- - 接下来的工作流是需要你用`Chrome DevTools`或codex的`Chrome`插件读取figma的节点信息,然后帮我布局页面的UI,目前你能否执行这个工作流?
  - 已经重启,帮我验证下如图![img_100224.png](img_100224.png)这个任务是否完成 -->
<!-- - 帮我总结下 git commit message -->
<!-- - 如果你在当前chat的上下文里没有用 `chrome_devtools` 读取过 `https://app.clickup.com/t/8553538/TECH-8370`页面的需求描述,先查看这个需求的需求描述和当前第一阶段只需要做的子需求`https://app.clickup.com/t/8553538/TECH-8458`的需求描述,不用看Activity里的内容,再解决以下未注释的问题; -->
<!-- - 你本地启动当前项目在`旧csx`系统的dev(http://192.168.99.29:8083)环境 -->
<!-- - 你本地启动当前项目在`旧csx`系统的poc环境,请求`https://poc.demo.clinicsolution.hk/api/` -->
<!-- -你本地启动当前项目在`旧csx`系统的prod环境 ,访问 sfsc3051 这个租户的页面 ,请求`https://sfsc3051.clinicsolution.hk/api`-->
<!-- - 你重新本地启动当前项目在`csx-K8`系统的dev(也是poc)环境 ,请求 `https://api-poc.clinicsolution.hk/api` -->
<!-- - 精简优化技术文档和`README.md`,技术文档只保留项目里已经做过的所有需求的已经沉淀的事实,而`README.md`只保留和具体需求无关的通用的项目配置和事实规则 -->
- 大屏需求相关:
    <!-- - 我访问了`http://192.168.99.29:8083/display-screen-config/tvScreenNew/?clinicCode=ClinicB` -->
    <!-- - 我访问了 `http://localhost:3000/display-screen-config/tvScreenNew/?clinicCode=TESTCLINIC` -->
    <!-- - 我访问了 mock页面 `http://localhost:3000/display-screen-config/tvScreenNew/?mock=1&doctors=2` -->
    <!-- - 我访问了 `http://localhost:3000/display-screen-config/tvScreenNew/?clinicCode=TES`页面 -->
    <!-- - 我访问了`https://csx-poc.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=TES` -->
    <!-- - 再帮我验证下目前页面加载逻辑是否是:
        - 页面加载后先请求一次`https://poc.demo.clinicsolution.hk/api/AppointmentQueueData/GetClincInfoAsync`和`https://poc.demo.clinicsolution.hk/api/AppointmentQueueData/GetQueueNewPatientListAsync?clinicCode=TESTCLINIC&pageIndex=1&pageSize=1000`API;
        - 第一轮请求完这2个API之后,每5秒再请求一轮`GetClincInfoAsync`和`GetQueueNewPatientListAsync`这2个API
        - 针对`GetClincInfoAsync`api,判断最新返回的数据是否和上次返回的数据的所有字段的值一致(不仅要比较每条数据对象的第一层的字段的值,还有比较子对象里的数据,也就是深度比较);如果不一致,就根据最新的某个字段的值是否变化更新页面的![img_164400.png](img_164400.png)区域或重新轮播![img_164415.png](img_164415.png)视频区域;
        - 针对`GetQueueNewPatientListAsync`API,判断最新请求的API返回的item数组的每条数据的顺序是否和上次这个API返回的item数组的每条数据的循序一致,并且每条数据的每个字段的值(不仅要比较每条数据对象的第一层的字段的值,还要比较子对象里的数据,也就是深度比较)是否和上次这个API返回的item数组的每条数据的每个字段的值一致,并且医生数量是否一致;如果都一致,就继续轮询显示;如果不一致,就根据最新这个API返回的数据刷新如图![img_105124.png](img_105124.png)红框处的医生轮播区域,重新轮询显示医生(![img_154503.png](img_154503.png)进度条记得重置;重新轮播的原因是`如果有10条数据,当前轮播到了第3条,改了第9条数据的某个字段,比如医生头像或简介,此时如果不重新轮播,本轮轮播到第9条数据时,就不会显示最新修改后的简介或其它字段;不能每页请求2条数据,因为轮播页面不能固定显示2个医生,可能4个,可能3个`),重新计算總排隊人數的值;轮询显示完所有医生后, 不再需要重新请求这2个API,只需要重新根据现有数据重新轮播;视频区域二维码的更新逻辑不变;
        - 如图![img_105204.png](img_105204.png)红框是叫号区,此处显示数据的更新逻辑只依赖`GetQueueNewPatientListAsync`返回的`latestCallNumberDoctorProfile`对象和上一次返回的`latestCallNumberDoctorProfile`对象进行深度对比之后是否变化;`latestCallNumberDoctorProfile`对象为null或者没有此字段时,整个叫号区不显示内容,只占位显示 -->
    <!-- - ![img_231652.png](img_231652.png),![img_231700.png](img_231700.png),![img_231709.png](img_231709.png),![img_231724.png](img_231724.png),![img_231736.png](img_231736.png),这几个区域的高度目前是根据当前浏览器显示区域的高度的百分比算的
          诊所栏：6.47%
          等待队列栏：5.06%
          医生区：60.47%
          媒体区：28%
          是否正确? -->
- 顯示屏配置需求 相关:
    <!-- - 点击 旧csx系统的`https://poc.demo.clinicsolution.hk/ui/index.html#/ManagementSettings/ProgramSettings` 页面里的 ![img_151956.png](img_151956.png)红框后,  浏览器会打开一个新标签, 打开类似![img_152016.png](img_152016.png)这种页面; 新标签的页面需要创建的一个新的react的项目(技术栈可借鉴 `/Users/stark/Desktop/work/MyStartupProject1`项目) ,新项目可以当做当前项目的react版本,API环境和当前项目一致,可以把 `/Users/<你的用户名>/Desktop/work/csx-display-screen-config` 项目 的名称就成 `csx-web-react`,然后作为这个新项目,然后把技术栈更新到和`/Users/stark/Desktop/work/MyStartupProject1`项目一致,新项目的PRD 是 `https://hmolwpux55nnq.ok.kimi.link/#/displays`,你用 chrome_devtools 读取,然后 新项目里的左侧菜单栏里只显示 `程序设定-显示屏配置`页面;也就是点击 当前项目的`https://poc.demo.clinicsolution.hk/ui/index.html#/ManagementSettings/ProgramSettings` 页面里的 ![img_151956.png](img_151956.png)红框后,浏览器打开新标签,跳转到新项目的`程序设定-显示屏配置`页面  -->
- 运维部署相关:
  - 旧csx系统:
      <!-- - 当前项目的大屏页面在旧csx系统的prod环境的域名比如是`https://sfsc3051.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=SFSC`
        - 为什么页面里还请求了`GetDoctorProfilePictureAsync`API, 页面明显不是最新的代码构建的包;不现在不知道运维是否部署了如图![img_110407.png](img_110407.png)后端给他的合包,因为运维不回复;最新的前后端合包里的前端的构建zip下载解压到了`/Users/stark/Downloads/display-screen-config`,你确认下前端构建的包是否有问题 -->
      <!-- - 我把 `/Users/stark/.codex/skills/csx-web-react/CSX顯示屏配置技术文档.md` 的 `686` 行开始的 问题发给后端开发人员后, 他回复:  -->
      <!-- - 我把 `/Users/stark/.codex/skills/csx-web-react/CSX顯示屏配置技术文档.md` 的 723 行开始的 问题发给运维开发人员后, 他回复:  -->
      <!-- - 你不要完全按他们的回复方案做,需要判断他们的回复是否符合事实;如果不对的地方,需要在新问题里给他解释 -->
      <!-- - 根据当前项目的状态和`csx-web`项目的源码,以及当前chat的上下文里你已经知道的内容,从当前项目的前端开发人员的视角,总结并执行当前项目前端能做的所有任务,再用中文更新技术文档里旧`csx`系统poc环境部署相关的问题(先包含当前项目已经做了哪些),再包括给`csx-web`项目的前端开发人员Nina的问题,给后端开发人员的问题,以及给运维的问题;然后告诉我当前阶段需要发给哪些人,从第几行开始复制给他们; -->
        <!-- - 你的改动不要影响已经在csx-k8系统的dev环境部署好了的'https://csx-poc.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode={clinicCode}' 域名
        - 你的改动和给后端人员和运维的建议,尽量不要给运维添加工作量,他很忙
        - 在你给的方案里尽量表现出不需要运维做任何改动的文案
        - 你的最新问题里需要包含前端需要的操作流程和后端需要的操作流程 -->
      <!-- - 根据项目最新状态和技术文档,以及后端的打包文档(/Users/stark/Desktop/work/csx-web-react/doc/csx打包 2.docx),帮我在`/Users/stark/Desktop/work/csx-web-react/README.md`里总结出,把当前项目部署到旧`csx`系统的poc环境的过程中,前端配置了什么(包括项目里的配置和`https://bitbucket.org/healshealthcare/csx-web-react/`里的配置以及其他地方的配置),后端配置了什么,运维配置了什么;这样如果以后部署到旧csx系统的prod环境时,可以借鉴 -->
  - csx-k8系统:
      <!-- - 目前当前项目已经部署到了旧csx系统的poc和prod环境,页面域名分别是`https://poc.demo.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=TESTCLINIC`和`https://sfsc3051.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=SFSC`(sfsc3051是商户号) -->
      <!-- - 之前也部署到了csx-k8系统的dev环境,页面是`https://csx-poc.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=TES`,之前能访问, 现在无法访问,你检查下是当前项目的配置问题还是运维的问题;csx-k8系统的dev环境的最新的前端构建在`https://bitbucket.org/healshealthcare/csx-web-react/pipelines/results/94/steps/%7Bcf55c738-d609-4d46-aec8-81c81d991779%7D` -->
      <!-- - 现在需要进行csx-k8系统的prod环境的部署 -->
      <!-- - 根据当前项目的状态,`csx-web`项目的源码,`https://bitbucket.org/healshealthcare/csx-web-react/pipelines`的已有配置,以及当前chat的上下文里你已经知道的内容,从当前项目的前端开发人员的视角,先执行当前项目前端能做的所有关于csx-k8系统的prod环境的部署的任务,再用中文更新技术文档里问运维的关于`csx-8`系统prod环境部署相关的问题,问题里先包含当前项目前端已经做了哪些,再包括给运维的问题;然后告诉我从第几行开始复制给他们; -->
        <!-- - 你的改动不要影响旧csx系统已经部署好的poc和prod环境的配置 -->
    <!-- - 我把 `/Users/stark/.codex/skills/csx-web-react/CSX顯示屏配置技术文档.md` 的 792 行开始的问题发给运维后, 他回复 ``; -->
      <!-- - 根据项目最新状态和技术文档,帮我在`/Users/stark/Desktop/work/csx-web-react/README.md`里总结出,把当前项目部署到`csx-k8`系统的dev环境的过程中,前端配置了什么(包括项目里的配置和`https://bitbucket.org/healshealthcare/csx-web-react/`里的配置以及其他地方的配置),运维配置了什么;这样如果以后部署到csx-k8系统的prod环境时,可以借鉴 -->
- figma 相关:
   <!-- - 把当前项目的页面的布局改成响应式布局的样式,适配不同大小和分辨率的浏览器,避免出现某个元素显示不下或者被截断的情况,外层如图![img_161601.png](img_161601.png)![img_161613.png](img_161613.png)![img_161622.png](img_161622.png)![img_161629.png](img_161629.png) 这4 个大区高度继续等比例匹配 Figma；区内所有容易溢出的字体、头像、卡片、二维码等用响应式 CSS 变量和 clamp() 随浏览器尺寸适配。也就是说不是压缩某个大区，而是在对应大区内部自适应。 -->
  <!-- - 使用当前Mac系统的cursor里的codex插件的`figma`mcp拿到 `https://www.figma.com/design/R2iu3VINGNezIvRMdUjucV/CSX?node-id=17462-134442&m=dev` 这个 Figma 节点数据 -->
  <!-- -  在 `/Users/<你的用户名>/Desktop/work/RN/csx-mobile/src/pages/Diagnosis/DiagnosisPage.tsx` 页面 的 `2018` 行 ,设计实现 和当前项目代码风格一致的 组件 -->
  <!-- - 要求：
    - 匹配当前项目的代码风格（命名规范、目录组织、import 顺序等）,项目结构和技术栈
    - 复用当前项目中已有的公共组件和工具函数
    - 使用当前项目里一致的样式方案（Tailwind CSS / 现有本地组件等） -->
