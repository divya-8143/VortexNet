import React from 'react';
import { Card } from '../common/Card';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';

export const NetflowAnalytics: React.FC = () => {
  const protocols = [
    { name: 'HTTPS (443)', value: 55, color: '#0c8ee9' },
    { name: 'HTTP (80)', value: 18, color: '#38bdf8' },
    { name: 'SSH (22)', value: 12, color: '#6366f1' },
    { name: 'DNS (53)', value: 9, color: '#10b981' },
    { name: 'BGP (179)', value: 6, color: '#f59e0b' },
  ];

  return (
    <Card title="Traffic Protocol Distribution" subtitle="NetFlow v9 application breakdown">
      <div className="h-64 w-full flex items-center justify-between">
        <ResponsiveContainer width="60%" height="100%">
          <PieChart>
            <Pie data={protocols} cx="50%" cy="50%" innerRadius={50} outerRadius={80} paddingAngle={5} dataKey="value">
              {protocols.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.color} />
              ))}
            </Pie>
            <Tooltip contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155' }} />
          </PieChart>
        </ResponsiveContainer>
        <div className="w-[40%] space-y-2 text-xs font-mono">
          {protocols.map((p) => (
            <div key={p.name} className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: p.color }}></span>
                <span className="text-slate-300">{p.name}</span>
              </div>
              <span className="font-bold text-slate-100">{p.value}%</span>
            </div>
          ))}
        </div>
      </div>
    </Card>
  );
};
