from dataclasses import dataclass
from typing import Dict, Any, Optional
from bop_common.enums.event_type import EventType

@dataclass
class EventDTO:
    event_type: EventType
    payload: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'EventDTO':
        return EventDTO(
            event_type=EventType(data["event_type"]),
            payload=data["payload"]
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_type": self.event_type.value,
            "payload": self.payload
        }