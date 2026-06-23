---
stage: 06-tts-synthesis
status: synthesized
source_workflow: /06-tts-synthesis
---

# ep02 TTS 语音合成记录

逐镜提取 04 脚本各镜头 `voice_slice` 文本，用 **edge-tts**（zh-CN 神经声、免 API Key）逐镜合成，实测每镜时长作为时间真相源回填到 07 时间轴。合成时捕获引擎的 `SentenceBoundary` 时间戳，按字符占比切到子句，生成**绝对毫秒级字幕**（`WordCaption`），同时驱动烧字幕与主持口型（lip-sync）。生成脚本：`OpenMontage/build_ep02_tts.py`。

## 配置

- 语言：zh-CN
- 引擎：**edge-tts**（Microsoft 在线神经 TTS，免 Key；离线/换厂商可改 `tools/audio/*`）
- 默认声音：`zh-CN-XiaoxiaoNeural`（女声，与当前 VRoid 形象匹配；换声：`python build_ep02_tts.py --voice <id>`）
- 命名规范：`assets/<镜头号>.mp3`（如 `1.1.mp3`）+ 合成总轨 `ep02-narration.mp3`

## 素材清单（实测 edge-tts 时长）

| 段 | segment_id | 轨 | 镜头数 | 实测时长 | 口播摘要 | 音频 |
|----|-----------|----|-------|------|---------|------|
| S1 | S1 | A | 3 | 35.2s | 一句话点题 + 数据驱动认知 + 三步路线 | ✅ synthesized |
| S2 | S2 | A | 4 | 35.9s | 把选型丢给 AI，摆出六条路线、同一内核 | ✅ synthesized |
| S3 | S3 | A | 6 | 77.3s | 选型最易翻车：看清每条路的坑，对需求做减法 | ✅ synthesized |
| S4 | S4 | A | 6 | 74.7s | 引擎怎么干活：配置→分发→现成组件，TS 兜底 | ✅ synthesized |
| S5 | S5 | A/B | 3 | 44.8s | SSR 坑与守卫，把规矩固化成 MDC 规则 | ✅ synthesized |
| S6 | S6 | A | 4 | 57.4s | 数字人选型：陪衬定位，选 3D 风格化 VRM | ✅ synthesized |
| S7 | S7 | A | 2 | 28.4s | 三步收束 + 下期预告 | ✅ synthesized |

**合计（实测）：约 353.5 秒（约 5 分 54 秒）**

## 产物

- `assets/<镜头号>.mp3` —— 28 段逐镜 narration 音频。
- `remotion-composer/public/audio/ep02-narration.mp3` —— 合成总轨（07 的 `audio.narration`）。
- `assets/manifest.json` —— 机器可读清单：`provider: edge-tts`、每镜 `start_seconds`/实测 `duration_seconds`/`audio_file`，以及绝对毫秒 `captions[]`。07 组装（`build_ep02_shots_props.py`）读取它把镜头时长换成实测时长、把 captions 注入 Explainer props（烧字幕 + 主持口型）。

## 重生成

```bash
python OpenMontage/build_ep02_tts.py            # 合成音频 + 写 manifest
python OpenMontage/build_ep02_shots_props.py    # 回填时长/字幕/音轨到 ep02-shots.json
```
