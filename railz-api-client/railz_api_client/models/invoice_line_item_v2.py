from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.inventory_ref_dto import InventoryRefDto
    from ..models.push_invoice_tracking_category_ref import PushInvoiceTrackingCategoryRef
    from ..models.tax_rate_ref_dto import TaxRateRefDto


T = TypeVar("T", bound="InvoiceLineItemV2")


@_attrs_define
class InvoiceLineItemV2:
    """
    Attributes:
        description (Union[Unset, str]):  Example: Services rendered..
        quantity (Union[Unset, float]):  Example: 3.
        id (Union[Unset, str]):  Example: 240.
        discount_percentage (Union[Unset, float]):  Example: 30.
        discount_amount (Union[Unset, float]):  Example: 20.5.
        tax_rate_ref (Union[Unset, TaxRateRefDto]):
        account_ref (Union[Unset, AccountRefDto]):
        inventory_ref (Union[Unset, InventoryRefDto]):
        tracking_category_refs (Union[Unset, List['PushInvoiceTrackingCategoryRef']]):
        unit_amount (Union[Unset, float]):  Example: 100.5.
    """

    description: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    id: Union[Unset, str] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    discount_amount: Union[Unset, float] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRefDto"] = UNSET
    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    inventory_ref: Union[Unset, "InventoryRefDto"] = UNSET
    tracking_category_refs: Union[Unset, List["PushInvoiceTrackingCategoryRef"]] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        quantity = self.quantity

        id = self.id

        discount_percentage = self.discount_percentage

        discount_amount = self.discount_amount

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        inventory_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_ref, Unset):
            inventory_ref = self.inventory_ref.to_dict()

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

        unit_amount = self.unit_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if id is not UNSET:
            field_dict["id"] = id
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if inventory_ref is not UNSET:
            field_dict["inventoryRef"] = inventory_ref
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.inventory_ref_dto import InventoryRefDto
        from ..models.push_invoice_tracking_category_ref import PushInvoiceTrackingCategoryRef
        from ..models.tax_rate_ref_dto import TaxRateRefDto

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        quantity = d.pop("quantity", UNSET)

        id = d.pop("id", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRefDto]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRefDto.from_dict(_tax_rate_ref)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRefDto]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRefDto.from_dict(_account_ref)

        _inventory_ref = d.pop("inventoryRef", UNSET)
        inventory_ref: Union[Unset, InventoryRefDto]
        if isinstance(_inventory_ref, Unset):
            inventory_ref = UNSET
        else:
            inventory_ref = InventoryRefDto.from_dict(_inventory_ref)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = PushInvoiceTrackingCategoryRef.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        unit_amount = d.pop("unitAmount", UNSET)

        invoice_line_item_v2 = cls(
            description=description,
            quantity=quantity,
            id=id,
            discount_percentage=discount_percentage,
            discount_amount=discount_amount,
            tax_rate_ref=tax_rate_ref,
            account_ref=account_ref,
            inventory_ref=inventory_ref,
            tracking_category_refs=tracking_category_refs,
            unit_amount=unit_amount,
        )

        invoice_line_item_v2.additional_properties = d
        return invoice_line_item_v2

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
