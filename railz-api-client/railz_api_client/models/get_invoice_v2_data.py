import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_invoice_v2_data_status import GetInvoiceV2DataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_ref import CustomerRef
    from ..models.get_invoice_v2_data_pass_through import GetInvoiceV2DataPassThrough
    from ..models.invoice_line_items_v2 import InvoiceLineItemsV2
    from ..models.payments import Payments
    from ..models.subsidiary_ref import SubsidiaryRef


T = TypeVar("T", bound="GetInvoiceV2Data")


@_attrs_define
class GetInvoiceV2Data:
    """
    Attributes:
        id (str):  Example: 1.
        status (GetInvoiceV2DataStatus):
        invoice_number (Union[Unset, str]):  Example: string.
        customer_ref (Union[Unset, CustomerRef]):
        due_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T15:59:47.118Z.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        total_amount (Union[Unset, float]):  Example: 283.
        total_discount (Union[Unset, float]):
        sub_total (Union[Unset, float]):  Example: 250.5.
        tax_amount (Union[Unset, float]):  Example: 32.5.
        amount_due (Union[Unset, float]):  Example: 283.
        discount_percentage (Union[Unset, float]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T15:59:47.118Z.
        memo (Union[Unset, str]):  Example: Example invoice memo..
        payments (Union[Unset, List['Payments']]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        posted_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T15:59:47.118Z.
        currency (Union[Unset, str]):  Example: USD.
        lines (Union[Unset, List['InvoiceLineItemsV2']]):
        pass_through (Union[Unset, GetInvoiceV2DataPassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    id: str
    status: GetInvoiceV2DataStatus
    invoice_number: Union[Unset, str] = UNSET
    customer_ref: Union[Unset, "CustomerRef"] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    amount_due: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    memo: Union[Unset, str] = UNSET
    payments: Union[Unset, List["Payments"]] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    lines: Union[Unset, List["InvoiceLineItemsV2"]] = UNSET
    pass_through: Union[Unset, "GetInvoiceV2DataPassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        status = self.status

        invoice_number = self.invoice_number

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        currency_rate = self.currency_rate

        total_amount = self.total_amount

        total_discount = self.total_discount

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        amount_due = self.amount_due

        discount_percentage = self.discount_percentage

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

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

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        currency = self.currency

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if memo is not UNSET:
            field_dict["memo"] = memo
        if payments is not UNSET:
            field_dict["payments"] = payments
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if lines is not UNSET:
            field_dict["lines"] = lines
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_ref import CustomerRef
        from ..models.get_invoice_v2_data_pass_through import GetInvoiceV2DataPassThrough
        from ..models.invoice_line_items_v2 import InvoiceLineItemsV2
        from ..models.payments import Payments
        from ..models.subsidiary_ref import SubsidiaryRef

        d = src_dict.copy()
        id = d.pop("id")

        status = d.pop("status")

        invoice_number = d.pop("invoiceNumber", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerRef.from_dict(_customer_ref)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        currency_rate = d.pop("currencyRate", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        amount_due = d.pop("amountDue", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

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

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        currency = d.pop("currency", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = InvoiceLineItemsV2.from_dict(lines_item_data)

            lines.append(lines_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, GetInvoiceV2DataPassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = GetInvoiceV2DataPassThrough.from_dict(_pass_through)

        get_invoice_v2_data = cls(
            id=id,
            status=status,
            invoice_number=invoice_number,
            customer_ref=customer_ref,
            due_date=due_date,
            currency_rate=currency_rate,
            total_amount=total_amount,
            total_discount=total_discount,
            sub_total=sub_total,
            tax_amount=tax_amount,
            amount_due=amount_due,
            discount_percentage=discount_percentage,
            source_modified_date=source_modified_date,
            memo=memo,
            payments=payments,
            subsidiary_refs=subsidiary_refs,
            posted_date=posted_date,
            currency=currency,
            lines=lines,
            pass_through=pass_through,
        )

        get_invoice_v2_data.additional_properties = d
        return get_invoice_v2_data

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
