# 角色体系（Roles）

> 这是 ai-ide-workflows 项目的内部角色库，遵循"**先自用后内容化**"的演进策略。
> 完整设计思路见 [Project Context (项目上下文).md](../../Project%20Context%20(%E9%A1%B9%E7%9B%AE%E4%B8%8A%E4%B8%8B%E6%96%87).md) | 内容化时间表见 [Content Plan (内容计划).md](../../Content%20Plan%20(%E5%86%85%E5%AE%B9%E8%AE%A1%E5%88%92).md)

---

## 设计哲学

**角色 = 思考视角；Agent = 执行能力；两者结合 = 真正的工作流。**

每个角色是一个 Markdown 文件，定义了：

- **身份与立场**（用什么视角思考）
- **核心能力**（擅长做什么）
- **工作流程**（输入→处理→输出）
- **输出格式**（结构化模板）
- **边界**（绝不做什么）
- **可直接复制的 Prompt**

---

## 演进路线

| 阶段 | 时间 | 形态 | 调用方式 |
|------|------|------|---------|
| **阶段1（当前）** | 第1-3期期间 | 纯 Markdown 模板 | 手动复制 Prompt 到 Cursor/Windsurf |
| **阶段2** | 第4-6期期间 | `.cursor/rules/` 集成 | 项目内自动加载，@角色名 调用 |
| **阶段3** | 第7期后 | 工作流编排 | 一个任务自动流转多角色 |

**当前阶段：阶段1**。所有角色都通过手动复制 Prompt 使用。

---

## 角色清单

### 视频生产线（5个）

| 角色 | 何时使用 | 状态 |
|------|---------|------|
| [选题分析师](./content/topic-analyst(选题分析师).md) | 选题可行性判断、标题候选、受众与传播分析 | ✅ 可用 |
| [内容策划师](./content/strategist(内容策划师).md) | 导演分镜、Demo 设计、故事大纲（苏格拉底协同） | ✅ 可用 |
| [视听策划师](./content/visual-planner(视听策划师).md) | Remotion 组件映射、Props 接口、动画 Cue、录屏 zoom 指令 | ✅ 可用 |
| [文案撰稿人](./content/copywriter(文案撰稿人).md) | 视频脚本、知乎文章、小红书图文 | ✅ 可用 |
| [视频工程师](./content/motion-engineer(视频工程师).md) | 用 Remotion 把脚本组装成片（A/B 两轨） | ✅ 可用 |
| [字幕编辑](./content/subtitle-editor(字幕编辑).md) | Whisper字幕校对、时间轴整理 | 🚧 占位 |
| [分发助手](./content/distributor(分发助手).md) | 各平台标题/描述/标签 + 短视频切片策略 | ✅ 可用 |

### 实战内容线（4个）

| 角色 | 何时使用 | 状态 |
|------|---------|------|
| [产品经理](./execution/product-manager(产品经理).md) | 需求拆解、MVP边界、验收标准 | 🚧 占位 |
| [架构师](./execution/architect(架构师).md) | 技术方案、风险评估（不写代码） | 🚧 占位 |
| [执行工程师](./execution/engineer(执行工程师).md) | 真正改文件、跑命令的 Agent 模式 | 🚧 占位 |
| [代码审查员](./execution/reviewer(代码审查员).md) | 改完后的检查、风险点提示 | 🚧 占位 |

### 通用判断层（1个）

| 角色 | 何时使用 | 状态 |
|------|---------|------|
| [判断层评审](./meta/judgment-layer(判断层评审).md) | 遵循 CHAI 规则与漏洞决策树的硬核质量门角色 | ✅ 可用 |

---

## 如何使用（阶段1）

1. 打开你需要的角色 `.md` 文件
2. 复制最底部 "调用Prompt" 部分
3. 粘贴到 Cursor / Windsurf 的对话框
4. 替换 `{{占位符}}` 为具体内容
5. 发送

**示例**：

```text
你现在扮演内容策划师。

任务：分析以下选题是否值得做成一期视频。
选题：「Cursor 做 PPT 能不能替代 Gamma」

请按你的工作流程输出。
```

---

## 添加新角色的红线

为了避免角色膨胀，**新增角色必须满足**：

1. **有明确触发场景**（至少3个真实使用案例）
2. **不能被现有角色覆盖**
3. **有独立的输出格式约束**

否则，优先用现有角色 + 任务上下文解决。

---

## 质量门与契约校验

为降低人机协作中的信息衰减并强制保障“操作层 + 判断层 + AI局限点”内容质量，本角色体系在 L0.5 阶段深度融合了 JSON Schema 契约校验与 CHAI 规则质量门。

### 1. 契约校验 (JSON Schema)
在每个阶段工作流执行完毕并产出 Markdown README 时，末尾必须包含一个 ` ```json ` 结构块，该结构块会被以下 Schema 物理校验：
- **选题阶段 (01)**：[`shared/schemas/01-topic.schema.json`](../schemas/01-topic.schema.json)（强制要求 `ai_limitations` 和 `judgment_layer`）
- **策划阶段 (02)**：[`shared/schemas/02-plan.schema.json`](../schemas/02-plan.schema.json)（强制要求 `demo_design.pitfalls_to_expose`）
- **B站视听编排阶段 (03)**：[`shared/schemas/03-plan-bilibili.schema.json`](../schemas/03-plan-bilibili.schema.json)（强制要求 `video_spec`, `scene_storyboards`, `zoom_crop_directives`）
- **脚本阶段 (04)**：[`shared/schemas/04-script.schema.json`](../schemas/04-script.schema.json)（强制要求 `judgment_layer_coverage` 等）

### 2. 终审质量门 (CHAI 评审员)
每个阶段落盘为 `draft` 后，必须调用 [判断层评审](./meta/judgment-layer(判断层评审).md) 角色。
该角色依据 **CHAI 规则**（准确、完整、建设性）对草稿进行审计，漏洞严重度分为 `[CRITICAL]` / `[SUGGESTION]` / `[NITPICK]`。
- **放行条件 (approved)**：必须 Schema 校验通过 且 评审结果为 **0 [CRITICAL] 漏洞** (获得 **PASS**)，才允许在 [`content-library/PIPELINE.md`](../../content-library/PIPELINE.md) 看板中将该阶段置为 `approved`。

---

## 内容化时间表

| 期数 | 与角色体系的关系 |
|------|----------------|
| 第1期 | 讲三层认知（Editor/Agent/Role），不展示具体角色 |
| 第2期 | 演示"内容策划师 + 执行工程师"两角色协作 |
| 第3期 PPT | 实操中暴露使用了"产品经理→架构师→执行工程师"流程 |
| 第8期 内部工具 | 角色体系作为工具的底层支撑 |
| 第9期 用代码生成视频 | 讲视频工程师 + Remotion 如何自动化后期 |
| 第10期 总结 | **完整公开整套角色库** |
