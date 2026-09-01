import React from 'react';
import { 
  Activity, Server, Network, Layers, Cpu, ShieldAlert, 
  Terminal, Users, FileText, Lock, Radio, PieChart, HardDrive
} from 'lucide-react';

interface SidebarProps {
  currentTab: string;
  setCurrentTab: (tab: string) => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ currentTab, setCurrentTab }) => {
  const menuItems = [
    { id: 'dashboard', label: 'NOC Dashboard', icon: Activity },
    { id: 'devices', label: 'Device Inventory', icon: Server },
    { id: 'router_switch', label: 'Routers & Switches', icon: Network },
    { id: 'ipam', label: 'IPAM (Subnets)', icon: HardDrive },
    { id: 'topology', label: 'Network Topology', icon: Layers },
    { id: 'bandwidth', label: 'Bandwidth Monitor', icon: Radio },
    { id: 'connectivity', label: 'Connectivity & SLA', icon: Cpu },
    { id: 'traffic', label: 'Traffic Analytics', icon: PieChart },
    { id: 'alerts', label: 'Incidents & Alerts', icon: ShieldAlert },
    { id: 'syslogs', label: 'Syslog Console', icon: Terminal },
    { id: 'users', label: 'User & Roles', icon: Users },
    { id: 'reports', label: 'Reports & Exports', icon: FileText },
    { id: 'audit', label: 'Audit Trail', icon: Lock },
  ];

  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-800 flex flex-col h-screen sticky top-0">
      {/* Brand Header */}
      <div className="p-5 border-b border-slate-800 flex items-center gap-3">
        <div className="p-2 bg-brand-600 rounded-lg shadow-lg shadow-brand-500/20 text-white">
          <Activity className="w-6 h-6 animate-pulse" />
        </div>
        <div>
          <h1 className="font-bold text-lg text-white tracking-wide">VortexNet</h1>
          <p className="text-xs text-slate-400 font-mono">v1.0.0 Enterprise NOC</p>
        </div>
      </div>

      {/* Navigation Links */}
      <nav className="flex-1 overflow-y-auto p-3 space-y-1">
        {menuItems.map((item) => {
          const Icon = item.icon;
          const isActive = currentTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setCurrentTab(item.id)}
              className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-all ${
                isActive
                  ? 'bg-brand-600/20 text-brand-400 border border-brand-500/30'
                  : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
              }`}
            >
              <Icon className={`w-4 h-4 ${isActive ? 'text-brand-400' : 'text-slate-400'}`} />
              <span>{item.label}</span>
            </button>
          );
        })}
      </nav>

      {/* System Status Footer */}
      <div className="p-4 border-t border-slate-800 bg-slate-950/50">
        <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
          <span>Engine Status</span>
          <span className="flex items-center gap-1.5 text-emerald-400 font-medium">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
            ACTIVE
          </span>
        </div>
        <p className="text-[11px] text-slate-500 font-mono">Telemetry Poller: 5s Tick</p>
      </div>
    </aside>
  );
};
