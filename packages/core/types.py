from dataclasses import dataclass
from typing import Any

@dataclass
class Event:
    event_id: str
    event_type: str
    data: Any

@dataclass
class State:
    state_id: str
    data: Any
