---
stage: 01-topic
status: approved
source_workflow: /01-topic-research
---

# ep02 选题分析：《代码即视频：如何用 100 行 React 代码编译卡点与图表动效？》
## 系列定位：【AI 视频自动化生产线】第 2 期：渲染引擎篇

## 1. 选题判断

- **值得做吗**：✅
- **AI 能做成吗**：能。Remotion 是纯前端 React 生态，由 Cursor 编写 React 动效、配置 CSS 弹性布局是 AI 的拿手好戏。
- **核心价值**：精讲 Remotion 渲染层细节，解密“Frame 与 Seconds 双向插值逻辑”。聚焦剖析 Cursor 在编写渲染器时极其致命的 **“SSR 阶段 window 未定义”** 报错，提供用 MDC Rule 降维打击一键封杀该 Bug 的实战方案。
- **目标受众**：
  - 主受众：前端工程师、对“代码即视频 (Video as Code)”拥有高接纳度并想开发自用剪辑工具的开发者。
  - 次受众：AI 效率工具爱好者，渴望了解如何给 Cursor 订立规则以拦截 SSR 报错的用户。
- **传播/截图点**：
  1. **window is not defined 红屏崩溃对比**：左侧没有规则约束时 Cursor 编写的组件在 SSR 阶段无限报错红屏；右侧加入 MDC 被动规则后 Cursor 自动补全 SSR 安全守卫一次渲染出片。
  2. **100行 React 动效渲染**：展示如何通过极简代码在 Remotion 中实现字级高亮与动态图表卡点。

---

## 2. 标题候选（≥3版）

1. **《代码即视频：如何用 100 行 React 代码编译卡点与图表动效？》**（主推，硬核技术风，契合技术受众）
2. **《放弃剪映！写 100 行 React 代码，让 AI 帮我自动剪片》**（适合 B 站信息流，反预期钩子）
3. **《别让 window 未定义毁了你的 AI 视频！用 Cursor 规则一键驯服 Remotion SSR》**（痛点直击，垂直受众精确引流）

---

## 3. 模版动态评估与声明

- **已有模版评估**：
  - `@IntroScene` / `@OutroScene`：用于片头黄金钩子与结尾。
  - `@TableScene`：用于横向比拼 Remotion vs MoviePy。
- **动态声明新模版**：
  - **模版代号**：`@SplitLayout`（分屏对比组件）
    * **作用**：展示 Cursor 规则有无情况下的编译对比，视觉冲击力强。
    * **数据 Schema**：
      ```typescript
      interface SplitLayoutProps {
        leftTitle: string;
        rightTitle: string;
        leftCode: string;
        rightCode: string;
        showStatus: 'error' | 'success' | 'none';
      }
      ```

---

## 4. 视频结构大纲（5段式）

### 第一段：开头黄金钩子（约30秒）
- **核心论点**：放弃拖拽轨道！用 React 的 State 编写视频动效到底有多爽？
- **画面视觉**：`@IntroScene` 黑色科技感背景渐入，动态展示代码如何被一帧帧渲染为精美 MP4 的生产线动画。

### 第二段：Remotion 底层解密（约 2 分钟）
- **核心论点**：视频的本质是 Frame 与 Seconds 的插值。讲解 Remotion 核心机制。
- **画面视觉**：`@TimelineScene` 动态分解：`useCurrentFrame()` 与 `fps` 如何映射为当前秒数，如何利用 CSS Grid 轻松排版。

### 第三段：致命 SSR 踩坑（约 2 分钟）
- **核心论点**：实播 AI 的翻车瞬间——在 React 顶层直接读取 `window.innerWidth` 导致 Puppeteer 截图阶段 SSR 报 `window is not defined` 崩溃。
- **画面视觉**：展示终端红屏报错，暴露 AI 的“环境无状态”软肋。

### 第四段：MDC 被动约束降维打击（约 2.5 分钟）
- **核心论点**：不用手改一行防守代码！编写一条简单的 MDC Rule，让 Cursor 在编写 Remotion 组件时永远自动避开 SSR 报错。
- **画面视觉**：演示加入规则后，Cursor 瞬间变聪明，自动写出安全守卫并一次编译成功。

### 第五段：结尾 CTA
- **核心论点**：掌握视频代码化，你的后期效率将提升百倍。关注我，下期解密字级字幕卡点！
- **画面视觉**：`@OutroScene`。展示开源仓库地址与关注。
