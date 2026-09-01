import React from 'react';
import { Card } from '../common/Card';
import { HardDrive, Plus } from 'lucide-react';

export const SubnetList: React.FC = () => {
  const subnets = [
    { id: 1, cidr: '10.0.0.0/24', name: 'Core Infrastructure Management', category: 'MANAGEMENT', gateway: '10.0.0.1', used: 15, total: 254, pct: 5.9 },
    { id: 2, cidr: '10.0.1.0/24', name: 'Data Center Server Subnet A', category: 'DATA_CENTER', gateway: '10.0.1.1', used: 42, total: 254, pct: 16.5 },
    { id: 3, cidr: '10.0.10.0/24', name: 'Enterprise VoIP Network', category: 'VOIP', gateway: '10.0.10.1', used: 88, total: 254, pct: 34.6 },
    { id: 4, cidr: '192.168.99.0/24', name: 'Guest Wi-Fi Pool', category: 'USER_LAN', gateway: '192.168.99.1', used: 210, total: 254, pct: 82.6 },
  ];

  return (
    <Card 
      title="IPAM Subnet Hierarchy & Utilization" 
      subtitle="CIDR Address Block Allocations"
      action={
        <button className="flex items-center gap-1.5 px-3 py-1.5 bg-brand-600 hover:bg-brand-500 text-white text-xs font-semibold rounded-lg">
          <Plus className="w-4 h-4" /> Add Subnet
        </button>
      }
    >
      <div className="space-y-4">
        {subnets.map((sub) => (
          <div key={sub.id} className="p-4 bg-slate-950 rounded-xl border border-slate-800 space-y-3">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="p-2 bg-slate-800 text-brand-400 rounded-lg">
                  <HardDrive className="w-5 h-5" />
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-mono font-bold text-slate-100 text-base">{sub.cidr}</span>
                    <span className="text-xs bg-slate-800 text-slate-400 px-2 py-0.5 rounded font-mono">{sub.category}</span>
                  </div>
                  <p className="text-xs text-slate-400 mt-0.5">{sub.name} (Gateway: {sub.gateway})</p>
                </div>
              </div>
              <div className="text-right font-mono">
                <p className="text-sm font-bold text-slate-200">{sub.used} / {sub.total} IPs</p>
                <p className="text-xs text-slate-400">{sub.pct}% Utilized</p>
              </div>
            </div>

            {/* Utilization Bar */}
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
              <div
                className={`h-full rounded-full transition-all ${
                  sub.pct > 80 ? 'bg-amber-500' : 'bg-brand-500'
                }`}
                style={{ width: `${sub.pct}%` }}
              ></div>
            </div>
          </div>
        ))}
      </div>
    </Card>
  );
};
