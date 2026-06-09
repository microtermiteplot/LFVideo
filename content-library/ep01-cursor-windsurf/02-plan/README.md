---
stage: 02-content-planning
status: approved
source_workflow: /02-content-planning-bilibili
---

# ep01 内容策划方案（导演大纲）：《2026年的Cursor和Windsurf，已经不是你以为的AI IDE了》

本期视频定位为 **AI IDE 2026 变局先导片**。通过对两大顶流 IDE 的深度剖析与横向对比，向受众揭示从"单步辅助（Editor）"到"智能体狂奔（Agent）"，最终通过"岗位规则化（Role）"进行控制的行业终极趋势。

---

## 1. 定稿标题

《2026年的Cursor和Windsurf，已经不是你以为的AI IDE了》

*(备选：《别再盲目点 Fix 了！用岗位规则驯服 AI 智能体野马》)*

---

## 2. 画面配比与视觉风格

- **A 轨（程序化概念动画）比例**：70%（Remotion 模板驱动：IntroScene + TimelineScene + TableScene + ConceptScene + OutroScene）
- **B 轨（实操录屏/外部资产）比例**：30%（画中画 `@VideoSlot` 嵌入真实 IDE 录屏：死循环报错、Workflow 编排、Rules 配置）
- **核心视觉隐喻**：
  - **Editor（螺丝刀）**：精准但纯人工驱动，点一行改一行。
  - **Agent（脱缰野马）**：狂野奔跑，自动多步拆解，但在报错时极度容易陷入死循环，原地打转。
  - **Role（缰绳与规矩）**：岗位说明书，通过 Rules 规则限制和约束野马，让其稳健、闭环运行。

---

## 3. Demo 实操设计

- **痛点展示**：在没有配置 Rules 约束时，Windsurf 或 Cursor Agents 在遇到库版本冲突或路径报错时，不断重复尝试修改同一个文件，导致上下文急剧堆叠，最终由于无状态决策陷入死循环，白白消耗大量 Token。
- **解法演示**：通过配置 `.cursorrules` (Cursor) 或 `.md` (Windsurf) Rules，明确写明项目运行规范（如："禁止修改 package.json 中的 typescript 版本，遇到编译报错必须运行 npm run build 验证"）。AI 智能体读取后，在规则约束内一次性跑通，彻底避免死循环。

---

## 4. 视频结构大纲（B站单轨：22秒精华版 + 扩展长版）

### 第一段：开头黄金钩子（0f - 90f，约3秒）
- **核心论点**：到了 2026 年，你还把 Cursor 当作"补全几行代码的编辑器"？认知已经严重落后。
- **画面视觉**：黑色粒子背景，`@IntroScene` 开场，参数：title="2026 AI IDE 质变", subtitle="你手里的螺丝刀，早就是脱缰野马了"。右下角画中画闪过 IDE 死循环报错录屏。

### 第二段：纵向进化：Cursor 的角色化质变（90f - 270f，约6秒）
- **核心论点**：Cursor 近三年从"智能输入法"到"岗位骨架"的剧烈质变。
- **画面视觉**：`@TimelineScene` 时间轴演进，三年节点顺次浮现，轴线延伸 + Spring 弹跳动画。
  - 2024：Editor 辅助时代（🔧）
  - 2025：Composer 智能体狂飙（🐴）
  - 2026：岗位角色化阶段（🕸️）

### 第三段：横向华山论剑：Cursor vs Windsurf（270f - 450f，约6秒）
- **核心论点**：IDE 机制设计严重影响 AI 智能体效率。Windsurf Workflows 在多步骤编排上原生优于 Cursor MDC。
- **画面视觉**：`@TableScene` 硬核对比表格，4 个维度横向扫描，第 120 帧高亮胜出单元格。
  - 文件格式：.mdc 专有 vs .md 通用 → Windsurf 胜
  - 多步骤编排：单步触发器 vs 原生多步 → Windsurf 胜
  - 跨角色调用：手动 @ vs 原生串联 → Windsurf 胜
  - 跨工具兼容：互不兼容 → 平局

### 第四段：判断层——避坑与边界（450f - 570f，约4秒）
- **核心论点**：Agent 死循环的根因是上下文堆叠溢出。解法是 Role 约束 + Rules 边界 + 人工终审。
- **画面视觉**：`@ConceptScene` 三张概念卡片依次浮现。
  - ⚠️ 死循环陷阱：上下文堆叠导致原地打转
  - 📋 规训解法：Role 约束 + Rules 边界
  - ✋ 验收标准：关键决策点必须人工终审
- **画中画**：Rules 配置界面实操录屏

### 第五段：结尾 CTA（570f - 660f，约3秒）
- **核心论点**：下期带企业级重构项目，手把手演示 Rules 实战。
- **画面视觉**：`@OutroScene`，headline="下期预告：用 Rules 玩转企业级重构", cta="关注 · 抢先验证真实 AI 能力"。

---

## 5. 已用模板清单（已开发完成）

| 模板 | 用途 | 位置 |
|------|------|------|
| `@IntroScene` | 片头黄金钩子 | `video/src/template/scenes/IntroScene.tsx` |
| `@TimelineScene` | 纵向进化时间轴 | `video/src/template/scenes/TimelineScene.tsx` |
| `@TableScene` | 横向硬核对比表 | `video/src/template/scenes/TableScene.tsx` |
| `@ConceptScene` | 概念卡片（3张） | `video/src/template/scenes/ConceptScene.tsx` |
| `@OutroScene` | 结尾 CTA | `video/src/template/scenes/OutroScene.tsx` |
| `@VideoSlot` | 画中画 B 轨嵌入 | 复用为画中画组件 |

---

## 6. 数据对接

- **文案数据源**：`video/src/episodes/ep01-cursor-windsurf/data.ts`
- **场景组装**：`video/src/episodes/ep01-cursor-windsurf/Episode.tsx`
- **脚本对齐**：`content-library/ep01-cursor-windsurf/04-script/README.md`

---

## 7. 风险提示

- 视频中引用的 Subagents/Bugbot 等特性对 2026 年初以前的版本不生效，口播需明确强调"更新到最新版"。
- B 轨录屏素材（3 处画中画）需在视频渲染前补充完整，否则成品缺少实操说服力。
- 口播字数约 650 字，按 30 字/秒语速，恰好匹配 22 秒视频时长，无需额外剪辑变速。
