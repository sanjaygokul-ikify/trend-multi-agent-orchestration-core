import logging
from typing import List
from ..core.types import Event
from ..core.engine import Engine

# Set up a logger for the executor
logger = logging.getLogger(__name__)


class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.running = False

    def start(self) -> None:
        self.running = True
        logger.info('Executor started')

    def stop(self) -> None:
        self.running = False
        logger.info('Executor stopped')

    def execute(self, events: List[Event]) -> None:
        for event in events:
            self.engine.process_event(event)
