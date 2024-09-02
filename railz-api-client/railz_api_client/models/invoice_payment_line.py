from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoicePaymentLine")


@_attrs_define
class InvoicePaymentLine:
    """
    Attributes:
        amount (float):  Example: 342.99.
        invoice_ref (Union[Unset, str]):  Example: 3n2.
        memo (Union[Unset, str]):  Example: Sample memo for transaction.
    """

    amount: float
    invoice_ref: Union[Unset, str] = UNSET
    memo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        invoice_ref = self.invoice_ref

        memo = self.memo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
            }
        )
        if invoice_ref is not UNSET:
            field_dict["invoiceRef"] = invoice_ref
        if memo is not UNSET:
            field_dict["memo"] = memo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount")

        invoice_ref = d.pop("invoiceRef", UNSET)

        memo = d.pop("memo", UNSET)

        invoice_payment_line = cls(
            amount=amount,
            invoice_ref=invoice_ref,
            memo=memo,
        )

        invoice_payment_line.additional_properties = d
        return invoice_payment_line

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
