from datetime import datetime

alert_history = []

previous_states = {}


def process_alerts(services):

    alerts = []

    for service in services:

        name = service["service"]

        current_status = service["status"]

        previous_status = previous_states.get(name)

        # Trigger alert only if degraded -> critical
        if previous_status == "degraded" and current_status == "critical":

            alert = {
                "service": name,
                "previous_status": previous_status,
                "current_status": current_status,
                "response_time_ms": service["response_time_ms"],
                "timestamp": datetime.utcnow().isoformat()
            }

            alert_history.append(alert)

            alerts.append(alert)

        previous_states[name] = current_status

    return alerts


def get_alerts():

    return alert_history