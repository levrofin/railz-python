import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_ref_dto import CustomerRefDto
    from ..models.invoice_credit_note_line_v2 import InvoiceCreditNoteLineV2
    from ..models.push_invoice_credit_note_v2_pass_through import PushInvoiceCreditNoteV2PassThrough
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto


T = TypeVar("T", bound="PushInvoiceCreditNoteV2")


@_attrs_define
class PushInvoiceCreditNoteV2:
    """
    Attributes:
        customer_ref (CustomerRefDto):
        lines (List['InvoiceCreditNoteLineV2']):
        pass_through (Union[Unset, PushInvoiceCreditNoteV2PassThrough]):  Example: {'CustomField': [{'DefinitionId':
            '1', 'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        allocated_on_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        memo (Union[Unset, str]):  Example: Example memo..
        currency (Union[Unset, str]):  Example: CAD.
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        invoice_credit_note_number (Union[Unset, str]): The buyer facing document number of the invoice credit note.
    """

    customer_ref: "CustomerRefDto"
    lines: List["InvoiceCreditNoteLineV2"]
    pass_through: Union[Unset, "PushInvoiceCreditNoteV2PassThrough"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    allocated_on_date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    invoice_credit_note_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_ref = self.customer_ref.to_dict()

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

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        invoice_credit_note_number = self.invoice_credit_note_number

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
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if invoice_credit_note_number is not UNSET:
            field_dict["invoiceCreditNoteNumber"] = invoice_credit_note_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_ref_dto import CustomerRefDto
        from ..models.invoice_credit_note_line_v2 import InvoiceCreditNoteLineV2
        from ..models.push_invoice_credit_note_v2_pass_through import PushInvoiceCreditNoteV2PassThrough
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto

        d = src_dict.copy()
        customer_ref = CustomerRefDto.from_dict(d.pop("customerRef"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = InvoiceCreditNoteLineV2.from_dict(lines_item_data)

            lines.append(lines_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushInvoiceCreditNoteV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushInvoiceCreditNoteV2PassThrough.from_dict(_pass_through)

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

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        invoice_credit_note_number = d.pop("invoiceCreditNoteNumber", UNSET)

        push_invoice_credit_note_v2 = cls(
            customer_ref=customer_ref,
            lines=lines,
            pass_through=pass_through,
            currency_rate=currency_rate,
            posted_date=posted_date,
            allocated_on_date=allocated_on_date,
            memo=memo,
            currency=currency,
            subsidiary_refs=subsidiary_refs,
            invoice_credit_note_number=invoice_credit_note_number,
        )

        push_invoice_credit_note_v2.additional_properties = d
        return push_invoice_credit_note_v2

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
