import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_payment_link import InvoicePaymentLink
    from ..models.invoice_payment_links import InvoicePaymentLinks


T = TypeVar("T", bound="InvoicePaymentLineItem")


@_attrs_define
class InvoicePaymentLineItem:
    """
    Attributes:
        allocated_on_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:57:54.294Z.
        amount (Union[Unset, float]):  Example: 200.5.
        link (Union[Unset, InvoicePaymentLink]):
        links (Union[Unset, List['InvoicePaymentLinks']]):
    """

    allocated_on_date: Union[Unset, datetime.datetime] = UNSET
    amount: Union[Unset, float] = UNSET
    link: Union[Unset, "InvoicePaymentLink"] = UNSET
    links: Union[Unset, List["InvoicePaymentLinks"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocated_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat()

        amount = self.amount

        link: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated_on_date is not UNSET:
            field_dict["allocatedOnDate"] = allocated_on_date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if link is not UNSET:
            field_dict["link"] = link
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_payment_link import InvoicePaymentLink
        from ..models.invoice_payment_links import InvoicePaymentLinks

        d = src_dict.copy()
        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, datetime.datetime]
        if isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date)

        amount = d.pop("amount", UNSET)

        _link = d.pop("link", UNSET)
        link: Union[Unset, InvoicePaymentLink]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = InvoicePaymentLink.from_dict(_link)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = InvoicePaymentLinks.from_dict(links_item_data)

            links.append(links_item)

        invoice_payment_line_item = cls(
            allocated_on_date=allocated_on_date,
            amount=amount,
            link=link,
            links=links,
        )

        invoice_payment_line_item.additional_properties = d
        return invoice_payment_line_item

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
