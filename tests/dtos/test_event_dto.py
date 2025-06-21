import pytest
from bop_common.dtos.event_dto import EventDTO
from bop_common.enums.event_type import EventType

class TestEventDTO:

    def test_to_dict(self):
        dto = EventDTO(event_type=EventType.BOP_DANCE)
        result = dto.to_dict()
        assert result == {
            'event_type': EventType.BOP_DANCE.value,
        }

    def test_from_dict(self):
        data = {
            'event_type': EventType.BOP_ANGRY.value,
        }

        dto = EventDTO.from_dict(data)
        assert isinstance(dto, EventDTO)
        assert dto.event_type == EventType.BOP_ANGRY