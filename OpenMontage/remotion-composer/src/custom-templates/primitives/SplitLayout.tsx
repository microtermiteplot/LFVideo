import React from 'react';
import {AbsoluteFill} from 'remotion';
import {SPACING} from '../theme/tokens';

interface Props {
	left: React.ReactNode;
	right: React.ReactNode;
	// 左侧占比 0-1，默认对半
	ratio?: number;
	// 方向：horizontal 左右分屏，vertical 上下分屏
	direction?: 'horizontal' | 'vertical';
	gap?: number;
	padding?: number;
}

export const SplitLayout: React.FC<Props> = ({
	left,
	right,
	ratio = 0.5,
	direction = 'horizontal',
	gap = SPACING.lg,
	padding = SPACING.gutter,
}) => {
	const isH = direction === 'horizontal';
	return (
		<AbsoluteFill
			style={{
				flexDirection: isH ? 'row' : 'column',
				gap,
				padding,
			}}
		>
			<div style={{flex: ratio, minWidth: 0, minHeight: 0}}>{left}</div>
			<div style={{flex: 1 - ratio, minWidth: 0, minHeight: 0}}>{right}</div>
		</AbsoluteFill>
	);
};
