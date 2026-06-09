import React from 'react';
import {
	AbsoluteFill,
	interpolate,
	spring,
	useCurrentFrame,
	useVideoConfig,
} from 'remotion';
import {AnimatedBackground} from '../primitives';
import type {BackgroundVariant} from '../primitives';
import {COLORS, FONT_SIZE, SPACING, RADIUS} from '../theme/tokens';
import {FONT_FAMILY} from '../theme/fonts';

interface Props {
	headline: string;
	cta?: string;
	background?: BackgroundVariant;
}

export const OutroScene: React.FC<Props> = ({
	headline,
	cta = '关注 · 一起验证 AI IDE 的真实能力',
	background = 'gradient',
}) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	const enter = spring({fps, frame, config: {damping: 20, stiffness: 90}});
	const opacity = interpolate(enter, [0, 1], [0, 1]);
	const translateY = interpolate(enter, [0, 1], [30, 0]);

	return (
		<AnimatedBackground variant={background}>
			{/* Inject Pulsing Keyframes */}
			<style>{`
				@keyframes button-pulse {
					0% { box-shadow: 0 8px 30px -4px rgba(79, 156, 249, 0.4); transform: scale(1); }
					50% { box-shadow: 0 8px 35px 4px rgba(167, 139, 250, 0.6); transform: scale(1.03); }
					100% { box-shadow: 0 8px 30px -4px rgba(79, 156, 249, 0.4); transform: scale(1); }
				}
			`}</style>

			<AbsoluteFill
				style={{
					fontFamily: FONT_FAMILY,
					justifyContent: 'center',
					alignItems: 'center',
					textAlign: 'center',
					opacity,
					transform: `translateY(${translateY}px)`,
				}}
			>
				{/* Glowing ambient background circle */}
				<div
					style={{
						position: 'absolute',
						width: 500,
						height: 200,
						borderRadius: '50%',
						background: 'radial-gradient(circle, rgba(167, 139, 250, 0.08) 0%, transparent 70%)',
						filter: 'blur(70px)',
						zIndex: 0,
						pointerEvents: 'none',
					}}
				/>

				<div
					style={{
						fontSize: FONT_SIZE.title + 4,
						fontWeight: 900,
						color: COLORS.text.primary,
						marginBottom: SPACING.xl,
						maxWidth: 1400,
						lineHeight: 1.25,
						letterSpacing: -0.5,
						zIndex: 1,
					}}
				>
					{headline}
				</div>
				<div
					style={{
						fontSize: FONT_SIZE.subtitle,
						fontWeight: 700,
						color: COLORS.text.primary,
						padding: `${SPACING.sm + 4}px ${SPACING.xl}px`,
						borderRadius: RADIUS.pill,
						background: `linear-gradient(135deg, ${COLORS.accent[0]} 0%, ${COLORS.accent[1]} 100%)`,
						animation: 'button-pulse 3.5s infinite ease-in-out',
						letterSpacing: 1.5,
						zIndex: 1,
						border: '1px solid rgba(255,255,255,0.1)',
					}}
				>
					{cta}
				</div>
			</AbsoluteFill>
		</AnimatedBackground>
	);
};
