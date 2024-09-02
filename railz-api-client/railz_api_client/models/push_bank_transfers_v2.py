import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.push_bank_transfers_v2_pass_through import PushBankTransfersV2PassThrough


T = TypeVar("T", bound="PushBankTransfersV2")


@_attrs_define
class PushBankTransfersV2:
    """
    Attributes:
        total_amount (float):  Example: 150.50.
        from_account_ref (AccountRefDto):
        to_account_ref (AccountRefDto):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        date (Union[Unset, datetime.date]):  Example: 2021-03-09.
        memo (Union[Unset, str]):  Example: Services rendered..
        currency (Union[Unset, str]):  Example: CAD.
        pass_through (Union[Unset, PushBankTransfersV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    total_amount: float
    from_account_ref: "AccountRefDto"
    to_account_ref: "AccountRefDto"
    currency_rate: Union[Unset, float] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    pass_through: Union[Unset, "PushBankTransfersV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_amount = self.total_amount

        from_account_ref = self.from_account_ref.to_dict()

        to_account_ref = self.to_account_ref.to_dict()

        currency_rate = self.currency_rate

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        memo = self.memo

        currency = self.currency

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

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
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.push_bank_transfers_v2_pass_through import PushBankTransfersV2PassThrough

        d = src_dict.copy()
        total_amount = d.pop("totalAmount")

        from_account_ref = AccountRefDto.from_dict(d.pop("fromAccountRef"))

        to_account_ref = AccountRefDto.from_dict(d.pop("toAccountRef"))

        currency_rate = d.pop("currencyRate", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushBankTransfersV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushBankTransfersV2PassThrough.from_dict(_pass_through)

        push_bank_transfers_v2 = cls(
            total_amount=total_amount,
            from_account_ref=from_account_ref,
            to_account_ref=to_account_ref,
            currency_rate=currency_rate,
            date=date,
            memo=memo,
            currency=currency,
            pass_through=pass_through,
        )

        push_bank_transfers_v2.additional_properties = d
        return push_bank_transfers_v2

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
