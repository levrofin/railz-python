import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_payment_line import InvoicePaymentLine


T = TypeVar("T", bound="PushInvoicePayment")


@_attrs_define
class PushInvoicePayment:
    """
    Attributes:
        account_ref (Union[Unset, str]):  Example: 132.
        customer_ref (Union[Unset, str]):  Example: 250.
        invoice_ref (Union[Unset, str]):  Example: 250.
        total_amount (Union[Unset, float]):  Example: 200.5.
        currency (Union[Unset, str]):  Example: CAD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        lines (Union[Unset, List['InvoicePaymentLine']]):
        date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        memo (Union[Unset, str]):  Example: Invoice payment memo..
    """

    account_ref: Union[Unset, str] = UNSET
    customer_ref: Union[Unset, str] = UNSET
    invoice_ref: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    lines: Union[Unset, List["InvoicePaymentLine"]] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_ref = self.account_ref

        customer_ref = self.customer_ref

        invoice_ref = self.invoice_ref

        total_amount = self.total_amount

        currency = self.currency

        currency_rate = self.currency_rate

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        memo = self.memo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if invoice_ref is not UNSET:
            field_dict["invoiceRef"] = invoice_ref
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if lines is not UNSET:
            field_dict["lines"] = lines
        if date is not UNSET:
            field_dict["date"] = date
        if memo is not UNSET:
            field_dict["memo"] = memo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_payment_line import InvoicePaymentLine

        d = src_dict.copy()
        account_ref = d.pop("accountRef", UNSET)

        customer_ref = d.pop("customerRef", UNSET)

        invoice_ref = d.pop("invoiceRef", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = InvoicePaymentLine.from_dict(lines_item_data)

            lines.append(lines_item)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        memo = d.pop("memo", UNSET)

        push_invoice_payment = cls(
            account_ref=account_ref,
            customer_ref=customer_ref,
            invoice_ref=invoice_ref,
            total_amount=total_amount,
            currency=currency,
            currency_rate=currency_rate,
            lines=lines,
            date=date,
            memo=memo,
        )

        push_invoice_payment.additional_properties = d
        return push_invoice_payment

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
