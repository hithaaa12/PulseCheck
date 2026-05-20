const overallStatus = document.getElementById("overall-status");
const healthScore = document.getElementById("health-score");

const servicesContainer = document.getElementById("services-container");

const cpu = document.getElementById("cpu");
const memory = document.getElementById("memory");
const disk = document.getElementById("disk");

const alertsDiv = document.getElementById("alerts");

const serviceCount =
    document.getElementById("service-count");

const lastUpdated =
    document.getElementById("last-updated");
// Chart Setup
const ctx = document.getElementById("latencyChart").getContext("2d");

const latencyChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: [],
        datasets: [
            {
                label: "Average Latency (ms)",
                data: [],
                borderColor: "#38bdf8",
                backgroundColor: "rgba(56,189,248,0.2)",
                tension: 0.3
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                labels: {
                    color: "white"
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: "white"
                }
            },
            y: {
                ticks: {
                    color: "white"
                }
            }
        }
    }
});


// Fetch Health Data
async function fetchHealth() {

    const response = await fetch("http://127.0.0.1:8000/health");

    const data = await response.json();

    overallStatus.innerText =
        data.overall_status.toUpperCase();

    healthScore.innerText =
        `Health Score: ${data.health_score}%`;
        serviceCount.innerText =
    `Services Monitored: ${data.services.length}`;

lastUpdated.innerText =
    `Last Updated: ${new Date().toLocaleTimeString()}`;

    servicesContainer.innerHTML = "";

    let totalLatency = 0;

    data.services.forEach(service => {

        totalLatency += service.response_time_ms || 0;

        const card = document.createElement("div");

        card.classList.add("service-card");

        card.innerHTML = `
            <h3>${service.service}</h3>
            <p class="${service.status}">
                ${service.status.toUpperCase()}
            </p>
            <p>Latency: ${service.response_time_ms} ms</p>
        `;

        servicesContainer.appendChild(card);
    });

    // Update chart
    const avgLatency =
        totalLatency / data.services.length;

    const currentTime =
        new Date().toLocaleTimeString();

    latencyChart.data.labels.push(currentTime);

    latencyChart.data.datasets[0].data.push(avgLatency);

    if (latencyChart.data.labels.length > 10) {

        latencyChart.data.labels.shift();

        latencyChart.data.datasets[0].data.shift();
    }

    latencyChart.update();
}


// Fetch System Metrics
async function fetchMetrics() {

    const response =
        await fetch("http://127.0.0.1:8000/metrics");

    const data = await response.json();

    cpu.innerText =
        `${data.cpu_percent}%`;

    memory.innerText =
        `${data.memory_percent}%`;

    disk.innerText =
        `${data.disk_percent}%`;
}


// Fetch Alerts
async function fetchAlerts() {

    const response =
        await fetch("http://127.0.0.1:8000/alerts");

    const data = await response.json();

    alertsDiv.innerHTML = "";

    if (data.alerts.length === 0) {

        alertsDiv.innerHTML =
            "<p>No active alerts</p>";

        return;
    }

    data.alerts.forEach(alert => {

        const div = document.createElement("div");

        div.classList.add("alert-item");

        div.innerHTML = `
            <strong>${alert.service}</strong>
            transitioned from
            ${alert.previous_status}
            to
            ${alert.current_status}
        `;

        alertsDiv.appendChild(div);
    });
}


// Main Dashboard Refresh
async function refreshDashboard() {

    await fetchHealth();

    await fetchMetrics();

    await fetchAlerts();
}


// Initial Load
refreshDashboard();


// Auto Refresh Every 5 Seconds
setInterval(refreshDashboard, 5000);