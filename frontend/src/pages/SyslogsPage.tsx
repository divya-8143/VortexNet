import React from 'react';
import { SyslogConsole } from '../components/syslogs/SyslogConsole';

export const SyslogsPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">Network Syslog Terminal</h2>
        <p className="text-xs text-slate-400">Centralized log collection, facility filters, and full-text log search</p>
      </div>

      <SyslogConsole />
    </div>
  );
};
