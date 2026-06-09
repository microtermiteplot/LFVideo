---
stage: 03-video-planning-bilibili
status: draft
source_workflow: /03-video-planning-bilibili
---

# ep02 B站视听编排蓝图：《代码即视频：如何用 100 行 React 代码编译卡点与图表动效？》

---

## 1. 视频规格

- **平台**：Bilibili
- **画幅**：16:9（1920×1080）
- **帧率**：30fps
- **总时长预估**：7 分 30 秒
- **视觉隐喻**：数字渲染生产线（代码像乐高积木在时间帧传送带上流动）

---

## 2. 场景分镜与组件映射

### 第一段：开头黄金钩子（0:00-0:30）

- **组件**：`@IntroScene`
- **Props 填充**：
  ```json
  {
    "title": "代码即视频",
    "subtitle": "如何用 100 行 React 编译卡点与图表动效？",
    "background": "particles"
  }
  ```
- **动画 Cue 表**：
  - `frame=0`: `fade_in(background, duration=30f)` - 粒子背景渐显
  - `frame=15`: `spring_scale(title, from=0.8, to=1.0, mass=1, stiffness=100)` - 标题弹性放大入场
  - `frame=45`: `fade_in(subtitle, duration=20f)` - 副标题淡入
  - `frame=75`: `shimmer(title, color="#00D26A", duration=15f)` - 标题微光闪烁强调

---

### 第二段：Remotion 底层解密（0:30-2:30）

- **组件**：`@TimelineScene`（新组件，见下方 Template Ticket）
- **Props 填充**：
  ```json
  {
    "eyebrow": "底层机制",
    "title": "Frame 与 Seconds 的数学映射",
    "timeline_data": [
      { "frame": 0, "seconds": 0, "label": "起始帧", "highlight": true },
      { "frame": 30, "seconds": 1, "label": "1秒@30fps", "highlight": false },
      { "frame": 60, "seconds": 2, "label": "2秒", "highlight": false },
      { "frame": 120, "seconds": 4, "label": "useCurrentFrame() 返回值", "highlight": true }
    ],
    "code_snippet": "const { fps, durationInFrames } = useVideoConfig();\nconst frame = useCurrentFrame();\nconst seconds = frame / fps;",
    "animation_type": "spring"
  }
  ```
- **动画 Cue 表**：
  - `frame=0`: `slide_in(timeline_bar, from="bottom", duration=40f)` - 时间轴从底部滑入
  - `frame=30`: `stagger_fade(timeline_data.points, stagger=5f)` - 数据点依次淡入（间隔5帧）
  - `frame=90`: `highlight_point(frame=120, glow_color="#00D26A")` - 当前帧高亮发光
  - `frame=120`: `scale_up(code_snippet, factor=1.05, duration=10f)` - 代码片段微缩放强调

---

### 第三段：致命 SSR 踩坑（2:30-4:30）

- **组件**：`@ConceptScene` + `@VideoSlot`（B 轨 overlay）
- **A 轨 Props（概念层）**：
  ```json
  {
    "eyebrow": "翻车现场",
    "title": "SSR 渲染的致命陷阱",
    "items": [
      {
        "label": "ERROR",
        "title": "window is not defined",
        "desc": "在 React 顶层直接读取 window.innerWidth，Node 端无 DOM 环境，立即崩溃",
        "icon": "💥"
      },
      {
        "label": "ROOT CAUSE",
        "title": "Puppeteer 预渲染阶段",
        "desc": "Remotion SSR 截图时，组件在 Node.js 环境执行，无浏览器全局对象",
        "icon": "🔍"
      },
      {
        "label": "IMPACT",
        "title": "编译流程中断",
        "desc": "npx remotion render 红屏报错，MP4 无法生成，项目阻断",
        "icon": "🚫"
      }
    ],
    "background": "gradient"
  }
  ```
