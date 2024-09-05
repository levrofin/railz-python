import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bill_credit_note_data_v1_status import (
    GetBillCreditNoteDataV1Status,
    check_get_bill_credit_note_data_v1_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_ref import CurrencyRef
    from ..models.invoice_bill_line_items_v1 import InvoiceBillLineItemsV1
    from ..models.location_ref import LocationRef
    from ..models.payments import Payments
    from ..models.vendor_ref import VendorRef


T = TypeVar("T", bound="GetBillCreditNoteDataV1")


@_attrs_define
class GetBillCreditNoteDataV1:
    """
    Attributes:
        id (str):  Example: 1.
        posted_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        total_amount (float):  Example: 322.
        status (GetBillCreditNoteDataV1Status):
        allocated_on_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency_ref (Union[Unset, CurrencyRef]):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        total_discount (Union[Unset, float]):  Example: 322.
        discount_percentage (Union[Unset, float]):  Example: 322.
        sub_total (Union[Unset, float]):  Example: 301.5.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        remaining_credit (Union[Unset, float]):  Example: 322.
        memo (Union[Unset, str]):  Example: Example bill memo..
        payments (Union[Unset, List['Payments']]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        location_ref (Union[Unset, LocationRef]):
        vendor_ref (Union[Unset, VendorRef]):
        lines (Union[Unset, List['InvoiceBillLineItemsV1']]):
    """

    id: str
    posted_date: datetime.datetime
    total_amount: float
    status: GetBillCreditNoteDataV1Status
    allocated_on_date: Union[Unset, datetime.datetime] = UNSET
    currency_ref: Union[Unset, "CurrencyRef"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    remaining_credit: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    payments: Union[Unset, List["Payments"]] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    location_ref: Union[Unset, "LocationRef"] = UNSET
    vendor_ref: Union[Unset, "VendorRef"] = UNSET
    lines: Union[Unset, List["InvoiceBillLineItemsV1"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        posted_date = self.posted_date.isoformat()

        total_amount = self.total_amount

        status: str = self.status

        allocated_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat()

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

        currency_rate = self.currency_rate

        total_discount = self.total_discount

        discount_percentage = self.discount_percentage

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        remaining_credit = self.remaining_credit

        memo = self.memo

        payments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payments, Unset):
            payments = []
            for payments_item_data in self.payments:
                payments_item = payments_item_data.to_dict()
                payments.append(payments_item)

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        location_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location_ref, Unset):
            location_ref = self.location_ref.to_dict()

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

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
                "id": id,
                "postedDate": posted_date,
                "totalAmount": total_amount,
                "status": status,
            }
        )
        if allocated_on_date is not UNSET:
            field_dict["allocatedOnDate"] = allocated_on_date
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if remaining_credit is not UNSET:
            field_dict["remainingCredit"] = remaining_credit
        if memo is not UNSET:
            field_dict["memo"] = memo
        if payments is not UNSET:
            field_dict["payments"] = payments
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency_ref import CurrencyRef
        from ..models.invoice_bill_line_items_v1 import InvoiceBillLineItemsV1
        from ..models.location_ref import LocationRef
        from ..models.payments import Payments
        from ..models.vendor_ref import VendorRef

        d = src_dict.copy()
        id = d.pop("id")

        posted_date = isoparse(d.pop("postedDate"))

        total_amount = d.pop("totalAmount")

        status = check_get_bill_credit_note_data_v1_status(d.pop("status"))

        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, datetime.datetime]
        if isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CurrencyRef.from_dict(_currency_ref)

        currency_rate = d.pop("currencyRate", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        remaining_credit = d.pop("remainingCredit", UNSET)

        memo = d.pop("memo", UNSET)

        payments = []
        _payments = d.pop("payments", UNSET)
        for payments_item_data in _payments or []:
            payments_item = Payments.from_dict(payments_item_data)

            payments.append(payments_item)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        _location_ref = d.pop("locationRef", UNSET)
        location_ref: Union[Unset, LocationRef]
        if isinstance(_location_ref, Unset):
            location_ref = UNSET
        else:
            location_ref = LocationRef.from_dict(_location_ref)

        _vendor_ref = d.pop("vendorRef", UNSET)
        vendor_ref: Union[Unset, VendorRef]
        if isinstance(_vendor_ref, Unset):
            vendor_ref = UNSET
        else:
            vendor_ref = VendorRef.from_dict(_vendor_ref)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = InvoiceBillLineItemsV1.from_dict(lines_item_data)

            lines.append(lines_item)

        get_bill_credit_note_data_v1 = cls(
            id=id,
            posted_date=posted_date,
            total_amount=total_amount,
            status=status,
            allocated_on_date=allocated_on_date,
            currency_ref=currency_ref,
            currency_rate=currency_rate,
            total_discount=total_discount,
            discount_percentage=discount_percentage,
            sub_total=sub_total,
            tax_amount=tax_amount,
            remaining_credit=remaining_credit,
            memo=memo,
            payments=payments,
            source_modified_date=source_modified_date,
            location_ref=location_ref,
            vendor_ref=vendor_ref,
            lines=lines,
        )

        get_bill_credit_note_data_v1.additional_properties = d
        return get_bill_credit_note_data_v1

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
