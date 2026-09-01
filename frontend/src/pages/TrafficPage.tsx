import React from 'react';
import { NetflowAnalytics } from '../components/traffic/NetflowAnalytics';
import { Card } from '../components/common/Card';

export const TrafficPage: React.FC = () => {
  const topTalkers = [
    { ip: '10.0.1.15', bytes: '4.2 GB', packets: '3,120,400', pct: '38.5%' },
    { ip: '10.0.1.45', bytes: '2.8 GB', packets: '2,010,120', pct: '25.6%' },
    { ip: '172.16.10.99', bytes: '1.4 GB', packets: '980,500', pct: '12.8%' },
    { ip: '10.0.2.108', bytes: '950 MB', packets: '720,100', pct: '8.7%' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">Network Traffic & NetFlow Analytics</h2>
        <p className="text-xs text-slate-400">Flow collection, protocol distribution, and Top Talkers analysis</p>
      </div>

      <div className="grid grid-cols-2 gap-6">
        <NetflowAnalytics />

        <Card title="Top Talkers (Flow Volume)" subtitle="Highest bandwidth consuming host IP addresses">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm border-collapse font-mono">
              <thead>
                <tr className="border-b border-slate-800 text-xs text-slate-400 font-semibold uppercase font-sans">
                  <th className="py-3 px-4">Host IP Address</th>
                  <th className="py-3 px-4">Total Volume</th>
                  <th className="py-3 px-4">Packets</th>
                  <th className="py-3 px-4">Traffic %</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800 text-xs">
                {topTalkers.map((t, i) => (
                  <tr key={i} className="hover:bg-slate-850/40">
                    <td className="py-3 px-4 font-bold text-brand-400">{t.ip}</td>
                    <td className="py-3 px-4 text-emerald-400">{t.bytes}</td>
                    <td className="py-3 px-4 text-slate-300">{t.packets}</td>
                    <td className="py-3 px-4 text-indigo-400 font-bold">{t.pct}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Card>
      </div>
    </div>
  );
};
