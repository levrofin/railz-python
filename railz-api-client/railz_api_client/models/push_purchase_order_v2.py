import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_account_ref_dto import ApAccountRefDto
    from ..models.purchase_order_line_v2 import PurchaseOrderLineV2
    from ..models.push_purchase_order_v2_pass_through import PushPurchaseOrderV2PassThrough
    from ..models.shipping_address_dto import ShippingAddressDto
    from ..models.shipping_contact import ShippingContact
    from ..models.vendor_ref_dto import VendorRefDto


T = TypeVar("T", bound="PushPurchaseOrderV2")


@_attrs_define
class PushPurchaseOrderV2:
    """
    Attributes:
        vendor_ref (VendorRefDto):
        lines (List['PurchaseOrderLineV2']):
        pass_through (Union[Unset, PushPurchaseOrderV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        due_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        delivery_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        memo (Union[Unset, str]):  Example: Example memo..
        currency (Union[Unset, str]):  Example: CAD.
        ap_account_ref (Union[Unset, ApAccountRefDto]):
        expected_arrival_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        shipping_address (Union[Unset, ShippingAddressDto]):
        contact (Union[Unset, ShippingContact]):
    """

    vendor_ref: "VendorRefDto"
    lines: List["PurchaseOrderLineV2"]
    pass_through: Union[Unset, "PushPurchaseOrderV2PassThrough"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    delivery_date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    ap_account_ref: Union[Unset, "ApAccountRefDto"] = UNSET
    expected_arrival_date: Union[Unset, datetime.date] = UNSET
    shipping_address: Union[Unset, "ShippingAddressDto"] = UNSET
    contact: Union[Unset, "ShippingContact"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vendor_ref = self.vendor_ref.to_dict()

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

        ap_account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ap_account_ref, Unset):
            ap_account_ref = self.ap_account_ref.to_dict()

        expected_arrival_date: Union[Unset, str] = UNSET
        if not isinstance(self.expected_arrival_date, Unset):
            expected_arrival_date = self.expected_arrival_date.isoformat()

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

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
        if ap_account_ref is not UNSET:
            field_dict["apAccountRef"] = ap_account_ref
        if expected_arrival_date is not UNSET:
            field_dict["expectedArrivalDate"] = expected_arrival_date
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if contact is not UNSET:
            field_dict["contact"] = contact

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ap_account_ref_dto import ApAccountRefDto
        from ..models.purchase_order_line_v2 import PurchaseOrderLineV2
        from ..models.push_purchase_order_v2_pass_through import PushPurchaseOrderV2PassThrough
        from ..models.shipping_address_dto import ShippingAddressDto
        from ..models.shipping_contact import ShippingContact
        from ..models.vendor_ref_dto import VendorRefDto

        d = src_dict.copy()
        vendor_ref = VendorRefDto.from_dict(d.pop("vendorRef"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = PurchaseOrderLineV2.from_dict(lines_item_data)

            lines.append(lines_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushPurchaseOrderV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushPurchaseOrderV2PassThrough.from_dict(_pass_through)

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

        _ap_account_ref = d.pop("apAccountRef", UNSET)
        ap_account_ref: Union[Unset, ApAccountRefDto]
        if isinstance(_ap_account_ref, Unset):
            ap_account_ref = UNSET
        else:
            ap_account_ref = ApAccountRefDto.from_dict(_ap_account_ref)

        _expected_arrival_date = d.pop("expectedArrivalDate", UNSET)
        expected_arrival_date: Union[Unset, datetime.date]
        if isinstance(_expected_arrival_date, Unset):
            expected_arrival_date = UNSET
        else:
            expected_arrival_date = isoparse(_expected_arrival_date).date()

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, ShippingAddressDto]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = ShippingAddressDto.from_dict(_shipping_address)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ShippingContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ShippingContact.from_dict(_contact)

        push_purchase_order_v2 = cls(
            vendor_ref=vendor_ref,
            lines=lines,
            pass_through=pass_through,
            currency_rate=currency_rate,
            posted_date=posted_date,
            due_date=due_date,
            delivery_date=delivery_date,
            memo=memo,
            currency=currency,
            ap_account_ref=ap_account_ref,
            expected_arrival_date=expected_arrival_date,
            shipping_address=shipping_address,
            contact=contact,
        )

        push_purchase_order_v2.additional_properties = d
        return push_purchase_order_v2

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
