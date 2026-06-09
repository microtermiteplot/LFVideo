---
description: 内容策划 - 基于标题进行技术调研与多方案判断层对比，选定技术路线与待验证假设，最终完成分镜导演大纲与结构化策划案。
---

# 内容策划 Workflow (02-content-planning)

本工作流用于连接**战略选题（01）**与**B站视听编排（03）**，由内容策划师完成技术选型、判断层多方案对比、技术路线锁定，并生成视频的“故事大纲与分镜导演策划”。

---

## 前置依赖与目录初始化

本工作流接收上游选题成果。需要具备：
- 确定的视频选题或已经定稿的候选标题（如来自 `01-topic-research` 的选择）
- 目标：围绕该标题进行深度技术调研并产出分镜导演案

### 🚀 目录脚手架初始化命令 (Bootstrap)
在启动本阶段前，由 AI 或人工运行以下命令，为该期（如 `epNN-slug`）初始化标准多文件目录：
```powershell
$slug = "ep02-video-render" # 替换为当前期的 Slug
New-Item -ItemType Directory -Path "content-library/$slug/01-topic", "content-library/$slug/02-plan", "content-library/$slug/04-distribute" -Force
New-Item -ItemType File -Path "content-library/$slug/01-topic/README.md", "content-library/$slug/02-plan/README.md", "content-library/$slug/02-plan/tutorial.md", "content-library/$slug/CONTENTLIB.md", "content-library/$slug/03-assembly.md" -Force
```

如果上游缺失标题，请提示用户先执行 `/01-topic-research`。

---

## 步骤

### 1. 加载协同角色与技术底座

1. 读取 `shared/roles/content/strategist(内容策划师).md` 文件，理解“技术调研驱动型内容架构师”的定位和五阶段交互协议。
2. **【核心前置动作】强制读取架构决策 (TAD)**：
   - 检查并读取本期目录下的 `CONTENTLIB.md`（或全局决策库 `content-library/_decisions/`），加载核心技术大纲。
   - **严格遵守 TAD-01（人录 B-Rail 真实录屏 + OpenMontage 模块编译器）**，绝对禁止在脚本中凭空脑补纯 AIGC 的画面。

### 2. 执行阶段 1：标题解析与技术关联提取 (Title Decomposition)

1. **输入分析**：接收用户选定的标题。
2. **技术拆解**：
   - 拆解标题中的**核心技术名词**（如 Remotion、Cursor、Whisper 等）。
   - 提取标题隐含的**技术维度**（如视频生成、字幕同步、渲染优化、代码驱动等）。
   - 推断**目标受众的技术栈背景**（如 React/Python 开发者、AI 工具使用者）。
3. **输出**：在对话中输出《标题解析报告》（技术关联清单 + 调研方向建议），并请求用户确认或补充。

### 3. 执行阶段 2：开源落地方案调研 (Landscape Research)

1. **自动搜索**：基于阶段 1 确认的技术关联清单，使用 `search_web` 工具在互联网搜索（或由用户粘贴补充）。
2. **方案收集**：收集每个核心技术维度的**开源方案/GitHub 项目/社区优秀实践**。
3. **关键数据**：记录项目名、GitHub Star 数、核心功能、集成复杂度、中文文档与教程丰富度。
4. **输出**：在对话中展示结构化的《开源落地方案调研报告》，提示用户是否需要补充其他备选方案。

### 4. 执行阶段 3：判断层对比矩阵 (Judgment-Layer Comparison)

> 核心护城河：拒绝中立的技术综述，强制提取判断层决策信息。

1. **建立矩阵**：对阶段 2 收集 of 方案进行多维度打分与深度对比。
2. **判断层四要素提取**：对每个关键方案强制标注：
   - **适用场景**：什么前提下该方案才成立？
   - **不适用场景**：哪些情况下会翻车？
   - **已知坑**：真实踩坑点（如 Remotion 的 SSR 渲染限制、本地 Whisper 的 GPU 依赖等）。
   - **验收标准**：怎么判断该方案在实际场景里算“跑通了”？
