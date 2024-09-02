from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.links_v2 import LinksV2
    from ..models.push_deposit_entity_ref_v2 import PushDepositEntityRefV2
    from ..models.tax_rate_ref_dto import TaxRateRefDto


T = TypeVar("T", bound="PushDepositLineV2")


@_attrs_define
class PushDepositLineV2:
    """
    Attributes:
        quantity (float):  Example: 4.
        unit_amount (float):  Example: 50.4.
        account_ref (AccountRefDto):
        description (Union[Unset, str]):  Example: Services rendered..
        id (Union[Unset, str]):
        tax_rate_ref (Union[Unset, TaxRateRefDto]):
        entity_ref (Union[Unset, PushDepositEntityRefV2]):
        links (Union[Unset, List['LinksV2']]):
    """

    quantity: float
    unit_amount: float
    account_ref: "AccountRefDto"
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRefDto"] = UNSET
    entity_ref: Union[Unset, "PushDepositEntityRefV2"] = UNSET
    links: Union[Unset, List["LinksV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity

        unit_amount = self.unit_amount

        account_ref = self.account_ref.to_dict()

        description = self.description

        id = self.id

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

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
                "quantity": quantity,
                "unitAmount": unit_amount,
                "accountRef": account_ref,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.links_v2 import LinksV2
        from ..models.push_deposit_entity_ref_v2 import PushDepositEntityRefV2
        from ..models.tax_rate_ref_dto import TaxRateRefDto

        d = src_dict.copy()
        quantity = d.pop("quantity")

        unit_amount = d.pop("unitAmount")

        account_ref = AccountRefDto.from_dict(d.pop("accountRef"))

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRefDto]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRefDto.from_dict(_tax_rate_ref)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, PushDepositEntityRefV2]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = PushDepositEntityRefV2.from_dict(_entity_ref)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = LinksV2.from_dict(links_item_data)

            links.append(links_item)

        push_deposit_line_v2 = cls(
            quantity=quantity,
            unit_amount=unit_amount,
            account_ref=account_ref,
            description=description,
            id=id,
            tax_rate_ref=tax_rate_ref,
            entity_ref=entity_ref,
            links=links,
        )

        push_deposit_line_v2.additional_properties = d
        return push_deposit_line_v2

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
