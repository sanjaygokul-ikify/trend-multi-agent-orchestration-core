import logging
from typing import List, Dict
from .types import Event, State
from .exceptions import InvalidEventError, StateInconsistencyError

# Set up a logger for the engine
logger = logging.getLogger(__name__)


class Engine:
    def __init__(self, state_replicator, event_log, reconciliation_engine, control_plane):
        self.state_replicator = state_replicator
        self.event_log = event_log
        self.reconciliation_engine = reconciliation_engine
        self.control_plane = control_plane
        self.running = False

    def start(self) -> None:
        self.running = True
        logger.info('Engine started')

    def stop(self) -> None:
        self.running = False
        logger.info('Engine stopped')

    def process_event(self, event: Event) -> None:
        if not isinstance(event, Event):
            logger.error(f'Invalid event: {event}')
            raise InvalidEventError('Invalid event')

        try:
            # Apply the event to the state replicator
            self.state_replicator.apply_event(event)
        except Exception as e:
            logger.error(f'Failed to apply event: {e}')
            raise StateInconsistencyError('Failed to apply event')

        # Add the event to the event log
        self.event_log.add_event(event)

        # Reconcile the state with the event log
        self.reconciliation_engine.reconcile()

    def reconcile(self) -> None:
        # Reconcile the state replicator with the event log
        self.reconciliation_engine.reconcile()

    def get_state(self) -> State:
        return self.state_replicator.get_state()

    def apply_temporal_logic(self, workflow_definition: Dict[str, str]) -> None:
        # Apply the temporal logic workflow definition to the state replicator
        self.state_replicator.apply_temporal_logic(workflow_definition)

    def apply_realtime_reconfiguration(self, reconfiguration: Dict[str, str]) -> None:
        # Apply the real-time reconfiguration to the control plane
        self.control_plane.apply_reconfiguration(reconfiguration)
