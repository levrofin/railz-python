import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_purchase_order_data_v2_status import (
    GetPurchaseOrderDataV2Status,
    check_get_purchase_order_data_v2_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.base_address import BaseAddress
    from ..models.basic_contact import BasicContact
    from ..models.get_purchase_order_data_v2_pass_through import GetPurchaseOrderDataV2PassThrough
    from ..models.invoice_bill_line_items_v2 import InvoiceBillLineItemsV2
    from ..models.vendor_ref import VendorRef


T = TypeVar("T", bound="GetPurchaseOrderDataV2")


@_attrs_define
class GetPurchaseOrderDataV2:
    """
    Attributes:
        id (str):  Example: 1.
        posted_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        total_amount (float):  Example: 322.
        status (GetPurchaseOrderDataV2Status):  Example: open.
        vendor_ref (VendorRef):
        lines (List['InvoiceBillLineItemsV2']):
        delivery_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        expected_arrival_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        due_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        total_discount (Union[Unset, float]):  Example: 322.
        discount_percentage (Union[Unset, float]):  Example: 322.
        sub_total (Union[Unset, float]):  Example: 301.5.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        memo (Union[Unset, str]):  Example: Example bill memo..
        shipping_address (Union[Unset, BaseAddress]):
        contact (Union[Unset, BasicContact]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency (Union[Unset, str]):  Example: USD.
        ap_account_ref (Union[Unset, AccountRef]):
        pass_through (Union[Unset, GetPurchaseOrderDataV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    id: str
    posted_date: datetime.datetime
    total_amount: float
    status: GetPurchaseOrderDataV2Status
    vendor_ref: "VendorRef"
    lines: List["InvoiceBillLineItemsV2"]
    delivery_date: Union[Unset, datetime.datetime] = UNSET
    expected_arrival_date: Union[Unset, datetime.datetime] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    shipping_address: Union[Unset, "BaseAddress"] = UNSET
    contact: Union[Unset, "BasicContact"] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    ap_account_ref: Union[Unset, "AccountRef"] = UNSET
    pass_through: Union[Unset, "GetPurchaseOrderDataV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        posted_date = self.posted_date.isoformat()

        total_amount = self.total_amount

        status: str = self.status

        vendor_ref = self.vendor_ref.to_dict()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.isoformat()

        expected_arrival_date: Union[Unset, str] = UNSET
        if not isinstance(self.expected_arrival_date, Unset):
            expected_arrival_date = self.expected_arrival_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        currency_rate = self.currency_rate

        total_discount = self.total_discount

        discount_percentage = self.discount_percentage

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        memo = self.memo

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        currency = self.currency

        ap_account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ap_account_ref, Unset):
            ap_account_ref = self.ap_account_ref.to_dict()

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "postedDate": posted_date,
                "totalAmount": total_amount,
                "status": status,
                "vendorRef": vendor_ref,
                "lines": lines,
            }
        )
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if expected_arrival_date is not UNSET:
            field_dict["expectedArrivalDate"] = expected_arrival_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if memo is not UNSET:
            field_dict["memo"] = memo
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if contact is not UNSET:
            field_dict["contact"] = contact
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if ap_account_ref is not UNSET:
            field_dict["apAccountRef"] = ap_account_ref
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.base_address import BaseAddress
        from ..models.basic_contact import BasicContact
        from ..models.get_purchase_order_data_v2_pass_through import GetPurchaseOrderDataV2PassThrough
        from ..models.invoice_bill_line_items_v2 import InvoiceBillLineItemsV2
        from ..models.vendor_ref import VendorRef

        d = src_dict.copy()
        id = d.pop("id")

        posted_date = isoparse(d.pop("postedDate"))

        total_amount = d.pop("totalAmount")

        status = check_get_purchase_order_data_v2_status(d.pop("status"))

        vendor_ref = VendorRef.from_dict(d.pop("vendorRef"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = InvoiceBillLineItemsV2.from_dict(lines_item_data)

            lines.append(lines_item)

        _delivery_date = d.pop("deliveryDate", UNSET)
        delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = isoparse(_delivery_date)

        _expected_arrival_date = d.pop("expectedArrivalDate", UNSET)
        expected_arrival_date: Union[Unset, datetime.datetime]
        if isinstance(_expected_arrival_date, Unset):
            expected_arrival_date = UNSET
        else:
            expected_arrival_date = isoparse(_expected_arrival_date)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        currency_rate = d.pop("currencyRate", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        memo = d.pop("memo", UNSET)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, BaseAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = BaseAddress.from_dict(_shipping_address)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, BasicContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = BasicContact.from_dict(_contact)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        currency = d.pop("currency", UNSET)

        _ap_account_ref = d.pop("apAccountRef", UNSET)
        ap_account_ref: Union[Unset, AccountRef]
        if isinstance(_ap_account_ref, Unset):
            ap_account_ref = UNSET
        else:
            ap_account_ref = AccountRef.from_dict(_ap_account_ref)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, GetPurchaseOrderDataV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = GetPurchaseOrderDataV2PassThrough.from_dict(_pass_through)

        get_purchase_order_data_v2 = cls(
            id=id,
            posted_date=posted_date,
            total_amount=total_amount,
            status=status,
            vendor_ref=vendor_ref,
            lines=lines,
            delivery_date=delivery_date,
            expected_arrival_date=expected_arrival_date,
            due_date=due_date,
            currency_rate=currency_rate,
            total_discount=total_discount,
            discount_percentage=discount_percentage,
            sub_total=sub_total,
            tax_amount=tax_amount,
            memo=memo,
            shipping_address=shipping_address,
            contact=contact,
            source_modified_date=source_modified_date,
            currency=currency,
            ap_account_ref=ap_account_ref,
            pass_through=pass_through,
        )

        get_purchase_order_data_v2.additional_properties = d
        return get_purchase_order_data_v2

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