- **B 轨指令（录屏层）**：
  ```json
  {
    "clip_id": "ssr-error-demo",
    "slot_component": "@VideoSlot",
    "slot_props": {
      "position": "bottom-right",
      "width": 720,
      "rounded": true,
      "src": "./assets/ep02/ssr_error_redscreen.mp4"
    },
    "zoom_crop_directives": [
      {
        "timestamp_start": "0:00",
        "timestamp_end": "0:08",
        "zoom_level": 1.0,
        "focal_point": { "x": 0.5, "y": 0.5 },
        "description": "初始状态：IDE 正常显示代码"
      },
      {
        "timestamp_start": "0:08",
        "timestamp_end": "0:15",
        "zoom_level": 1.3,
        "focal_point": { "x": 0.5, "y": 0.7 },
        "description": "聚焦终端：执行 npx remotion render"
      },
      {
        "timestamp_start": "0:15",
        "timestamp_end": "0:30",
        "zoom_level": 1.5,
        "focal_point": { "x": 0.5, "y": 0.4 },
        "description": "放大报错：ReferenceError: window is not defined 红屏"
      },
      {
        "timestamp_start": "0:30",
        "timestamp_end": "0:45",
        "zoom_level": 1.2,
        "focal_point": { "x": 0.3, "y": 0.3 },
        "description": "聚焦代码：展示问题代码行 window.innerWidth"
      }
    ]
  }
  ```
- **动画 Cue 表**：
  - `frame=0`: `shake(items[0], intensity=3px, duration=20f)` - 错误卡片震动强调
  - `frame=30`: `color_pulse(items[0].icon, from="#FF4444", to="#FF0000")` - 爆炸图标红闪
  - `frame=60`: `fade_in(video_slot, duration=20f)` - B 轨录屏画中画淡入

---

### 第四段：MDC 被动约束降维打击（4:30-7:00）

- **组件**：`@SplitLayout`（左右分屏对比）
- **Props 填充**：
  ```json
  {
    "direction": "horizontal",
    "ratio": 0.5,
    "left": {
      "label": "❌ 无规则",
      "content": "@VideoSlot",
      "video_props": {
        "src": "./assets/ep02/agent_loop_error.mp4",
        "position": "fill",
        "rounded": false
      }
    },
    "right": {
      "label": "✅ 有 MDC Rule",
      "content": "@VideoSlot",
      "video_props": {
        "src": "./assets/ep02/agent_rule_pass.mp4",
        "position": "fill",
        "rounded": false
      }
    }
  }
  ```
- **B 轨指令（双录屏）**：
  ```json
  {
    "clip_id": "mdc-comparison",
    "left_directives": [
      {
        "timestamp_start": "0:00",
        "timestamp_end": "0:20",
        "zoom_level": 1.0,
        "focal_point": { "x": 0.5, "y": 0.5 },
        "description": "左侧：Cursor Agent 循环报错，反复尝试读取 window"
      },
      {
        "timestamp_start": "0:20",
        "timestamp_end": "0:45",
        "zoom_level": 1.4,
        "focal_point": { "x": 0.5, "y": 0.2 },
        "description": "放大：展示错误堆栈和反复出现的 ReferenceError"
      }
    ],
    "right_directives": [
      {
        "timestamp_start": "0:00",
        "timestamp_end": "0:15",
        "zoom_level": 1.0,
        "focal_point": { "x": 0.5, "y": 0.5 },
        "description": "右侧：加入 .cursor/rules/remotion-ssr.mdc 约束"
      },
      {
        "timestamp_start": "0:15",
        "timestamp_end": "0:30",
        "zoom_level": 1.3,
        "focal_point": { "x": 0.3, "y": 0.4 },
        "description": "聚焦规则文件内容：展示 typeof window 守卫强制要求"
      },
      {
        "timestamp_start": "0:30",
        "timestamp_end": "0:45",
        "zoom_level": 1.2,
        "focal_point": { "x": 0.5, "y": 0.8 },
        "description": "终端输出：npx remotion render 一次通过，生成 MP4"
      }
    ]
  }
  ```
- **动画 Cue 表**：
  - `frame=0`: `wipe_reveal(split_layout, direction="left-to-right", duration=30f)` - 分屏擦除显现
  - `frame=30`: `fade_in(left.label, color="#FF4444", duration=15f)` - 左侧红标淡入
  - `frame=45`: `fade_in(right.label, color="#00D26A", duration=15f)` - 右侧绿标淡入
  - `frame=120`: `scale_up(right.label, factor=1.1, spring=true)` - 成功侧弹性强调

