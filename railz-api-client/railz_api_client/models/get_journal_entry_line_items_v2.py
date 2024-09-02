from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.journal_entry_entity_ref import JournalEntryEntityRef
    from ..models.tax_rate_ref import TaxRateRef
    from ..models.tracking_category_ref_v2 import TrackingCategoryRefV2


T = TypeVar("T", bound="GetJournalEntryLineItemsV2")


@_attrs_define
class GetJournalEntryLineItemsV2:
    """
    Attributes:
        description (Union[Unset, str]):  Example: Services rendered..
        credit (Union[Unset, float]):  Example: 100.5.
        debit (Union[Unset, float]):  Example: 3.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        account_ref (Union[Unset, AccountRef]):
        entity_ref (Union[Unset, JournalEntryEntityRef]):
        tax_rate_ref (Union[Unset, TaxRateRef]):
        id (Union[Unset, str]):  Example: 1.
        tracking_category_refs (Union[Unset, List['TrackingCategoryRefV2']]):
    """

    description: Union[Unset, str] = UNSET
    credit: Union[Unset, float] = UNSET
    debit: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    entity_ref: Union[Unset, "JournalEntryEntityRef"] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRef"] = UNSET
    id: Union[Unset, str] = UNSET
    tracking_category_refs: Union[Unset, List["TrackingCategoryRefV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        credit = self.credit

        debit = self.debit

        tax_amount = self.tax_amount

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        id = self.id

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if credit is not UNSET:
            field_dict["credit"] = credit
        if debit is not UNSET:
            field_dict["debit"] = debit
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if id is not UNSET:
            field_dict["id"] = id
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.journal_entry_entity_ref import JournalEntryEntityRef
        from ..models.tax_rate_ref import TaxRateRef
        from ..models.tracking_category_ref_v2 import TrackingCategoryRefV2

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        credit = d.pop("credit", UNSET)

        debit = d.pop("debit", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, JournalEntryEntityRef]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = JournalEntryEntityRef.from_dict(_entity_ref)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRef]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRef.from_dict(_tax_rate_ref)

        id = d.pop("id", UNSET)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = TrackingCategoryRefV2.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        get_journal_entry_line_items_v2 = cls(
            description=description,
            credit=credit,
            debit=debit,
            tax_amount=tax_amount,
            account_ref=account_ref,
            entity_ref=entity_ref,
            tax_rate_ref=tax_rate_ref,
            id=id,
            tracking_category_refs=tracking_category_refs,
        )

        get_journal_entry_line_items_v2.additional_properties = d
        return get_journal_entry_line_items_v2

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
