from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackingCategoryRef")


@_attrs_define
class TrackingCategoryRef:
    """
    Attributes:
        id (str):  Example: 4040.
        name (Union[Unset, str]):  Example: Region.
        option (Union[Unset, str]):  Example: East.
        option_id (Union[Unset, str]):  Example: 40401.
    """

    id: str
    name: Union[Unset, str] = UNSET
    option: Union[Unset, str] = UNSET
    option_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        option = self.option

        option_id = self.option_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if option is not UNSET:
            field_dict["option"] = option
        if option_id is not UNSET:
            field_dict["optionId"] = option_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        option = d.pop("option", UNSET)

        option_id = d.pop("optionId", UNSET)

        tracking_category_ref = cls(
            id=id,
            name=name,
            option=option,
            option_id=option_id,
        )

        tracking_category_ref.additional_properties = d
        return tracking_category_ref

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
