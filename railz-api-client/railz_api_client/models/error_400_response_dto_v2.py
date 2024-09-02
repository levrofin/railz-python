from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.error_400_dto_v2 import Error400DtoV2
    from ..models.error_400_response_dto_v2_payload import Error400ResponseDtoV2Payload


T = TypeVar("T", bound="Error400ResponseDtoV2")


@_attrs_define
class Error400ResponseDtoV2:
    """
    Attributes:
        error (Error400DtoV2):
        payload (Error400ResponseDtoV2Payload):
    """

    error: "Error400DtoV2"
    payload: "Error400ResponseDtoV2Payload"
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
        from ..models.error_400_dto_v2 import Error400DtoV2
        from ..models.error_400_response_dto_v2_payload import Error400ResponseDtoV2Payload

        d = src_dict.copy()
        error = Error400DtoV2.from_dict(d.pop("error"))

        payload = Error400ResponseDtoV2Payload.from_dict(d.pop("payload"))

        error_400_response_dto_v2 = cls(
            error=error,
            payload=payload,
        )

        error_400_response_dto_v2.additional_properties = d
        return error_400_response_dto_v2

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
