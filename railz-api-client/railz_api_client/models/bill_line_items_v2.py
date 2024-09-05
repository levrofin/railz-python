from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bill_line_items_v2_billable_status import (
    BillLineItemsV2BillableStatus,
    check_bill_line_items_v2_billable_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.customer_object_ref_response import CustomerObjectRefResponse
    from ..models.inventory_ref import InventoryRef
    from ..models.tax_rate_ref import TaxRateRef
    from ..models.tracking_category_response import TrackingCategoryResponse


T = TypeVar("T", bound="BillLineItemsV2")


@_attrs_define
class BillLineItemsV2:
    """
    Attributes:
        id (str):  Example: 8a3fdcc9-83eb-4fdd-83e0-52ec1b40b072.
        amount (float):  Example: 322.
        account_ref (Union[Unset, AccountRef]):
        tax_rate_ref (Union[Unset, TaxRateRef]):
        inventory_ref (Union[Unset, InventoryRef]):
        tracking_category_refs (Union[Unset, List['TrackingCategoryResponse']]):
        description (Union[Unset, str]):  Example: Services rendered..
        unit_amount (Union[Unset, float]):  Example: 100.5.
        quantity (Union[Unset, float]):  Example: 3.
        discount_amount (Union[Unset, float]):
        tax_amount (Union[Unset, float]):  Example: 20.5.
        discount_percentage (Union[Unset, float]):  Example: 10.5.
        customer_ref (Union[Unset, CustomerObjectRefResponse]):
        billable_status (Union[Unset, BillLineItemsV2BillableStatus]):  Example: notBillable.
    """

    id: str
    amount: float
    account_ref: Union[Unset, "AccountRef"] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRef"] = UNSET
    inventory_ref: Union[Unset, "InventoryRef"] = UNSET
    tracking_category_refs: Union[Unset, List["TrackingCategoryResponse"]] = UNSET
    description: Union[Unset, str] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    discount_amount: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    customer_ref: Union[Unset, "CustomerObjectRefResponse"] = UNSET
    billable_status: Union[Unset, BillLineItemsV2BillableStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        amount = self.amount

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        inventory_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_ref, Unset):
            inventory_ref = self.inventory_ref.to_dict()

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

        description = self.description

        unit_amount = self.unit_amount

        quantity = self.quantity

        discount_amount = self.discount_amount

        tax_amount = self.tax_amount

        discount_percentage = self.discount_percentage

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        billable_status: Union[Unset, str] = UNSET
        if not isinstance(self.billable_status, Unset):
            billable_status = self.billable_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "amount": amount,
            }
        )
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if inventory_ref is not UNSET:
            field_dict["inventoryRef"] = inventory_ref
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs
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
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if billable_status is not UNSET:
            field_dict["billableStatus"] = billable_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.customer_object_ref_response import CustomerObjectRefResponse
        from ..models.inventory_ref import InventoryRef
        from ..models.tax_rate_ref import TaxRateRef
        from ..models.tracking_category_response import TrackingCategoryResponse

        d = src_dict.copy()
        id = d.pop("id")

        amount = d.pop("amount")

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

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

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = TrackingCategoryResponse.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        description = d.pop("description", UNSET)

        unit_amount = d.pop("unitAmount", UNSET)

        quantity = d.pop("quantity", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerObjectRefResponse]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerObjectRefResponse.from_dict(_customer_ref)

        _billable_status = d.pop("billableStatus", UNSET)
        billable_status: Union[Unset, BillLineItemsV2BillableStatus]
        if isinstance(_billable_status, Unset):
            billable_status = UNSET
        else:
            billable_status = check_bill_line_items_v2_billable_status(_billable_status)

        bill_line_items_v2 = cls(
            id=id,
            amount=amount,
            account_ref=account_ref,
            tax_rate_ref=tax_rate_ref,
            inventory_ref=inventory_ref,
            tracking_category_refs=tracking_category_refs,
            description=description,
            unit_amount=unit_amount,
            quantity=quantity,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
            discount_percentage=discount_percentage,
            customer_ref=customer_ref,
            billable_status=billable_status,
        )

        bill_line_items_v2.additional_properties = d
        return bill_line_items_v2

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
