from fastapi import FastAPI
from datetime import datetime
from app.metrics import get_system_metrics
from app.health_checker import check_services
from app.history import add_to_history, get_history
from app.alerts import process_alerts, get_alerts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PulseCheck",
    description="Lightweight DevOps Observability Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "PulseCheck API Running"
    }

@app.get("/health")
def health_check():

    services = check_services()
    alerts = process_alerts(services)

    healthy_count = sum(
        1 for service in services
        if service["status"] == "healthy"
    )

    health_score = round(
        (healthy_count / len(services)) * 100
    )
    snapshot = {
        "timestamp": datetime.utcnow().isoformat(),
        "health_score": health_score,
        "services": services
    }

    add_to_history(snapshot)
    return {
    "overall_status": (
        "healthy"
        if health_score >= 70
        else "degraded"
    ),
    "health_score": health_score,
    "timestamp": datetime.utcnow().isoformat(),
    "services": services,
    "alerts_triggered": alerts
}


@app.get("/services")
def services_status():
    return {
        "services": check_services()
    }

@app.get("/metrics")
def metrics():
    return get_system_metrics()

@app.get("/history")
def history():
    return {
        "history": get_history()
    }

@app.get("/alerts")
def alerts():
    return {
        "alerts": get_alerts()
    }