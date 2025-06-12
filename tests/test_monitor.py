from app.monitor import REQUEST_COUNT, REQUEST_LATENCY


def test_metrics_counters():
    assert hasattr(REQUEST_COUNT, "labels")
    assert hasattr(REQUEST_LATENCY, "labels")
