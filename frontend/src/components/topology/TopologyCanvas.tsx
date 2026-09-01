import React, { useState } from 'react';
import { Card } from '../common/Card';
import { Server, Shield, Layers, Radio, RefreshCw, ZoomIn, ZoomOut } from 'lucide-react';

export const TopologyCanvas: React.FC = () => {
  const [zoom, setZoom] = useState(100);

  const nodes = [
    { id: 'dev-1', label: 'core-router-01', ip: '10.0.0.1', type: 'ROUTER', x: 250, y: 80, status: 'ONLINE' },
    { id: 'dev-2', label: 'core-router-02', ip: '10.0.0.2', type: 'ROUTER', x: 500, y: 80, status: 'ONLINE' },
    { id: 'dev-3', label: 'dist-switch-01', ip: '10.0.0.11', type: 'SWITCH', x: 180, y: 240, status: 'ONLINE' },
    { id: 'dev-4', label: 'dist-switch-02', ip: '10.0.0.12', type: 'SWITCH', x: 570, y: 240, status: 'ONLINE' },
    { id: 'dev-5', label: 'edge-firewall-01', ip: '10.0.0.254', type: 'FIREWALL', x: 375, y: 380, status: 'WARNING' },
  ];

  const links = [
    { from: nodes[0], to: nodes[1], label: '100G Trunk (LACP)' },
    { from: nodes[0], to: nodes[2], label: '10G Uplink' },
    { from: nodes[1], to: nodes[3], label: '10G Uplink' },
    { from: nodes[2], to: nodes[4], label: '10G LAN' },
    { from: nodes[3], to: nodes[4], label: '10G LAN' },
  ];

  return (
    <Card 
      title="Network Topology Canvas" 
      subtitle="Interactive Physical & Logical Link Mapping"
      action={
        <div className="flex items-center gap-2">
          <button onClick={() => setZoom(Math.max(50, zoom - 10))} className="p-1.5 bg-slate-800 rounded hover:bg-slate-700 text-slate-300">
            <ZoomOut className="w-4 h-4" />
          </button>
          <span className="text-xs font-mono text-slate-400 w-12 text-center">{zoom}%</span>
          <button onClick={() => setZoom(Math.min(150, zoom + 10))} className="p-1.5 bg-slate-800 rounded hover:bg-slate-700 text-slate-300">
            <ZoomIn className="w-4 h-4" />
          </button>
        </div>
      }
    >
      <div className="relative w-full h-[450px] bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
        {/* SVG Links */}
        <svg className="absolute inset-0 w-full h-full pointer-events-none">
          {links.map((link, idx) => (
            <g key={idx}>
              <line
                x1={link.from.x + 60}
                y1={link.from.y + 30}
                x2={link.to.x + 60}
                y2={link.to.y + 30}
                stroke="#0c8ee9"
                strokeWidth="2.5"
                strokeDasharray={link.label.includes('100G') ? 'none' : '4'}
                className="opacity-80"
              />
            </g>
          ))}
        </svg>

        {/* Device Nodes */}
        {nodes.map((node) => (
          <div
            key={node.id}
            style={{ left: `${node.x}px`, top: `${node.y}px`, transform: `scale(${zoom / 100})` }}
            className="absolute p-3 bg-slate-900 border border-slate-700 hover:border-brand-500 rounded-xl shadow-lg w-40 flex flex-col items-center gap-1.5 transition-all cursor-pointer group"
          >
            <div className="p-2 bg-brand-600/20 text-brand-400 rounded-lg group-hover:bg-brand-500 group-hover:text-white transition-colors">
              {node.type === 'FIREWALL' ? <Shield className="w-5 h-5" /> : <Server className="w-5 h-5" />}
            </div>
            <p className="text-xs font-mono font-bold text-slate-100">{node.label}</p>
            <p className="text-[10px] font-mono text-slate-400">{node.ip}</p>
            <span className={`w-2 h-2 rounded-full ${node.status === 'ONLINE' ? 'bg-emerald-500' : 'bg-amber-500'}`}></span>
          </div>
        ))}
      </div>
    </Card>
  );
};
