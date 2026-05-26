import unittest
from packages.utils import metrics

class TestRuntime(unittest.TestCase):
    def test_metrics(self) -> None:
        metrics_obj = metrics.Metrics()
        metrics_obj.log_metrics()