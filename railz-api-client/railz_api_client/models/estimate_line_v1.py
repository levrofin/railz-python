from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EstimateLineV1")


@_attrs_define
class EstimateLineV1:
    """
    Attributes:
        description (Union[Unset, str]):  Example: Services rendered..
        quantity (Union[Unset, float]):  Example: 4.
        unit_amount (Union[Unset, float]):  Example: 50.5.
        discount_percentage (Union[Unset, float]):  Example: 10.0.
        sub_total (Union[Unset, float]):  Example: 202.0.
        tax_amount (Union[Unset, float]):  Example: 45.
        total_amount (Union[Unset, float]):  Example: 15.25.
        account_ref (Union[Unset, str]):  Example: 200.
        tax_ref (Union[Unset, str]):  Example: 197.05.
        inventory_ref (Union[Unset, str]):  Example: BOOK.
    """

    description: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    account_ref: Union[Unset, str] = UNSET
    tax_ref: Union[Unset, str] = UNSET
    inventory_ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        quantity = self.quantity

        unit_amount = self.unit_amount

        discount_percentage = self.discount_percentage

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        total_amount = self.total_amount

        account_ref = self.account_ref

        tax_ref = self.tax_ref

        inventory_ref = self.inventory_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tax_ref is not UNSET:
            field_dict["taxRef"] = tax_ref
        if inventory_ref is not UNSET:
            field_dict["inventoryRef"] = inventory_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        quantity = d.pop("quantity", UNSET)

        unit_amount = d.pop("unitAmount", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        account_ref = d.pop("accountRef", UNSET)

        tax_ref = d.pop("taxRef", UNSET)

        inventory_ref = d.pop("inventoryRef", UNSET)

        estimate_line_v1 = cls(
            description=description,
            quantity=quantity,
            unit_amount=unit_amount,
            discount_percentage=discount_percentage,
            sub_total=sub_total,
            tax_amount=tax_amount,
            total_amount=total_amount,
            account_ref=account_ref,
            tax_ref=tax_ref,
            inventory_ref=inventory_ref,
        )

        estimate_line_v1.additional_properties = d
        return estimate_line_v1

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
