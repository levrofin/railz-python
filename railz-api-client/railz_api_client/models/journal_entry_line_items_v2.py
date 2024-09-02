from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.bill_tracking_category_ref_dto import BillTrackingCategoryRefDto
    from ..models.entity_ref_dto import EntityRefDto
    from ..models.tax_rate_ref_dto import TaxRateRefDto


T = TypeVar("T", bound="JournalEntryLineItemsV2")


@_attrs_define
class JournalEntryLineItemsV2:
    """
    Attributes:
        account_ref (AccountRefDto):
        description (Union[Unset, str]):  Example: Journal Entry description..
        tracking_category_refs (Union[Unset, List['BillTrackingCategoryRefDto']]):
        entity_ref (Union[Unset, EntityRefDto]):
        tax_rate_ref (Union[Unset, TaxRateRefDto]):
        debit (Union[Unset, float]):  Example: 100.3.
        credit (Union[Unset, float]):  Example: 100.3.
        id (Union[Unset, str]):  Example: 1.
    """

    account_ref: "AccountRefDto"
    description: Union[Unset, str] = UNSET
    tracking_category_refs: Union[Unset, List["BillTrackingCategoryRefDto"]] = UNSET
    entity_ref: Union[Unset, "EntityRefDto"] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRefDto"] = UNSET
    debit: Union[Unset, float] = UNSET
    credit: Union[Unset, float] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_ref = self.account_ref.to_dict()

        description = self.description

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        debit = self.debit

        credit = self.credit

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountRef": account_ref,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if debit is not UNSET:
            field_dict["debit"] = debit
        if credit is not UNSET:
            field_dict["credit"] = credit
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.bill_tracking_category_ref_dto import BillTrackingCategoryRefDto
        from ..models.entity_ref_dto import EntityRefDto
        from ..models.tax_rate_ref_dto import TaxRateRefDto

        d = src_dict.copy()
        account_ref = AccountRefDto.from_dict(d.pop("accountRef"))

        description = d.pop("description", UNSET)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = BillTrackingCategoryRefDto.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, EntityRefDto]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = EntityRefDto.from_dict(_entity_ref)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRefDto]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRefDto.from_dict(_tax_rate_ref)

        debit = d.pop("debit", UNSET)

        credit = d.pop("credit", UNSET)

        id = d.pop("id", UNSET)

        journal_entry_line_items_v2 = cls(
            account_ref=account_ref,
            description=description,
            tracking_category_refs=tracking_category_refs,
            entity_ref=entity_ref,
            tax_rate_ref=tax_rate_ref,
            debit=debit,
            credit=credit,
            id=id,
        )

        journal_entry_line_items_v2.additional_properties = d
        return journal_entry_line_items_v2

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
