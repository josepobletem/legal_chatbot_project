"""
Tests para validar los objetos de métricas Prometheus definidos en monitor.py.
"""

from app.monitor import REQUEST_COUNT, REQUEST_LATENCY


def test_metrics_counters():
    """
    Verifica que los objetos de métricas expongan el método 'labels'.

    Asegura que los contadores y histogramas definidos para monitoreo
    permiten etiquetado dinámico con `.labels(...)`, como requiere Prometheus.

    Returns
    -------
    None
    """
    assert hasattr(REQUEST_COUNT, "labels")
    assert hasattr(REQUEST_LATENCY, "labels")
