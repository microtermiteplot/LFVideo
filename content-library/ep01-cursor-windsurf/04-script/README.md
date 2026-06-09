---
stage: 04-script
platform: bilibili
status: draft
source_workflow: /04-script-draft
---

# ep01 视频脚本（B站长视频版）：《2026年的Cursor和Windsurf，已经不是你以为的AI IDE了》

---

## 第一段：`@IntroScene` 开头黄金钩子（0f - 90f，约3秒）

- **[画面]**
  - 引入片头场景 `@IntroScene`
  - 参数：title="2026 AI IDE 质变", subtitle="你手里的螺丝刀，早就是脱缰野马了", background="particles"
  - 右下角画中画 `@VideoSlot(position="bottom-right", rounded=true, src="ep01-assets/fix-loop-pain.mp4")` [B轨占位：请补充 IDE 界面中疯狂点击 Fix 导致套牢报错的录屏]

- **[口播]**
  兄弟们，如果你到了 2026 年，还把 Cursor 和 Windsurf 当作"补全几行代码的编辑器"，那你对 AI IDE 的认知已经严重落后于时代了。

---

## 第二段：`@TimelineScene` 纵向进化：Cursor 的角色化质变（90f - 270f，约6秒）

- **[画面]**
  - 引入时间轴场景 `@TimelineScene`
  - 参数：
    ```
    eyebrow="纵向进化史"
    title="Cursor 2024 - 2026 演进质变"
    events=[
      { year: "2024", title: "Editor 辅助时代", desc: "代码智能补全，点对点单步修改", icon: "🔧" },
      { year: "2025", title: "Composer 智能体狂飙", desc: "多文件自动拆解，AI 开启自动驾驶", icon: "🐴" },
      { year: "2026", title: "岗位角色化阶段", desc: "集成 Subagents、Bugbot、Security Review", icon: "🕸️" }
    ]
    ```

- **[口播]**
  先看 Cursor 这三年的质变。2024 年它只是个"智能输入法"，你点 Tab 补一行代码。2025 年 Composer 横空出世，AI 能自己拆任务、改多文件。而 2026 年，Cursor 开始长出"岗位骨架"——Subagents 给你当打手、Bugbot 自动抓虫、Security Review 做安全审计。这不是功能堆砌，是给 AI 建立"岗位职责"，让它知道什么该做、什么不该做。

---

## 第三段：`@TableScene` 横向华山论剑：Cursor vs Windsurf（270f - 450f，约6秒）

- **[画面]**
  - 引入对比表格场景 `@TableScene`
  - 参数：
    ```
    eyebrow="横向华山论剑"
    title="Cursor 与 Windsurf 核心机制对比"
    headers=["对比项", "Cursor (MDC)", "Windsurf (Workflows)"]
    rows=[
      { feature: "文件格式", cursor: ".mdc 专有格式", windsurf: ".md 通用 Markdown", win: "windsurf" },
      { feature: "多步骤编排", cursor: "不支持", windsurf: "原生多步编排", win: "windsurf" },
      { feature: "跨角色调用", cursor: "手动 @ 引入", windsurf: "Workflows 原生串联", win: "windsurf" },
      { feature: "跨工具兼容", cursor: "互不兼容", windsurf: "互不兼容", win: "neutral" }
    ]
    highlightCell="2-3"
    ```
  - 画中画切换展示 Windsurf Workflow 编辑器 [B轨占位：Workflow 多步骤编排录屏]

- **[口播]**
  看这个硬核对比表。第一，文件格式：Cursor 用 .mdc 专有格式，Windsurf 直接用通用 Markdown，随手可改。第二，多步骤编排是 Windsurf 的杀手锏——它的 Workflows 原生支持流程编排，一步走完自动触发下一步。Cursor 的 MDC 本质是"单步触发器"，每次都要手动给指令。第三，跨角色调用：Windsurf 能原生串联不同 Agent，Cursor 得在同一个对话里手动 @。但注意最后一行——两家互不兼容，各建生态围墙。

---

## 第四段：`@ConceptScene` 判断层——避坑与边界（450f - 570f，约4秒）

- **[画面]**
  - 引入概念卡片场景 `@ConceptScene`
  - 参数：
    ```
    eyebrow="判断层"
    title="避坑与边界：驯服 AI 的三条军规"
    items=[
      { label: "⚠️", title: "死循环陷阱", desc: "上下文堆叠溢出导致 Agent 原地打转", icon: "warning" },
      { label: "📋", title: "规训解法", desc: "用 Role 约束 + Rules 边界限定行为", icon: "rule" },
      { label: "✋", title: "验收标准", desc: "关键决策点必须人工终审", icon: "stop" }
    ]
    ```
  - 画中画展示 .cursorrules 或 Windsurf Rules 配置界面 [B轨占位：Rule 配置实操录屏]

- **[口播]**
  看完对比，你必须知道底层坑点：Agent 原地打转死循环。为什么？因为 AI 上下文窗口有限，连续改 Bug 时会把自己每次修改堆进上下文。改错→报错→再改→再报错，几轮后上下文全是错误信息，AI 彻底"失忆"，在死循环里疯狂烧 Token。

  怎么破？两个解法：第一，Role 约束。不说"帮我修 Bug"，要说"你是一位代码审查员，只指出问题不修改"。给 AI 明确岗位身份，行为就会收敛。第二，Rules 边界。用 .cursorrules 写明："遇到报错先停止，向用户说明原因，等待确认后再继续"。

  但记住，关键决策点必须人工终审——这是不可让渡的边界。

---

## 第五段：`@OutroScene` 结尾 CTA（570f - 660f，约3秒）

- **[画面]**
  - 引入结尾场景 `@OutroScene`
  - 参数：headline="下期预告：用 Rules 玩转企业级重构", cta="关注 · 抢先验证真实 AI 能力", background="particles"
  - 右下角展示二维码/头像占位

- **[口播]**
  下期，我会拿真实的企业级重构项目，手把手演示怎么写 Rules、怎么验收 AI 输出、怎么在关键节点人工介入。我们不是在做 AI 演示，是在做 AI 的"岗位培训"。关注频道，抢先验证真实的 AI 能力边界。

---

## 技术备注

- **总时长**：660 帧 = 22 秒（@30fps）
- **A轨（Remotion动画）**：
  - IntroScene (90f) + TimelineScene (180f) + TableScene (180f) + ConceptScene (120f) + OutroScene (90f)
- **B轨（人工录屏）**：3 处 VideoSlot 占位
  1. ep01-assets/fix-loop-pain.mp4 —— IDE 死循环报错录屏
  2. Workflow 编辑器多步骤编排录屏
  3. Rules 配置界面实操录屏
- **背景音乐**：科幻电子风格
  - TimelineScene：渐进节奏
  - TableScene：对比强调重低音
  - ConceptScene：警示音效
- **口播字数**：约 650 字，语速 30 字/秒，总口播时长约 22 秒，与视频时长匹配
