from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.deposit_entity_ref import DepositEntityRef
    from ..models.link import Link
    from ..models.links import Links
    from ..models.tax_rate_ref import TaxRateRef


T = TypeVar("T", bound="DepositLineItems")


@_attrs_define
class DepositLineItems:
    """
    Attributes:
        total_amount (float):  Example: 322.
        description (Union[Unset, str]):  Example: Services rendered..
        unit_amount (Union[Unset, float]):  Example: 100.5.
        quantity (Union[Unset, float]):  Example: 3.
        sub_total (Union[Unset, float]):  Example: 301.5.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        account_ref (Union[Unset, AccountRef]):
        tax_rate_ref (Union[Unset, TaxRateRef]):
        entity_ref (Union[Unset, DepositEntityRef]):
        link (Union[Unset, Link]):
        links (Union[Unset, List['Links']]):
    """

    total_amount: float
    description: Union[Unset, str] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRef"] = UNSET
    entity_ref: Union[Unset, "DepositEntityRef"] = UNSET
    link: Union[Unset, "Link"] = UNSET
    links: Union[Unset, List["Links"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_amount = self.total_amount

        description = self.description

        unit_amount = self.unit_amount

        quantity = self.quantity

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

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
        field_dict.update(
            {
                "totalAmount": total_amount,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref
        if link is not UNSET:
            field_dict["link"] = link
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.deposit_entity_ref import DepositEntityRef
        from ..models.link import Link
        from ..models.links import Links
        from ..models.tax_rate_ref import TaxRateRef

        d = src_dict.copy()
        total_amount = d.pop("totalAmount")

        description = d.pop("description", UNSET)

        unit_amount = d.pop("unitAmount", UNSET)

        quantity = d.pop("quantity", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRef]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRef.from_dict(_tax_rate_ref)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, DepositEntityRef]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = DepositEntityRef.from_dict(_entity_ref)

        _link = d.pop("link", UNSET)
        link: Union[Unset, Link]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = Link.from_dict(_link)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Links.from_dict(links_item_data)

            links.append(links_item)

        deposit_line_items = cls(
            total_amount=total_amount,
            description=description,
            unit_amount=unit_amount,
            quantity=quantity,
            sub_total=sub_total,
            tax_amount=tax_amount,
            account_ref=account_ref,
            tax_rate_ref=tax_rate_ref,
            entity_ref=entity_ref,
            link=link,
            links=links,
        )

        deposit_line_items.additional_properties = d
        return deposit_line_items

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
