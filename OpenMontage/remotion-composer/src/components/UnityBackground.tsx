import React from "react";
import { AbsoluteFill, staticFile } from "remotion";

export interface UnityBackgroundConfig {
  /** Toggle the Unity WebGL background layer. */
  enabled?: boolean;
  /**
   * public/-relative path to the Unity WebGL build's index.html.
   * Example: "UnityBG/index.html" → public/UnityBG/index.html.
   */
  src?: string;
}

/**
 * Bottom-most layer: a live Unity WebGL build embedded via <iframe>.
 *
 * The Unity build is served as a static asset from public/, so its own
 * index.html bootstraps the Unity loader and resolves Build/* relative to the
 * iframe URL — no path rewriting needed.
 *
 * NOTE: this renders in real time inside the browser (Remotion Studio preview,
 * or any live playback). It is NOT frame-deterministic, so a headless
 * `remotion render`/`remotion still` will not capture it reliably. For a
 * deterministic MP4 export, pre-render the Unity scene to a video file and use
 * a normal background video layer instead.
 */
export const UnityBackground: React.FC<UnityBackgroundConfig> = ({
  enabled = true,
  src = "UnityBG/index.html",
}) => {
  if (!enabled) return null;

  return (
    <AbsoluteFill style={{ zIndex: 0, pointerEvents: "none", background: "transparent" }}>
      <iframe
        src={staticFile(src)}
        title="UnityBG"
        scrolling="no"
        style={{
          width: "100%",
          height: "100%",
          border: "none",
          display: "block",
        }}
      />
    </AbsoluteFill>
  );
};
