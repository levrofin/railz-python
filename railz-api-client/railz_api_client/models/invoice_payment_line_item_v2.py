import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_payment_links_v2 import InvoicePaymentLinksV2


T = TypeVar("T", bound="InvoicePaymentLineItemV2")


@_attrs_define
class InvoicePaymentLineItemV2:
    """
    Attributes:
        allocated_on_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:57:54.294Z.
        amount (Union[Unset, float]):  Example: 200.5.
        links (Union[Unset, List['InvoicePaymentLinksV2']]):
    """

    allocated_on_date: Union[Unset, datetime.datetime] = UNSET
    amount: Union[Unset, float] = UNSET
    links: Union[Unset, List["InvoicePaymentLinksV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocated_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat()

        amount = self.amount

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
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_payment_links_v2 import InvoicePaymentLinksV2

        d = src_dict.copy()
        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, datetime.datetime]
        if isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date)

        amount = d.pop("amount", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = InvoicePaymentLinksV2.from_dict(links_item_data)

            links.append(links_item)

        invoice_payment_line_item_v2 = cls(
            allocated_on_date=allocated_on_date,
            amount=amount,
            links=links,
        )

        invoice_payment_line_item_v2.additional_properties = d
        return invoice_payment_line_item_v2

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
