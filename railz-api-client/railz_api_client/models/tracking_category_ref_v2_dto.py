from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracking_category_ref_v2_dto_type import (
    TrackingCategoryRefV2DtoType,
    check_tracking_category_ref_v2_dto_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackingCategoryRefV2Dto")


@_attrs_define
class TrackingCategoryRefV2Dto:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 4040.
        type (Union[Unset, TrackingCategoryRefV2DtoType]):  Example: class.
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, TrackingCategoryRefV2DtoType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TrackingCategoryRefV2DtoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_tracking_category_ref_v2_dto_type(_type)

        tracking_category_ref_v2_dto = cls(
            id=id,
            type=type,
        )

        tracking_category_ref_v2_dto.additional_properties = d
        return tracking_category_ref_v2_dto

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
