from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_ref_v2_type import EntityRefV2Type, check_entity_ref_v2_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityRefV2")


@_attrs_define
class EntityRefV2:
    """
    Attributes:
        id (str):  Example: 130.
        type (Union[Unset, EntityRefV2Type]):  Example: customer.
        name (Union[Unset, str]):  Example: ABC Inc.
    """

    id: str
    type: Union[Unset, EntityRefV2Type] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _type = d.pop("type", UNSET)
        type: Union[Unset, EntityRefV2Type]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_entity_ref_v2_type(_type)

        name = d.pop("name", UNSET)

        entity_ref_v2 = cls(
            id=id,
            type=type,
            name=name,
        )

        entity_ref_v2.additional_properties = d
        return entity_ref_v2

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
