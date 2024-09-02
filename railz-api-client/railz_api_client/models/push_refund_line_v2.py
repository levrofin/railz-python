from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.inventory_ref_dto import InventoryRefDto
    from ..models.push_refund_line_link_v2 import PushRefundLineLinkV2
    from ..models.refund_tracking_category_ref_dto import RefundTrackingCategoryRefDto
    from ..models.tax_rate_ref_dto import TaxRateRefDto


T = TypeVar("T", bound="PushRefundLineV2")


@_attrs_define
class PushRefundLineV2:
    """
    Attributes:
        amount (float):  Example: 12.88.
        description (Union[Unset, str]):  Example: Refund description.
        inventory_ref (Union[Unset, InventoryRefDto]):
        tax_rate_ref (Union[Unset, TaxRateRefDto]):
        unit_amount (Union[Unset, float]):  Example: 12.88.
        quantity (Union[Unset, float]):  Example: 3.
        discount_percentage (Union[Unset, float]):  Example: 100.5.
        account_ref (Union[Unset, AccountRefDto]):
        tracking_category_refs (Union[Unset, List['RefundTrackingCategoryRefDto']]):
        links (Union[Unset, List['PushRefundLineLinkV2']]):
    """

    amount: float
    description: Union[Unset, str] = UNSET
    inventory_ref: Union[Unset, "InventoryRefDto"] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRefDto"] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    tracking_category_refs: Union[Unset, List["RefundTrackingCategoryRefDto"]] = UNSET
    links: Union[Unset, List["PushRefundLineLinkV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        description = self.description

        inventory_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_ref, Unset):
            inventory_ref = self.inventory_ref.to_dict()

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        unit_amount = self.unit_amount

        quantity = self.quantity

        discount_percentage = self.discount_percentage

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

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
        if inventory_ref is not UNSET:
            field_dict["inventoryRef"] = inventory_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.inventory_ref_dto import InventoryRefDto
        from ..models.push_refund_line_link_v2 import PushRefundLineLinkV2
        from ..models.refund_tracking_category_ref_dto import RefundTrackingCategoryRefDto
        from ..models.tax_rate_ref_dto import TaxRateRefDto

        d = src_dict.copy()
        amount = d.pop("amount")

        description = d.pop("description", UNSET)

        _inventory_ref = d.pop("inventoryRef", UNSET)
        inventory_ref: Union[Unset, InventoryRefDto]
        if isinstance(_inventory_ref, Unset):
            inventory_ref = UNSET
        else:
            inventory_ref = InventoryRefDto.from_dict(_inventory_ref)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRefDto]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRefDto.from_dict(_tax_rate_ref)

        unit_amount = d.pop("unitAmount", UNSET)

        quantity = d.pop("quantity", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRefDto]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRefDto.from_dict(_account_ref)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = RefundTrackingCategoryRefDto.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = PushRefundLineLinkV2.from_dict(links_item_data)

            links.append(links_item)

        push_refund_line_v2 = cls(
            amount=amount,
            description=description,
            inventory_ref=inventory_ref,
            tax_rate_ref=tax_rate_ref,
            unit_amount=unit_amount,
            quantity=quantity,
            discount_percentage=discount_percentage,
            account_ref=account_ref,
            tracking_category_refs=tracking_category_refs,
            links=links,
        )

        push_refund_line_v2.additional_properties = d
        return push_refund_line_v2

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
