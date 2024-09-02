from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_address_dto import BillingAddressDto
    from ..models.parent_ref_dto import ParentRefDto
    from ..models.payment_method_ref_dto import PaymentMethodRefDto
    from ..models.push_customer_vendor_contact_v2 import PushCustomerVendorContactV2
    from ..models.put_customer_v2_pass_through import PutCustomerV2PassThrough
    from ..models.shipping_address_dto import ShippingAddressDto
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto


T = TypeVar("T", bound="PutCustomerV2")


@_attrs_define
class PutCustomerV2:
    """
    Attributes:
        contact_first_name (Union[Unset, str]):  Example: Jane.
        contact_last_name (Union[Unset, str]):  Example: Smith.
        email_address (Union[Unset, str]):  Example: email@acme.com.
        phone (Union[Unset, str]):  Example: 8889990000.
        website (Union[Unset, str]):  Example: www.acme.com.
        is_person (Union[Unset, bool]):
        customer_name (Union[Unset, str]):  Example: ACME Inc..
        contact_name (Union[Unset, str]):  Example: Jane Smith.
        tax_number (Union[Unset, str]):  Example: 987654321.
        parent_ref (Union[Unset, ParentRefDto]):
        billing_address (Union[Unset, BillingAddressDto]):
        currency (Union[Unset, str]):  Example: CAD.
        shipping_address (Union[Unset, ShippingAddressDto]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        contacts (Union[Unset, List['PushCustomerVendorContactV2']]):
        pass_through (Union[Unset, PutCustomerV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        payment_method_ref (Union[Unset, PaymentMethodRefDto]):
    """

    contact_first_name: Union[Unset, str] = UNSET
    contact_last_name: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    is_person: Union[Unset, bool] = UNSET
    customer_name: Union[Unset, str] = UNSET
    contact_name: Union[Unset, str] = UNSET
    tax_number: Union[Unset, str] = UNSET
    parent_ref: Union[Unset, "ParentRefDto"] = UNSET
    billing_address: Union[Unset, "BillingAddressDto"] = UNSET
    currency: Union[Unset, str] = UNSET
    shipping_address: Union[Unset, "ShippingAddressDto"] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    contacts: Union[Unset, List["PushCustomerVendorContactV2"]] = UNSET
    pass_through: Union[Unset, "PutCustomerV2PassThrough"] = UNSET
    payment_method_ref: Union[Unset, "PaymentMethodRefDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact_first_name = self.contact_first_name

        contact_last_name = self.contact_last_name

        email_address = self.email_address

        phone = self.phone

        website = self.website

        is_person = self.is_person

        customer_name = self.customer_name

        contact_name = self.contact_name

        tax_number = self.tax_number

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        currency = self.currency

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if tax_number is not UNSET:
            field_dict["taxNumber"] = tax_number
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if currency is not UNSET:
            field_dict["currency"] = currency
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.billing_address_dto import BillingAddressDto
        from ..models.parent_ref_dto import ParentRefDto
        from ..models.payment_method_ref_dto import PaymentMethodRefDto
        from ..models.push_customer_vendor_contact_v2 import PushCustomerVendorContactV2
        from ..models.put_customer_v2_pass_through import PutCustomerV2PassThrough
        from ..models.shipping_address_dto import ShippingAddressDto
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto

        d = src_dict.copy()
        contact_first_name = d.pop("contactFirstName", UNSET)

        contact_last_name = d.pop("contactLastName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        phone = d.pop("phone", UNSET)

        website = d.pop("website", UNSET)

        is_person = d.pop("isPerson", UNSET)

        customer_name = d.pop("customerName", UNSET)

        contact_name = d.pop("contactName", UNSET)

        tax_number = d.pop("taxNumber", UNSET)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, ParentRefDto]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = ParentRefDto.from_dict(_parent_ref)

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, BillingAddressDto]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = BillingAddressDto.from_dict(_billing_address)

        currency = d.pop("currency", UNSET)

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

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = PushCustomerVendorContactV2.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PutCustomerV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PutCustomerV2PassThrough.from_dict(_pass_through)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentMethodRefDto]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentMethodRefDto.from_dict(_payment_method_ref)

        put_customer_v2 = cls(
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            email_address=email_address,
            phone=phone,
            website=website,
            is_person=is_person,
            customer_name=customer_name,
            contact_name=contact_name,
            tax_number=tax_number,
            parent_ref=parent_ref,
            billing_address=billing_address,
            currency=currency,
            shipping_address=shipping_address,
            subsidiary_refs=subsidiary_refs,
            contacts=contacts,
            pass_through=pass_through,
            payment_method_ref=payment_method_ref,
        )

        put_customer_v2.additional_properties = d
        return put_customer_v2

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
