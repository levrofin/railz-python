import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_credit_note_line_v1 import InvoiceCreditNoteLineV1
    from ..models.push_invoice_credit_note_v1_pass_through import PushInvoiceCreditNoteV1PassThrough


T = TypeVar("T", bound="PushInvoiceCreditNoteV1")


@_attrs_define
class PushInvoiceCreditNoteV1:
    """
    Attributes:
        customer_ref (str):  Example: 124.
        lines (List['InvoiceCreditNoteLineV1']):
        pass_through (Union[Unset, PushInvoiceCreditNoteV1PassThrough]):  Example: {'CustomField': [{'DefinitionId':
            '1', 'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        allocated_on_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        memo (Union[Unset, str]):  Example: Example memo..
        currency (Union[Unset, str]):  Example: CAD.
    """

    customer_ref: str
    lines: List["InvoiceCreditNoteLineV1"]
    pass_through: Union[Unset, "PushInvoiceCreditNoteV1PassThrough"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    allocated_on_date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_ref = self.customer_ref

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        currency_rate = self.currency_rate

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        allocated_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat()

        memo = self.memo

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerRef": customer_ref,
                "lines": lines,
            }
        )
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if allocated_on_date is not UNSET:
            field_dict["allocatedOnDate"] = allocated_on_date
        if memo is not UNSET:
            field_dict["memo"] = memo
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_credit_note_line_v1 import InvoiceCreditNoteLineV1
        from ..models.push_invoice_credit_note_v1_pass_through import PushInvoiceCreditNoteV1PassThrough

        d = src_dict.copy()
        customer_ref = d.pop("customerRef")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = InvoiceCreditNoteLineV1.from_dict(lines_item_data)

            lines.append(lines_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushInvoiceCreditNoteV1PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushInvoiceCreditNoteV1PassThrough.from_dict(_pass_through)

        currency_rate = d.pop("currencyRate", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, datetime.date]
        if isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date).date()

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        push_invoice_credit_note_v1 = cls(
            customer_ref=customer_ref,
            lines=lines,
            pass_through=pass_through,
            currency_rate=currency_rate,
            posted_date=posted_date,
            allocated_on_date=allocated_on_date,
            memo=memo,
            currency=currency,
        )

        push_invoice_credit_note_v1.additional_properties = d
        return push_invoice_credit_note_v1

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
