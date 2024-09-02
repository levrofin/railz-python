from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.bank_tax_rate_ref import BankTaxRateRef
    from ..models.tracking_category_ref_accounting import TrackingCategoryRefAccounting


T = TypeVar("T", bound="BankTransactionsAccountingLineItem")


@_attrs_define
class BankTransactionsAccountingLineItem:
    """
    Attributes:
        amount (float):  Example: 322.
        account_ref (AccountRef):
        unit_amount (float):  Example: 50.5.
        quantity (float):  Example: 4.
        id (Union[Unset, str]):  Example: 8a3fdcc9-83eb-4fdd-83e0-52ec1b40b072.
        description (Union[Unset, str]):  Example: Railz store.
        tax_rate_ref (Union[Unset, BankTaxRateRef]):
        tax_amount (Union[Unset, float]):  Example: 20.5.
        tracking_category_refs (Union[Unset, List['TrackingCategoryRefAccounting']]):
    """

    amount: float
    account_ref: "AccountRef"
    unit_amount: float
    quantity: float
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tax_rate_ref: Union[Unset, "BankTaxRateRef"] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tracking_category_refs: Union[Unset, List["TrackingCategoryRefAccounting"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        account_ref = self.account_ref.to_dict()

        unit_amount = self.unit_amount

        quantity = self.quantity

        id = self.id

        description = self.description

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        tax_amount = self.tax_amount

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "accountRef": account_ref,
                "unitAmount": unit_amount,
                "quantity": quantity,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.bank_tax_rate_ref import BankTaxRateRef
        from ..models.tracking_category_ref_accounting import TrackingCategoryRefAccounting

        d = src_dict.copy()
        amount = d.pop("amount")

        account_ref = AccountRef.from_dict(d.pop("accountRef"))

        unit_amount = d.pop("unitAmount")

        quantity = d.pop("quantity")

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, BankTaxRateRef]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = BankTaxRateRef.from_dict(_tax_rate_ref)

        tax_amount = d.pop("taxAmount", UNSET)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = TrackingCategoryRefAccounting.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        bank_transactions_accounting_line_item = cls(
            amount=amount,
            account_ref=account_ref,
            unit_amount=unit_amount,
            quantity=quantity,
            id=id,
            description=description,
            tax_rate_ref=tax_rate_ref,
            tax_amount=tax_amount,
            tracking_category_refs=tracking_category_refs,
        )

        bank_transactions_accounting_line_item.additional_properties = d
        return bank_transactions_accounting_line_item

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
