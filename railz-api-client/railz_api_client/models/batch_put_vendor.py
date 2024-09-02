from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_put_vendor_pass_through import BatchPutVendorPassThrough
    from ..models.billing_address_dto import BillingAddressDto
    from ..models.parent_ref_dto import ParentRefDto
    from ..models.payment_method_ref_dto import PaymentMethodRefDto
    from ..models.push_customer_vendor_contact_v2 import PushCustomerVendorContactV2
    from ..models.shipping_address_dto import ShippingAddressDto
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto


T = TypeVar("T", bound="BatchPutVendor")


@_attrs_define
class BatchPutVendor:
    """
    Attributes:
        vendor_ref (str): id of vendor to be updated
        contact_first_name (Union[Unset, str]):  Example: Jane.
        contact_last_name (Union[Unset, str]):  Example: Smith.
        email_address (Union[Unset, str]):  Example: email@acme.com.
        phone (Union[Unset, str]):  Example: 8889990000.
        website (Union[Unset, str]):  Example: www.acme.com.
        is_person (Union[Unset, bool]):
        vendor_name (Union[Unset, str]):  Example: ACME Inc..
        contact_name (Union[Unset, str]):  Example: Jane Smith.
        parent_ref (Union[Unset, ParentRefDto]):
        currency (Union[Unset, str]):  Example: CAD.
        payment_method_ref (Union[Unset, PaymentMethodRefDto]):
        billing_address (Union[Unset, BillingAddressDto]):
        contacts (Union[Unset, List['PushCustomerVendorContactV2']]):
        tax_number (Union[Unset, str]):  Example: 987654321.
        shipping_address (Union[Unset, ShippingAddressDto]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        pass_through (Union[Unset, BatchPutVendorPassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    vendor_ref: str
    contact_first_name: Union[Unset, str] = UNSET
    contact_last_name: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    is_person: Union[Unset, bool] = UNSET
    vendor_name: Union[Unset, str] = UNSET
    contact_name: Union[Unset, str] = UNSET
    parent_ref: Union[Unset, "ParentRefDto"] = UNSET
    currency: Union[Unset, str] = UNSET
    payment_method_ref: Union[Unset, "PaymentMethodRefDto"] = UNSET
    billing_address: Union[Unset, "BillingAddressDto"] = UNSET
    contacts: Union[Unset, List["PushCustomerVendorContactV2"]] = UNSET
    tax_number: Union[Unset, str] = UNSET
    shipping_address: Union[Unset, "ShippingAddressDto"] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    pass_through: Union[Unset, "BatchPutVendorPassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vendor_ref = self.vendor_ref

        contact_first_name = self.contact_first_name

        contact_last_name = self.contact_last_name

        email_address = self.email_address

        phone = self.phone

        website = self.website

        is_person = self.is_person

        vendor_name = self.vendor_name

        contact_name = self.contact_name

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        currency = self.currency

        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        tax_number = self.tax_number

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vendorRef": vendor_ref,
            }
        )
        if contact_first_name is not UNSET:
            field_dict["contactFirstName"] = contact_first_name
        if contact_last_name is not UNSET:
            field_dict["contactLastName"] = contact_last_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if phone is not UNSET:
            field_dict["phone"] = phone
        if website is not UNSET:
            field_dict["website"] = website
        if is_person is not UNSET:
            field_dict["isPerson"] = is_person
        if vendor_name is not UNSET:
            field_dict["vendorName"] = vendor_name
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if tax_number is not UNSET:
            field_dict["taxNumber"] = tax_number
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_put_vendor_pass_through import BatchPutVendorPassThrough
        from ..models.billing_address_dto import BillingAddressDto
        from ..models.parent_ref_dto import ParentRefDto
        from ..models.payment_method_ref_dto import PaymentMethodRefDto
        from ..models.push_customer_vendor_contact_v2 import PushCustomerVendorContactV2
        from ..models.shipping_address_dto import ShippingAddressDto
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto

        d = src_dict.copy()
        vendor_ref = d.pop("vendorRef")

        contact_first_name = d.pop("contactFirstName", UNSET)

        contact_last_name = d.pop("contactLastName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        phone = d.pop("phone", UNSET)

        website = d.pop("website", UNSET)

        is_person = d.pop("isPerson", UNSET)

        vendor_name = d.pop("vendorName", UNSET)

        contact_name = d.pop("contactName", UNSET)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, ParentRefDto]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = ParentRefDto.from_dict(_parent_ref)

        currency = d.pop("currency", UNSET)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentMethodRefDto]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentMethodRefDto.from_dict(_payment_method_ref)

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, BillingAddressDto]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = BillingAddressDto.from_dict(_billing_address)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = PushCustomerVendorContactV2.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        tax_number = d.pop("taxNumber", UNSET)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, ShippingAddressDto]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = ShippingAddressDto.from_dict(_shipping_address)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, BatchPutVendorPassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = BatchPutVendorPassThrough.from_dict(_pass_through)

        batch_put_vendor = cls(
            vendor_ref=vendor_ref,
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            email_address=email_address,
            phone=phone,
            website=website,
            is_person=is_person,
            vendor_name=vendor_name,
            contact_name=contact_name,
            parent_ref=parent_ref,
            currency=currency,
            payment_method_ref=payment_method_ref,
            billing_address=billing_address,
            contacts=contacts,
            tax_number=tax_number,
            shipping_address=shipping_address,
            subsidiary_refs=subsidiary_refs,
            pass_through=pass_through,
        )

        batch_put_vendor.additional_properties = d
        return batch_put_vendor

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
