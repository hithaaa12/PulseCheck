# PulseCheck — DevOps Observability Platform

PulseCheck is a lightweight DevOps-oriented observability and monitoring platform designed to monitor external services, collect infrastructure metrics, visualize operational health in real time, and automate deployment workflows using containerization and CI/CD practices.

---

# Features

## Real-Time Service Monitoring
- Monitors external APIs such as GitHub, Google, and OpenAI
- Measures response latency
- Performs health classification:
  - Healthy
  - Degraded
  - Critical

## Infrastructure Metrics
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring

## Historical Monitoring Engine
- Stores rolling monitoring snapshots
- Tracks latency trends over time
- Powers live dashboard graphing

## Alerting System
- Detects degraded-to-critical transitions
- Generates operational alerts
- Maintains alert history

## Structured Logging
- Persistent operational logs
- INFO and ERROR severity tracking
- Production-style monitoring logs

## Live Dashboard
- Real-time observability dashboard
- Live latency visualization
- Infrastructure metrics display
- Operational status cards

## Containerization
- Fully containerized using Docker
- Multi-container orchestration using Docker Compose

## CI/CD Automation
- GitHub Actions pipeline
- Automated testing
- Docker image build validation
- Deployment simulation
- Health endpoint verification

## Infrastructure-as-Code
- AWS CloudFormation template
- ECS Fargate deployment architecture

---

# Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| Monitoring | psutil, requests |
| Containerization | Docker |
| Orchestration | Docker Compose |
| CI/CD | GitHub Actions |
| IaC | AWS CloudFormation |
| Web Server | NGINX |

---

# Architecture Overview

```text
Dashboard UI
     ↓
FastAPI Monitoring API
     ↓
Health Check Engine
     ↓
External Services + System Metrics
```

# Architecture Diagram

![Architecture Diagram](assets/architecture-diagram.png)

# Project Structure

```text
PulseCheck/
│
├── app/
│   ├── main.py
│   ├── health_checker.py
│   ├── metrics.py
│   ├── alerts.py
│   └── logger.py
│
├── dashboard/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── Dockerfile
│
├── infrastructure/
│   └── cloudformation.yaml
│
├── tests/
│   └── test_health.py
│
├── assets/
│   ├── dashboard-main.png
│   ├── dashboard-metrics.png
│   ├── github-actions.png
│   ├── docker-compose.png
│   └── architecture-diagram.png
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```


# Screenshots

# Monitoring Dashboard

## Real-Time Service Monitoring

![Dashboard Main](assets/dashboard-main.png)

---

## Infrastructure Metrics & Alerts

![Dashboard Metrics](assets/dashboard-metrics.png)

## CI/CD Pipeline

![GitHub Actions](assets/github-actions.png)

---

## Docker Compose Deployment

![Docker Compose](assets/docker-compose.png)

---

## Health API Response

![API Response](assets/api-response.png)

# Demo Video

A complete walkthrough demonstrating:
- Docker Compose deployment
- Real-time observability dashboard
- Monitoring APIs
- GitHub Actions CI/CD
- Infrastructure architecture

[Watch Demo Video](https://drive.google.com/file/d/1a4o6_r4z7VGYW_nuDI_ak13xGqw61IUU/view?usp=sharing)

# Future Improvements

- Prometheus integration for advanced metrics collection
- Grafana dashboards for enterprise-grade visualization
- Slack/Webhook alert integrations
- Kubernetes deployment using Minikube or EKS
- Persistent database storage for long-term monitoring history
- Authentication and role-based access control
- Real-time WebSocket monitoring updates
- Distributed service discovery support