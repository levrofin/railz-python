from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_tracking_category_ref_type import InvoiceTrackingCategoryRefType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceTrackingCategoryRef")


@_attrs_define
class InvoiceTrackingCategoryRef:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 4040.
        name (Union[Unset, str]):  Example: Region.
        type (Union[Unset, InvoiceTrackingCategoryRefType]):  Example: class.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, InvoiceTrackingCategoryRefType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, InvoiceTrackingCategoryRefType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = _type

        invoice_tracking_category_ref = cls(
            id=id,
            name=name,
            type=type,
        )

        invoice_tracking_category_ref.additional_properties = d
        return invoice_tracking_category_ref

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
