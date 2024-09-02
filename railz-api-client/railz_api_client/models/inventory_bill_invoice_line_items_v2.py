from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.tax_rate_ref_dto import TaxRateRefDto


T = TypeVar("T", bound="InventoryBillInvoiceLineItemsV2")


@_attrs_define
class InventoryBillInvoiceLineItemsV2:
    """
    Attributes:
        description (Union[Unset, str]):  Example: Item description..
        unit_price (Union[Unset, float]):  Example: 2.5.
        account_ref (Union[Unset, AccountRefDto]):
        tax_rate_ref (Union[Unset, TaxRateRefDto]):
    """

    description: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRefDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        unit_price = self.unit_price

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.tax_rate_ref_dto import TaxRateRefDto

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

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

        inventory_bill_invoice_line_items_v2 = cls(
            description=description,
            unit_price=unit_price,
            account_ref=account_ref,
            tax_rate_ref=tax_rate_ref,
        )

        inventory_bill_invoice_line_items_v2.additional_properties = d
        return inventory_bill_invoice_line_items_v2

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
