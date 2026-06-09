# Remotion 视频模板与分镜规范 (Remotion Specification)

本规范定义了当前 Remotion 工程（`video/`）中已经实现、可直接调用的 UI 组件、场景与动画能力。
在进行 **02 内容策划**与 **04 脚本撰写**时，必须**100% 严格遵守本规范进行画面设计**，确保 AI 编写的脚本画面在本地“一键可渲染”，杜绝幻想不切实际的特效。

---

## 1. 核心设计原则

1. **Remotion 原生组件优先**：
   - 所有“概念解释”、“理论模型”、“金字塔图”等，优先使用已有的组件（如 `@ConceptScene` 或 `@SplitLayout`）以 2D 卡片、Emoji、纯文字排版展现。
   - **绝对禁止**幻想着写出：*“一匹 3D 马在代码荒野狂奔”、“金字塔模型从土里破土而出”* 等复杂特效。这些必须降维设计为 `@ConceptScene` 里的 2D 卡片加对应的 Emoji。
2. **B 轨外部资产占位显式标注**：
   - 凡是 Remotion 代码无法生成的画面（如：Cursor 真实界面截图、报错弹窗截图、人声口播 mp4、执行代码的终端录屏），必须在脚本中用 **`[B 轨占位：请用户提供 screen_error.png/mp4]`** 的格式显式标出，提醒用户后期补充。

---

## 2. 现成可用组件库清单

目前在 `video/src/template/` 下已封装好的、可一键在数据源 `data.ts` 里配置的组件：

### 2.1 基础场景组件 (Scenes)

*   **`@IntroScene` (片头场景)**
    *   **作用**：大字报开场，15秒内抓人眼球。
    *   **参数**：
        *   `title`: 主标题（建议 900 粗体，字号大，如 `FONT_SIZE.display`）
        *   `subtitle`: 副标题（选填）
        *   `background`: 背景类型（可选 `'particles' | 'gradient' | 'grid'`）
*   **`@OutroScene` (片尾场景)**
    *   **作用**：结尾呼吁订阅 (CTA)。
    *   **参数**：
        *   `headline`: 主文案（如“关注我们，一起变强”）
        *   `cta`: 按钮内文案（默认“关注 · 一起验证 AI IDE 的真实能力”）
        *   `background`: 背景类型（默认 `'gradient'`）
*   **`@ConceptScene` (概念解释场景 - 核心！)**
    *   **作用**：最常用的概念拆解、认知框架、三层用法讲解。
    *   **参数**：
        *   `eyebrow`: 小标题（如“AI IDE 三层认知”）
        *   `title`: 大标题
        *   `background`: 背景类型（默认 `'gradient'`）
        *   `items`: 概念卡片数组（最大支持 3 个，超出会溢出），每个 Item 包含：
            *   `label`: 卡片分类（如 `EDITOR`）
            *   `title`: 卡片小标题（如 `编辑模式`）
            *   `desc`: 卡片具体描述（如 `手拿螺丝刀，你指哪它改哪`）
            *   `icon`: 卡片左侧图标（**必须使用 Emoji 字符**，如 🔧, 🐴, 缰）

### 2.2 基础布局组件 (Primitives)

*   **`@SplitLayout` (分屏组件)**
    *   **作用**：画面一分为二（如：左边讲理论，右边放录屏；或者左边 Agent 原地打转，右边 Rules 约束运行）。
    *   **参数**：
        *   `direction`: 分屏方向（`'horizontal'` 左右分，`'vertical'` 上下分，默认 `'horizontal'`）
        *   `ratio`: 左/上侧占比（0-1，默认 `0.5` 对半开）
        *   `left`: 左/上侧渲染的 React 节点（可放入 `@VideoSlot` 或文本）
        *   `right`: 右/下侧渲染的 React 节点
*   **`@VideoSlot` (视频插槽/画中画)**
    *   **作用**：嵌入外部录制的 mp4/png 资产（如口播视频、实操录屏、静态截图）。支持淡入与缩放动画。
    *   **参数**：
        *   `src`: 资源路径（如 `./assets/screen_recording.mp4`）
        *   `position`: 位置（`'fill'` 填满分屏，`'left'` / `'right'` 居侧，`'top-left'` 等四角，默认 `'bottom-right'`）
        *   `width`: 画中画宽度（单位 px，在 `fill` 模式下被忽略，默认 `420`）
        *   `rounded`: 是否有圆角（默认 `true`）
*   **`@AnimatedBackground` (动态背景)**
    *   **可选 Variant**：
        *   `'gradient'`: 随时间缓慢变色的漂移流动渐变背景（暗色系，不刺眼）。
        *   `'grid'`: 暗色科技感静态网格，随时间缓慢对角平移。
        *   `'particles'`: 科技感浮动微光粒子背景，适合开场。

---

## 3. 在 02 策划与 04 脚本中的落地指令

1. **画面描述必须使用组件代号**：
   在编写脚本 `@/content-library/<epNN-slug>/04-script/video.md` 中的 `[画面]` 时，必须以以下格式指明调用的组件和具体参数：
   ```markdown
   - **[画面]** 引入 `@ConceptScene`。参数 eyebrow="三层用法", title="核心认知框架", items=[1. "Editor/编辑模式/🔧 适合5%微调", 2. "Agent/智能体模式/🐴 自动多步执行", 3. "Role/角色模式/🕸️ 约束与规矩"]
   ```
2. **无法自动渲染的画面必须标注替换提醒**：
   ```markdown
   - **[画面]** 引入 `@SplitLayout`。左侧 `@VideoSlot(position="fill", src="agent-loop.mp4")` [B轨替换提醒：请用户在此补充 Agent 报错死循环录屏]，右侧 `@VideoSlot(position="fill", src="rule-pass.mp4")` [B轨替换提醒：请用户在此补充加入 Rule 后一次性跑通的录屏]
   ```

---

## 4. 如何节约 Token？

- 当 Cascade 扮演 **02内容策划师** 或 **04文案撰稿人** 时，工作流会强制通过 `@read_file` 读取本文件 `@/shared/docs/remotion-spec.md`。
- **这极大地节约了 Token**：AI 脑中拥有了精准的组件蓝图，不再需要你在 prompt 里重复解释“我们有哪些组件，怎么写才不会报错”，大幅降低了每次聊天的上下文体积。
