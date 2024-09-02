import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_payment_line import BillPaymentLine


T = TypeVar("T", bound="PushBillPayment")


@_attrs_define
class PushBillPayment:
    """
    Attributes:
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Bill payment memo..
        date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        location_ref (Union[Unset, str]):  Example: 3.
        total_amount (Union[Unset, float]):  Example: 200.5.
        tracking_category_ref (Union[Unset, str]):  Example: 23118.
        account_ref (Union[Unset, str]):  Example: 132.
        vendor_ref (Union[Unset, str]):  Example: 250.
        bill_ref (Union[Unset, str]):  Example: 250.
        currency (Union[Unset, str]):  Example: CAD.
        lines (Union[Unset, List['BillPaymentLine']]):
        subsidiary_refs (Union[Unset, List[str]]):  Example: ['4'].
    """

    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    location_ref: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    tracking_category_ref: Union[Unset, str] = UNSET
    account_ref: Union[Unset, str] = UNSET
    vendor_ref: Union[Unset, str] = UNSET
    bill_ref: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    lines: Union[Unset, List["BillPaymentLine"]] = UNSET
    subsidiary_refs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_rate = self.currency_rate

        memo = self.memo

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        location_ref = self.location_ref

        total_amount = self.total_amount

        tracking_category_ref = self.tracking_category_ref

        account_ref = self.account_ref

        vendor_ref = self.vendor_ref

        bill_ref = self.bill_ref

        currency = self.currency

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        subsidiary_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = self.subsidiary_refs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if memo is not UNSET:
            field_dict["memo"] = memo
        if date is not UNSET:
            field_dict["date"] = date
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if tracking_category_ref is not UNSET:
            field_dict["trackingCategoryRef"] = tracking_category_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if bill_ref is not UNSET:
            field_dict["billRef"] = bill_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if lines is not UNSET:
            field_dict["lines"] = lines
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bill_payment_line import BillPaymentLine

        d = src_dict.copy()
        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        location_ref = d.pop("locationRef", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        tracking_category_ref = d.pop("trackingCategoryRef", UNSET)

        account_ref = d.pop("accountRef", UNSET)

        vendor_ref = d.pop("vendorRef", UNSET)

        bill_ref = d.pop("billRef", UNSET)

        currency = d.pop("currency", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = BillPaymentLine.from_dict(lines_item_data)

            lines.append(lines_item)

        subsidiary_refs = cast(List[str], d.pop("subsidiaryRefs", UNSET))

        push_bill_payment = cls(
            currency_rate=currency_rate,
            memo=memo,
            date=date,
            location_ref=location_ref,
            total_amount=total_amount,
            tracking_category_ref=tracking_category_ref,
            account_ref=account_ref,
            vendor_ref=vendor_ref,
            bill_ref=bill_ref,
            currency=currency,
            lines=lines,
            subsidiary_refs=subsidiary_refs,
        )

        push_bill_payment.additional_properties = d
        return push_bill_payment

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
