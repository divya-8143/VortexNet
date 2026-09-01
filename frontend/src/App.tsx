import React, { useState } from 'react';
import { useAuthStore } from './store/authStore';
import { Sidebar } from './components/common/Sidebar';
import { Navbar } from './components/common/Navbar';
import { LoginPage } from './pages/LoginPage';
import { DashboardPage } from './pages/DashboardPage';
import { DevicesPage } from './pages/DevicesPage';
import { RouterSwitchPage } from './pages/RouterSwitchPage';
import { IpamPage } from './pages/IpamPage';
import { TopologyPage } from './pages/TopologyPage';
import { BandwidthPage } from './pages/BandwidthPage';
import { ConnectivityPage } from './pages/ConnectivityPage';
import { TrafficPage } from './pages/TrafficPage';
import { AlertsPage } from './pages/AlertsPage';
import { SyslogsPage } from './pages/SyslogsPage';
import { UsersPage } from './pages/UsersPage';
import { ReportsPage } from './pages/ReportsPage';
import { AuditPage } from './pages/AuditPage';

export const App: React.FC = () => {
  const { isAuthenticated } = useAuthStore();
  const [currentTab, setCurrentTab] = useState('dashboard');

  if (!isAuthenticated) {
    return <LoginPage />;
  }

  const renderContent = () => {
    switch (currentTab) {
      case 'dashboard':
        return <DashboardPage />;
      case 'devices':
        return <DevicesPage />;
      case 'router_switch':
        return <RouterSwitchPage />;
      case 'ipam':
        return <IpamPage />;
      case 'topology':
        return <TopologyPage />;
      case 'bandwidth':
        return <BandwidthPage />;
      case 'connectivity':
        return <ConnectivityPage />;
      case 'traffic':
        return <TrafficPage />;
      case 'alerts':
        return <AlertsPage />;
      case 'syslogs':
        return <SyslogsPage />;
      case 'users':
        return <UsersPage />;
      case 'reports':
        return <ReportsPage />;
      case 'audit':
        return <AuditPage />;
      default:
        return <DashboardPage />;
    }
  };

  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100">
      <Sidebar currentTab={currentTab} setCurrentTab={setCurrentTab} />
      <div className="flex-1 flex flex-col min-w-0">
        <Navbar />
        <main className="flex-1 p-6 overflow-y-auto">
          {renderContent()}
        </main>
      </div>
    </div>
  );
};

export default App;
