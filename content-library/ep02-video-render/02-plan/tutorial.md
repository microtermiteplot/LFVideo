# 代码即视频：如何用 100 行 React 代码编译卡点与图表动效？
## 【AI 视频自动化生产线】第 2 期：渲染引擎篇实操落地指南

在上一期（系列总体构建）中，我们向大家展示了如何利用 AI 智能体作为控制面指挥多媒体库。本期我们将深度潜入**视频自动化生产线的“渲染引擎层”**。

我们将解密如何直接使用 React / TypeScript（Remotion 引擎）编写可编译成 4K 视频的高保真 UI、卡点动效与动态图表，并破解 AI 在编写视频组件时最致命的 “window/document 未定义” SSR 崩溃报错。

---

## 一、核心概念：什么是 Video-as-Code（代码即视频）？

传统剪辑软件（如 PR、FCPX、剪映）的核心逻辑是**轨道与绝对时间轴**。而 Remotion 的核心逻辑是：
1. **视频就是一个 React 组件**。
2. **时间轴就是当前的帧数（Frame）**。
3. **渲染器的任务是把 React 状态在特定 Frame 下绘制出来，截图拼装成视频**。

### 帧与秒的双向插值公式
在 Remotion 中，一切动效的本质都是**帧数（Current Frame）到属性状态值（State Value）的数学映射**：

```typescript
import { useCurrentFrame, useVideoConfig } from 'remotion';

export const FadeInComponent = () => {
  const frame = useCurrentFrame();          // 当前播放到了第几帧（0, 1, 2...）
  const { fps } = useVideoConfig();        // 获取视频的帧率（例如 30 fps）
  
  const currentSeconds = frame / fps;      // 换算为当前播到了第几秒
  
  // 核心插值：在前 15 帧内，不透明度从 0 渐变到 1
  const opacity = Math.min(1, frame / 15); 
  
  return <div style={{ opacity }}>代码即视频！</div>;
};
```

这种“帧即状态”的模式天生对 AI 极度友好——AI 不需要理解轨道拖拽，它只需要编写极其擅长的**数学映射函数与 CSS 排版**。

---

## 二、开源落地方案对比（渲染层深度对比）

在代码视频化领域，有几种截然不同的渲染实现，它们的边界划分如下：

| 技术维度 | 方案名 | 核心渲染机制 | 动效与自适应排版复杂度 | 避坑点 (Pitfalls) | 证据状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **视频代码化** | **Remotion (React)** | 基于 Chrome (Puppeteer) 无头渲染 DOM 帧，配合 FFmpeg 合成 | 🌟 极高。支持完整的 CSS/SVG, Flexbox, Tailwind, 网页动效库（Cubic-bezier） | **SSR（服务器预渲染）阶段 window/document 未定义报错** | `verified` |
| **视频代码化** | **MoviePy (Python)** | 基于 NumPy 像素矩阵计算，底层调用 Imageio/FFmpeg | ❌ 极低。文本布局计算极度繁琐，难以实现响应式自适应排版 | 渲染效率极低，多层画布堆叠时内存开销巨大 | `paper_spec` |
| **视频代码化** | **Cocos2d-HTML5** | 基于 HTML5 Canvas 绘图上下文逐帧绘制 | ⚠️ 中等。适合游戏类复杂粒子动画，但编写标准网页 UI 成本太高 | 文本换行与 DOM 结构对齐计算复杂 | `paper_spec` |

### 核心决策：
我们全面拥抱 **Remotion (React)**，这是目前唯一能让 Cursor 智能体通过**修改标准网页 CSS 代码**就能输出高信息密度视频的渲染方案。

---

## 三、致命 SSR 踩坑：window/document is not defined

在开发视频组件时，你一定会遇到这个**阻碍 90% 开发者通关的超级巨坑**。

### 1. 为什么会红屏崩溃？
Remotion 在执行 `npx remotion render` 渲染命令时，为了提前获取视频的时长、尺寸并进行多核任务拆分，会首先在 **Node.js 环境下对 React 树进行首轮服务器端预渲染（SSR）**。

由于 Node.js 里面**没有浏览器环境**，一旦 AI（Cursor）编写组件时，在顶层作用域或 React 初始化阶段写下了如下常见的“常识性”代码：

```tsx
// ❌ 灾难：SSR 阶段会直接爆出 ReferenceError: window is not defined
const screenWidth = window.innerWidth; 
const isChrome = navigator.userAgent.includes('Chrome');

export const MyScene = () => {
  ...
}
```
渲染进程会立刻红屏中断，哪怕你仅仅是在本地 Dev 预览，也会崩溃。

---

## 四、MDC Rule 约束：用岗位规则一键驯服 Cursor

我们不需要自己手动去给 AI 编写的代码打补丁。在项目根目录下，我们创建 `.cursor/rules/remotion-ssr.mdc`（或 `.windsurf/rules` ），让 AI IDE 永远自动避开这个坑。

### 1. 约束规则配置 (`.cursor/rules/remotion-ssr.mdc`)

