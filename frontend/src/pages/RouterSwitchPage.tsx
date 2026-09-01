import React from 'react';
import { InterfaceManager } from '../components/router_switch/InterfaceManager';
import { VlanManager } from '../components/router_switch/VlanManager';
import { RoutingTableViewer } from '../components/router_switch/RoutingTableViewer';

export const RouterSwitchPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">Router & Switch Management</h2>
        <p className="text-xs text-slate-400">Interface ports, VLAN trunks, and RIB routing table entries</p>
      </div>

      <InterfaceManager />
      <div className="grid grid-cols-2 gap-6">
        <VlanManager />
        <RoutingTableViewer />
      </div>
    </div>
  );
};
