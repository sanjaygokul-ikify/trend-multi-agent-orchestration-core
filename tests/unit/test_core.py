import unittest
from packages.core import Engine, Event, State
from packages.core.exceptions import InvalidEventError

class TestCore(unittest.TestCase):
    def test_engine_start(self) -> None:
        engine = Engine(None, None, None, None)
        engine.start()
        self.assertTrue(engine.running)
    
    def test_engine_stop(self) -> None:
        engine = Engine(None, None, None, None)
        engine.start()
        engine.stop()
        self.assertFalse(engine.running)
    
    def test_process_event(self) -> None:
        engine = Engine(None, None, None, None)
        event = Event('1', 'test', None)
        engine.process_event(event)
    
    def test_invalid_event(self) -> None:
        engine = Engine(None, None, None, None)
        with self.assertRaises(InvalidEventError):
            engine.process_event('invalid event')