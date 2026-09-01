import React, { useState } from 'react';
import { Device } from '../../types';
import { Badge } from '../common/Badge';
import { Server, Cpu, HardDrive, Thermometer, MoreVertical, ExternalLink } from 'lucide-react';

interface DeviceListProps {
  devices: Device[];
  onSelectDevice: (device: Device) => void;
}

export const DeviceList: React.FC<DeviceListProps> = ({ devices, onSelectDevice }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const filtered = devices.filter(d =>
    d.hostname.toLowerCase().includes(searchTerm.toLowerCase()) ||
    d.management_ip.includes(searchTerm) ||
    d.vendor.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between gap-4">
        <input
          type="text"
          placeholder="Filter devices by hostname, IP, or vendor..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="bg-slate-900 border border-slate-800 rounded-lg px-4 py-2 text-sm text-slate-200 w-80 focus:outline-none focus:border-brand-500"
        />
        <span className="text-xs text-slate-400 font-mono">Showing {filtered.length} of {devices.length} Devices</span>
      </div>

      <div className="overflow-x-auto rounded-xl border border-slate-800 bg-slate-900">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="border-b border-slate-800 bg-slate-950/60 text-xs font-semibold text-slate-400 uppercase tracking-wider">
              <th className="py-3.5 px-4">Device / Hostname</th>
              <th className="py-3.5 px-4">Type & Vendor</th>
              <th className="py-3.5 px-4">Management IP</th>
              <th className="py-3.5 px-4">Status</th>
              <th className="py-3.5 px-4">CPU Utilization</th>
              <th className="py-3.5 px-4">RAM Utilization</th>
              <th className="py-3.5 px-4">Temp (°C)</th>
              <th className="py-3.5 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800 text-sm">
            {filtered.map((device) => {
              const statusVariant = 
                device.status === 'ONLINE' ? 'online' :
                device.status === 'CRITICAL' ? 'critical' :
                device.status === 'WARNING' ? 'warning' : 'offline';

              return (
                <tr key={device.id} className="hover:bg-slate-850/60 transition-colors">
                  <td className="py-3 px-4">
                    <div className="flex items-center gap-3">
                      <div className="p-2 rounded-lg bg-slate-800 text-brand-400">
                        <Server className="w-4 h-4" />
                      </div>
                      <div>
                        <p className="font-semibold text-slate-100 font-mono">{device.hostname}</p>
                        <p className="text-xs text-slate-500">{device.location}</p>
                      </div>
                    </div>
                  </td>

                  <td className="py-3 px-4">
                    <span className="text-xs font-medium text-slate-300 bg-slate-800 px-2 py-0.5 rounded">
                      {device.vendor} {device.model}
                    </span>
                  </td>

                  <td className="py-3 px-4 font-mono text-slate-300 text-xs">{device.management_ip}</td>

                  <td className="py-3 px-4">
                    <Badge variant={statusVariant}>{device.status}</Badge>
                  </td>

                  <td className="py-3 px-4">
                    <div className="w-28">
                      <div className="flex justify-between text-xs font-mono mb-1">
                        <span>{device.cpu_usage_pct}%</span>
                      </div>
                      <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                        <div
                          className={`h-full rounded-full ${
                            device.cpu_usage_pct > 85 ? 'bg-rose-500' : device.cpu_usage_pct > 70 ? 'bg-amber-500' : 'bg-brand-500'
                          }`}
                          style={{ width: `${device.cpu_usage_pct}%` }}
                        ></div>
                      </div>
                    </div>
                  </td>

                  <td className="py-3 px-4">
                    <div className="w-28">
                      <div className="flex justify-between text-xs font-mono mb-1">
                        <span>{device.ram_usage_pct}%</span>
                      </div>
                      <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                        <div
                          className={`h-full rounded-full ${
                            device.ram_usage_pct > 85 ? 'bg-rose-500' : 'bg-indigo-500'
                          }`}
                          style={{ width: `${device.ram_usage_pct}%` }}
                        ></div>
                      </div>
                    </div>
                  </td>

                  <td className="py-3 px-4 font-mono text-xs">
                    <span className={device.temperature_celsius > 55 ? 'text-rose-400 font-bold' : 'text-slate-300'}>
                      {device.temperature_celsius}°C
                    </span>
                  </td>

                  <td className="py-3 px-4 text-right">
                    <button
                      onClick={() => onSelectDevice(device)}
                      className="p-1.5 rounded hover:bg-slate-800 text-slate-400 hover:text-brand-400"
                    >
                      <ExternalLink className="w-4 h-4" />
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
