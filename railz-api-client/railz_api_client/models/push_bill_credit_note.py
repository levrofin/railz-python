import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_credit_note_line_item import BillCreditNoteLineItem


T = TypeVar("T", bound="PushBillCreditNote")


@_attrs_define
class PushBillCreditNote:
    """
    Attributes:
        vendor_ref (str):  Example: 124.
        lines (List['BillCreditNoteLineItem']):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        allocated_on_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        memo (Union[Unset, str]):  Example: Example memo..
        currency (Union[Unset, str]):  Example: CAD.
    """

    vendor_ref: str
    lines: List["BillCreditNoteLineItem"]
    currency_rate: Union[Unset, float] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    allocated_on_date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vendor_ref = self.vendor_ref

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

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
                "vendorRef": vendor_ref,
                "lines": lines,
            }
        )
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
        from ..models.bill_credit_note_line_item import BillCreditNoteLineItem

        d = src_dict.copy()
        vendor_ref = d.pop("vendorRef")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = BillCreditNoteLineItem.from_dict(lines_item_data)

            lines.append(lines_item)

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

        push_bill_credit_note = cls(
            vendor_ref=vendor_ref,
            lines=lines,
            currency_rate=currency_rate,
            posted_date=posted_date,
            allocated_on_date=allocated_on_date,
            memo=memo,
            currency=currency,
        )

        push_bill_credit_note.additional_properties = d
        return push_bill_credit_note

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
