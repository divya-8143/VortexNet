# VortexNet – Network Monitoring & Management Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Backend-FastAPI%20%7C%20Python%203.11-green)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-React%2018%20%7C%20TypeScript-blue)](https://reactjs.org/)
[![Tailwind CSS](https://img.shields.io/badge/UI-Tailwind%20CSS-38bdf8)](https://tailwindcss.com/)

**VortexNet** is an enterprise-grade, full-stack Network Monitoring and Operations Platform designed for Network Operations Centers (NOC), system administrators, and infrastructure engineers. The platform provides real-time telemetry, interactive network topology, IP address management (IPAM), bandwidth monitoring, NetFlow traffic analytics, automated alert/incident workflows, and live syslog consoles.

---

## 🌟 Key Functional Modules (14 Enterprise Modules)

1. **Network Device Management**: Multi-vendor inventory (Cisco, Juniper, Arista, Palo Alto, Fortinet, Aruba), CPU/RAM telemetry, firmware version tracking, physical rack locations.
2. **Router & Switch Management**: Interface port manager (Up/Down/AdminDown status, RX/TX counters), VLAN configuration, and RIB routing table inspection.
3. **Device Health Monitoring**: Real-time CPU load per core, RAM usage, chassis temperature sensors, and uptime tracking.
4. **IP Address Management (IPAM)**: Subnet hierarchy (CIDR block allocations), static vs DHCP lease tracking, gateway associations, and PTR DNS mapping.
5. **Interactive Network Topology**: Visual link canvas linking core routers, distribution switches, and firewalls with live capacity and status indicators.
6. **Bandwidth & Port Utilization**: Inbound and outbound throughput graphs (bps/Mbps/Gbps), utilization percentages, and peak vs average throughput analysis.
7. **Connectivity & SLA Monitoring**: Synthetic ICMP Ping Echo probes, HTTP service endpoint uptime tracking, RTT latency, jitter, and packet loss matrices.
8. **Network Traffic Analytics**: NetFlow v9 / IPFIX flow collector, Top Talkers host analysis, and protocol breakdown (HTTPS, HTTP, SSH, DNS, BGP).
9. **Alerts & Incident Management**: Threshold alert triggers (CPU > 85%, RAM > 90%), severity levels (`Critical`, `Major`, `Warning`), and incident lifecycle workflows (`Triggered` -> `Acknowledged` -> `Resolved`).
10. **Network Syslog Console**: RFC 5424 / RFC 3164 syslog receiver stream, log severity filters (`Emergency`, `Critical`, `Warning`, `Info`), and full-text log search.
11. **User & Role-Based Access Control (RBAC)**: Role hierarchy (`Super Admin`, `Network Engineer`, `NOC Operator`, `Read-Only Viewer`), JWT auth, and password hashing.
12. **NOC Dashboard & Reports**: Real-time KPI summary cards, time-series chart grid, and downloadable CSV/PDF audit reports.
13. **REST APIs & Webhooks**: OpenAPI 3.0 (Swagger UI) compliant REST endpoints and webhook triggers.
14. **Audit Trail**: Immutable system audit logging tracking user actions, IP addresses, timestamps, and diff payloads.

---

## 🏗️ System Architecture & Stack

```
+-----------------------------------------------------------------------------------+
|                            VortexNet Web UI (React + TS)                          |
|  - NOC Dashboard  - Device Manager  - IPAM Subnets  - Interactive Topology Canvas  |
|  - Bandwidth Charts  - Traffic Analytics  - Incident Board  - Syslog Terminal     |
+-----------------------------------------+-----------------------------------------+
                                          | REST API / WebSockets
                                          v
+-----------------------------------------------------------------------------------+
|                           VortexNet Backend (FastAPI / Py)                        |
|  - REST API Router & Controllers          - JWT Security & RBAC Middleware          |
|  - Business Logic Services & IPAM Engine  - Telemetry Generator & Alert Evaluator   |
+-----------------------------------------+-----------------------------------------+
                                          |
                        +-----------------+-----------------+
                        v                                   v
+---------------------------------------+ +---------------------------------------+
|  Relational Database (SQLAlchemy)    | |  Synthetic Network Simulation Engine  |
|  - Devices, Interfaces, Subnets, IPs  | |  - SNMP MIB-II Telemetry Simulator    |
|  - Alerts, Incidents, Syslogs, Audits | |  - NetFlow v9 Traffic Generator       |
+---------------------------------------+ +---------------------------------------+
```

---

## 🛠️ Quick Start Guide

### 1. Backend Setup & Data Seeding

```bash
# Install Python dependencies
pip install -r requirements.txt

# Seed initial database with synthetic network devices, subnets, and RBAC users
python scripts/seed_generator.py

# Launch FastAPI Backend Server (Runs on http://localhost:8000)
uvicorn backend.main:app --reload --port 8000
```

### 2. Frontend Setup

```bash
# Install Node dependencies
npm install

# Start Vite Development Server (Runs on http://localhost:3000)
npm run dev
```

---

## 🧪 Automated Testing Suite

To execute the automated test suites:

```bash
# Run pytest for backend integration & simulation tests
pytest backend/tests
```

Default Demo Credentials:
- **Username**: `admin`
- **Password**: `admin123`
