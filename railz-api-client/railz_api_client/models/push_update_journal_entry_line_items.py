from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_update_journal_entry_line_items_type import PushUpdateJournalEntryLineItemsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PushUpdateJournalEntryLineItems")


@_attrs_define
class PushUpdateJournalEntryLineItems:
    """
    Attributes:
        account_ref (str):  Example: 200.
        type (PushUpdateJournalEntryLineItemsType):  Example: debit.
        description (Union[Unset, str]):  Example: Journal Entry description..
        customer_ref (Union[Unset, str]):  Example: 250.
        vendor_ref (Union[Unset, str]):  Example: 345.
        tracking_category_ref (Union[Unset, str]):  Example: 4040.
        amount (Union[Unset, float]):  Example: 150.5.
        id (Union[Unset, str]):  Example: 200.
    """

    account_ref: str
    type: PushUpdateJournalEntryLineItemsType
    description: Union[Unset, str] = UNSET
    customer_ref: Union[Unset, str] = UNSET
    vendor_ref: Union[Unset, str] = UNSET
    tracking_category_ref: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_ref = self.account_ref

        type = self.type

        description = self.description

        customer_ref = self.customer_ref

        vendor_ref = self.vendor_ref

        tracking_category_ref = self.tracking_category_ref

        amount = self.amount

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountRef": account_ref,
                "type": type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if tracking_category_ref is not UNSET:
            field_dict["trackingCategoryRef"] = tracking_category_ref
        if amount is not UNSET:
            field_dict["amount"] = amount
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_ref = d.pop("accountRef")

        type = d.pop("type")

        description = d.pop("description", UNSET)

        customer_ref = d.pop("customerRef", UNSET)

        vendor_ref = d.pop("vendorRef", UNSET)

        tracking_category_ref = d.pop("trackingCategoryRef", UNSET)

        amount = d.pop("amount", UNSET)

        id = d.pop("id", UNSET)

        push_update_journal_entry_line_items = cls(
            account_ref=account_ref,
            type=type,
            description=description,
            customer_ref=customer_ref,
            vendor_ref=vendor_ref,
            tracking_category_ref=tracking_category_ref,
            amount=amount,
            id=id,
        )

        push_update_journal_entry_line_items.additional_properties = d
        return push_update_journal_entry_line_items

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
