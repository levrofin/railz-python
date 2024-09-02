from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.inventory_ref import InventoryRef
    from ..models.tax_rate_ref import TaxRateRef
    from ..models.tracking_category_ref import TrackingCategoryRef


T = TypeVar("T", bound="InvoiceBillLineItemsV1")


@_attrs_define
class InvoiceBillLineItemsV1:
    """
    Attributes:
        description (Union[Unset, str]):  Example: Services rendered..
        unit_amount (Union[Unset, float]):  Example: 100.5.
        quantity (Union[Unset, float]):  Example: 3.
        discount_amount (Union[Unset, float]):
        tax_amount (Union[Unset, float]):  Example: 20.5.
        tax_rate_ref (Union[Unset, TaxRateRef]):
        inventory_ref (Union[Unset, InventoryRef]):
        discount_percentage (Union[Unset, float]):  Example: 10.5.
        id (Union[Unset, str]):
        account_ref (Union[Unset, AccountRef]):
        total_amount (Union[Unset, float]):  Example: 10.5.
        sub_total (Union[Unset, float]):  Example: 301.5.
        tracking_category_ref (Union[Unset, TrackingCategoryRef]):
    """

    description: Union[Unset, str] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    discount_amount: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRef"] = UNSET
    inventory_ref: Union[Unset, "InventoryRef"] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    id: Union[Unset, str] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    total_amount: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tracking_category_ref: Union[Unset, "TrackingCategoryRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        unit_amount = self.unit_amount

        quantity = self.quantity

        discount_amount = self.discount_amount

        tax_amount = self.tax_amount

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        inventory_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_ref, Unset):
            inventory_ref = self.inventory_ref.to_dict()

        discount_percentage = self.discount_percentage

        id = self.id

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        total_amount = self.total_amount

        sub_total = self.sub_total

        tracking_category_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracking_category_ref, Unset):
            tracking_category_ref = self.tracking_category_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if inventory_ref is not UNSET:
            field_dict["inventoryRef"] = inventory_ref
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if id is not UNSET:
            field_dict["id"] = id
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tracking_category_ref is not UNSET:
            field_dict["trackingCategoryRef"] = tracking_category_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.inventory_ref import InventoryRef
        from ..models.tax_rate_ref import TaxRateRef
        from ..models.tracking_category_ref import TrackingCategoryRef

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        unit_amount = d.pop("unitAmount", UNSET)

        quantity = d.pop("quantity", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRef]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRef.from_dict(_tax_rate_ref)

        _inventory_ref = d.pop("inventoryRef", UNSET)
        inventory_ref: Union[Unset, InventoryRef]
        if isinstance(_inventory_ref, Unset):
            inventory_ref = UNSET
        else:
            inventory_ref = InventoryRef.from_dict(_inventory_ref)

        discount_percentage = d.pop("discountPercentage", UNSET)

        id = d.pop("id", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

        total_amount = d.pop("totalAmount", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        _tracking_category_ref = d.pop("trackingCategoryRef", UNSET)
        tracking_category_ref: Union[Unset, TrackingCategoryRef]
        if isinstance(_tracking_category_ref, Unset):
            tracking_category_ref = UNSET
        else:
            tracking_category_ref = TrackingCategoryRef.from_dict(_tracking_category_ref)

        invoice_bill_line_items_v1 = cls(
            description=description,
            unit_amount=unit_amount,
            quantity=quantity,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
            tax_rate_ref=tax_rate_ref,
            inventory_ref=inventory_ref,
            discount_percentage=discount_percentage,
            id=id,
            account_ref=account_ref,
            total_amount=total_amount,
            sub_total=sub_total,
            tracking_category_ref=tracking_category_ref,
        )

        invoice_bill_line_items_v1.additional_properties = d
        return invoice_bill_line_items_v1

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
