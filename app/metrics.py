import psutil
from datetime import datetime


def get_system_metrics():

    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage('/')

    return {
        "cpu_percent": cpu_usage,
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "timestamp": datetime.utcnow().isoformat()
    }