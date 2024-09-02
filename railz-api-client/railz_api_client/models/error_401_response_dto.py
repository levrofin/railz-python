from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.error_401_dto import Error401Dto
    from ..models.error_401_response_dto_payload import Error401ResponseDtoPayload


T = TypeVar("T", bound="Error401ResponseDto")


@_attrs_define
class Error401ResponseDto:
    """
    Attributes:
        error (Error401Dto):
        payload (Error401ResponseDtoPayload):
    """

    error: "Error401Dto"
    payload: "Error401ResponseDtoPayload"
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
        from ..models.error_401_dto import Error401Dto
        from ..models.error_401_response_dto_payload import Error401ResponseDtoPayload

        d = src_dict.copy()
        error = Error401Dto.from_dict(d.pop("error"))

        payload = Error401ResponseDtoPayload.from_dict(d.pop("payload"))

        error_401_response_dto = cls(
            error=error,
            payload=payload,
        )

        error_401_response_dto.additional_properties = d
        return error_401_response_dto

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
