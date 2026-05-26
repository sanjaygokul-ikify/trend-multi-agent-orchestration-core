from packages.core import Engine
from packages.utils import logging

class Orchestrator:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
    
    def start(self) -> None:
        self.engine.start()
    
    def stop(self) -> None:
        self.engine.stop()
    
    def process_event(self, event: Engine.Event) -> None:
        self.engine.process_event(event)