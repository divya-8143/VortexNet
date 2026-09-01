import React from 'react';
import { Bell, Search, User, LogOut, ShieldCheck } from 'lucide-react';
import { useAuthStore } from '../../store/authStore';

export const Navbar: React.FC = () => {
  const { user, logout } = useAuthStore();

  return (
    <header className="h-16 bg-slate-900/80 backdrop-blur border-b border-slate-800 px-6 flex items-center justify-between sticky top-0 z-30">
      <div className="flex items-center gap-4 flex-1 max-w-md">
        <div className="relative w-full">
          <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" />
          <input
            type="text"
            placeholder="Search IP, Hostname, VLAN, or Syslog..."
            className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-9 pr-4 py-1.5 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-brand-500"
          />
        </div>
      </div>

      <div className="flex items-center gap-4">
        {/* Quick Notification Bell */}
        <button className="p-2 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800 relative">
          <Bell className="w-5 h-5" />
          <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-rose-500"></span>
        </button>

        <div className="h-6 w-[1px] bg-slate-800"></div>

        {/* User Profile info */}
        <div className="flex items-center gap-3">
          <div className="p-2 rounded-full bg-slate-800 text-brand-400 border border-slate-700">
            <User className="w-4 h-4" />
          </div>
          <div className="text-left hidden sm:block">
            <p className="text-xs font-semibold text-slate-200">{user?.full_name || 'NetOps Admin'}</p>
            <div className="flex items-center gap-1">
              <ShieldCheck className="w-3 h-3 text-emerald-400" />
              <span className="text-[10px] text-slate-400 font-mono">{user?.role || 'SUPER_ADMIN'}</span>
            </div>
          </div>

          <button
            onClick={logout}
            title="Logout"
            className="p-2 rounded-lg text-slate-400 hover:text-rose-400 hover:bg-rose-500/10 transition-colors"
          >
            <LogOut className="w-4 h-4" />
          </button>
        </div>
      </div>
    </header>
  );
};
