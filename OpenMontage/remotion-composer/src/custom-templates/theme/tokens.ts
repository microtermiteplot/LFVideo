// 设计令牌：所有组件共享的视觉规则。修改这里，全片统一生效。

// ---- 字号阶梯（1920×1080 基准）----
// 规范：任何可见文字不得小于 MIN（见 motion-engineer 角色排版规范）
export const FONT_SIZE = {
	min: 24, // 硬下限，标注/角标也不得低于此
	caption: 24, // 角标、来源、序号
	body: 28, // 正文、描述
	bodyLg: 32, // 强调正文
	subtitle: 36, // 段落标题、卡片标题
	title: 48, // 场景标题
	display: 72, // 全屏主标题、片名
} as const;

// ---- 颜色 ----
export const COLORS = {
	bg: {
		from: '#0F172A',
		to: '#1E293B',
	},
	text: {
		primary: '#F8FAFC',
		secondary: '#94A3B8',
		muted: '#64748B',
	},
	accent: ['#4F9CF9', '#A78BFA', '#34D399', '#FBBF24'] as const,
	line: 'rgba(255,255,255,0.08)',
	surface: 'rgba(255,255,255,0.04)',
} as const;

// ---- 间距 ----
export const SPACING = {
	xs: 8,
	sm: 16,
	md: 28,
	lg: 44,
	xl: 80,
	gutter: 140, // 全屏左右安全边距
} as const;

// ---- 圆角 ----
export const RADIUS = {
	sm: 12,
	md: 16,
	lg: 20,
	pill: 999,
} as const;

// ---- 动画默认参数 ----
export const SPRING = {
	gentle: {damping: 20, stiffness: 100, mass: 1},
	snappy: {damping: 18, stiffness: 120, mass: 0.8},
} as const;
