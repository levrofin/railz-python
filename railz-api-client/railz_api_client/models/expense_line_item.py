from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.tax_rate_object_ref_response import TaxRateObjectRefResponse
    from ..models.tracking_category_response import TrackingCategoryResponse


T = TypeVar("T", bound="ExpenseLineItem")


@_attrs_define
class ExpenseLineItem:
    """
    Attributes:
        amount (float):  Example: 10.5.
        account_ref (Union[Unset, AccountRef]):
        description (Union[Unset, str]):  Example: Services rendered..
        unit_amount (Union[Unset, float]):  Example: 100.5.
        quantity (Union[Unset, float]):  Example: 3.
        tax_rate_ref (Union[Unset, TaxRateObjectRefResponse]):
        tax_amount (Union[Unset, float]):  Example: 20.5.
        tracking_category_refs (Union[Unset, List['TrackingCategoryResponse']]):
    """

    amount: float
    account_ref: Union[Unset, "AccountRef"] = UNSET
    description: Union[Unset, str] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateObjectRefResponse"] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tracking_category_refs: Union[Unset, List["TrackingCategoryResponse"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        description = self.description

        unit_amount = self.unit_amount

        quantity = self.quantity

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
            }
        )
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if description is not UNSET:
            field_dict["description"] = description
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
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
        from ..models.tax_rate_object_ref_response import TaxRateObjectRefResponse
        from ..models.tracking_category_response import TrackingCategoryResponse

        d = src_dict.copy()
        amount = d.pop("amount")

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

        description = d.pop("description", UNSET)

        unit_amount = d.pop("unitAmount", UNSET)

        quantity = d.pop("quantity", UNSET)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateObjectRefResponse]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateObjectRefResponse.from_dict(_tax_rate_ref)

        tax_amount = d.pop("taxAmount", UNSET)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = TrackingCategoryResponse.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        expense_line_item = cls(
            amount=amount,
            account_ref=account_ref,
            description=description,
            unit_amount=unit_amount,
            quantity=quantity,
            tax_rate_ref=tax_rate_ref,
            tax_amount=tax_amount,
            tracking_category_refs=tracking_category_refs,
        )

        expense_line_item.additional_properties = d
        return expense_line_item

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
