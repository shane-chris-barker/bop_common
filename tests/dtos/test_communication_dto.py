from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.enums.hardware_type import HardwareType
def test_from_dict_creates_dto_correctly():
    data = {"input":"mic", "content":"Peace and love"}
    dto = CommunicationDTO.from_dict(data)
    assert dto.input == HardwareType.MIC
    assert dto.content ==  "Peace and love"

def test_to_dict_outputs_the_correct_format():
    dto = CommunicationDTO(
        input=HardwareType.CAMERA,
        content={"data": "Base64Image"}
    )
    result = dto.to_dict()
    assert result == {
        "input": "camera",
        "content": {"data": "Base64Image"}
    }