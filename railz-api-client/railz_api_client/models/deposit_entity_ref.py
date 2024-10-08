from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deposit_entity_ref_type import DepositEntityRefType, check_deposit_entity_ref_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="DepositEntityRef")


@_attrs_define
class DepositEntityRef:
    """
    Attributes:
        id (str):  Example: 1.
        type (DepositEntityRefType):  Example: vendor.
        name (Union[Unset, str]):  Example: ABC Inc..
    """

    id: str
    type: DepositEntityRefType
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type: str = self.type

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = check_deposit_entity_ref_type(d.pop("type"))

        name = d.pop("name", UNSET)

        deposit_entity_ref = cls(
            id=id,
            type=type,
            name=name,
        )

        deposit_entity_ref.additional_properties = d
        return deposit_entity_ref

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
