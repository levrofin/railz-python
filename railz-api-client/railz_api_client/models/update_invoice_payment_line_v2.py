import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_payment_link_dto import InvoicePaymentLinkDto


T = TypeVar("T", bound="UpdateInvoicePaymentLineV2")


@_attrs_define
class UpdateInvoicePaymentLineV2:
    """
    Attributes:
        amount (Union[Unset, float]):  Example: 342.99.
        links (Union[Unset, List['InvoicePaymentLinkDto']]):
        allocated_on_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
    """

    amount: Union[Unset, float] = UNSET
    links: Union[Unset, List["InvoicePaymentLinkDto"]] = UNSET
    allocated_on_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        allocated_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if links is not UNSET:
            field_dict["links"] = links
        if allocated_on_date is not UNSET:
            field_dict["allocatedOnDate"] = allocated_on_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_payment_link_dto import InvoicePaymentLinkDto

        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = InvoicePaymentLinkDto.from_dict(links_item_data)

            links.append(links_item)

        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, datetime.date]
        if isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date).date()

        update_invoice_payment_line_v2 = cls(
            amount=amount,
            links=links,
            allocated_on_date=allocated_on_date,
        )

        update_invoice_payment_line_v2.additional_properties = d
        return update_invoice_payment_line_v2

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
