import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bill_credit_note_data_v2_status import (
    GetBillCreditNoteDataV2Status,
    check_get_bill_credit_note_data_v2_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_bill_line_items_v2 import InvoiceBillLineItemsV2
    from ..models.payments import Payments
    from ..models.subsidiary_ref import SubsidiaryRef
    from ..models.vendor_ref import VendorRef


T = TypeVar("T", bound="GetBillCreditNoteDataV2")


@_attrs_define
class GetBillCreditNoteDataV2:
    """
    Attributes:
        id (str):  Example: 1.
        posted_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        total_amount (float):  Example: 322.
        status (GetBillCreditNoteDataV2Status):
        vendor_ref (VendorRef):
        lines (List['InvoiceBillLineItemsV2']):
        allocated_on_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency (Union[Unset, str]):  Example: USD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        total_discount (Union[Unset, float]):  Example: 322.
        discount_percentage (Union[Unset, float]):  Example: 322.
        sub_total (Union[Unset, float]):  Example: 301.5.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        remaining_credit (Union[Unset, float]):  Example: 322.
        memo (Union[Unset, str]):  Example: Example bill memo..
        payments (Union[Unset, List['Payments']]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
    """

    id: str
    posted_date: datetime.datetime
    total_amount: float
    status: GetBillCreditNoteDataV2Status
    vendor_ref: "VendorRef"
    lines: List["InvoiceBillLineItemsV2"]
    allocated_on_date: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    remaining_credit: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    payments: Union[Unset, List["Payments"]] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        posted_date = self.posted_date.isoformat()

        total_amount = self.total_amount

        status: str = self.status

        vendor_ref = self.vendor_ref.to_dict()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        allocated_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat()

        currency = self.currency

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

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "postedDate": posted_date,
                "totalAmount": total_amount,
                "status": status,
                "vendorRef": vendor_ref,
                "lines": lines,
            }
        )
        if allocated_on_date is not UNSET:
            field_dict["allocatedOnDate"] = allocated_on_date
        if currency is not UNSET:
            field_dict["currency"] = currency
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
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_bill_line_items_v2 import InvoiceBillLineItemsV2
        from ..models.payments import Payments
        from ..models.subsidiary_ref import SubsidiaryRef
        from ..models.vendor_ref import VendorRef

        d = src_dict.copy()
        id = d.pop("id")

        posted_date = isoparse(d.pop("postedDate"))

        total_amount = d.pop("totalAmount")

        status = check_get_bill_credit_note_data_v2_status(d.pop("status"))

        vendor_ref = VendorRef.from_dict(d.pop("vendorRef"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = InvoiceBillLineItemsV2.from_dict(lines_item_data)

            lines.append(lines_item)

        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, datetime.datetime]
        if isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date)

        currency = d.pop("currency", UNSET)

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

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRef.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_bill_credit_note_data_v2 = cls(
            id=id,
            posted_date=posted_date,
            total_amount=total_amount,
            status=status,
            vendor_ref=vendor_ref,
            lines=lines,
            allocated_on_date=allocated_on_date,
            currency=currency,
            currency_rate=currency_rate,
            total_discount=total_discount,
            discount_percentage=discount_percentage,
            sub_total=sub_total,
            tax_amount=tax_amount,
            remaining_credit=remaining_credit,
            memo=memo,
            payments=payments,
            subsidiary_refs=subsidiary_refs,
            source_modified_date=source_modified_date,
        )

        get_bill_credit_note_data_v2.additional_properties = d
        return get_bill_credit_note_data_v2

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
