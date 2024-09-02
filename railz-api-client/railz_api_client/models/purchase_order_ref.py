from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderRef")


@_attrs_define
class PurchaseOrderRef:
    """
    Attributes:
        id (str):  Example: 15.
        purchase_order_number (Union[Unset, str]):  Example: 1500.
    """

    id: str
    purchase_order_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        purchase_order_number = self.purchase_order_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if purchase_order_number is not UNSET:
            field_dict["purchaseOrderNumber"] = purchase_order_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        purchase_order_number = d.pop("purchaseOrderNumber", UNSET)

        purchase_order_ref = cls(
            id=id,
            purchase_order_number=purchase_order_number,
        )

        purchase_order_ref.additional_properties = d
        return purchase_order_ref

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
