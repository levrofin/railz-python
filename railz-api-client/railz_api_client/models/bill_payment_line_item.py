import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_p_links import BillPLinks
    from ..models.bill_payment_link import BillPaymentLink


T = TypeVar("T", bound="BillPaymentLineItem")


@_attrs_define
class BillPaymentLineItem:
    """
    Attributes:
        amount (float):  Example: 200.5.
        link (Union[Unset, BillPaymentLink]):
        links (Union[Unset, List['BillPLinks']]):
        allocated_on_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:57:54.294Z.
    """

    amount: float
    link: Union[Unset, "BillPaymentLink"] = UNSET
    links: Union[Unset, List["BillPLinks"]] = UNSET
    allocated_on_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        allocated_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
            }
        )
        if link is not UNSET:
            field_dict["link"] = link
        if links is not UNSET:
            field_dict["links"] = links
        if allocated_on_date is not UNSET:
            field_dict["allocatedOnDate"] = allocated_on_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bill_p_links import BillPLinks
        from ..models.bill_payment_link import BillPaymentLink

        d = src_dict.copy()
        amount = d.pop("amount")

        _link = d.pop("link", UNSET)
        link: Union[Unset, BillPaymentLink]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = BillPaymentLink.from_dict(_link)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = BillPLinks.from_dict(links_item_data)

            links.append(links_item)

        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, datetime.datetime]
        if isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date)

        bill_payment_line_item = cls(
            amount=amount,
            link=link,
            links=links,
            allocated_on_date=allocated_on_date,
        )

        bill_payment_line_item.additional_properties = d
        return bill_payment_line_item

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
