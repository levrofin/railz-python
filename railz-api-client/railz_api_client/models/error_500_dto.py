from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Error500Dto")


@_attrs_define
class Error500Dto:
    """
    Attributes:
        error (str):  Example: Internal Server Error.
        message (List[str]):  Example: ['INTERNAL_ERROR'].
        status_code (float):  Example: 500.
    """

    error: str
    message: List[str]
    status_code: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error

        message = self.message

        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
                "statusCode": status_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error")

        message = cast(List[str], d.pop("message"))

        status_code = d.pop("statusCode")

        error_500_dto = cls(
            error=error,
            message=message,
            status_code=status_code,
        )

        error_500_dto.additional_properties = d
        return error_500_dto

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
