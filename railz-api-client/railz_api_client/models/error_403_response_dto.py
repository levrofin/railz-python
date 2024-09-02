from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.error_403_dto import Error403Dto
    from ..models.error_403_response_dto_payload import Error403ResponseDtoPayload


T = TypeVar("T", bound="Error403ResponseDto")


@_attrs_define
class Error403ResponseDto:
    """
    Attributes:
        error (Error403Dto):
        payload (Error403ResponseDtoPayload):
    """

    error: "Error403Dto"
    payload: "Error403ResponseDtoPayload"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error.to_dict()

        payload = self.payload.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "payload": payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_403_dto import Error403Dto
        from ..models.error_403_response_dto_payload import Error403ResponseDtoPayload

        d = src_dict.copy()
        error = Error403Dto.from_dict(d.pop("error"))

        payload = Error403ResponseDtoPayload.from_dict(d.pop("payload"))

        error_403_response_dto = cls(
            error=error,
            payload=payload,
        )

        error_403_response_dto.additional_properties = d
        return error_403_response_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
