import React from 'react';
import { Card } from '../common/Card';
import { Layers, Plus } from 'lucide-react';

export const VlanManager: React.FC = () => {
  const vlans = [
    { vlan_id: 1, name: 'default', subnet: '10.0.0.0/24', desc: 'Management VLAN' },
    { vlan_id: 10, name: 'DATA_SERVERS', subnet: '10.0.1.0/24', desc: 'Core Application & DB Tier' },
    { vlan_id: 20, name: 'VOIP_PHONES', subnet: '10.0.10.0/24', desc: 'SIP & Telephony Traffic' },
    { vlan_id: 99, name: 'GUEST_WIFI', subnet: '192.168.99.0/24', desc: 'Isolated Visitor Network' },
  ];

  return (
    <Card 
      title="VLAN Database Configuration" 
      subtitle="Virtual LAN assignments and subnets"
      action={
        <button className="flex items-center gap-1.5 px-3 py-1.5 bg-brand-600 hover:bg-brand-500 text-white text-xs font-semibold rounded-lg">
          <Plus className="w-4 h-4" /> Add VLAN
        </button>
      }
    >
      <div className="grid grid-cols-2 gap-4">
        {vlans.map((v) => (
          <div key={v.vlan_id} className="p-4 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-between">
            <div>
              <div className="flex items-center gap-2">
                <span className="px-2 py-0.5 bg-brand-600/20 text-brand-400 font-mono text-xs font-bold rounded">
                  VLAN {v.vlan_id}
                </span>
                <span className="font-semibold text-slate-100 text-sm">{v.name}</span>
              </div>
              <p className="text-xs text-slate-400 mt-1">{v.desc}</p>
              <p className="text-xs font-mono text-slate-500 mt-0.5">Subnet: {v.subnet}</p>
            </div>
          </div>
        ))}
      </div>
    </Card>
  );
};
