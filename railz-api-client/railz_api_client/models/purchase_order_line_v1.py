from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderLineV1")


@_attrs_define
class PurchaseOrderLineV1:
    """
    Attributes:
        quantity (float):  Example: 4.
        unit_amount (float):  Example: 50.4.
        description (Union[Unset, str]):  Example: Services rendered..
        discount_percentage (Union[Unset, float]):  Example: 10.0.
        tax_amount (Union[Unset, float]):  Example: 15.25.
        sub_total (Union[Unset, float]):  Example: 202.0.
        total_amount (Union[Unset, float]):  Example: 197.05.
        account_ref (Union[Unset, str]):  Example: 12.
        tax_ref (Union[Unset, str]):  Example: 45.
        inventory_ref (Union[Unset, str]):  Example: 32.
        memo (Union[Unset, str]):  Example: Example memo..
    """

    quantity: float
    unit_amount: float
    description: Union[Unset, str] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    account_ref: Union[Unset, str] = UNSET
    tax_ref: Union[Unset, str] = UNSET
    inventory_ref: Union[Unset, str] = UNSET
    memo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity

        unit_amount = self.unit_amount

        description = self.description

        discount_percentage = self.discount_percentage

        tax_amount = self.tax_amount

        sub_total = self.sub_total

        total_amount = self.total_amount

        account_ref = self.account_ref

        tax_ref = self.tax_ref

        inventory_ref = self.inventory_ref

        memo = self.memo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "unitAmount": unit_amount,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tax_ref is not UNSET:
            field_dict["taxRef"] = tax_ref
        if inventory_ref is not UNSET:
            field_dict["inventoryRef"] = inventory_ref
        if memo is not UNSET:
            field_dict["memo"] = memo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity = d.pop("quantity")

        unit_amount = d.pop("unitAmount")

        description = d.pop("description", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        account_ref = d.pop("accountRef", UNSET)

        tax_ref = d.pop("taxRef", UNSET)

        inventory_ref = d.pop("inventoryRef", UNSET)

        memo = d.pop("memo", UNSET)

        purchase_order_line_v1 = cls(
            quantity=quantity,
            unit_amount=unit_amount,
            description=description,
            discount_percentage=discount_percentage,
            tax_amount=tax_amount,
            sub_total=sub_total,
            total_amount=total_amount,
            account_ref=account_ref,
            tax_ref=tax_ref,
            inventory_ref=inventory_ref,
            memo=memo,
        )

        purchase_order_line_v1.additional_properties = d
        return purchase_order_line_v1

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
