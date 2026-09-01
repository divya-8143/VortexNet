import { create } from 'zustand';
import { User } from '../types';

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  setAuth: (user: User, token: string) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  token: localStorage.getItem('vortexnet_token'),
  isAuthenticated: !!localStorage.getItem('vortexnet_token'),
  setAuth: (user, token) => {
    localStorage.setItem('vortexnet_token', token);
    set({ user, token, isAuthenticated: true });
  },
  logout: () => {
    localStorage.removeItem('vortexnet_token');
    set({ user: null, token: null, isAuthenticated: false });
  },
}));
