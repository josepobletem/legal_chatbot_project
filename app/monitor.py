"""Módulo para instrumentación y monitoreo usando Prometheus en FastAPI."""

# pylint: disable=import-error
from prometheus_client import Counter, Histogram, make_asgi_app

# Métricas definidas para contar peticiones y medir latencia
REQUEST_COUNT = Counter("request_count", "Total HTTP Requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency", ["endpoint"])


def setup_monitoring(app):
    """
    Configura el middleware para capturar métricas HTTP y monta /metrics para Prometheus.

    Args:
        app (FastAPI): La aplicación FastAPI donde se integrará el monitoreo.
    """

    @app.middleware("http")
    async def metrics_middleware(request, call_next):
        endpoint = request.url.path
        method = request.method
        REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
        with REQUEST_LATENCY.labels(endpoint=endpoint).time():
            response = await call_next(request)
        return response

    app.mount("/metrics", make_asgi_app())
