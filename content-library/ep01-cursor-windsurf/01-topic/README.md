---
stage: 01-topic
status: approved
source_workflow: /01-topic-research
---

# ep01 选题分析：《2026年的Cursor和Windsurf，已经不是你以为的AI IDE了》

## 选题判断

- **值得做吗**：✅
- **AI 能做成吗**：能。Cursor 与 Windsurf 在 2024–2026 年间的功能演进是公开可查、真实可验证的；两者在 Rules / Workflows / Agent 编排上的差异，完全可以在本地 IDE 中复现。
- **核心价值**：打破"AI IDE = 代码补全工具"的旧心智，建立"Editor → Agent → Role"三层认知升级，并横向对比两大顶流 IDE 在角色化约束（Rules）与智能体编排（Workflows）上的机制差异。
- **目标受众**：
  - 主受众：已使用 Cursor / Windsurf 半年以上、遇到 Agent 死循环和失控问题的中高级开发者。
  - 次受众：在技术选型中犹豫的团队 TL 与架构师。
- **传播/截图点**：
  1. **横向硬核对比表**：Cursor MDC vs Windsurf Workflows 的 4-6 个核心维度一览，极易被截图转发到技术社群。
  2. **Agent 死循环 vs Role 一次通过**：左右分屏的极端对比，视觉冲击力极强。
- **长尾价值**：
  - 三层认知框架（Editor / Agent / Role）将成为全频道后续所有实操期的"底层协议"，本期作为先导片具有极高引用价值。
  - Rules 配置技巧（.mdc / .md）可被直接复刻到观众自己的项目中，具备教程沉淀属性。

## 标题候选（≥3版）

1. **《2026年的Cursor和Windsurf，已经不是你以为的AI IDE了》**（钩子：时效性 + 反预期 + 工具名前置）
   - *主推。直接打破旧认知，制造"我还停留在哪一年"的焦虑感。*
2. **《别再盲目点 Fix 了！用岗位规则驯服 AI 智能体野马》**（钩子：痛点共鸣 + 解决方案 + 比喻）
   - *适合 B 站信息流。精准命中 Agent 死循环的集体创伤。*
3. **《Cursor MDC vs Windsurf Workflows：谁才是2026年真·智能体 orchestrator？》**（钩子：对比冲突 + 英文技术术语 + 年份锚定）
   - *适合知乎/技术社群分发。硬核感强，容易引发站队讨论。*
4. **《从螺丝刀到脱缰野马：AI IDE 的三层跃迁，你在第几层？》**（钩子：比喻递进 + 互动提问）
   - *适合抖音/小红书封面。视觉隐喻明确，评论互动率高。*

## 模版动态评估与声明

- **已有模版评估**：
  - `@IntroScene` / `@OutroScene`：够用，可承担片头钩子与结尾 CTA。
  - `@ConceptScene`：**严重不足**。该组件最大仅支持 3 张文字卡片，无法承载"2024→2025→2026 功能演进轨迹"，更无法展示"多维度横向硬核对比矩阵"。信息密度与视觉表现力均不满足本期需求。
- **动态声明新模版**：
  - **模版代号**：`@TimelineScene`（纵向进化时间轴）
    * **作用**：可视化 Cursor 从 Editor 辅助时代 → Composer 智能体狂飙 → 岗位角色化阶段（Role）的三年质变。
    * **数据 Schema**：
      ```typescript
      interface TimelineEvent {
        year: string;
        title: string;
        desc: string;
        icon: string; // Emoji
      }
      interface TimelineSceneProps {
        eyebrow: string;
        title: string;
        events: TimelineEvent[];
      }
      ```
  - **模版代号**：`@TableScene`（横向硬核对比表格）
    * **作用**：高密度展示 Cursor (MDC) 与 Windsurf (Workflows) 在多步骤编排、跨角色调用、文件格式兼容性等维度的差异。
    * **数据 Schema**：
      ```typescript
      interface TableRow {
        feature: string;
        cursor: string;
        windsurf: string;
        win: 'cursor' | 'windsurf' | 'neutral';
      }
      interface TableSceneProps {
        eyebrow: string;
        title: string;
        headers: string[];
        rows: TableRow[];
      }
      ```

## 视频结构大纲（B站中长版：5-10分钟，高密度深度版）

### 开头 15 秒黄金钩子
- **核心论点**：到了 2026 年，你还把 Cursor 当作一个会补全代码的"Editor 螺丝刀"？那是暴殄天物。
- **画面视觉**：黑色科技背景，`@IntroScene` 打出 title="2026 AI IDE 质变", subtitle="你手里的螺丝刀，早就是脱缰野马了"。快速闪过疯狂点 Fix 报错的 IDE 录像，唤起共鸣。

### 第一段：纵向进化——Cursor 的角色化雏形（约 2 分钟）
- **核心论点**：Cursor 在近几个版本的剧烈重构中，已通过 Rules、Subagents、Bugbot、Security Review、Skills 的组合，形成了实质上的"岗位角色化"雏形。
- **画面视觉**：调用 `@TimelineScene`。时间轴从左至右延伸，依次弹跳浮现：
  - 2024 Editor 辅助时代（🔧）
  - 2025 Composer 智能体狂飙（🐴）
  - 2026 岗位角色化阶段（🕸️）

