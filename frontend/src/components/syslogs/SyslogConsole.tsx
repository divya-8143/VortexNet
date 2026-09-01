import React, { useState } from 'react';
import { Card } from '../common/Card';
import { Terminal, Pause, Play, Filter, Download } from 'lucide-react';

export const SyslogConsole: React.FC = () => {
  const [streaming, setStreaming] = useState(true);

  const mockLogs = [
    { time: '2026-09-01T20:15:02Z', host: 'core-router-01', sev: 'INFO', facility: 'LOCAL0', msg: '%OSPF-5-ADJCHG: Process 1, Nbr 10.0.1.2 on Gi0/0/1 from FULL to DOWN' },
    { time: '2026-09-01T20:14:58Z', host: 'dist-switch-01', sev: 'WARNING', facility: 'LOCAL1', msg: '%LINK-3-UPDOWN: Interface GigabitEthernet0/0/3, changed state to down' },
    { time: '2026-09-01T20:14:45Z', host: 'edge-firewall-01', sev: 'CRITICAL', facility: 'AUTH', msg: 'SEC-4-LOGIN_FAILED: Failed SSH login attempt for user admin from 198.51.100.45' },
    { time: '2026-09-01T20:14:30Z', host: 'core-router-02', sev: 'NOTICE', facility: 'LOCAL2', msg: '%BGP-5-ADJCHANGE: neighbor 10.0.0.254 Up' },
  ];

  return (
    <Card 
      title="Live Network Syslog Terminal (RFC 5424)" 
      subtitle="Real-time log aggregation stream"
      action={
        <div className="flex items-center gap-2">
          <button
            onClick={() => setStreaming(!streaming)}
            className={`flex items-center gap-1 px-3 py-1 text-xs font-semibold rounded-lg ${
              streaming ? 'bg-amber-600/20 text-amber-400 border border-amber-500/30' : 'bg-emerald-600/20 text-emerald-400'
            }`}
          >
            {streaming ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
            {streaming ? 'Pause Stream' : 'Resume Live Stream'}
          </button>
        </div>
      }
    >
      <div className="bg-slate-950 p-4 rounded-xl font-mono text-xs space-y-2 border border-slate-800 max-h-96 overflow-y-auto">
        {mockLogs.map((log, idx) => (
          <div key={idx} className="flex items-start gap-3 border-b border-slate-900 pb-1.5 hover:bg-slate-900/60">
            <span className="text-slate-500">{log.time}</span>
            <span className="font-bold text-brand-400">{log.host}</span>
            <span className={`px-1.5 py-0.2 rounded ${log.sev === 'CRITICAL' ? 'bg-rose-950 text-rose-400 font-bold' : log.sev === 'WARNING' ? 'bg-amber-950 text-amber-400' : 'bg-slate-800 text-slate-300'}`}>
              [{log.sev}]
            </span>
            <span className="text-slate-200 flex-1">{log.msg}</span>
          </div>
        ))}
      </div>
    </Card>
  );
};
