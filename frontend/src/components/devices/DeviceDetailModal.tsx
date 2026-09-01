import React from 'react';
import { Device } from '../../types';
import { Badge } from '../common/Badge';
import { X, Server, Cpu, HardDrive, Thermometer, ShieldCheck, Clock, MapPin, Hash } from 'lucide-react';

interface DeviceDetailModalProps {
  device: Device | null;
  onClose: () => void;
}

export const DeviceDetailModal: React.FC<DeviceDetailModalProps> = ({ device, onClose }) => {
  if (!device) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-2xl overflow-hidden shadow-2xl animate-in fade-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="p-6 border-b border-slate-800 flex items-center justify-between bg-slate-950/40">
          <div className="flex items-center gap-3">
            <div className="p-3 bg-brand-600/20 text-brand-400 border border-brand-500/30 rounded-xl">
              <Server className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-lg font-bold text-slate-100 font-mono">{device.hostname}</h2>
              <p className="text-xs text-slate-400">{device.vendor} {device.model} ({device.device_type})</p>
            </div>
          </div>
          <button onClick={onClose} className="p-2 rounded-lg text-slate-400 hover:bg-slate-800 hover:text-slate-200">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-6 space-y-6">
          {/* Key Status Grid */}
          <div className="grid grid-cols-4 gap-4">
            <div className="p-4 bg-slate-950 rounded-xl border border-slate-800">
              <p className="text-xs text-slate-400 mb-1">Status</p>
              <Badge variant={device.status === 'ONLINE' ? 'online' : 'critical'}>{device.status}</Badge>
            </div>
            <div className="p-4 bg-slate-950 rounded-xl border border-slate-800">
              <p className="text-xs text-slate-400 mb-1">CPU Load</p>
              <p className="text-lg font-bold font-mono text-brand-400">{device.cpu_usage_pct}%</p>
            </div>
            <div className="p-4 bg-slate-950 rounded-xl border border-slate-800">
              <p className="text-xs text-slate-400 mb-1">RAM Memory</p>
              <p className="text-lg font-bold font-mono text-indigo-400">{device.ram_usage_pct}%</p>
            </div>
            <div className="p-4 bg-slate-950 rounded-xl border border-slate-800">
              <p className="text-xs text-slate-400 mb-1">Temp</p>
              <p className="text-lg font-bold font-mono text-amber-400">{device.temperature_celsius}°C</p>
            </div>
          </div>

          {/* Detailed Info Cards */}
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div className="p-4 bg-slate-950/60 rounded-xl border border-slate-800 space-y-3">
              <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Network Hardware Specs</h4>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-500">Management IP:</span>
                <span className="font-mono text-slate-200">{device.management_ip}</span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-500">MAC Address:</span>
                <span className="font-mono text-slate-200">{device.mac_address}</span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-500">Serial Number:</span>
                <span className="font-mono text-slate-200">{device.serial_number}</span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-500">Firmware:</span>
                <span className="font-mono text-emerald-400">{device.firmware_version}</span>
              </div>
            </div>

            <div className="p-4 bg-slate-950/60 rounded-xl border border-slate-800 space-y-3">
              <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Location & Health</h4>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-500">Physical Rack:</span>
                <span className="text-slate-200">{device.location}</span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-500">System Uptime:</span>
                <span className="font-mono text-slate-200">{Math.floor(device.uptime_seconds / 3600)} hrs</span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-500">SNMP Polling:</span>
                <span className="text-emerald-400">Active (v2c / public)</span>
              </div>
            </div>
          </div>
        </div>

        {/* Modal Footer */}
        <div className="p-4 bg-slate-950 border-t border-slate-800 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-sm font-medium rounded-lg"
          >
            Close Details
          </button>
        </div>
      </div>
    </div>
  );
};
