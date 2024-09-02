import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_account_ref_dto import BankAccountRefDto
    from ..models.customer_ref_dto import CustomerRefDto
    from ..models.push_deposit_line_v2 import PushDepositLineV2
    from ..models.push_deposit_v2_pass_through import PushDepositV2PassThrough


T = TypeVar("T", bound="PushDepositV2")


@_attrs_define
class PushDepositV2:
    """
    Attributes:
        bank_account_ref (BankAccountRefDto):
        lines (List['PushDepositLineV2']):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Example memo..
        currency (Union[Unset, str]):  Example: CAD.
        customer_ref (Union[Unset, CustomerRefDto]):
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        pass_through (Union[Unset, PushDepositV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    bank_account_ref: "BankAccountRefDto"
    lines: List["PushDepositLineV2"]
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    customer_ref: Union[Unset, "CustomerRefDto"] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    pass_through: Union[Unset, "PushDepositV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bank_account_ref = self.bank_account_ref.to_dict()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        currency_rate = self.currency_rate

        memo = self.memo

        currency = self.currency

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_account_ref_dto import BankAccountRefDto
        from ..models.customer_ref_dto import CustomerRefDto
        from ..models.push_deposit_line_v2 import PushDepositLineV2
        from ..models.push_deposit_v2_pass_through import PushDepositV2PassThrough

        d = src_dict.copy()
        bank_account_ref = BankAccountRefDto.from_dict(d.pop("bankAccountRef"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = PushDepositLineV2.from_dict(lines_item_data)

            lines.append(lines_item)

        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerRefDto]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerRefDto.from_dict(_customer_ref)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushDepositV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushDepositV2PassThrough.from_dict(_pass_through)

        push_deposit_v2 = cls(
            bank_account_ref=bank_account_ref,
            lines=lines,
            currency_rate=currency_rate,
            memo=memo,
            currency=currency,
            customer_ref=customer_ref,
            posted_date=posted_date,
            pass_through=pass_through,
        )

        push_deposit_v2.additional_properties = d
        return push_deposit_v2

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
