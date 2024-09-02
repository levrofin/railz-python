import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purchase_order_line_v1 import PurchaseOrderLineV1
    from ..models.push_purchase_order_v1_pass_through import PushPurchaseOrderV1PassThrough
    from ..models.shipping_address_dto import ShippingAddressDto
    from ..models.shipping_contact import ShippingContact


T = TypeVar("T", bound="PushPurchaseOrderV1")


@_attrs_define
class PushPurchaseOrderV1:
    """
    Attributes:
        vendor_ref (str):  Example: 130.
        lines (List['PurchaseOrderLineV1']):
        pass_through (Union[Unset, PushPurchaseOrderV1PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        due_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        delivery_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        memo (Union[Unset, str]):  Example: Example memo..
        currency (Union[Unset, str]):  Example: CAD.
        bill_ref (Union[Unset, str]):  Example: 164.
        expected_delivery_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        ship_to_address (Union[Unset, ShippingAddressDto]):
        ship_to_contact (Union[Unset, ShippingContact]):
    """

    vendor_ref: str
    lines: List["PurchaseOrderLineV1"]
    pass_through: Union[Unset, "PushPurchaseOrderV1PassThrough"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    delivery_date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    bill_ref: Union[Unset, str] = UNSET
    expected_delivery_date: Union[Unset, datetime.date] = UNSET
    ship_to_address: Union[Unset, "ShippingAddressDto"] = UNSET
    ship_to_contact: Union[Unset, "ShippingContact"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vendor_ref = self.vendor_ref

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        currency_rate = self.currency_rate

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.isoformat()

        memo = self.memo

        currency = self.currency

        bill_ref = self.bill_ref

        expected_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.expected_delivery_date, Unset):
            expected_delivery_date = self.expected_delivery_date.isoformat()

        ship_to_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_address, Unset):
            ship_to_address = self.ship_to_address.to_dict()

        ship_to_contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_contact, Unset):
            ship_to_contact = self.ship_to_contact.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vendorRef": vendor_ref,
                "lines": lines,
            }
        )
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if memo is not UNSET:
            field_dict["memo"] = memo
        if currency is not UNSET:
            field_dict["currency"] = currency
        if bill_ref is not UNSET:
            field_dict["billRef"] = bill_ref
        if expected_delivery_date is not UNSET:
            field_dict["expectedDeliveryDate"] = expected_delivery_date
        if ship_to_address is not UNSET:
            field_dict["shipToAddress"] = ship_to_address
        if ship_to_contact is not UNSET:
            field_dict["shipToContact"] = ship_to_contact

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.purchase_order_line_v1 import PurchaseOrderLineV1
        from ..models.push_purchase_order_v1_pass_through import PushPurchaseOrderV1PassThrough
        from ..models.shipping_address_dto import ShippingAddressDto
        from ..models.shipping_contact import ShippingContact

        d = src_dict.copy()
        vendor_ref = d.pop("vendorRef")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = PurchaseOrderLineV1.from_dict(lines_item_data)

            lines.append(lines_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushPurchaseOrderV1PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushPurchaseOrderV1PassThrough.from_dict(_pass_through)

        currency_rate = d.pop("currencyRate", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        _delivery_date = d.pop("deliveryDate", UNSET)
        delivery_date: Union[Unset, datetime.date]
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = isoparse(_delivery_date).date()

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        bill_ref = d.pop("billRef", UNSET)

        _expected_delivery_date = d.pop("expectedDeliveryDate", UNSET)
        expected_delivery_date: Union[Unset, datetime.date]
        if isinstance(_expected_delivery_date, Unset):
            expected_delivery_date = UNSET
        else:
            expected_delivery_date = isoparse(_expected_delivery_date).date()

        _ship_to_address = d.pop("shipToAddress", UNSET)
        ship_to_address: Union[Unset, ShippingAddressDto]
        if isinstance(_ship_to_address, Unset):
            ship_to_address = UNSET
        else:
            ship_to_address = ShippingAddressDto.from_dict(_ship_to_address)

        _ship_to_contact = d.pop("shipToContact", UNSET)
        ship_to_contact: Union[Unset, ShippingContact]
        if isinstance(_ship_to_contact, Unset):
            ship_to_contact = UNSET
        else:
            ship_to_contact = ShippingContact.from_dict(_ship_to_contact)

        push_purchase_order_v1 = cls(
            vendor_ref=vendor_ref,
            lines=lines,
            pass_through=pass_through,
            currency_rate=currency_rate,
            posted_date=posted_date,
            due_date=due_date,
            delivery_date=delivery_date,
            memo=memo,
            currency=currency,
            bill_ref=bill_ref,
            expected_delivery_date=expected_delivery_date,
            ship_to_address=ship_to_address,
            ship_to_contact=ship_to_contact,
        )

        push_purchase_order_v1.additional_properties = d
        return push_purchase_order_v1

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
