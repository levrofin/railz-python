import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.customer_ref_dto import CustomerRefDto
    from ..models.push_refund_data_v2_pass_through import PushRefundDataV2PassThrough
    from ..models.push_refund_line_v2 import PushRefundLineV2


T = TypeVar("T", bound="PushRefundDataV2")


@_attrs_define
class PushRefundDataV2:
    """
    Attributes:
        account_ref (AccountRefDto):
        pass_through (Union[Unset, PushRefundDataV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        total_amount (Union[Unset, float]):  Example: 150.5.
        memo (Union[Unset, str]):  Example: Services rendered..
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-09.
        customer_ref (Union[Unset, CustomerRefDto]):
        currency (Union[Unset, str]):  Example: CAD.
        lines (Union[Unset, List['PushRefundLineV2']]):
    """

    account_ref: "AccountRefDto"
    pass_through: Union[Unset, "PushRefundDataV2PassThrough"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    customer_ref: Union[Unset, "CustomerRefDto"] = UNSET
    currency: Union[Unset, str] = UNSET
    lines: Union[Unset, List["PushRefundLineV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_ref = self.account_ref.to_dict()

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        currency_rate = self.currency_rate

        total_amount = self.total_amount

        memo = self.memo

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        currency = self.currency

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountRef": account_ref,
            }
        )
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if memo is not UNSET:
            field_dict["memo"] = memo
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.customer_ref_dto import CustomerRefDto
        from ..models.push_refund_data_v2_pass_through import PushRefundDataV2PassThrough
        from ..models.push_refund_line_v2 import PushRefundLineV2

        d = src_dict.copy()
        account_ref = AccountRefDto.from_dict(d.pop("accountRef"))

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushRefundDataV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushRefundDataV2PassThrough.from_dict(_pass_through)

        currency_rate = d.pop("currencyRate", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        memo = d.pop("memo", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerRefDto]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerRefDto.from_dict(_customer_ref)

        currency = d.pop("currency", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = PushRefundLineV2.from_dict(lines_item_data)

            lines.append(lines_item)

        push_refund_data_v2 = cls(
            account_ref=account_ref,
            pass_through=pass_through,
            currency_rate=currency_rate,
            total_amount=total_amount,
            memo=memo,
            posted_date=posted_date,
            customer_ref=customer_ref,
            currency=currency,
            lines=lines,
        )

        push_refund_data_v2.additional_properties = d
        return push_refund_data_v2

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
