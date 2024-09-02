import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_ref_dto import CustomerRefDto
    from ..models.invoice_line_item_v2 import InvoiceLineItemV2
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto
    from ..models.update_invoice_v2_pass_through import UpdateInvoiceV2PassThrough


T = TypeVar("T", bound="UpdateInvoiceV2")


@_attrs_define
class UpdateInvoiceV2:
    """
    Attributes:
        customer_ref (CustomerRefDto):
        lines (List['InvoiceLineItemV2']):
        pass_through (Union[Unset, UpdateInvoiceV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        invoice_number (Union[Unset, str]):
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        due_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        currency (Union[Unset, str]):  Example: USD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
    """

    customer_ref: "CustomerRefDto"
    lines: List["InvoiceLineItemV2"]
    pass_through: Union[Unset, "UpdateInvoiceV2PassThrough"] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
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

        invoice_number = self.invoice_number

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        currency = self.currency

        currency_rate = self.currency_rate

        memo = self.memo

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

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
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if memo is not UNSET:
            field_dict["memo"] = memo
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_ref_dto import CustomerRefDto
        from ..models.invoice_line_item_v2 import InvoiceLineItemV2
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto
        from ..models.update_invoice_v2_pass_through import UpdateInvoiceV2PassThrough

        d = src_dict.copy()
        customer_ref = CustomerRefDto.from_dict(d.pop("customerRef"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = InvoiceLineItemV2.from_dict(lines_item_data)

            lines.append(lines_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, UpdateInvoiceV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = UpdateInvoiceV2PassThrough.from_dict(_pass_through)

        invoice_number = d.pop("invoiceNumber", UNSET)

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

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        update_invoice_v2 = cls(
            customer_ref=customer_ref,
            lines=lines,
            pass_through=pass_through,
            invoice_number=invoice_number,
            posted_date=posted_date,
            due_date=due_date,
            currency=currency,
            currency_rate=currency_rate,
            memo=memo,
            subsidiary_refs=subsidiary_refs,
        )

        update_invoice_v2.additional_properties = d
        return update_invoice_v2

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
