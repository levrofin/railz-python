from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Property")


@_attrs_define
class Property:
    """
    Attributes:
        type (str):
        description (str):
        required (bool):
        enum_values (List[str]):
    """

    type: str
    description: str
    required: bool
    enum_values: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        description = self.description

        required = self.required

        enum_values = self.enum_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "description": description,
                "required": required,
                "enumValues": enum_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        description = d.pop("description")

        required = d.pop("required")

        enum_values = cast(List[str], d.pop("enumValues"))

        property_ = cls(
            type=type,
            description=description,
            required=required,
            enum_values=enum_values,
        )

        property_.additional_properties = d
        return property_

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
