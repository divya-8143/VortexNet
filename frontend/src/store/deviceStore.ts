import { create } from 'zustand';
import { Device, DeviceSummary } from '../types';
import api from '../services/api';

interface DeviceState {
  devices: Device[];
  summary: DeviceSummary | null;
  loading: boolean;
  fetchDevices: () => Promise<void>;
  fetchSummary: () => Promise<void>;
}

export const useDeviceStore = create<DeviceState>((set) => ({
  devices: [],
  summary: null,
  loading: false,
  fetchDevices: async () => {
    set({ loading: true });
    try {
      const res = await api.get('/devices/');
      set({ devices: res.data, loading: false });
    } catch (e) {
      set({ loading: false });
    }
  },
  fetchSummary: async () => {
    try {
      const res = await api.get('/devices/summary');
      set({ summary: res.data });
    } catch (e) {}
  },
}));
