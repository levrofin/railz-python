import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bill_v2_data_status import GetBillV2DataStatus, check_get_bill_v2_data_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_line_items_v2 import BillLineItemsV2
    from ..models.payments import Payments
    from ..models.purchase_order_ref import PurchaseOrderRef
    from ..models.subsidiary_ref import SubsidiaryRef
    from ..models.vendor_ref import VendorRef


T = TypeVar("T", bound="GetBillV2Data")


@_attrs_define
class GetBillV2Data:
    """
    Attributes:
        id (str):  Example: 1.
        posted_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        lines (List['BillLineItemsV2']):
        status (GetBillV2DataStatus):
        total_amount (float):  Example: 322.
        vendor_ref (Union[Unset, VendorRef]):
        purchase_order_refs (Union[Unset, List['PurchaseOrderRef']]):
        due_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency (Union[Unset, str]):  Example: USD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        vendor_invoice_number (Union[Unset, str]):  Example: INV-0028.
        sub_total (Union[Unset, float]):  Example: 301.5.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        amount_due (Union[Unset, float]):  Example: 322.
        memo (Union[Unset, str]):  Example: Example bill memo..
        payments (Union[Unset, List['Payments']]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
    """

    id: str
    posted_date: datetime.datetime
    lines: List["BillLineItemsV2"]
    status: GetBillV2DataStatus
    total_amount: float
    vendor_ref: Union[Unset, "VendorRef"] = UNSET
    purchase_order_refs: Union[Unset, List["PurchaseOrderRef"]] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    vendor_invoice_number: Union[Unset, str] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    amount_due: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    payments: Union[Unset, List["Payments"]] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        posted_date = self.posted_date.isoformat()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        status: str = self.status

        total_amount = self.total_amount

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

        purchase_order_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_order_refs, Unset):
            purchase_order_refs = []
            for purchase_order_refs_item_data in self.purchase_order_refs:
                purchase_order_refs_item = purchase_order_refs_item_data.to_dict()
                purchase_order_refs.append(purchase_order_refs_item)

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        currency = self.currency

        currency_rate = self.currency_rate

        vendor_invoice_number = self.vendor_invoice_number

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        amount_due = self.amount_due

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
                "lines": lines,
                "status": status,
                "totalAmount": total_amount,
            }
        )
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if purchase_order_refs is not UNSET:
            field_dict["purchaseOrderRefs"] = purchase_order_refs
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if vendor_invoice_number is not UNSET:
            field_dict["vendorInvoiceNumber"] = vendor_invoice_number
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
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
        from ..models.bill_line_items_v2 import BillLineItemsV2
        from ..models.payments import Payments
        from ..models.purchase_order_ref import PurchaseOrderRef
        from ..models.subsidiary_ref import SubsidiaryRef
        from ..models.vendor_ref import VendorRef

        d = src_dict.copy()
        id = d.pop("id")

        posted_date = isoparse(d.pop("postedDate"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = BillLineItemsV2.from_dict(lines_item_data)

            lines.append(lines_item)

        status = check_get_bill_v2_data_status(d.pop("status"))

        total_amount = d.pop("totalAmount")

        _vendor_ref = d.pop("vendorRef", UNSET)
        vendor_ref: Union[Unset, VendorRef]
        if isinstance(_vendor_ref, Unset):
            vendor_ref = UNSET
        else:
            vendor_ref = VendorRef.from_dict(_vendor_ref)

        purchase_order_refs = []
        _purchase_order_refs = d.pop("purchaseOrderRefs", UNSET)
        for purchase_order_refs_item_data in _purchase_order_refs or []:
            purchase_order_refs_item = PurchaseOrderRef.from_dict(purchase_order_refs_item_data)

            purchase_order_refs.append(purchase_order_refs_item)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        vendor_invoice_number = d.pop("vendorInvoiceNumber", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        amount_due = d.pop("amountDue", UNSET)

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

        get_bill_v2_data = cls(
            id=id,
            posted_date=posted_date,
            lines=lines,
            status=status,
            total_amount=total_amount,
            vendor_ref=vendor_ref,
            purchase_order_refs=purchase_order_refs,
            due_date=due_date,
            currency=currency,
            currency_rate=currency_rate,
            vendor_invoice_number=vendor_invoice_number,
            sub_total=sub_total,
            tax_amount=tax_amount,
            amount_due=amount_due,
            memo=memo,
            payments=payments,
            subsidiary_refs=subsidiary_refs,
            source_modified_date=source_modified_date,
        )

        get_bill_v2_data.additional_properties = d
        return get_bill_v2_data

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
