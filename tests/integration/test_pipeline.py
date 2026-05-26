import unittest
from packages.core import Engine, Event
from packages.services import orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self) -> None:
        engine = Engine(None, None, None, None)
        orchestrator = orchestrator.Orchestrator(engine)
        
        orchestrator.start()
        event = Event('1', 'test', None)
        orchestrator.process_event(event)
        orchestrator.stop()