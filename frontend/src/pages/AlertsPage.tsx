import React from 'react';
import { IncidentBoard } from '../components/alerts/IncidentBoard';

export const AlertsPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-100">Alerts & Incident Management</h2>
        <p className="text-xs text-slate-400">Automated threshold triggers, incident response lifecycle & escalation policies</p>
      </div>

      <IncidentBoard />
    </div>
  );
};
