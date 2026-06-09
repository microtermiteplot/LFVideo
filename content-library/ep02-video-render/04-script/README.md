---
stage: 04-script
platform: bilibili
status: draft
source_workflow: /04-script-draft
---

# ep02 视频脚本：《代码即视频：如何用 100 行 React 代码编译卡点与图表动效？》

**总时长预估**：7 分 30 秒  
**口播字数预估**：约 2000 字  
**视觉隐喻**：数字渲染生产线

---

## 第一段：【@IntroScene】开头黄金钩子（0:00-0:30）

**[画面]**  
调用 `@IntroScene`。参数：
- `title` = "代码即视频"
- `subtitle` = "如何用 100 行 React 编译卡点与图表动效？"
- `background` = "particles"（粒子背景，科技感动态流动）

动画时序：
- 0.0s：粒子背景渐显
- 0.5s：标题弹性放大入场（spring 动效）
- 1.5s：副标题淡入
- 2.5s：标题微光闪烁强调

**[口播]**  
你还在用 PR、AE 一帧一帧地剪视频吗？停。今天我要告诉你一个完全不同的思路。写代码，就是在写视频。一百行 React，直接编译成 4K 高清 MP4。这就是 Remotion。但别急着兴奋，这条路上有一个几乎所有 AI 都会踩的致命深坑。 SSR 渲染时，window is not defined。什么意思？就是你的代码在浏览器里跑得欢，一编译就崩。怎么解？一条 MDC 规则，被动约束，让 AI 自动写出安全代码。今天这期，手把手带你跑通。

---

## 第二段：【@TimelineScene】Remotion 底层解密（0:30-2:30）

**[画面]**  
调用 `@TimelineScene`（新组件 TICKET-ep02-01）：
- `eyebrow` = "底层机制"
- `title` = "Frame 与 Seconds 的数学映射"
- `timeline_data` = [
  - {frame: 0, seconds: 0, label: "起始帧", highlight: true},
  - {frame: 30, seconds: 1, label: "1秒@30fps"},
  - {frame: 60, seconds: 2, label: "2秒"},
  - {frame: 120, seconds: 4, label: "useCurrentFrame() 返回值", highlight: true}
]
- `code_snippet` = "const { fps } = useVideoConfig();\nconst frame = useCurrentFrame();\nconst seconds = frame / fps;"
- `animation_type` = "spring"

动画时序：
- 0:30：时间轴从底部滑入
- 0:35：数据点依次淡入（stagger 间隔 5 帧）
- 1:00：当前帧高亮发光（#00D26A）
- 1:30：代码片段微缩放强调

**[口播]**  
先搞清楚 Remotion 的核心机制。视频的本质是什么？是帧。帧的本质是什么？是时间。Remotion 给你一个 `useCurrentFrame()` Hook，返回当前是第几帧。再给你一个 `useVideoConfig()`，返回 fps 和总帧数。简单除法，`frame / fps`，你就得到了当前时间点。这意味着什么？意味着你可以用 React 的状态、Props、Effect，来驱动视频的每一帧。想做一个进度条？监听 frame。想做动画插值？spring 物理公式直接上。你写的不是视频，是"时间的函数"。这才是代码即视频的真正含义。

---

## 第三段：【@ConceptScene + @VideoSlot】致命 SSR 踩坑（2:30-4:30）

**[画面]**  
主画面调用 `@ConceptScene`：
- `eyebrow` = "翻车现场"
- `title` = "SSR 渲染的致命陷阱"
- `items` = [
  - {label: "ERROR", title: "window is not defined", desc: "在 React 顶层直接读取 window.innerWidth，Node 端无 DOM 环境，立即崩溃", icon: "💥"},
  - {label: "ROOT CAUSE", title: "Puppeteer 预渲染阶段", desc: "Remotion SSR 截图时，组件在 Node.js 环境执行，无浏览器全局对象", icon: "🔍"},
  - {label: "IMPACT", title: "编译流程中断", desc: "npx remotion render 红屏报错，MP4 无法生成，项目阻断", icon: "🚫"}
]

右侧画中画 `@VideoSlot`（B轨占位）：
- `position` = "bottom-right"
- `width` = 720
- `rounded` = true
- `[B轨占位替换提醒：请用户在此补充 SSR 报错红屏录屏片段]`

动画时序：
- 2:30：错误卡片震动强调（3px 抖动）
- 2:35：爆炸图标红闪脉冲
- 2:40：B轨录屏画中画淡入

**[口播]**  
好，原理明白了，开始实操。你让 Cursor 写一个 Remotion 组件，读取窗口宽度做响应式布局。代码看起来没问题，在浏览器预览里跑得欢。你信心满满，执行 `npx remotion render`，准备导出成片。啪，红屏。`ReferenceError: window is not defined`。为什么？Remotion 的渲染分两个阶段。第一阶段，SSR 预渲染，Puppeteer 在 Node.js 环境里截图。Node 里没有 window，没有 document，没有任何浏览器全局对象。你的代码在顶层直接读 `window.innerWidth`，Node 端直接崩溃。这不是你代码的问题，是 AI 的环境感知盲区。它不知道这段代码要在两个完全不同的环境里跑。

---

## 第四段：【@SplitLayout】MDC 被动约束降维打击（4:30-7:00）

**[画面]**  
调用 `@SplitLayout` 左右分屏对比：
- `direction` = "horizontal"
- `ratio` = 0.5
- `left` = `@VideoSlot` 填充左侧，标签 "❌ 无规则"，红色
  - `[B轨占位替换提醒：请用户在此补充 Agent 循环报错录屏]`
- `right` = `@VideoSlot` 填充右侧，标签 "✅ 有 MDC Rule"，绿色
  - `[B轨占位替换提醒：请用户在此补充 MDC 规则后一次通过录屏]`

