from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryBillInvoiceLineItems")


@_attrs_define
class InventoryBillInvoiceLineItems:
    """
    Attributes:
        description (Union[Unset, str]):  Example: Item description..
        unit_price (Union[Unset, float]):  Example: 2.5.
        account_ref (Union[Unset, str]):  Example: 200.
        tax_rate_ref (Union[Unset, str]):  Example: 12.
    """

    description: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    account_ref: Union[Unset, str] = UNSET
    tax_rate_ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        unit_price = self.unit_price

        account_ref = self.account_ref

        tax_rate_ref = self.tax_rate_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        account_ref = d.pop("accountRef", UNSET)

        tax_rate_ref = d.pop("taxRateRef", UNSET)

        inventory_bill_invoice_line_items = cls(
            description=description,
            unit_price=unit_price,
            account_ref=account_ref,
            tax_rate_ref=tax_rate_ref,
        )

        inventory_bill_invoice_line_items.additional_properties = d
        return inventory_bill_invoice_line_items

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
