from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.refund_tracking_category_ref_dto_type import (
    RefundTrackingCategoryRefDtoType,
    check_refund_tracking_category_ref_dto_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RefundTrackingCategoryRefDto")


@_attrs_define
class RefundTrackingCategoryRefDto:
    """
    Attributes:
        id (str):  Example: 4040.
        type (Union[Unset, RefundTrackingCategoryRefDtoType]):  Example: class.
    """

    id: str
    type: Union[Unset, RefundTrackingCategoryRefDtoType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _type = d.pop("type", UNSET)
        type: Union[Unset, RefundTrackingCategoryRefDtoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_refund_tracking_category_ref_dto_type(_type)

        refund_tracking_category_ref_dto = cls(
            id=id,
            type=type,
        )

        refund_tracking_category_ref_dto.additional_properties = d
        return refund_tracking_category_ref_dto

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
