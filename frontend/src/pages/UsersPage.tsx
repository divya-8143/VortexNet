import React from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { Users, ShieldCheck, Plus } from 'lucide-react';

export const UsersPage: React.FC = () => {
  const users = [
    { id: 1, name: 'NetOps Admin', username: 'admin', email: 'admin@vortexnet.local', role: 'SUPER_ADMIN', dept: 'Network Operations Center' },
    { id: 2, name: 'Lead Network Architect', username: 'engineer', email: 'engineer@vortexnet.local', role: 'NETWORK_ENGINEER', dept: 'Infrastructure Team' },
    { id: 3, name: 'NOC Duty Shift 1', username: 'operator', email: 'operator@vortexnet.local', role: 'NOC_OPERATOR', dept: 'NOC Operations' },
  ];

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-xl font-bold text-slate-100">User & Role Management (RBAC)</h2>
          <p className="text-xs text-slate-400">Access permission matrix and NOC user accounts</p>
        </div>
        <button className="flex items-center gap-1.5 px-4 py-2 bg-brand-600 hover:bg-brand-500 text-white text-sm font-semibold rounded-lg shadow-lg">
          <Plus className="w-4 h-4" /> Add User
        </button>
      </div>

      <Card title="NOC User Accounts" subtitle="Active platform users">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse text-sm">
            <thead>
              <tr className="border-b border-slate-800 text-xs text-slate-400 font-semibold uppercase">
                <th className="py-3 px-4">Full Name</th>
                <th className="py-3 px-4">Username</th>
                <th className="py-3 px-4">Email</th>
                <th className="py-3 px-4">Role</th>
                <th className="py-3 px-4">Department</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800">
              {users.map((u) => (
                <tr key={u.id} className="hover:bg-slate-850/40">
                  <td className="py-3 px-4 font-semibold text-slate-200">{u.name}</td>
                  <td className="py-3 px-4 font-mono text-xs text-brand-400">{u.username}</td>
                  <td className="py-3 px-4 text-xs text-slate-400">{u.email}</td>
                  <td className="py-3 px-4 font-mono text-xs text-emerald-400 font-bold">{u.role}</td>
                  <td className="py-3 px-4 text-xs text-slate-300">{u.dept}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
};
