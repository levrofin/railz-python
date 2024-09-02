from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillPaymentLine")


@_attrs_define
class BillPaymentLine:
    """
    Attributes:
        bill_ref (str):  Example: 3n2.
        amount (Union[Unset, float]):  Example: 342.99.
        memo (Union[Unset, str]):  Example: Sample memo for transaction.
    """

    bill_ref: str
    amount: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bill_ref = self.bill_ref

        amount = self.amount

        memo = self.memo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billRef": bill_ref,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if memo is not UNSET:
            field_dict["memo"] = memo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bill_ref = d.pop("billRef")

        amount = d.pop("amount", UNSET)

        memo = d.pop("memo", UNSET)

        bill_payment_line = cls(
            bill_ref=bill_ref,
            amount=amount,
            memo=memo,
        )

        bill_payment_line.additional_properties = d
        return bill_payment_line

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
