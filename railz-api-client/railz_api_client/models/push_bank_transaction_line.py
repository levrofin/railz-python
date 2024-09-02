from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PushBankTransactionLine")


@_attrs_define
class PushBankTransactionLine:
    """
    Attributes:
        quantity (float):  Example: 4.
        unit_amount (float):  Example: 50.5.
        description (str):  Example: Services rendered..
        account_ref (str):  Example: 200.
        sub_total (Union[Unset, float]):  Example: 202.0.
        total_amount (Union[Unset, float]):  Example: 217.25.
        tax_ref (Union[Unset, str]):  Example: 45.
        memo (Union[Unset, str]):  Example: Example memo..
        tax_amount (Union[Unset, float]):  Example: 15.25.
    """

    quantity: float
    unit_amount: float
    description: str
    account_ref: str
    sub_total: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    tax_ref: Union[Unset, str] = UNSET
    memo: Union[Unset, str] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity

        unit_amount = self.unit_amount

        description = self.description

        account_ref = self.account_ref

        sub_total = self.sub_total

        total_amount = self.total_amount

        tax_ref = self.tax_ref

        memo = self.memo

        tax_amount = self.tax_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "unitAmount": unit_amount,
                "description": description,
                "accountRef": account_ref,
            }
        )
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if tax_ref is not UNSET:
            field_dict["taxRef"] = tax_ref
        if memo is not UNSET:
            field_dict["memo"] = memo
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity = d.pop("quantity")

        unit_amount = d.pop("unitAmount")

        description = d.pop("description")

        account_ref = d.pop("accountRef")

        sub_total = d.pop("subTotal", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        tax_ref = d.pop("taxRef", UNSET)

        memo = d.pop("memo", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        push_bank_transaction_line = cls(
            quantity=quantity,
            unit_amount=unit_amount,
            description=description,
            account_ref=account_ref,
            sub_total=sub_total,
            total_amount=total_amount,
            tax_ref=tax_ref,
            memo=memo,
            tax_amount=tax_amount,
        )

        push_bank_transaction_line.additional_properties = d
        return push_bank_transaction_line

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
