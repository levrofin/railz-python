import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_deposit_line_v1 import PushDepositLineV1


T = TypeVar("T", bound="PushDepositV1")


@_attrs_define
class PushDepositV1:
    """
    Attributes:
        posted_date (datetime.date):  Example: 2021-03-29.
        bank_account_ref (str):  Example: 200.
        lines (List['PushDepositLineV1']):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Example memo..
        currency (Union[Unset, str]):  Example: CAD.
        customer_ref (Union[Unset, str]):  Example: 124.
    """

    posted_date: datetime.date
    bank_account_ref: str
    lines: List["PushDepositLineV1"]
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    customer_ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date = self.posted_date.isoformat()

        bank_account_ref = self.bank_account_ref

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        currency_rate = self.currency_rate

        memo = self.memo

        currency = self.currency

        customer_ref = self.customer_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "postedDate": posted_date,
                "bankAccountRef": bank_account_ref,
                "lines": lines,
            }
        )
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if memo is not UNSET:
            field_dict["memo"] = memo
        if currency is not UNSET:
            field_dict["currency"] = currency
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_deposit_line_v1 import PushDepositLineV1

        d = src_dict.copy()
        posted_date = isoparse(d.pop("postedDate")).date()

        bank_account_ref = d.pop("bankAccountRef")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = PushDepositLineV1.from_dict(lines_item_data)

            lines.append(lines_item)

        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        customer_ref = d.pop("customerRef", UNSET)

        push_deposit_v1 = cls(
            posted_date=posted_date,
            bank_account_ref=bank_account_ref,
            lines=lines,
            currency_rate=currency_rate,
            memo=memo,
            currency=currency,
            customer_ref=customer_ref,
        )

        push_deposit_v1.additional_properties = d
        return push_deposit_v1

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
