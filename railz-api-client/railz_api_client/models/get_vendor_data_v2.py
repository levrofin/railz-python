from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_vendor_data_v2_status import GetVendorDataV2Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_address import BillingAddress
    from ..models.customer_vendor_contact_v2 import CustomerVendorContactV2
    from ..models.parent_ref import ParentRef
    from ..models.payment_method_ref_response import PaymentMethodRefResponse
    from ..models.shipping_address import ShippingAddress
    from ..models.subsidiary_ref import SubsidiaryRef


T = TypeVar("T", bound="GetVendorDataV2")


@_attrs_define
class GetVendorDataV2:
    """
    Attributes:
        id (str):  Example: 1.
        status (GetVendorDataV2Status):
        vendor_name (Union[Unset, str]):  Example: ACME Inc..
        contact_name (Union[Unset, str]):  Example: Jane Smith.
        email_address (Union[Unset, str]):  Example: email@acme.com.
        website (Union[Unset, str]):  Example: www.acme.com.
        phone (Union[Unset, str]):  Example: 8889990000.
        tax_number (Union[Unset, str]):  Example: 987654321.
        balance (Union[Unset, float]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        source_modified_date (Union[Unset, str]):  Example: 2021-03-09T08:49:36.035Z.
        parent_ref (Union[Unset, ParentRef]):
        contact_first_name (Union[Unset, str]):  Example: Jane.
        contact_last_name (Union[Unset, str]):  Example: Smith.
        is_person (Union[Unset, bool]):
        currency (Union[Unset, str]):  Example: USD.
        billing_address (Union[Unset, BillingAddress]):
        shipping_address (Union[Unset, ShippingAddress]):
        contacts (Union[Unset, List['CustomerVendorContactV2']]):
        payment_method_ref (Union[Unset, PaymentMethodRefResponse]):
    """

    id: str
    status: GetVendorDataV2Status
    vendor_name: Union[Unset, str] = UNSET
    contact_name: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    tax_number: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    source_modified_date: Union[Unset, str] = UNSET
    parent_ref: Union[Unset, "ParentRef"] = UNSET
    contact_first_name: Union[Unset, str] = UNSET
    contact_last_name: Union[Unset, str] = UNSET
    is_person: Union[Unset, bool] = UNSET
    currency: Union[Unset, str] = UNSET
    billing_address: Union[Unset, "BillingAddress"] = UNSET
    shipping_address: Union[Unset, "ShippingAddress"] = UNSET
    contacts: Union[Unset, List["CustomerVendorContactV2"]] = UNSET
    payment_method_ref: Union[Unset, "PaymentMethodRefResponse"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        status = self.status

        vendor_name = self.vendor_name

        contact_name = self.contact_name

        email_address = self.email_address

        website = self.website

        phone = self.phone

        tax_number = self.tax_number

        balance = self.balance

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        source_modified_date = self.source_modified_date

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        contact_first_name = self.contact_first_name

        contact_last_name = self.contact_last_name

        is_person = self.is_person

        currency = self.currency

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if vendor_name is not UNSET:
            field_dict["vendorName"] = vendor_name
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if website is not UNSET:
            field_dict["website"] = website
        if phone is not UNSET:
            field_dict["phone"] = phone
        if tax_number is not UNSET:
            field_dict["taxNumber"] = tax_number
        if balance is not UNSET:
            field_dict["balance"] = balance
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if contact_first_name is not UNSET:
            field_dict["contactFirstName"] = contact_first_name
        if contact_last_name is not UNSET:
            field_dict["contactLastName"] = contact_last_name
        if is_person is not UNSET:
            field_dict["isPerson"] = is_person
        if currency is not UNSET:
            field_dict["currency"] = currency
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.billing_address import BillingAddress
        from ..models.customer_vendor_contact_v2 import CustomerVendorContactV2
        from ..models.parent_ref import ParentRef
        from ..models.payment_method_ref_response import PaymentMethodRefResponse
        from ..models.shipping_address import ShippingAddress
        from ..models.subsidiary_ref import SubsidiaryRef

        d = src_dict.copy()
        id = d.pop("id")

        status = d.pop("status")

        vendor_name = d.pop("vendorName", UNSET)

        contact_name = d.pop("contactName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        website = d.pop("website", UNSET)

        phone = d.pop("phone", UNSET)

        tax_number = d.pop("taxNumber", UNSET)

        balance = d.pop("balance", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRef.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        source_modified_date = d.pop("sourceModifiedDate", UNSET)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, ParentRef]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = ParentRef.from_dict(_parent_ref)

        contact_first_name = d.pop("contactFirstName", UNSET)

        contact_last_name = d.pop("contactLastName", UNSET)

        is_person = d.pop("isPerson", UNSET)

        currency = d.pop("currency", UNSET)

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, BillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = BillingAddress.from_dict(_billing_address)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, ShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = ShippingAddress.from_dict(_shipping_address)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = CustomerVendorContactV2.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentMethodRefResponse]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentMethodRefResponse.from_dict(_payment_method_ref)

        get_vendor_data_v2 = cls(
            id=id,
            status=status,
            vendor_name=vendor_name,
            contact_name=contact_name,
            email_address=email_address,
            website=website,
            phone=phone,
            tax_number=tax_number,
            balance=balance,
            subsidiary_refs=subsidiary_refs,
            source_modified_date=source_modified_date,
            parent_ref=parent_ref,
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            is_person=is_person,
            currency=currency,
            billing_address=billing_address,
            shipping_address=shipping_address,
            contacts=contacts,
            payment_method_ref=payment_method_ref,
        )

        get_vendor_data_v2.additional_properties = d
        return get_vendor_data_v2

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
