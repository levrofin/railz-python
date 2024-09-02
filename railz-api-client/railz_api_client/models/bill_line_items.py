from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bill_line_items_billable_status import BillLineItemsBillableStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.customer_object_ref_response import CustomerObjectRefResponse
    from ..models.inventory_ref import InventoryRef
    from ..models.tax_rate_ref import TaxRateRef
    from ..models.tracking_category_ref import TrackingCategoryRef


T = TypeVar("T", bound="BillLineItems")


@_attrs_define
class BillLineItems:
    """
    Attributes:
        id (str):  Example: 8a3fdcc9-83eb-4fdd-83e0-52ec1b40b072.
        description (Union[Unset, str]):  Example: Services rendered..
        unit_amount (Union[Unset, float]):  Example: 100.5.
        quantity (Union[Unset, float]):  Example: 3.
        discount_amount (Union[Unset, float]):
        tax_amount (Union[Unset, float]):  Example: 20.5.
        tax_rate_ref (Union[Unset, TaxRateRef]):
        inventory_ref (Union[Unset, InventoryRef]):
        discount_percentage (Union[Unset, float]):  Example: 10.5.
        account_ref (Union[Unset, AccountRef]):
        tracking_category_ref (Union[Unset, TrackingCategoryRef]):
        total_amount (Union[Unset, float]):  Example: 10.5.
        customer_ref (Union[Unset, CustomerObjectRefResponse]):
        billable_status (Union[Unset, BillLineItemsBillableStatus]):  Example: notBillable.
        sub_total (Union[Unset, float]):  Example: 301.5.
    """

    id: str
    description: Union[Unset, str] = UNSET
    unit_amount: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    discount_amount: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRef"] = UNSET
    inventory_ref: Union[Unset, "InventoryRef"] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    tracking_category_ref: Union[Unset, "TrackingCategoryRef"] = UNSET
    total_amount: Union[Unset, float] = UNSET
    customer_ref: Union[Unset, "CustomerObjectRefResponse"] = UNSET
    billable_status: Union[Unset, BillLineItemsBillableStatus] = UNSET
    sub_total: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

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

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tracking_category_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracking_category_ref, Unset):
            tracking_category_ref = self.tracking_category_ref.to_dict()

        total_amount = self.total_amount

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        billable_status: Union[Unset, str] = UNSET
        if not isinstance(self.billable_status, Unset):
            billable_status = self.billable_status

        sub_total = self.sub_total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
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
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tracking_category_ref is not UNSET:
            field_dict["trackingCategoryRef"] = tracking_category_ref
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if billable_status is not UNSET:
            field_dict["billableStatus"] = billable_status
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.customer_object_ref_response import CustomerObjectRefResponse
        from ..models.inventory_ref import InventoryRef
        from ..models.tax_rate_ref import TaxRateRef
        from ..models.tracking_category_ref import TrackingCategoryRef

        d = src_dict.copy()
        id = d.pop("id")

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

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

        _tracking_category_ref = d.pop("trackingCategoryRef", UNSET)
        tracking_category_ref: Union[Unset, TrackingCategoryRef]
        if isinstance(_tracking_category_ref, Unset):
            tracking_category_ref = UNSET
        else:
            tracking_category_ref = TrackingCategoryRef.from_dict(_tracking_category_ref)

        total_amount = d.pop("totalAmount", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerObjectRefResponse]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerObjectRefResponse.from_dict(_customer_ref)

        _billable_status = d.pop("billableStatus", UNSET)
        billable_status: Union[Unset, BillLineItemsBillableStatus]
        if isinstance(_billable_status, Unset):
            billable_status = UNSET
        else:
            billable_status = _billable_status

        sub_total = d.pop("subTotal", UNSET)

        bill_line_items = cls(
            id=id,
            description=description,
            unit_amount=unit_amount,
            quantity=quantity,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
            tax_rate_ref=tax_rate_ref,
            inventory_ref=inventory_ref,
            discount_percentage=discount_percentage,
            account_ref=account_ref,
            tracking_category_ref=tracking_category_ref,
            total_amount=total_amount,
            customer_ref=customer_ref,
            billable_status=billable_status,
            sub_total=sub_total,
        )

        bill_line_items.additional_properties = d
        return bill_line_items

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
