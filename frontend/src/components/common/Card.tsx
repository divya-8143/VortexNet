import React from 'react';

interface CardProps {
  children: React.ReactNode;
  className?: string;
  title?: string;
  subtitle?: string;
  action?: React.ReactNode;
}

export const Card: React.FC<CardProps> = ({ children, className = '', title, subtitle, action }) => {
  return (
    <div className={`bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-sm ${className}`}>
      {(title || action) && (
        <div className="flex items-center justify-between mb-4 pb-3 border-b border-slate-800/60">
          <div>
            {title && <h3 className="font-semibold text-slate-100 text-base">{title}</h3>}
            {subtitle && <p className="text-xs text-slate-400 mt-0.5">{subtitle}</p>}
          </div>
          {action && <div>{action}</div>}
        </div>
      )}
      {children}
    </div>
  );
};
