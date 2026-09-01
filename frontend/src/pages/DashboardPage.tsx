import React, { useEffect } from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { useDeviceStore } from '../store/deviceStore';
import { RealtimeBandwidthChart } from '../components/bandwidth/RealtimeBandwidthChart';
import { IncidentBoard } from '../components/alerts/IncidentBoard';
import { Server, Activity, AlertTriangle, ShieldCheck, Cpu, Radio } from 'lucide-react';

export const DashboardPage: React.FC = () => {
  const { summary, fetchSummary } = useDeviceStore();

  useEffect(() => {
    fetchSummary();
  }, [fetchSummary]);

  return (
    <div className="space-y-6">
      {/* Top Stat KPI Cards */}
      <div className="grid grid-cols-4 gap-5">
        <Card className="flex items-center gap-4">
          <div className="p-3 bg-brand-600/20 text-brand-400 rounded-xl">
            <Server className="w-6 h-6" />
          </div>
          <div>
            <p className="text-xs text-slate-400">Total Infrastructure Devices</p>
            <h3 className="text-2xl font-bold font-mono text-slate-100">{summary?.total_devices || 7}</h3>
          </div>
        </Card>

        <Card className="flex items-center gap-4">
          <div className="p-3 bg-emerald-500/20 text-emerald-400 rounded-xl">
            <Activity className="w-6 h-6" />
          </div>
          <div>
            <p className="text-xs text-slate-400">Healthy Devices (Online)</p>
            <h3 className="text-2xl font-bold font-mono text-emerald-400">{summary?.online_count || 6}</h3>
          </div>
        </Card>

        <Card className="flex items-center gap-4">
          <div className="p-3 bg-amber-500/20 text-amber-400 rounded-xl">
            <AlertTriangle className="w-6 h-6" />
          </div>
          <div>
            <p className="text-xs text-slate-400">Warning / Degraded State</p>
            <h3 className="text-2xl font-bold font-mono text-amber-400">{summary?.warning_count || 1}</h3>
          </div>
        </Card>

        <Card className="flex items-center gap-4">
          <div className="p-3 bg-indigo-500/20 text-indigo-400 rounded-xl">
            <Radio className="w-6 h-6" />
          </div>
          <div>
            <p className="text-xs text-slate-400">Average Fleet CPU Load</p>
            <h3 className="text-2xl font-bold font-mono text-indigo-400">{summary?.avg_cpu_pct || 28.5}%</h3>
          </div>
        </Card>
      </div>

      {/* Main Grid Charts */}
      <div className="grid grid-cols-3 gap-6">
        <div className="col-span-2">
          <RealtimeBandwidthChart />
        </div>
        <div>
          <Card title="NOC Operational Status" subtitle="Fleet health metrics">
            <div className="space-y-4 pt-2">
              <div className="flex justify-between items-center text-xs">
                <span className="text-slate-400">SLA Uptime Target:</span>
                <span className="font-mono text-emerald-400 font-bold">99.999%</span>
              </div>
              <div className="flex justify-between items-center text-xs">
                <span className="text-slate-400">Active Alert Thresholds:</span>
                <span className="font-mono text-brand-400 font-bold">12 Rules Enabled</span>
              </div>
              <div className="flex justify-between items-center text-xs">
                <span className="text-slate-400">SNMP Polling Interval:</span>
                <span className="font-mono text-slate-300">5 seconds</span>
              </div>
              <div className="flex justify-between items-center text-xs">
                <span className="text-slate-400">IPAM CIDR Subnets:</span>
                <span className="font-mono text-indigo-400 font-bold">4 Active Pools</span>
              </div>
            </div>
          </Card>
        </div>
      </div>

      <IncidentBoard />
    </div>
  );
};
