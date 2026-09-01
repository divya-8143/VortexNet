import React from 'react';
import { Card } from '../components/common/Card';
import { Download, FileText } from 'lucide-react';
import api from '../services/api';

export const ReportsPage: React.FC = () => {
  const downloadReport = async (type: 'devices' | 'ipam') => {
    try {
      const res = await api.get(`/reports/export/${type}/csv`, { responseType: 'blob' });
      const url = window.URL.createObjectURL(new Blob([res.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `vortexnet_${type}.csv`);
      document.body.appendChild(link);
      link.click();
    } catch (e) {
      alert('Report export failed');
    }
  };

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">Reports & Export Center</h2>
        <p className="text-xs text-slate-400">Download CSV/PDF reports for SLA compliance and infrastructure audits</p>
      </div>

      <div className="grid grid-cols-2 gap-6">
        <Card title="Devices Inventory Audit Report" subtitle="Complete list of hardware devices, IPs, and health statuses">
          <button
            onClick={() => downloadReport('devices')}
            className="mt-4 flex items-center gap-2 px-4 py-2 bg-brand-600 hover:bg-brand-500 text-white text-sm font-semibold rounded-lg shadow-md"
          >
            <Download className="w-4 h-4" /> Download Devices CSV
          </button>
        </Card>

        <Card title="IPAM Subnet Allocation Report" subtitle="Complete CIDR subnet usage and IP allocation data">
          <button
            onClick={() => downloadReport('ipam')}
            className="mt-4 flex items-center gap-2 px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white text-sm font-semibold rounded-lg shadow-md"
          >
            <Download className="w-4 h-4" /> Download IPAM CSV
          </button>
        </Card>
      </div>
    </div>
  );
};
