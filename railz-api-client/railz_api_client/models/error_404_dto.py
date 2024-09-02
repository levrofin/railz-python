from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Error404Dto")


@_attrs_define
class Error404Dto:
    """
    Attributes:
        status_code (float):  Example: 404.
        message (List[str]):  Example: ['Not Found'].
        error (str):  Example: Not Found.
    """

    status_code: float
    message: List[str]
    error: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_code = self.status_code

        message = self.message

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statusCode": status_code,
                "message": message,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_code = d.pop("statusCode")

        message = cast(List[str], d.pop("message"))

        error = d.pop("error")

        error_404_dto = cls(
            status_code=status_code,
            message=message,
            error=error,
        )

        error_404_dto.additional_properties = d
        return error_404_dto

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
