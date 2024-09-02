from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceLineItem")


@_attrs_define
class InvoiceLineItem:
    """
    Attributes:
        quantity (float):  Example: 3.
        description (Union[Unset, str]):  Example: Services rendered..
        inventory_ref (Union[Unset, str]):  Example: 240.
        location_ref (Union[Unset, str]):  Example: 3.
        account_ref (Union[Unset, str]):  Example: 145.
        discount_percentage (Union[Unset, float]):  Example: 30.
        sub_total (Union[Unset, float]):  Example: 301.5.
        total_amount (Union[Unset, float]):  Example: 322.
        unit_amount (Union[Unset, float]):  Example: 100.5.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        tax_ref (Union[Unset, str]):  Example: 24.
    """

    quantity: float
    description: Union[Unset, str] = UNSET
    inventory_ref: Union[Unset, str] = UNSET
    location_ref: Union[Unset, str] = UNSET
    account_ref: Union[Unset, str] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tax_ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity

        description = self.description

        inventory_ref = self.inventory_ref

        location_ref = self.location_ref

        account_ref = self.account_ref

        discount_percentage = self.discount_percentage

        sub_total = self.sub_total

        total_amount = self.total_amount

        unit_amount = self.unit_amount

        tax_amount = self.tax_amount

        tax_ref = self.tax_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if inventory_ref is not UNSET:
            field_dict["inventoryRef"] = inventory_ref
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if tax_ref is not UNSET:
            field_dict["taxRef"] = tax_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity = d.pop("quantity")

        description = d.pop("description", UNSET)

        inventory_ref = d.pop("inventoryRef", UNSET)

        location_ref = d.pop("locationRef", UNSET)

        account_ref = d.pop("accountRef", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        unit_amount = d.pop("unitAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        tax_ref = d.pop("taxRef", UNSET)

        invoice_line_item = cls(
            quantity=quantity,
            description=description,
            inventory_ref=inventory_ref,
            location_ref=location_ref,
            account_ref=account_ref,
            discount_percentage=discount_percentage,
            sub_total=sub_total,
            total_amount=total_amount,
            unit_amount=unit_amount,
            tax_amount=tax_amount,
            tax_ref=tax_ref,
        )

        invoice_line_item.additional_properties = d
        return invoice_line_item

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
