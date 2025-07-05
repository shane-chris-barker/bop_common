from bop_common.dtos.event_dto import EventDTO
from bop_common.enums.event_type import EventType

class TestEventDTO:

    def test_to_dict_no_payload(self):
        dto = EventDTO(event_type=EventType.BOP_DANCE)
        result = dto.to_dict()
        assert result == {
            'event_type': EventType.BOP_DANCE.value,
            'payload': None
        }

    def test_from_dict_no_payload(self):
        data = {
            'event_type': EventType.BOP_ANGRY.value,
            'payload': None
        }
        dto = EventDTO.from_dict(data)
        assert isinstance(dto, EventDTO)
        assert dto.event_type == EventType.BOP_ANGRY
        assert dto.payload is None

    def test_to_dict_with_payload(self):
        dto = EventDTO(
            event_type=EventType.BOP_DANCE,
            payload={'test':'test'}
        )
        result = dto.to_dict()
        assert result == {
            'event_type': EventType.BOP_DANCE.value,
            'payload': {'test':'test'}
        }

    def test_from_dict_with_payload(self):
        data = {
            'event_type': EventType.BOP_ANGRY.value,
            'payload': {'test':'test'}
        }

        dto = EventDTO.from_dict(data)
        assert isinstance(dto, EventDTO)
        assert dto.event_type == EventType.BOP_ANGRY
        assert dto.payload == {'test':'test'}