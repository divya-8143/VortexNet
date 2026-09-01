import React from 'react';
import { Card } from '../common/Card';
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { Radio } from 'lucide-react';

export const RealtimeBandwidthChart: React.FC = () => {
  const data = [
    { time: '10:00', inbound: 12.4, outbound: 8.2 },
    { time: '10:05', inbound: 18.1, outbound: 11.5 },
    { time: '10:10', inbound: 24.6, outbound: 15.0 },
    { time: '10:15', inbound: 31.2, outbound: 22.8 },
    { time: '10:20', inbound: 28.5, outbound: 19.4 },
    { time: '10:25', inbound: 35.8, outbound: 26.1 },
    { time: '10:30', inbound: 29.4, outbound: 21.0 },
  ];

  return (
    <Card title="Interface Throughput (Gbps)" subtitle="Real-time inbound and outbound bandwidth telemetry">
      <div className="h-64 w-full pt-4">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data}>
            <defs>
              <linearGradient id="colorIn" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#0c8ee9" stopOpacity={0.8}/>
                <stop offset="95%" stopColor="#0c8ee9" stopOpacity={0}/>
              </linearGradient>
              <linearGradient id="colorOut" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#6366f1" stopOpacity={0.8}/>
                <stop offset="95%" stopColor="#6366f1" stopOpacity={0}/>
              </linearGradient>
            </defs>
            <XAxis dataKey="time" stroke="#64748b" />
            <YAxis stroke="#64748b" unit=" Gbps" />
            <Tooltip contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155' }} />
            <Area type="monotone" dataKey="inbound" stroke="#0c8ee9" fillOpacity={1} fill="url(#colorIn)" name="Inbound Throughput" />
            <Area type="monotone" dataKey="outbound" stroke="#6366f1" fillOpacity={1} fill="url(#colorOut)" name="Outbound Throughput" />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </Card>
  );
};
