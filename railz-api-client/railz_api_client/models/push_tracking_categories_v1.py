from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PushTrackingCategoriesV1")


@_attrs_define
class PushTrackingCategoriesV1:
    """
    Attributes:
        name (str):  Example: Region.
        parent_ref (Union[Unset, str]):  Example: 1334.
    """

    name: str
    parent_ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        parent_ref = self.parent_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        parent_ref = d.pop("parentRef", UNSET)

        push_tracking_categories_v1 = cls(
            name=name,
            parent_ref=parent_ref,
        )

        push_tracking_categories_v1.additional_properties = d
        return push_tracking_categories_v1

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