### 第二段：横向比拼——Cursor Rules vs Windsurf Workflows（约 2.5 分钟）
- **核心论点**：IDE 的机制设计严重影响 AI 智能体的效率。Cursor 的 Rules MDC 提供被动长期约束；Windsurf 的 Workflows 原生支持多步骤、多角色的显式编排，是更极致的智能体协同形态。
- **画面视觉**：调用 `@TableScene`。表头拉开后，各行数据顺次下滑浮现。第 120 帧，所有 `win !== 'neutral'` 的单元格高亮呼吸，视觉指明赢家。

### 第三段：判断层——Agent 为什么死循环，Role 如何降维打击（约 1.5 分钟）
- **核心论点**：Agent 的软肋在于复杂编译报错下，上下文丢失 + 单步决策无状态，必然陷入无限套娃。唯一的生路是建立 Role（岗位规矩），用约束拉回缰绳。
- **画面视觉**：`@SplitLayout` 左右分屏。左侧 `@VideoSlot` 演示 Agent 疯狂原地死循环、Token 狂飙；右侧展示在 Rules 约束下，智能体按清单打钩、一次通过。

### 结尾 CTA
- **核心论点**：认知已升级。下期直接带上这套 Rules 资产，在本地开跑企业级重构实战。
- **画面视觉**：`@OutroScene`。headline="下期预告：用 Rules 玩转企业级重构", cta="关注 · 抢先验证真实 AI 能力"。

## 视频结构大纲（抖音短版：1-2分钟，极速卡点版）

### 黄金 3 秒秒吸钩子
- **核心口播**：别再用老办法用 Cursor 了！2026 年了，写代码还要疯狂点 Fix 报错？
- **画面视觉**：`@IntroScene` 红光微闪，大字打出：*"2026 年，你被 AI 智能体套雷了吗？"*

### 快切对比切片（重低音卡点扫盲，约 40 秒）
- **核心口播**：直接看这张大表！Cursor MDC 和 Windsurf Workflows 到底差多少？格式、多步、跨角色，差距就在这几百毫秒的编排里！
- **画面视觉**：`@TableScene` 伴随重低音，快速横向扫描高亮 `win` 行，最紧凑的动画展现差异。

### 高能结论与冲突提示（约 20 秒）
- **核心口播**：记住了，全自动智能体都是忽悠人的，只有用 Rules 订立岗位规矩（Role），套上缰绳，野马才不会跑偏！
- **画面视觉**：`@SplitLayout`。左边野马失控，右边缰绳拉紧，突出结论。

### 结尾极速 CTA（约 5 秒）
- **核心口播**：关注我，明天带你跑具体的 Rules 避坑实战。
- **画面视觉**：画面淡出，打出关注动画。

## Remotion 模版编写工单 (Template extension Ticket)

- **工单号**：`TICKET-ep01-01`
- **模版名称 1**：`TimelineScene`
  * **组件物理路径**：`video/src/template/scenes/TimelineScene.tsx`
  * **所需 Props**：
    ```typescript
    interface TimelineEvent {
      year: string;
      title: string;
      desc: string;
      icon: string;
    }
    interface TimelineSceneProps {
      eyebrow: string;
      title: string;
      events: TimelineEvent[];
    }
    ```
  * **动画规范**：顶部大标题淡入；下方时间轴轴线由左至右渐进延伸；各年份事件卡片伴随 Spring 缩放动画，Emoji 顺次由左至右弹跳浮现。

- **模版名称 2**：`TableScene`
  * **组件物理路径**：`video/src/template/scenes/TableScene.tsx`
  * **所需 Props**：
    ```typescript
    interface TableRow {
      feature: string;
      cursor: string;
      windsurf: string;
      win: 'cursor' | 'windsurf' | 'neutral';
    }
    interface TableSceneProps {
      eyebrow: string;
      title: string;
      headers: string[];
      rows: TableRow[];
    }
    ```
  * **动画规范**：表头首先拉伸展现；各行对比数据自上而下顺次浮现；在第 120 帧，所有 `win !== 'neutral'` 的关键单元格，动态套上一个荧光呼吸边框或微光扫过特效，指明绝对赢家。

## 风险提示

- **版本兼容性**：视频中引用的 Subagents、Bugbot、Security Review 等特性对 2026 年初以前的 Cursor 版本不生效，口播中必须明确强调"请更新到最新版"。
- **抖音版极限压缩**：抖音版台词必须控制在 50 秒以内，画面切片速度极高，对 Remotion 渲染帧稳定性要求高，务必控制组件层级和透明度计算量。
- **技术中立性**：对比表必须基于真实可验证的机制差异（如 .mdc vs .md 格式、Workflows 的多步骤原生支持），避免主观站队引发争议。
- **边界交代**：必须如实呈现 AI 短板——即便有了 Role 约束，Agent 在遇到从未见过的新报错类型时仍可能失控，不能为了传播效果而夸大 Rules 的绝对掌控力。
