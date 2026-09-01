import React from 'react';
import { RealtimeBandwidthChart } from '../components/bandwidth/RealtimeBandwidthChart';

export const BandwidthPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">Bandwidth & Port Utilization</h2>
        <p className="text-xs text-slate-400">Inbound and outbound bit-rate counters per interface</p>
      </div>

      <RealtimeBandwidthChart />
    </div>
  );
};
