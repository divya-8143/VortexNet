import React from 'react';
import { Card } from '../common/Card';
import { Network } from 'lucide-react';

export const RoutingTableViewer: React.FC = () => {
  const routes = [
    { dest: '0.0.0.0/0', next_hop: '198.51.100.1', iface: 'TenGigabitEthernet1/0/1', proto: 'BGP', metric: 20 },
    { dest: '10.0.0.0/24', next_hop: 'Directly Connected', iface: 'GigabitEthernet0/0/1', proto: 'CONNECTED', metric: 0 },
    { dest: '10.0.1.0/24', next_hop: '10.0.0.2', iface: 'GigabitEthernet0/0/2', proto: 'OSPF', metric: 110 },
    { dest: '172.16.0.0/16', next_hop: '10.0.0.254', iface: 'GigabitEthernet0/0/2', proto: 'STATIC', metric: 1 },
  ];

  return (
    <Card title="Device Routing Table (RIB)" subtitle="Active IPv4 unicast routing entries">
      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm border-collapse">
          <thead>
            <tr className="border-b border-slate-800 text-xs text-slate-400 font-semibold uppercase">
              <th className="py-3 px-4">Destination Subnet</th>
              <th className="py-3 px-4">Next-Hop IP</th>
              <th className="py-3 px-4">Out Interface</th>
              <th className="py-3 px-4">Protocol</th>
              <th className="py-3 px-4">Metric Cost</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800 font-mono text-xs">
            {routes.map((r, i) => (
              <tr key={i} className="hover:bg-slate-850/40">
                <td className="py-3 px-4 font-bold text-slate-200">{r.dest}</td>
                <td className="py-3 px-4 text-slate-300">{r.next_hop}</td>
                <td className="py-3 px-4 text-brand-400">{r.iface}</td>
                <td className="py-3 px-4">
                  <span className="px-2 py-0.5 rounded bg-slate-800 text-indigo-400 font-sans font-semibold">
                    {r.proto}
                  </span>
                </td>
                <td className="py-3 px-4 text-slate-400">{r.metric}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Card>
  );
};
