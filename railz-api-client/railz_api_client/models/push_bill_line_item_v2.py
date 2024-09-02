from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_bill_line_item_v2_billable_status import PushBillLineItemV2BillableStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.bill_tracking_category_ref_dto import BillTrackingCategoryRefDto
    from ..models.customer_object_ref_dto import CustomerObjectRefDto
    from ..models.inventory_ref_dto import InventoryRefDto
    from ..models.tax_rate_ref_dto import TaxRateRefDto


T = TypeVar("T", bound="PushBillLineItemV2")


@_attrs_define
class PushBillLineItemV2:
    """
    Attributes:
        unit_amount (float):  Example: 100.5.
        quantity (float):  Example: 3.
        id (Union[Unset, str]):  Example: 8a3fdcc9-83eb-4fdd-83e0-52ec1b40b072.
        account_ref (Union[Unset, AccountRefDto]):
        tracking_category_refs (Union[Unset, List['BillTrackingCategoryRefDto']]):
        tax_rate_ref (Union[Unset, TaxRateRefDto]):
        description (Union[Unset, str]):  Example: Services rendered..
        customer_ref (Union[Unset, CustomerObjectRefDto]):
        billable_status (Union[Unset, PushBillLineItemV2BillableStatus]):  Example: notBillable.
        discount_percentage (Union[Unset, float]):  Example: 100.5.
        inventory_ref (Union[Unset, InventoryRefDto]):
        tax_amount (Union[Unset, float]):  Example: 100.5.
    """

    unit_amount: float
    quantity: float
    id: Union[Unset, str] = UNSET
    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    tracking_category_refs: Union[Unset, List["BillTrackingCategoryRefDto"]] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRefDto"] = UNSET
    description: Union[Unset, str] = UNSET
    customer_ref: Union[Unset, "CustomerObjectRefDto"] = UNSET
    billable_status: Union[Unset, PushBillLineItemV2BillableStatus] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    inventory_ref: Union[Unset, "InventoryRefDto"] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_amount = self.unit_amount

        quantity = self.quantity

        id = self.id

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        description = self.description

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        billable_status: Union[Unset, str] = UNSET
        if not isinstance(self.billable_status, Unset):
            billable_status = self.billable_status

        discount_percentage = self.discount_percentage

        inventory_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_ref, Unset):
            inventory_ref = self.inventory_ref.to_dict()

        tax_amount = self.tax_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitAmount": unit_amount,
                "quantity": quantity,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if description is not UNSET:
            field_dict["description"] = description
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if billable_status is not UNSET:
            field_dict["billableStatus"] = billable_status
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if inventory_ref is not UNSET:
            field_dict["inventoryRef"] = inventory_ref
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.bill_tracking_category_ref_dto import BillTrackingCategoryRefDto
        from ..models.customer_object_ref_dto import CustomerObjectRefDto
        from ..models.inventory_ref_dto import InventoryRefDto
        from ..models.tax_rate_ref_dto import TaxRateRefDto

        d = src_dict.copy()
        unit_amount = d.pop("unitAmount")

        quantity = d.pop("quantity")

        id = d.pop("id", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRefDto]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRefDto.from_dict(_account_ref)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = BillTrackingCategoryRefDto.from_dict(tracking_category_refs_item_data)

            tracking_category_refs.append(tracking_category_refs_item)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRefDto]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRefDto.from_dict(_tax_rate_ref)

        description = d.pop("description", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerObjectRefDto]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerObjectRefDto.from_dict(_customer_ref)

        _billable_status = d.pop("billableStatus", UNSET)
        billable_status: Union[Unset, PushBillLineItemV2BillableStatus]
        if isinstance(_billable_status, Unset):
            billable_status = UNSET
        else:
            billable_status = _billable_status

        discount_percentage = d.pop("discountPercentage", UNSET)

        _inventory_ref = d.pop("inventoryRef", UNSET)
        inventory_ref: Union[Unset, InventoryRefDto]
        if isinstance(_inventory_ref, Unset):
            inventory_ref = UNSET
        else:
            inventory_ref = InventoryRefDto.from_dict(_inventory_ref)

        tax_amount = d.pop("taxAmount", UNSET)

        push_bill_line_item_v2 = cls(
            unit_amount=unit_amount,
            quantity=quantity,
            id=id,
            account_ref=account_ref,
            tracking_category_refs=tracking_category_refs,
            tax_rate_ref=tax_rate_ref,
            description=description,
            customer_ref=customer_ref,
            billable_status=billable_status,
            discount_percentage=discount_percentage,
            inventory_ref=inventory_ref,
            tax_amount=tax_amount,
        )

        push_bill_line_item_v2.additional_properties = d
        return push_bill_line_item_v2

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