动画时序：
- 4:30：分屏擦除显现（左到右 wipe）
- 4:35：左侧红标淡入
- 4:40：右侧绿标淡入
- 5:15：成功侧弹性缩放强调

**[口播]**  
传统解法？手动改代码，加 `typeof window === 'undefined'` 守卫。但这很蠢。你要跟 AI 反复拉扯，每次它都可能忘掉。更好的解法？被动约束。写一个 `.cursor/rules/remotion-ssr.mdc` 文件，里面只有一条规则：所有 Remotion 组件，访问浏览器全局对象前，必须检查环境。Cursor 读到这条规则，自动在生成的代码里加上守卫。你不用改一行代码，不用跟 AI 拉锯。看左边，没规则，Cursor 反复循环，不停报错。看右边，加了 MDC 规则，一次通过，直接出片。这就是约束的力量。不是人去盯 AI，是让规则去盯。

---

## 第五段：【@OutroScene】结尾 CTA（7:00-7:30）

**[画面]**  
调用 `@OutroScene`：
- `headline` = "掌握代码即视频，后期效率提升百倍"
- `cta` = "关注 · 下期解密 Whisper 毫秒级字幕卡点"
- `background` = "gradient"
- `repo_url` = "https://github.com/yourname/ai-ide-workflows"
- `platform_links` = [
  - {name: "Bilibili", icon: "📺", handle: "@AIIDE实验室"},
  - {name: "GitHub", icon: "⭐", handle: "ai-ide-workflows"}
]

动画时序：
- 7:00：主文案淡入
- 7:05：CTA 打字机逐字显现
- 7:10：社交链接依次从底部滑入

**[口播]**  
掌握这套代码即视频的流程，你的后期效率能提升百倍。同样的内容，别人剪一天，你写一小时代码直接编译。而且，MDC 约束这套思路，不止用在 Remotion，任何 AI 辅助的场景都能套。想拿到本期完整的代码和规则模板？开源仓库在简介，自取。下期，我们讲一个更细的技术点：Whisper 毫秒级字幕卡点。如何让字幕精准跟上口播节奏，而且是自动的。关注，别错过。

---

## 6. 自我检查清单

- ✅ B 站深度版完整产出（5 段式，约 2000 字）
- ✅ 新模版组件 `@TimelineScene` Props 和数据 Schema 100% 填充
- ✅ 恶俗 AI 词汇检查：已删除"赋能、打造、革新、全方位、数字化浪潮"等
- ✅ 口播短句优先，换气感强
- ✅ B 轨占位标记清晰（第三、四段已标注）

---

## 7. 结构化校验块 (JSON Schema Block)

```json
{
  "title": "代码即视频：如何用 100 行 React 代码编译卡点与图表动效？",
  "platform": "bilibili",
  "estimated_duration_seconds": 450,
  "total_word_count": 1980,
  "sections": [
    {
      "id": "1",
      "track": "A",
      "scene_template": "@IntroScene",
      "voice": "你还在用 PR、AE 一帧一帧地剪视频吗？停。今天我要告诉你一个完全不同的思路...",
      "visual_instructions": "粒子背景 + 标题弹性入场 + 副标题淡入",
      "duration_hint_seconds": 30
    },
    {
      "id": "2",
      "track": "A",
      "scene_template": "@TimelineScene",
      "voice": "先搞清楚 Remotion 的核心机制。视频的本质是什么？是帧...",
      "visual_instructions": "时间轴滑入 + 数据点 stagger 淡入 + 代码高亮",
      "duration_hint_seconds": 120
    },
    {
      "id": "3",
      "track": "A+B",
      "scene_template": "@ConceptScene + @VideoSlot",
      "voice": "好，原理明白了，开始实操。你让 Cursor 写一个 Remotion 组件...",
      "visual_instructions": "错误概念卡片 + B轨录屏画中画",
      "duration_hint_seconds": 120,
      "b_track_required": true,
      "b_track_notes": "SSR 报错红屏录屏片段"
    },
    {
      "id": "4",
      "track": "A+B",
      "scene_template": "@SplitLayout",
      "voice": "传统解法？手动改代码，加守卫。但这很蠢...",
      "visual_instructions": "左右分屏对比：左侧无规则报错，右侧有 MDC 规则通过",
      "duration_hint_seconds": 150,
      "b_track_required": true,
      "b_track_notes": "左右两侧各需一段录屏：Agent 循环报错 vs MDC 规则后一次通过"
    },
    {
      "id": "5",
      "track": "A",
      "scene_template": "@OutroScene",
      "voice": "掌握这套代码即视频的流程，你的后期效率能提升百倍...",
      "visual_instructions": "渐变背景 + 打字机 CTA + 社交链接滑入",
      "duration_hint_seconds": 30
    }
  ],
  "judgment_layer_coverage": {
    "highlights_pitfall": true,
    "explains_boundary": true,
    "acceptance_standard": true,
    "ai_limitations_exposed": true
  },
  "b_track_assets_required": [
    {
      "clip_id": "ssr-error-demo",
      "description": "Cursor 执行 remotion render 报错红屏录屏",
      "timestamp_segments": 4
    },
    {
      "clip_id": "agent-loop-error",
      "description": "无 MDC 规则时 Cursor Agent 反复循环报错录屏",
      "timestamp_segments": 2
    },
    {
      "clip_id": "agent-rule-pass",
      "description": "有 MDC 规则后 Cursor Agent 一次通过录屏",
      "timestamp_segments": 3
    }
  ],
  "template_tickets_referenced": [
    "TICKET-ep02-01: @TimelineScene"
  ]
}
```
