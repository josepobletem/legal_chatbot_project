from prometheus_client import Counter, Histogram, make_asgi_app

REQUEST_COUNT = Counter("request_count", "Total HTTP Requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency", ["endpoint"])

def setup_monitoring(app):
    @app.middleware("http")
    async def metrics_middleware(request, call_next):
        endpoint = request.url.path
        method = request.method
        REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
        with REQUEST_LATENCY.labels(endpoint=endpoint).time():
            response = await call_next(request)
        return response

    app.mount("/metrics", make_asgi_app())
