# Content Library（生产成品库）

> 人工审核后的**定稿内容**，每期一个文件夹，按 4 个 workflow 阶段归档。未定稿的脑暴放 `../ideas/`。

## 目录结构

```
content-library/
├── PIPELINE.md              # 全局看板：所有期 × 各阶段状态
├── _decisions/              # 跨期技术/策略决策
└── epNN-slug/               # 每期一个独立的模块化文件夹
    ├── 01-topic/
    │   └── README.md        # 选题分析与模版评估报告（workflow 01）
    ├── 02-plan/
    │   ├── README.md        # 视频5段分镜大纲与 JSON 格式校验块（workflow 02）
    │   └── tutorial.md      # 企业级硬核技术教学落地软文（workflow 02 核心灵魂）
    ├── CONTENTLIB.md        # 本期专属：技术架构决策（TAD）与 OpenMontage 模块适配图
    ├── 03-assembly.md       # 组装记录，链接 video/ 与 remotion-composer/（workflow 03）
    └── 04-distribute/       # 分发文案，按平台分（workflow 04）
        ├── bilibili.md
        ├── xiaohongshu.md
        └── zhihu.md
```

## 阶段文件 frontmatter

每个阶段文件头标注状态，与 `PIPELINE.md` 看板对应：

```yaml
---
stage: 01-topic
status: approved        # todo / draft / reviewed / approved
source_workflow: /01-topic-research
---
```

## 工作规则

- 看板 `PIPELINE.md` 是进度唯一真相，每推进一阶段必须更新。
- 上一阶段 `approved` 才允许产出下一阶段（L0 全人工审核）。
- 决策类文档放 `_decisions/`，不绑定单期。

## 当前期

- **ep02-video-render** — 渲染引擎：代码即视频 + 流程即代码（推进到 08 字幕 `draft`，见 [PIPELINE.md](./PIPELINE.md)）

## Meta

- [为什么放弃 HyperFrames，使用 Remotion](./_decisions/why-remotion-over-hyperframes.md)

---

*选题路线见 [Content Plan (内容计划).md](../Content%20Plan%20(内容计划).md)，脑暴库见 [ideas/](../ideas/)*
