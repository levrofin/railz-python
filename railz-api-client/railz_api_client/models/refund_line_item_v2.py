from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.inventory_ref import InventoryRef
    from ..models.refund_line_item_links import RefundLineItemLinks
    from ..models.tax_rate_ref import TaxRateRef
    from ..models.tracking_category_ref_v2 import TrackingCategoryRefV2


T = TypeVar("T", bound="RefundLineItemV2")


@_attrs_define
class RefundLineItemV2:
    """
    Attributes:
        amount (float):  Example: 10.5.
        description (Union[Unset, str]):  Example: Services rendered..
        unit_amount (Union[Unset, float]):  Example: 100.5.
        quantity (Union[Unset, float]):  Example: 3.
        discount_amount (Union[Unset, float]):
        tax_amount (Union[Unset, float]):  Example: 20.5.
        tax_rate_ref (Union[Unset, TaxRateRef]):
        inventory_ref (Union[Unset, InventoryRef]):
        discount_percentage (Union[Unset, float]):  Example: 10.5.
        tracking_category_refs (Union[Unset, List['TrackingCategoryRefV2']]):
        account_ref (Union[Unset, AccountRef]):
        links (Union[Unset, List['RefundLineItemLinks']]):
    """

    amount: float
    description: Union[Unset, str] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    discount_amount: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRef"] = UNSET
    inventory_ref: Union[Unset, "InventoryRef"] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    tracking_category_refs: Union[Unset, List["TrackingCategoryRefV2"]] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    links: Union[Unset, List["RefundLineItemLinks"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

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

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
            }
        )
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
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.inventory_ref import InventoryRef
        from ..models.refund_line_item_links import RefundLineItemLinks
        from ..models.tax_rate_ref import TaxRateRef
        from ..models.tracking_category_ref_v2 import TrackingCategoryRefV2

        d = src_dict.copy()
        amount = d.pop("amount")

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

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = TrackingCategoryRefV2.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = RefundLineItemLinks.from_dict(links_item_data)

            links.append(links_item)

        refund_line_item_v2 = cls(
            amount=amount,
            description=description,
            unit_amount=unit_amount,
            quantity=quantity,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
            tax_rate_ref=tax_rate_ref,
            inventory_ref=inventory_ref,
            discount_percentage=discount_percentage,
            tracking_category_refs=tracking_category_refs,
            account_ref=account_ref,
            links=links,
        )

        refund_line_item_v2.additional_properties = d
        return refund_line_item_v2

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