3. **证据状态标注**：明确标注每项信息的证据状态为 `paper_spec`（纸面假设）或 `verified`（已验证）。
4. **输出与中间评审 (Review Gate)**：
   - 在对话中展示《判断层对比矩阵表》与推荐技术路线排序。
   - **强制触发中间确认**：请求用户进行技术决策确认（评审推荐路线、判定坑点与验收标准是否符合实际）。
   - **根据用户反馈修正**：若用户对路线有异议，需立即调整对比打分或补充调研，直到用户拍板“无异议，同意进入软文撰写”。

### 5. 执行阶段 4：技术教程软文撰写 (Tutorial Content Creation)

> 核心变革：拒绝平庸的故事脑补。将阶段 1-3 的技术拆解、开源扫描、对比矩阵全部整合，以该视频选定的技术路线为基础，撰写一篇高强度、面向程序员的、具备实际项目落地指导意义的**企业级硬核教学落地软文**。该软文将作为整期视频的核心灵魂与信息唯一真相源。

1. **内容整合**：结合阶段 3 锁定的技术路线。
2. **深度拆解**：文章中需详细叙述本项目的实施逻辑（或逻辑实施路线）、核心架构、代码组织方式、Cursor Prompt 提示词链和人机避坑配置。
3. **输出与确认**：在对话中展示完整的《技术教学软文草稿》，并请求用户进行内容和技术真实性校对。

### 6. 执行阶段 5：分镜提取与物理落盘拆分 (Synthesis & Storyboarding)

基于用户确认的教学软文，执行“内容提取”与“物理文件拆分落盘”：
1. **物理文件 A：`tutorial.md` (故事与软文线)**：
   - 将阶段 4 定稿的教学软文写入该期目录下的 `02-plan/tutorial.md`。
2. **物理文件 B：`README.md` (视频分镜与校验线)**：
   - 提取软文中的核心步骤，转化为 5 段式视频结构大纲（每段明确 **Beat Type** 叙事节奏与 **Visual Priority** 视觉焦点）。
   - 包含画面配比、视觉模式（Visual Mode 预选）和待验证假设清单。
   - 包含符合 `shared/schemas/02-plan.schema.json` 规范的 ` ```json ` 结构化校验块。
   - 写入该期目录下的 `02-plan/README.md`。
3. **状态与看板变更**：
   - `02-plan/README.md` 头部 frontmatter 设置 `status: draft`。
   - 将 `content-library/PIPELINE.md` 看板中的 02 策划状态列置为 `draft`。

### 7. ~~触发判断层评审门 (Review Gate)~~ ⏸️ 已挂起（暂停使用）

> ⚠️ **判断层评审门已挂起**：判断层评审（CHAI 质量门）已暂时从流程中移除，本阶段无需调用 `/meta/judgment-layer(判断层评审)`。
> 完成 Schema 校验并自查无误后，可直接将 `content-library/PIPELINE.md` 看板中该期 02 策划列置为 `approved`，然后执行 `/03-video-planning-bilibili` 进入 B站视听编排阶段。
> 恢复方法：删除本节的"已挂起"标记与本提示，并取消下方注释块的注释即可还原评审门。

<!-- 判断层评审门（已挂起，恢复时取消本块注释）
提示用户：
> “技术调研驱动的内容策划已落盘归档至 `02-plan/README.md`，并生成了待验证假设清单。
> 请通过调用 `/meta/judgment-layer(判断层评审)` 对本产物进行首轮 CHAI 规则质量评审。
> 评审通过且看板标为 `approved` 后，可执行 `/03-video-planning-bilibili` 进入 B站视听编排阶段。”
-->


---

## 关联文件

- 角色：`shared/roles/content/strategist(内容策划师).md`
- 上游：`01-topic-research (选题分析).md`
- 下游：`03-video-planning-bilibili (B站视听策划).md`
- 校验：`shared/schemas/02-plan.schema.json`
