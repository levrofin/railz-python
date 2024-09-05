from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_bill_line_item_v1_billable_status import (
    PushBillLineItemV1BillableStatus,
    check_push_bill_line_item_v1_billable_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_object_ref_dto import CustomerObjectRefDto


T = TypeVar("T", bound="PushBillLineItemV1")


@_attrs_define
class PushBillLineItemV1:
    """
    Attributes:
        unit_amount (float):  Example: 100.5.
        quantity (float):  Example: 3.
        description (Union[Unset, str]):  Example: Services rendered..
        tax_amount (Union[Unset, float]):  Example: 20.5.
        customer_ref (Union[Unset, CustomerObjectRefDto]):
        billable_status (Union[Unset, PushBillLineItemV1BillableStatus]):  Example: notBillable.
        account_ref (Union[Unset, str]):  Example: 145.
        tracking_category_ref (Union[Unset, str]):  Example: 231.
        tax_ref (Union[Unset, str]):  Example: 24.
        sub_total (Union[Unset, float]):  Example: 301.5.
        total_amount (Union[Unset, float]):  Example: 322.
    """

    unit_amount: float
    quantity: float
    description: Union[Unset, str] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    customer_ref: Union[Unset, "CustomerObjectRefDto"] = UNSET
    billable_status: Union[Unset, PushBillLineItemV1BillableStatus] = UNSET
    account_ref: Union[Unset, str] = UNSET
    tracking_category_ref: Union[Unset, str] = UNSET
    tax_ref: Union[Unset, str] = UNSET
    sub_total: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_amount = self.unit_amount

        quantity = self.quantity

        description = self.description

        tax_amount = self.tax_amount

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        billable_status: Union[Unset, str] = UNSET
        if not isinstance(self.billable_status, Unset):
            billable_status = self.billable_status

        account_ref = self.account_ref

        tracking_category_ref = self.tracking_category_ref

        tax_ref = self.tax_ref

        sub_total = self.sub_total

        total_amount = self.total_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitAmount": unit_amount,
                "quantity": quantity,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if billable_status is not UNSET:
            field_dict["billableStatus"] = billable_status
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tracking_category_ref is not UNSET:
            field_dict["trackingCategoryRef"] = tracking_category_ref
        if tax_ref is not UNSET:
            field_dict["taxRef"] = tax_ref
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_object_ref_dto import CustomerObjectRefDto

        d = src_dict.copy()
        unit_amount = d.pop("unitAmount")

        quantity = d.pop("quantity")

        description = d.pop("description", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerObjectRefDto]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerObjectRefDto.from_dict(_customer_ref)

        _billable_status = d.pop("billableStatus", UNSET)
        billable_status: Union[Unset, PushBillLineItemV1BillableStatus]
        if isinstance(_billable_status, Unset):
            billable_status = UNSET
        else:
            billable_status = check_push_bill_line_item_v1_billable_status(_billable_status)

        account_ref = d.pop("accountRef", UNSET)

        tracking_category_ref = d.pop("trackingCategoryRef", UNSET)

        tax_ref = d.pop("taxRef", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        push_bill_line_item_v1 = cls(
            unit_amount=unit_amount,
            quantity=quantity,
            description=description,
            tax_amount=tax_amount,
            customer_ref=customer_ref,
            billable_status=billable_status,
            account_ref=account_ref,
            tracking_category_ref=tracking_category_ref,
            tax_ref=tax_ref,
            sub_total=sub_total,
            total_amount=total_amount,
        )

        push_bill_line_item_v1.additional_properties = d
        return push_bill_line_item_v1

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
