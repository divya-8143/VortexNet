import React from 'react';

interface BadgeProps {
  children: React.ReactNode;
  variant?: 'online' | 'offline' | 'warning' | 'critical' | 'info' | 'default';
  size?: 'sm' | 'md';
}

export const Badge: React.FC<BadgeProps> = ({ children, variant = 'default', size = 'sm' }) => {
  const variantStyles = {
    online: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30',
    offline: 'bg-slate-800 text-slate-400 border-slate-700',
    warning: 'bg-amber-500/10 text-amber-400 border-amber-500/30',
    critical: 'bg-rose-500/10 text-rose-400 border-rose-500/30',
    info: 'bg-brand-500/10 text-brand-400 border-brand-500/30',
    default: 'bg-slate-800 text-slate-300 border-slate-700',
  };

  const sizeStyles = {
    sm: 'text-xs px-2 py-0.5',
    md: 'text-xs px-2.5 py-1 font-semibold',
  };

  return (
    <span className={`inline-flex items-center gap-1.5 rounded-full border font-mono ${variantStyles[variant]} ${sizeStyles[size]}`}>
      {children}
    </span>
  );
};
