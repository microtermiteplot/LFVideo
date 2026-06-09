---
stage: 05-video-assembly
status: draft
source_workflow: /05-video-assembly
---

# ep01 视频组装记录

## Remotion 资源

- **数据**: `video/src/episodes/ep01-cursor-windsurf/data.ts`
- **组装**: `video/src/episodes/ep01-cursor-windsurf/Episode.tsx`
- **Composition id**: `ep01-cursor-windsurf`
- **时长**: 660 帧 @ 30fps（22 秒）

## 场景编排

| 序列 | 场景 | 时长 | 背景 | 用途 |
|------|------|------|------|------|
| 1 | IntroScene | 90f | particles | 开头黄金钩子 |
| 2 | TimelineScene | 180f | grid | 纵向进化史 |
| 3 | TableScene | 180f | gradient | 横向硬核对比 |
| 4 | ConceptScene | 120f | grid | 判断层避坑 |
| 5 | OutroScene | 90f | particles | 结尾 CTA |

## B 轨画中画占位（待补充录屏素材）

| 位置 | 素材路径 | 内容 | 对应段落 |
|------|----------|------|----------|
| IntroScene 右下角 | `ep01-assets/fix-loop-pain.mp4` | IDE 死循环报错录屏 | 第一段 |
| TableScene 右下角 | `ep01-assets/workflow-demo.mp4` | Windsurf Workflow 多步骤编排 | 第三段 |
| ConceptScene 右下角 | `ep01-assets/rules-config.mp4` | Rules 配置界面实操 | 第四段 |

## A 轨试跑验证

- TypeScript 编译：通过
- 字号规范：合规（最小 24px）
- Studio 预览：可用（`npm run studio`）
- 16:9 横版渲染：待执行

## 渲染命令

```bash
# 16:9 横版主成片（B站）
npm run render
```

## 成片输出

- 16:9: `video/out/ep01.mp4`（待生成）
