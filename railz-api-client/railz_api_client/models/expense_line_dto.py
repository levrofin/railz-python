from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.bill_tracking_category_ref_dto import BillTrackingCategoryRefDto
    from ..models.tax_rate_ref_dto import TaxRateRefDto


T = TypeVar("T", bound="ExpenseLineDto")


@_attrs_define
class ExpenseLineDto:
    """
    Attributes:
        account_ref (Union[Unset, AccountRefDto]):
        tax_rate_ref (Union[Unset, TaxRateRefDto]):
        tracking_category_refs (Union[Unset, List['BillTrackingCategoryRefDto']]):
        description (Union[Unset, str]):  Example: Services rendered..
        quantity (Union[Unset, float]):  Example: 4.
        unit_amount (Union[Unset, float]):  Example: 50.4.
        tax_amount (Union[Unset, float]):  Example: 50.4.
        amount (Union[Unset, float]):  Example: 50.4.
    """

    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRefDto"] = UNSET
    tracking_category_refs: Union[Unset, List["BillTrackingCategoryRefDto"]] = UNSET
    description: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

        description = self.description

        quantity = self.quantity

        unit_amount = self.unit_amount

        tax_amount = self.tax_amount

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs
        if description is not UNSET:
            field_dict["description"] = description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.bill_tracking_category_ref_dto import BillTrackingCategoryRefDto
        from ..models.tax_rate_ref_dto import TaxRateRefDto

        d = src_dict.copy()
        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRefDto]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRefDto.from_dict(_account_ref)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRefDto]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRefDto.from_dict(_tax_rate_ref)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = BillTrackingCategoryRefDto.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        description = d.pop("description", UNSET)

        quantity = d.pop("quantity", UNSET)

        unit_amount = d.pop("unitAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        amount = d.pop("amount", UNSET)

        expense_line_dto = cls(
            account_ref=account_ref,
            tax_rate_ref=tax_rate_ref,
            tracking_category_refs=tracking_category_refs,
            description=description,
            quantity=quantity,
            unit_amount=unit_amount,
            tax_amount=tax_amount,
            amount=amount,
        )

        expense_line_dto.additional_properties = d
        return expense_line_dto

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
