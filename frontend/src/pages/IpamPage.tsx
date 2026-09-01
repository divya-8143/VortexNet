import React from 'react';
import { SubnetList } from '../components/ipam/SubnetList';

export const IpamPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">IP Address Management (IPAM)</h2>
        <p className="text-xs text-slate-400">CIDR subnets, static allocations, and DHCP lease pools</p>
      </div>

      <SubnetList />
    </div>
  );
};
