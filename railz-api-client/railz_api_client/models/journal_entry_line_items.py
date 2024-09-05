from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.journal_entry_line_items_type import JournalEntryLineItemsType, check_journal_entry_line_items_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="JournalEntryLineItems")


@_attrs_define
class JournalEntryLineItems:
    """
    Attributes:
        account_ref (str):  Example: 200.
        type (JournalEntryLineItemsType):  Example: debit.
        amount (float):  Example: 150.5.
        description (Union[Unset, str]):  Example: Journal Entry description..
        customer_ref (Union[Unset, str]):  Example: 250.
        vendor_ref (Union[Unset, str]):  Example: 345.
        tracking_category_ref (Union[Unset, str]):  Example: 4040.
    """

    account_ref: str
    type: JournalEntryLineItemsType
    amount: float
    description: Union[Unset, str] = UNSET
    customer_ref: Union[Unset, str] = UNSET
    vendor_ref: Union[Unset, str] = UNSET
    tracking_category_ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_ref = self.account_ref

        type: str = self.type

        amount = self.amount

        description = self.description

        customer_ref = self.customer_ref

        vendor_ref = self.vendor_ref

        tracking_category_ref = self.tracking_category_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountRef": account_ref,
                "type": type,
                "amount": amount,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_ref = d.pop("accountRef")

        type = check_journal_entry_line_items_type(d.pop("type"))

        amount = d.pop("amount")

        description = d.pop("description", UNSET)

        customer_ref = d.pop("customerRef", UNSET)

        vendor_ref = d.pop("vendorRef", UNSET)

        tracking_category_ref = d.pop("trackingCategoryRef", UNSET)

        journal_entry_line_items = cls(
            account_ref=account_ref,
            type=type,
            amount=amount,
            description=description,
            customer_ref=customer_ref,
            vendor_ref=vendor_ref,
            tracking_category_ref=tracking_category_ref,
        )

        journal_entry_line_items.additional_properties = d
        return journal_entry_line_items

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