```markdown
---
description: 限制 AI 在编写 Remotion 视频组件时引入 SSR 报错
globs: video/src/template/**/*.tsx, video/src/template/**/*.ts
---

# Remotion SSR 安全守卫法则

你在为 Remotion 视频渲染引擎编写 React 组件。Remotion 会在渲染的第一阶段执行 Node.js SSR 预渲染，此时 window, document, navigator 均不存在。

### 强制守卫要求：
1. **绝对禁止**在 React 组件的顶层作用域、外部变量初始化、或 `useState` 初始值中直接读取 `window`、`document`、`navigator`、`localStorage` 或任何其他浏览器全局专有对象。
2. 任何需要读取视口宽高或元素尺寸的逻辑，必须在 React 的 **`useEffect`** 中执行（此时组件已被挂载到真实浏览器中），或使用安全守卫：
   ```typescript
   const getWidth = () => {
     if (typeof window !== 'undefined') {
       return window.innerWidth;
     }
     return 1920; // 默认 SSR 安全宽度
   };
   ```
3. 在进行 Canvas、Lottie 或复杂粒子动画库（其内部依赖浏览器 DOM）初始化时，必须加上 SSR 状态门控：
   ```typescript
   const [isMounted, setIsMounted] = useState(false);
   useEffect(() => { setIsMounted(true); }, []);
   if (!isMounted) return null; // 阻塞预渲染，安全通过 SSR
   ```
```

一旦在 IDE 中加载了此规则，Cursor 在生成任何 React 视频组件时，都会自动穿上“防弹衣”，完美规避 SSR 报错。

---

## 五、核心代码实操：编写 100 行 React 动效渲染器

下面我们编写一个 100 行以内的、包含 CSS 弹性排版与 Spring 弹簧动效的硬核对比卡片场景组件。

### 1. 场景组件代码 (`src/template/ComparisonScene.tsx`)

```tsx
import { useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import React, { useEffect, useState } from 'react';

export const ComparisonScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  // SSR 安全守卫：门控组件是否已被真实挂载到浏览器
  const [mounted, setMounted] = useState(false);
  useEffect(() => {
    setMounted(true);
  }, []);

  // 弹簧物理动画配置：damping(阻尼), stiffness(刚度), mass(质量)
  const springAnim = spring({
    frame,
    fps,
    config: { damping: 15, stiffness: 100, mass: 1 }
  });

  // 动画属性插值：0帧到30帧，纵向位移由 100px 变为 0px
  const translateY = interpolate(springAnim, [0, 1], [100, 0]);
  const opacity = interpolate(springAnim, [0, 1], [0, 1]);

  if (!mounted) {
    return <div style={{ backgroundColor: '#0f172a', width: '100%', height: '100%' }} />;
  }

  return (
    <div style={{
      width: '100%',
      height: '100%',
      backgroundColor: '#0f172a',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      fontFamily: 'system-ui, sans-serif'
    }}>
      {/* 顶部标题，带渐入 */}
      <h1 style={{
        color: '#f8fafc',
        fontSize: '72px',
        marginBottom: '40px',
        opacity,
        transform: `translateY(${translateY}px)`
      }}>
        MDC 被动约束对比
      </h1>

      {/* 左右弹性卡片容器 */}
      <div style={{
        display: 'flex',
        gap: '40px',
        width: '80%',
        maxWidth: '1200px'
      }}>
        {/* 左卡片：无规则 */}
        <div style={{
          flex: 1,
          backgroundColor: '#1e293b',
          borderRadius: '16px',
          padding: '40px',
          border: '2px solid #ef4444',
          transform: `scale(${springAnim})`
        }}>
          <h2 style={{ color: '#ef4444', fontSize: '36px', marginBottom: '20px' }}>无规则约束 ⚠️</h2>
          <p style={{ color: '#94a3b8', fontSize: '24px', lineHeight: '1.6' }}>
            AI 极其容易在 React 组件顶层读取 window，导致 SSR 预渲染阶段直接 ReferenceError 崩溃红屏。
          </p>
        </div>

        {/* 右卡片：MDC 约束 */}
        <div style={{
          flex: 1,
          backgroundColor: '#1e293b',
          borderRadius: '16px',
          padding: '40px',
          border: '2px solid #10b981',
          transform: `scale(${springAnim})`,
          boxShadow: '0 0 20px rgba(16, 185, 129, 0.3)'
        }}>
          <h2 style={{ color: '#10b981', fontSize: '36px', marginBottom: '20px' }}>加入 MDC 守卫 ✅</h2>
          <p style={{ color: '#94a3b8', fontSize: '24px', lineHeight: '1.6' }}>
            AI 智能体自动检测并补齐浏览器环境安全守卫，多核多线程秒级渲染，一键流畅打包 MP4。
          </p>
        </div>
      </div>
    </div>
  );
};
```

你只需使用终端命令即可启动预览或渲染：
```bash
# 启动 Remotion Studio 浏览器可视化调试面板
npx remotion studio

# 编译并渲染该场景为 1080P MP4 视频
npx remotion render src/index.ts ComparisonScene out/comparison.mp4
```

---

## 六、总结

通过本期 Remotion 渲染引擎篇的实操：
- 我们掌握了 **“帧数 (Frame) 即状态 (State)”** 的 Video-as-Code 核心技术本质。
- 我们利用 **MDC Rule 订立了岗位约束规矩**，完美封锁了 AI 编写 Remotion 组件时的 SSR 致命 bug。

在下一期中，我们将攻克**“字幕与卡点”**，教大家如何向 OpenAI Whisper 接口获取毫秒级时间戳 JSON，并自动驱动本期编写的高亮与卡点 React 动效组件！
