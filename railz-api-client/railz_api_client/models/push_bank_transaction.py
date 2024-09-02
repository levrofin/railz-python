import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.push_bank_transaction_transaction_type import PushBankTransactionTransactionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_bank_transaction_line import PushBankTransactionLine


T = TypeVar("T", bound="PushBankTransaction")


@_attrs_define
class PushBankTransaction:
    """
    Attributes:
        transaction_type (PushBankTransactionTransactionType):  Example: payment.
        bank_account_ref (str):  Example: 090.
        lines (List['PushBankTransactionLine']):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        currency (Union[Unset, str]):  Example: CAD.
        customer_ref (Union[Unset, str]):  Example: 6d42f03b-181f-43e3-93fb-2025c012de92.
        vendor_ref (Union[Unset, str]):  Example: 6d42f03b-181f-43e3-93fb-2025c012de92.
        date (Union[Unset, datetime.date]):  Example: 2021-03-29.
    """

    transaction_type: PushBankTransactionTransactionType
    bank_account_ref: str
    lines: List["PushBankTransactionLine"]
    currency_rate: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    customer_ref: Union[Unset, str] = UNSET
    vendor_ref: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_type = self.transaction_type

        bank_account_ref = self.bank_account_ref

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        currency_rate = self.currency_rate

        currency = self.currency

        customer_ref = self.customer_ref

        vendor_ref = self.vendor_ref

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactionType": transaction_type,
                "bankAccountRef": bank_account_ref,
                "lines": lines,
            }
        )
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if currency is not UNSET:
            field_dict["currency"] = currency
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_bank_transaction_line import PushBankTransactionLine

        d = src_dict.copy()
        transaction_type = d.pop("transactionType")

        bank_account_ref = d.pop("bankAccountRef")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = PushBankTransactionLine.from_dict(lines_item_data)

            lines.append(lines_item)

        currency_rate = d.pop("currencyRate", UNSET)

        currency = d.pop("currency", UNSET)

        customer_ref = d.pop("customerRef", UNSET)

        vendor_ref = d.pop("vendorRef", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        push_bank_transaction = cls(
            transaction_type=transaction_type,
            bank_account_ref=bank_account_ref,
            lines=lines,
            currency_rate=currency_rate,
            currency=currency,
            customer_ref=customer_ref,
            vendor_ref=vendor_ref,
            date=date,
        )

        push_bank_transaction.additional_properties = d
        return push_bank_transaction

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
