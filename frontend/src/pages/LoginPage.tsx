import React, { useState } from 'react';
import { useAuthStore } from '../store/authStore';
import { Activity, Lock, User } from 'lucide-react';
import api from '../services/api';

export const LoginPage: React.FC = () => {
  const [username, setUsername] = useState('admin');
  const [password, setPassword] = useState('admin123');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const setAuth = useAuthStore((state) => state.setAuth);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const formData = new FormData();
      formData.append('username', username);
      formData.append('password', password);
      const res = await api.post('/auth/login', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setAuth(res.data.user, res.data.access_token);
    } catch (err: any) {
      setError('Invalid username or password. Default demo: admin / admin123');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-md p-8 shadow-2xl space-y-6">
        <div className="text-center space-y-2">
          <div className="w-12 h-12 bg-brand-600 rounded-2xl mx-auto flex items-center justify-center text-white shadow-lg shadow-brand-500/20">
            <Activity className="w-7 h-7" />
          </div>
          <h1 className="text-2xl font-bold text-slate-100">VortexNet NOC Portal</h1>
          <p className="text-xs text-slate-400">Enterprise Network Monitoring & Telemetry Platform</p>
        </div>

        {error && (
          <div className="p-3 bg-rose-500/10 border border-rose-500/30 text-rose-400 text-xs rounded-lg font-medium text-center">
            {error}
          </div>
        )}

        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="text-xs font-semibold text-slate-400 block mb-1">Username</label>
            <div className="relative">
              <User className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" />
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-9 pr-4 py-2 text-sm text-slate-100 focus:outline-none focus:border-brand-500"
                required
              />
            </div>
          </div>

          <div>
            <label className="text-xs font-semibold text-slate-400 block mb-1">Password</label>
            <div className="relative">
              <Lock className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" />
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-9 pr-4 py-2 text-sm text-slate-100 focus:outline-none focus:border-brand-500"
                required
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-2.5 bg-brand-600 hover:bg-brand-500 text-white font-semibold text-sm rounded-lg shadow-lg transition-colors"
          >
            {loading ? 'Authenticating...' : 'Sign In to NOC Portal'}
          </button>
        </form>

        <div className="text-center pt-2 border-t border-slate-800">
          <p className="text-xs text-slate-500 font-mono">Default Demo Admin: admin / admin123</p>
        </div>
      </div>
    </div>
  );
};