---

### 第五段：结尾 CTA（7:00-7:30）

- **组件**：`@OutroScene`
- **Props 填充**：
  ```json
  {
    "headline": "掌握代码即视频，后期效率提升百倍",
    "cta": "关注 · 下期解密 Whisper 毫秒级字幕卡点",
    "background": "gradient",
    "repo_url": "https://github.com/yourname/ai-ide-workflows",
    "platform_links": [
      { "name": "Bilibili", "icon": "📺", "handle": "@AIIDE实验室" },
      { "name": "GitHub", "icon": "⭐", "handle": "ai-ide-workflows" }
    ]
  }
  ```
- **动画 Cue 表**：
  - `frame=0`: `fade_in(headline, duration=20f)` - 主文案淡入
  - `frame=30`: `typewriter(cta, speed=2f/char)` - CTA 打字机效果
  - `frame=60`: `slide_in(platform_links, from="bottom", stagger=5f)` - 社交链接依次滑入

---

## 3. 组件扩展工单 (Template Tickets)

由于 `outline_sections[1]`（Remotion 底层解密段）需要的 `@TimelineScene` 不在现有组件库中，声明新组件工单：

| 工单号 | 组件名 | 物理路径建议 | Props 接口 | 动画规范 |
|:---|:---|:---|:---|:---|
| **TICKET-ep02-01** | `@TimelineScene` | `video/src/template/scenes/TimelineScene.tsx` | `interface TimelineSceneProps { eyebrow: string; title: string; timeline_data: Array<{frame: number; seconds: number; label: string; highlight?: boolean}>; code_snippet?: string; animation_type?: 'spring' \| 'linear' }` | 1. 时间轴条带：`useCurrentFrame()` 驱动 `scaleX` 从 0→1；2. 数据点：`spring({frame, fps, config: {mass: 1, stiffness: 100}})` 控制 `scale` 弹入；3. 高亮点：`glow` filter 脉冲动画 |

---

## 4. 流程质量自检

- ✅ **组件覆盖度自检**：5 个 section 全部映射完成（4 个复用 + 1 个新 Ticket）
- ✅ **B 轨指令完整度**：第三、四段 demonstration/comparison 类型已生成完整 zoom/crop 指令
- ✅ **Props 接口完整度**：所有复用组件的 Props 已按 remotion-spec.md 规范填充
- ✅ **视觉隐喻一致性**：全片保持"数字渲染生产线"隐喻（代码积木 → 帧传送带 → MP4 包裹）

---

## 5. 结构化校验块 (JSON Schema Block)

