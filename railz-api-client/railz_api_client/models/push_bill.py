import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_bill_line_item_v1 import PushBillLineItemV1


T = TypeVar("T", bound="PushBill")


@_attrs_define
class PushBill:
    """
    Attributes:
        vendor_ref (str):  Example: 132.
        lines (List['PushBillLineItemV1']):
        vendor_invoice_number (Union[Unset, str]):  Example: 254.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        due_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Example bill memo..
        currency (Union[Unset, str]):  Example: CAD.
        location_ref (Union[Unset, str]):  Example: 3.
        subsidiary_refs (Union[Unset, List[str]]):  Example: ['4'].
        tracking_category_ref (Union[Unset, str]):  Example: 23118.
    """

    vendor_ref: str
    lines: List["PushBillLineItemV1"]
    vendor_invoice_number: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    location_ref: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List[str]] = UNSET
    tracking_category_ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vendor_ref = self.vendor_ref

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        vendor_invoice_number = self.vendor_invoice_number

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        currency_rate = self.currency_rate

        memo = self.memo

        currency = self.currency

        location_ref = self.location_ref

        subsidiary_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = self.subsidiary_refs

        tracking_category_ref = self.tracking_category_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vendorRef": vendor_ref,
                "lines": lines,
            }
        )
        if vendor_invoice_number is not UNSET:
            field_dict["vendorInvoiceNumber"] = vendor_invoice_number
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if memo is not UNSET:
            field_dict["memo"] = memo
        if currency is not UNSET:
            field_dict["currency"] = currency
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if tracking_category_ref is not UNSET:
            field_dict["trackingCategoryRef"] = tracking_category_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_bill_line_item_v1 import PushBillLineItemV1

        d = src_dict.copy()
        vendor_ref = d.pop("vendorRef")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = PushBillLineItemV1.from_dict(lines_item_data)

            lines.append(lines_item)

        vendor_invoice_number = d.pop("vendorInvoiceNumber", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        location_ref = d.pop("locationRef", UNSET)

        subsidiary_refs = cast(List[str], d.pop("subsidiaryRefs", UNSET))

        tracking_category_ref = d.pop("trackingCategoryRef", UNSET)

        push_bill = cls(
            vendor_ref=vendor_ref,
            lines=lines,
            vendor_invoice_number=vendor_invoice_number,
            posted_date=posted_date,
            due_date=due_date,
            currency_rate=currency_rate,
            memo=memo,
            currency=currency,
            location_ref=location_ref,
            subsidiary_refs=subsidiary_refs,
            tracking_category_ref=tracking_category_ref,
        )

        push_bill.additional_properties = d
        return push_bill

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
