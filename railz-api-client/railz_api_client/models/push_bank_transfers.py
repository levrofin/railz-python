import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PushBankTransfers")


@_attrs_define
class PushBankTransfers:
    """
    Attributes:
        total_amount (float):  Example: 150.50.
        from_account_ref (str):  Example: 562555f2-8cde-4ce9-8203-0363922537a4.
        to_account_ref (str):  Example: 72f1dcfe-5d7d-4239-bf9d-e12469309716.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        date (Union[Unset, datetime.date]):  Example: 2021-03-09.
        memo (Union[Unset, str]):  Example: Services rendered..
        currency (Union[Unset, str]):  Example: CAD.
    """

    total_amount: float
    from_account_ref: str
    to_account_ref: str
    currency_rate: Union[Unset, float] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_amount = self.total_amount

        from_account_ref = self.from_account_ref

        to_account_ref = self.to_account_ref

        currency_rate = self.currency_rate

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        memo = self.memo

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalAmount": total_amount,
                "fromAccountRef": from_account_ref,
                "toAccountRef": to_account_ref,
            }
        )
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if date is not UNSET:
            field_dict["date"] = date
        if memo is not UNSET:
            field_dict["memo"] = memo
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_amount = d.pop("totalAmount")

        from_account_ref = d.pop("fromAccountRef")

        to_account_ref = d.pop("toAccountRef")

        currency_rate = d.pop("currencyRate", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        push_bank_transfers = cls(
            total_amount=total_amount,
            from_account_ref=from_account_ref,
            to_account_ref=to_account_ref,
            currency_rate=currency_rate,
            date=date,
            memo=memo,
            currency=currency,
        )

        push_bank_transfers.additional_properties = d
        return push_bank_transfers

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
