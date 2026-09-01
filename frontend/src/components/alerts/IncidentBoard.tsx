import React from 'react';
import { Card } from '../common/Card';
import { Badge } from '../common/Badge';
import { AlertTriangle, CheckCircle, Clock, User, ShieldAlert } from 'lucide-react';

export const IncidentBoard: React.FC = () => {
  const incidents = [
    { id: 101, title: 'BGP Peer Session Flapping on Edge Gateway', device: 'edge-firewall-01', severity: 'CRITICAL', status: 'TRIGGERED', assignee: 'Lead Network Architect', time: '12 mins ago' },
    { id: 102, title: 'High CPU Utilization (>88%) on Distribution Switch', device: 'dist-switch-01', severity: 'MAJOR', status: 'ACKNOWLEDGED', assignee: 'NOC Duty Engineer', time: '34 mins ago' },
    { id: 103, title: 'Interface GigabitEthernet0/0/3 Down', device: 'core-router-02', severity: 'MINOR', status: 'IN_PROGRESS', assignee: 'NOC Duty Engineer', time: '1 hr ago' },
    { id: 104, title: 'DHCP Subnet Capacity Reached 85%', device: 'core-router-01', severity: 'WARNING', status: 'RESOLVED', assignee: 'IPAM Team', time: '3 hrs ago' },
  ];

  return (
    <Card title="Active Incident Command Board" subtitle="Real-time alert resolution workflows">
      <div className="space-y-3">
        {incidents.map((inc) => (
          <div key={inc.id} className="p-4 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-between hover:border-slate-700 transition-colors">
            <div className="flex items-center gap-3">
              <div className={`p-2.5 rounded-lg ${inc.severity === 'CRITICAL' ? 'bg-rose-500/20 text-rose-400' : 'bg-amber-500/20 text-amber-400'}`}>
                <ShieldAlert className="w-5 h-5" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-mono font-bold text-xs text-slate-400">#INC-{inc.id}</span>
                  <h4 className="font-semibold text-slate-100 text-sm">{inc.title}</h4>
                </div>
                <p className="text-xs text-slate-400 mt-1 font-mono">Device: {inc.device} • Assigned: {inc.assignee}</p>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <Badge variant={inc.severity === 'CRITICAL' ? 'critical' : 'warning'}>{inc.severity}</Badge>
              <span className="text-xs text-slate-500 font-mono flex items-center gap-1">
                <Clock className="w-3 h-3" /> {inc.time}
              </span>
              <button className="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold rounded-lg">
                Manage Workflow
              </button>
            </div>
          </div>
        ))}
      </div>
    </Card>
  );
};
