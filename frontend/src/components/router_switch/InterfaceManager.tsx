import React from 'react';
import { Card } from '../common/Card';
import { Badge } from '../common/Badge';
import { Network, Activity, ArrowUpRight, ArrowDownLeft } from 'lucide-react';

export const InterfaceManager: React.FC = () => {
  const mockInterfaces = [
    { id: 1, name: 'GigabitEthernet0/0/1', type: 'GIGABIT_ETHERNET', status: 'UP', ip: '10.0.0.1/24', speed: '1000 Mbps', rx: '42.5 MB', tx: '18.2 MB' },
    { id: 2, name: 'GigabitEthernet0/0/2', type: 'GIGABIT_ETHERNET', status: 'UP', ip: '10.0.1.1/24', speed: '1000 Mbps', rx: '128.4 MB', tx: '95.1 MB' },
    { id: 3, name: 'TenGigabitEthernet1/0/1', type: 'TEN_GIGABIT', status: 'UP', ip: '192.168.100.1/30', speed: '10000 Mbps', rx: '1.4 GB', tx: '890 MB' },
    { id: 4, name: 'GigabitEthernet0/0/3', type: 'GIGABIT_ETHERNET', status: 'DOWN', ip: 'Unassigned', speed: '1000 Mbps', rx: '0 B', tx: '0 B' },
  ];

  return (
    <Card title="Interface Port Status & Counters" subtitle="Live port metrics for selected router / switch">
      <div className="overflow-x-auto">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="border-b border-slate-800 text-xs text-slate-400 font-semibold uppercase">
              <th className="py-3 px-4">Interface Name</th>
              <th className="py-3 px-4">Type</th>
              <th className="py-3 px-4">Status</th>
              <th className="py-3 px-4">IP Address</th>
              <th className="py-3 px-4">Speed</th>
              <th className="py-3 px-4">RX Inbound</th>
              <th className="py-3 px-4">TX Outbound</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800 text-sm">
            {mockInterfaces.map((iface) => (
              <tr key={iface.id} className="hover:bg-slate-850/40">
                <td className="py-3 px-4 font-mono font-medium text-brand-400">{iface.name}</td>
                <td className="py-3 px-4 text-xs text-slate-400">{iface.type}</td>
                <td className="py-3 px-4">
                  <Badge variant={iface.status === 'UP' ? 'online' : 'offline'}>{iface.status}</Badge>
                </td>
                <td className="py-3 px-4 font-mono text-xs text-slate-300">{iface.ip}</td>
                <td className="py-3 px-4 text-xs">{iface.speed}</td>
                <td className="py-3 px-4 font-mono text-xs text-emerald-400 flex items-center gap-1">
                  <ArrowDownLeft className="w-3 h-3" /> {iface.rx}
                </td>
                <td className="py-3 px-4 font-mono text-xs text-indigo-400 flex items-center gap-1">
                  <ArrowUpRight className="w-3 h-3" /> {iface.tx}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Card>
  );
};
