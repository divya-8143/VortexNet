import React from 'react';
import { TopologyCanvas } from '../components/topology/TopologyCanvas';

export const TopologyPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">Interactive Network Topology</h2>
        <p className="text-xs text-slate-400">Visual mapping of physical core routers, distribution switches, and trunk links</p>
      </div>

      <TopologyCanvas />
    </div>
  );
};
