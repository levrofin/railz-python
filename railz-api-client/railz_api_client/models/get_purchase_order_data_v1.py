import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_purchase_order_data_v1_status import GetPurchaseOrderDataV1Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_address import BaseAddress
    from ..models.basic_contact import BasicContact
    from ..models.currency_ref import CurrencyRef
    from ..models.invoice_bill_line_items_v1 import InvoiceBillLineItemsV1
    from ..models.vendor_ref import VendorRef


T = TypeVar("T", bound="GetPurchaseOrderDataV1")


@_attrs_define
class GetPurchaseOrderDataV1:
    """
    Attributes:
        id (str):  Example: 1.
        posted_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        total_amount (float):  Example: 322.
        status (GetPurchaseOrderDataV1Status):  Example: open.
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
        vendor_ref (Union[Unset, VendorRef]):
        currency_ref (Union[Unset, CurrencyRef]):
        lines (Union[Unset, List['InvoiceBillLineItemsV1']]):
    """

    id: str
    posted_date: datetime.datetime
    total_amount: float
    status: GetPurchaseOrderDataV1Status
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
    vendor_ref: Union[Unset, "VendorRef"] = UNSET
    currency_ref: Union[Unset, "CurrencyRef"] = UNSET
    lines: Union[Unset, List["InvoiceBillLineItemsV1"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        posted_date = self.posted_date.isoformat()

        total_amount = self.total_amount

        status = self.status

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

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "postedDate": posted_date,
                "totalAmount": total_amount,
                "status": status,
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
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_address import BaseAddress
        from ..models.basic_contact import BasicContact
        from ..models.currency_ref import CurrencyRef
        from ..models.invoice_bill_line_items_v1 import InvoiceBillLineItemsV1
        from ..models.vendor_ref import VendorRef

        d = src_dict.copy()
        id = d.pop("id")

        posted_date = isoparse(d.pop("postedDate"))

        total_amount = d.pop("totalAmount")

        status = d.pop("status")

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

        _vendor_ref = d.pop("vendorRef", UNSET)
        vendor_ref: Union[Unset, VendorRef]
        if isinstance(_vendor_ref, Unset):
            vendor_ref = UNSET
        else:
            vendor_ref = VendorRef.from_dict(_vendor_ref)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CurrencyRef.from_dict(_currency_ref)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = InvoiceBillLineItemsV1.from_dict(lines_item_data)

            lines.append(lines_item)

        get_purchase_order_data_v1 = cls(
            id=id,
            posted_date=posted_date,
            total_amount=total_amount,
            status=status,
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
            vendor_ref=vendor_ref,
            currency_ref=currency_ref,
            lines=lines,
        )

        get_purchase_order_data_v1.additional_properties = d
        return get_purchase_order_data_v1

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
