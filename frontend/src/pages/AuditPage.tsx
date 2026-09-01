import React from 'react';
import { Card } from '../components/common/Card';
import { Lock } from 'lucide-react';

export const AuditPage: React.FC = () => {
  const logs = [
    { time: '2026-09-01T20:10:00Z', user: 'admin', action: 'CREATE', module: 'Device Management', details: 'Provisioned core-router-01 (10.0.0.1)' },
    { time: '2026-09-01T20:05:22Z', user: 'engineer', action: 'UPDATE', module: 'IPAM', details: 'Allocated IP 10.0.1.45 to app-server-01' },
    { time: '2026-09-01T19:50:11Z', user: 'operator', action: 'EXECUTE', module: 'Incident', details: 'Acknowledged incident #INC-101' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">System Audit Trail</h2>
        <p className="text-xs text-slate-400">Immutable audit log of configuration changes and NOC user actions</p>
      </div>

      <Card title="Audit Event Logs" subtitle="Security & change tracking history">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm border-collapse font-mono">
            <thead>
              <tr className="border-b border-slate-800 text-xs text-slate-400 font-semibold uppercase font-sans">
                <th className="py-3 px-4">Timestamp</th>
                <th className="py-3 px-4">User</th>
                <th className="py-3 px-4">Action Type</th>
                <th className="py-3 px-4">Module</th>
                <th className="py-3 px-4">Details</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800 text-xs">
              {logs.map((l, i) => (
                <tr key={i} className="hover:bg-slate-850/40">
                  <td className="py-3 px-4 text-slate-500">{l.time}</td>
                  <td className="py-3 px-4 font-bold text-brand-400">{l.user}</td>
                  <td className="py-3 px-4 text-indigo-400">{l.action}</td>
                  <td className="py-3 px-4 text-slate-300 font-sans">{l.module}</td>
                  <td className="py-3 px-4 text-slate-200">{l.details}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
};
