import requests
import time
from datetime import datetime

from app.logger import logger

SERVICES = {
    "GitHub API": "https://api.github.com",
    "Google": "https://www.google.com",
    "OpenAI": "https://api.openai.com"
}

failure_counts = {
    service: 0 for service in SERVICES
}


def classify_status(latency, failures):

    if failures >= 3 or latency > 2000:
        return "critical"

    elif latency > 500:
        return "degraded"

    return "healthy"


def check_services():

    results = []

    for service_name, url in SERVICES.items():

        try:

            start_time = time.time()

            response = requests.get(url, timeout=3)

            latency = round(
                (time.time() - start_time) * 1000,
                2
            )

            if response.status_code == 200:
                failure_counts[service_name] = 0

            status = classify_status(
                latency,
                failure_counts[service_name]
            )

            logger.info(
                f"{service_name} healthy - {latency}ms"
            )

            results.append({
                "service": service_name,
                "status": status,
                "response_time_ms": latency,
                "timestamp": datetime.utcnow().isoformat()
            })

        except Exception:

            failure_counts[service_name] += 1

            logger.error(
                f"{service_name} critical failure"
            )

            results.append({
                "service": service_name,
                "status": "critical",
                "response_time_ms": None,
                "timestamp": datetime.utcnow().isoformat()
            })

    return results