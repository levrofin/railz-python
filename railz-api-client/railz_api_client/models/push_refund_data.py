import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_refund_data_pass_through import PushRefundDataPassThrough
    from ..models.push_refund_line import PushRefundLine


T = TypeVar("T", bound="PushRefundData")


@_attrs_define
class PushRefundData:
    """
    Attributes:
        total_amount (float):  Example: 150.5.
        customer_ref (str):  Example: 145.
        account_ref (str):  Example: 130.
        date (datetime.date):  Example: 2021-03-09.
        pass_through (Union[Unset, PushRefundDataPassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Services rendered..
        invoice_ref (Union[Unset, str]):  Example: 503.
        currency (Union[Unset, str]):  Example: CAD.
        lines (Union[Unset, List['PushRefundLine']]):
    """

    total_amount: float
    customer_ref: str
    account_ref: str
    date: datetime.date
    pass_through: Union[Unset, "PushRefundDataPassThrough"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    invoice_ref: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    lines: Union[Unset, List["PushRefundLine"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_amount = self.total_amount

        customer_ref = self.customer_ref

        account_ref = self.account_ref

        date = self.date.isoformat()

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        currency_rate = self.currency_rate

        memo = self.memo

        invoice_ref = self.invoice_ref

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
                "totalAmount": total_amount,
                "customerRef": customer_ref,
                "accountRef": account_ref,
                "date": date,
            }
        )
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if memo is not UNSET:
            field_dict["memo"] = memo
        if invoice_ref is not UNSET:
            field_dict["invoiceRef"] = invoice_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_refund_data_pass_through import PushRefundDataPassThrough
        from ..models.push_refund_line import PushRefundLine

        d = src_dict.copy()
        total_amount = d.pop("totalAmount")

        customer_ref = d.pop("customerRef")

        account_ref = d.pop("accountRef")

        date = isoparse(d.pop("date")).date()

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushRefundDataPassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushRefundDataPassThrough.from_dict(_pass_through)

        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        invoice_ref = d.pop("invoiceRef", UNSET)

        currency = d.pop("currency", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = PushRefundLine.from_dict(lines_item_data)

            lines.append(lines_item)

        push_refund_data = cls(
            total_amount=total_amount,
            customer_ref=customer_ref,
            account_ref=account_ref,
            date=date,
            pass_through=pass_through,
            currency_rate=currency_rate,
            memo=memo,
            invoice_ref=invoice_ref,
            currency=currency,
            lines=lines,
        )

        push_refund_data.additional_properties = d
        return push_refund_data

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
