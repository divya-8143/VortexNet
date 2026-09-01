import React, { useEffect, useState } from 'react';
import { useDeviceStore } from '../store/deviceStore';
import { DeviceList } from '../components/devices/DeviceList';
import { DeviceDetailModal } from '../components/devices/DeviceDetailModal';
import { Device } from '../types';
import { Plus } from 'lucide-react';

export const DevicesPage: React.FC = () => {
  const { devices, fetchDevices } = useDeviceStore();
  const [selectedDevice, setSelectedDevice] = useState<Device | null>(null);

  useEffect(() => {
    fetchDevices();
  }, [fetchDevices]);

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-xl font-bold text-slate-100">Network Devices Inventory</h2>
          <p className="text-xs text-slate-400">Manage routers, switches, firewalls, and servers</p>
        </div>
        <button className="flex items-center gap-1.5 px-4 py-2 bg-brand-600 hover:bg-brand-500 text-white text-sm font-semibold rounded-lg shadow-lg">
          <Plus className="w-4 h-4" /> Provision New Device
        </button>
      </div>

      <DeviceList devices={devices} onSelectDevice={(d) => setSelectedDevice(d)} />

      <DeviceDetailModal device={selectedDevice} onClose={() => setSelectedDevice(null)} />
    </div>
  );
};
