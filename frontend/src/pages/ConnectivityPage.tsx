import React from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { Cpu, Activity } from 'lucide-react';

export const ConnectivityPage: React.FC = () => {
  const probes = [
    { target: 'Core Router 01 Loopback', ip: '10.0.0.1', rtt: '1.2 ms', jitter: '0.1 ms', loss: '0.0%', status: 'ONLINE' },
    { target: 'DC-Server Gateway A', ip: '10.0.1.1', rtt: '2.4 ms', jitter: '0.3 ms', loss: '0.0%', status: 'ONLINE' },
    { target: 'Edge Firewall DMZ Probe', ip: '10.0.0.254', rtt: '18.5 ms', jitter: '1.2 ms', loss: '2.5%', status: 'WARNING' },
    { target: 'ISP Gateway Peer 1', ip: '198.51.100.1', rtt: '12.1 ms', jitter: '0.4 ms', loss: '0.0%', status: 'ONLINE' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">Connectivity & SLA Monitoring</h2>
        <p className="text-xs text-slate-400">Synthetic ICMP Ping probes, RTT latency & packet loss matrices</p>
      </div>

      <Card title="ICMP Echo SLA Probes" subtitle="Real-time round-trip latency & jitter tracking">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-slate-800 text-xs text-slate-400 font-semibold uppercase">
                <th className="py-3 px-4">Probe Target Name</th>
                <th className="py-3 px-4">Target IP</th>
                <th className="py-3 px-4">RTT Latency</th>
                <th className="py-3 px-4">Jitter</th>
                <th className="py-3 px-4">Packet Loss %</th>
                <th className="py-3 px-4">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800 text-sm font-mono">
              {probes.map((p, i) => (
                <tr key={i} className="hover:bg-slate-850/40">
                  <td className="py-3 px-4 font-sans font-semibold text-slate-200">{p.target}</td>
                  <td className="py-3 px-4 text-brand-400">{p.ip}</td>
                  <td className="py-3 px-4 text-emerald-400">{p.rtt}</td>
                  <td className="py-3 px-4 text-slate-300">{p.jitter}</td>
                  <td className="py-3 px-4 text-amber-400">{p.loss}</td>
                  <td className="py-3 px-4">
                    <Badge variant={p.status === 'ONLINE' ? 'online' : 'warning'}>{p.status}</Badge>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
};
