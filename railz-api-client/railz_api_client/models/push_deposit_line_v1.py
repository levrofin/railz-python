from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PushDepositLineV1")


@_attrs_define
class PushDepositLineV1:
    """
    Attributes:
        quantity (float):  Example: 4.
        unit_amount (float):  Example: 50.4.
        account_ref (str):  Example: 200.
        description (Union[Unset, str]):  Example: Services rendered..
        memo (Union[Unset, str]):  Example: Example memo..
        tax_ref (Union[Unset, str]):  Example: 45.
        sub_total (Union[Unset, float]):  Example: 202.0.
        total_amount (Union[Unset, float]):  Example: 197.05.
        tax_amount (Union[Unset, float]):  Example: 15.25.
    """

    quantity: float
    unit_amount: float
    account_ref: str
    description: Union[Unset, str] = UNSET
    memo: Union[Unset, str] = UNSET
    tax_ref: Union[Unset, str] = UNSET
    sub_total: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity

        unit_amount = self.unit_amount

        account_ref = self.account_ref

        description = self.description

        memo = self.memo

        tax_ref = self.tax_ref

        sub_total = self.sub_total

        total_amount = self.total_amount

        tax_amount = self.tax_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "unitAmount": unit_amount,
                "accountRef": account_ref,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if memo is not UNSET:
            field_dict["memo"] = memo
        if tax_ref is not UNSET:
            field_dict["taxRef"] = tax_ref
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity = d.pop("quantity")

        unit_amount = d.pop("unitAmount")

        account_ref = d.pop("accountRef")

        description = d.pop("description", UNSET)

        memo = d.pop("memo", UNSET)

        tax_ref = d.pop("taxRef", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        push_deposit_line_v1 = cls(
            quantity=quantity,
            unit_amount=unit_amount,
            account_ref=account_ref,
            description=description,
            memo=memo,
            tax_ref=tax_ref,
            sub_total=sub_total,
            total_amount=total_amount,
            tax_amount=tax_amount,
        )

        push_deposit_line_v1.additional_properties = d
        return push_deposit_line_v1

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
