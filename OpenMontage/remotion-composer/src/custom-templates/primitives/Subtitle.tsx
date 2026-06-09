import React from 'react';
import {FONT_SIZE, COLORS, RADIUS} from '../theme/tokens';

interface Props {
	text: string;
	// 距底部距离
	bottom?: number;
	maxWidth?: number;
}

// 上屏字幕条：遵守排版规范（≥24px、行高≥1.5），带半透明底衬保证可读性。
export const Subtitle: React.FC<Props> = ({
	text,
	bottom = 80,
	maxWidth = 1400,
}) => {
	return (
		<div
			style={{
				position: 'absolute',
				bottom,
				left: '50%',
				transform: 'translateX(-50%)',
				maxWidth,
				padding: '16px 32px',
				background: 'rgba(0,0,0,0.55)',
				borderRadius: RADIUS.md,
				fontSize: FONT_SIZE.bodyLg,
				lineHeight: 1.5,
				color: COLORS.text.primary,
				textAlign: 'center',
				fontWeight: 600,
				letterSpacing: 0.5,
			}}
		>
			{text}
		</div>
	);
};
