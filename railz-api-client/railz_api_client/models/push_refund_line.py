from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PushRefundLine")


@_attrs_define
class PushRefundLine:
    """
    Attributes:
        inventory_ref (Union[Unset, str]):  Example: 32.
        tax_ref (Union[Unset, str]):  Example: 2.
        total_amount (Union[Unset, float]):  Example: 12.88.
    """

    inventory_ref: Union[Unset, str] = UNSET
    tax_ref: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inventory_ref = self.inventory_ref

        tax_ref = self.tax_ref

        total_amount = self.total_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory_ref is not UNSET:
            field_dict["inventoryRef"] = inventory_ref
        if tax_ref is not UNSET:
            field_dict["taxRef"] = tax_ref
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        inventory_ref = d.pop("inventoryRef", UNSET)

        tax_ref = d.pop("taxRef", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        push_refund_line = cls(
            inventory_ref=inventory_ref,
            tax_ref=tax_ref,
            total_amount=total_amount,
        )

        push_refund_line.additional_properties = d
        return push_refund_line

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