```json
{
  "video_spec": {
    "aspect_ratio": "16:9",
    "resolution": "1920x1080",
    "fps": 30,
    "estimated_duration_seconds": 450
  },
  "scene_storyboards": [
    {
      "section_ref": "开头黄金钩子",
      "scene_template": "@IntroScene",
      "props": {
        "title": "代码即视频",
        "subtitle": "如何用 100 行 React 编译卡点与图表动效？",
        "background": "particles"
      },
      "duration_seconds": 30
    },
    {
      "section_ref": "Remotion 底层解密",
      "scene_template": "@TimelineScene",
      "props": {
        "eyebrow": "底层机制",
        "title": "Frame 与 Seconds 的数学映射",
        "timeline_data": [
          { "frame": 0, "seconds": 0, "label": "起始帧", "highlight": true },
          { "frame": 30, "seconds": 1, "label": "1秒@30fps", "highlight": false },
          { "frame": 60, "seconds": 2, "label": "2秒", "highlight": false },
          { "frame": 120, "seconds": 4, "label": "useCurrentFrame() 返回值", "highlight": true }
        ],
        "code_snippet": "const { fps } = useVideoConfig();\nconst frame = useCurrentFrame();",
        "animation_type": "spring"
      },
      "duration_seconds": 120,
      "template_ticket": "TICKET-ep02-01"
    },
    {
      "section_ref": "致命 SSR 踩坑",
      "scene_template": "@ConceptScene",
      "props": {
        "eyebrow": "翻车现场",
        "title": "SSR 渲染的致命陷阱",
        "items": [
          { "label": "ERROR", "title": "window is not defined", "desc": "Node 端无 DOM 环境", "icon": "💥" },
          { "label": "ROOT CAUSE", "title": "Puppeteer 预渲染阶段", "desc": "Remotion SSR 截图时崩溃", "icon": "🔍" },
          { "label": "IMPACT", "title": "编译流程中断", "desc": "MP4 无法生成", "icon": "🚫" }
        ],
        "background": "gradient"
      },
      "duration_seconds": 120,
      "b_track_overlay": {
        "component": "@VideoSlot",
        "position": "bottom-right",
        "clip_id": "ssr-error-demo"
      }
    },
    {
      "section_ref": "MDC 被动约束降维打击",
      "scene_template": "@SplitLayout",
      "props": {
        "direction": "horizontal",
        "ratio": 0.5,
        "left": { "label": "❌ 无规则", "video_src": "./assets/ep02/agent_loop_error.mp4" },
        "right": { "label": "✅ 有 MDC Rule", "video_src": "./assets/ep02/agent_rule_pass.mp4" }
      },
      "duration_seconds": 150
    },
    {
      "section_ref": "结尾 CTA",
      "scene_template": "@OutroScene",
      "props": {
        "headline": "掌握代码即视频，后期效率提升百倍",
        "cta": "关注 · 下期解密 Whisper 毫秒级字幕卡点",
        "background": "gradient"
      },
      "duration_seconds": 30
    }
  ],
  "zoom_crop_directives": [
    {
      "clip_id": "ssr-error-demo",
      "source_file": "./assets/ep02/ssr_error_redscreen.mp4",
      "directives": [
        { "timestamp_start": "0:00", "timestamp_end": "0:08", "zoom_level": 1.0, "focal_point": { "x": 0.5, "y": 0.5 } },
        { "timestamp_start": "0:08", "timestamp_end": "0:15", "zoom_level": 1.3, "focal_point": { "x": 0.5, "y": 0.7 } },
        { "timestamp_start": "0:15", "timestamp_end": "0:30", "zoom_level": 1.5, "focal_point": { "x": 0.5, "y": 0.4 } },
        { "timestamp_start": "0:30", "timestamp_end": "0:45", "zoom_level": 1.2, "focal_point": { "x": 0.3, "y": 0.3 } }
      ]
    },
    {
      "clip_id": "mdc-comparison-left",
      "source_file": "./assets/ep02/agent_loop_error.mp4",
      "directives": [
        { "timestamp_start": "0:00", "timestamp_end": "0:20", "zoom_level": 1.0, "focal_point": { "x": 0.5, "y": 0.5 } },
        { "timestamp_start": "0:20", "timestamp_end": "0:45", "zoom_level": 1.4, "focal_point": { "x": 0.5, "y": 0.2 } }
      ]
    },
    {
      "clip_id": "mdc-comparison-right",
      "source_file": "./assets/ep02/agent_rule_pass.mp4",
      "directives": [
        { "timestamp_start": "0:00", "timestamp_end": "0:15", "zoom_level": 1.0, "focal_point": { "x": 0.5, "y": 0.5 } },
        { "timestamp_start": "0:15", "timestamp_end": "0:30", "zoom_level": 1.3, "focal_point": { "x": 0.3, "y": 0.4 } },
        { "timestamp_start": "0:30", "timestamp_end": "0:45", "zoom_level": 1.2, "focal_point": { "x": 0.5, "y": 0.8 } }
      ]
    }
  ],
  "template_tickets": [
    {
      "ticket_id": "TICKET-ep02-01",
      "component_name": "@TimelineScene",
      "file_path": "video/src/template/scenes/TimelineScene.tsx",
      "rationale": "大纲要求展示 Frame 与 Seconds 的插值映射，现有组件库无时间轴可视化组件"
    }
  ],
  "judgment_layer_check": {
    "component_fidelity": "✅ 100% 映射到 Remotion 可渲染组件",
    "b_track_coverage": "✅ 所有 demonstration/comparison 段落已生成 zoom/crop 指令",
    "new_template_declared": "✅ TICKET-ep02-01 已声明，待视频工程师实现"
  }
}
```
