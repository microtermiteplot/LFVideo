# AI IDE Workflows 项目架构设计 (Project Architecture)

本项目采用 **“全收敛单运行时 (Fully Converged Single-Runtime)”** 架构体系。我们将精品教程的视觉组件（如 Timeline、Table）完全融入 OpenMontage 内部，并将 OpenMontage 内置渲染器升级至最新的 React 19 / Remotion 4.0.470 协议，从而达到极简的数据闭环与工业级全自动声画同步。

---

## 1. 物理目录拓扑 (Physical Directory Topology)

```
ai-ide-workflows/ (项目根目录)
├── .windsurf/ workflows/       # Windsurf Workflows 原生编排规则
├── shared/                     # 跨 IDE 共享资源
│   ├── roles/                  # 核心角色定义 (Single Source of Truth)
│   └── schemas/                # L0.5 严苛双核校验的 JSON Schema
├── content-library/            # 内容库 (按 epNN 分类，纯净不含 React 模板代码)
│   └── ep02-video-render/      # 视频生产全生命周期文件 (01-07 阶段)
└── OpenMontage/                # [单运行时核心] Python 生产流水线与 React 19 渲染双引擎
    ├── tools/                  # 屏幕录制、音轨合成、AI 语音字幕工具 (Python)
    └── remotion-composer/      # React 19 / Remotion 4.0.470 全功能渲染器 (合并了我们所有的自定义场景)
```

---

## 2. 单运行时收敛设计 (Converged Single Runtime)

通过将外部独立视频工程并入 OpenMontage，我们消除了两个运行时（React 18 vs React 19）的版本代差，获得了统一的高效生产力：

| 维度 | `OpenMontage/remotion-composer/` (升级合并后) |
|:---|:---|
| **React 版本** | **React 19.2.6** (全线升级) |
| **Remotion 版本** | **4.0.470** (全线升级) |
| **组件特性** | 通用 Explainer 模板 (数据图表、ProgressBar) + 精品教程模板 (TimelineScene、TableScene) 共存 |
| **主打场景** | 全片自动化渲染卡点、口播配音合成、GitHub 开源精品 React 模板库 |

### 收敛决策的核心优势
1. **100% 自动卡点**：直接利用 OpenMontage 内置的语音逆向对齐（TTS + WhisperX word-level 时间戳），React 场景自动根据音频长度适配帧数，彻底解决**长场景死时间、画音不同步**等质量硬伤。
2. **零启动开销**：我们无需从头手写打字机（TerminalScene）、页面局部放大（ScreenshotScene）、产品宣传卡（ProductReveal）等基础工程组件，直接调用 OpenMontage 成熟的高质量基础件作为杠杆。
3. **极速调试 (DX)**：在 `OpenMontage/remotion-composer/` 目录下运行 `npm run start` 即可在本地启动 Remotion Studio。在开发时，它同时支持通过 `cuts[i].type` 渲染我们移植进去的五大自定义精品场景（Intro, Outro, Concept, Timeline, Table）。

---

## 3. 全自动流水线数据流 (Automated Pipeline Data Flow)

```
[1. 口播脚本 Markdown]
         │
         ▼
[2. OpenMontage TTS 语音生成] ──► 生成 scene_N.mp3 分段音轨
         │
         ▼
[3. WhisperX 时间戳提取]      ──► 提取精确到单词/字级的 millisecond 标记
         │
         ▼
[4. Verify Scene Pacing]      ──► 自动匹配口播时间与 React 动作物理时长，报错拦截静死屏
         │
         ▼
[5. Remotion 自动渲染]        ──► npx remotion render Explainer --props .remotion_props.json
         │
         ▼
     [ 4K MP4 完片 ]
```

---

## 4. 单一事实源原则 (Single Source of Truth)

- **角色定义**：所有角色（如 `copywriter`, `strategist`）仅在 `shared/roles/` 维护一份 Markdown 文件。
- **IDE 适配**：
  - **Cursor**：通过 `.cursor/rules/*.mdc` 进行被动约束，仅做**路径指向与适配**，不复制角色内容。
  - **Windsurf**：通过 `.windsurf/rules/` 与 `.windsurf/workflows/*.md` 进行主动编排，同样采用软链接/相对引用指向 `shared/roles/`。
