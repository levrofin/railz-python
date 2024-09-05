from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_contact_data_contact_type import GetContactDataContactType, check_get_contact_data_contact_type
from ..models.get_contact_data_status import GetContactDataStatus, check_get_contact_data_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_account_ref import BankAccountRef
    from ..models.billing_address import BillingAddress
    from ..models.contact_person import ContactPerson
    from ..models.shipping_address import ShippingAddress


T = TypeVar("T", bound="GetContactData")


@_attrs_define
class GetContactData:
    """
    Attributes:
        id (str):  Example: 1.
        contact_name (Union[Unset, str]):  Example: Jane Smith.
        contact_first_name (Union[Unset, str]):  Example: Jane.
        contact_last_name (Union[Unset, str]):  Example: Smith.
        email_address (Union[Unset, str]):  Example: email@acme.com.
        bank_account_ref (Union[Unset, BankAccountRef]):
        website (Union[Unset, str]):  Example: www.acme.com.
        currency (Union[Unset, str]):  Example: USD.
        phone (Union[Unset, str]):  Example: 8889990000.
        billing_address (Union[Unset, BillingAddress]):
        shipping_address (Union[Unset, ShippingAddress]):
        contacts (Union[Unset, List['ContactPerson']]):
        tax_number (Union[Unset, str]):  Example: 987654321.
        status (Union[Unset, GetContactDataStatus]):
        balance (Union[Unset, float]):
        contact_type (Union[Unset, GetContactDataContactType]):  Example: customer.
        source_modified_date (Union[Unset, str]):  Example: 2021-03-09T08:49:36.035Z.
    """

    id: str
    contact_name: Union[Unset, str] = UNSET
    contact_first_name: Union[Unset, str] = UNSET
    contact_last_name: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    bank_account_ref: Union[Unset, "BankAccountRef"] = UNSET
    website: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    billing_address: Union[Unset, "BillingAddress"] = UNSET
    shipping_address: Union[Unset, "ShippingAddress"] = UNSET
    contacts: Union[Unset, List["ContactPerson"]] = UNSET
    tax_number: Union[Unset, str] = UNSET
    status: Union[Unset, GetContactDataStatus] = UNSET
    balance: Union[Unset, float] = UNSET
    contact_type: Union[Unset, GetContactDataContactType] = UNSET
    source_modified_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        contact_name = self.contact_name

        contact_first_name = self.contact_first_name

        contact_last_name = self.contact_last_name

        email_address = self.email_address

        bank_account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bank_account_ref, Unset):
            bank_account_ref = self.bank_account_ref.to_dict()

        website = self.website

        currency = self.currency

        phone = self.phone

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

        tax_number = self.tax_number

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        balance = self.balance

        contact_type: Union[Unset, str] = UNSET
        if not isinstance(self.contact_type, Unset):
            contact_type = self.contact_type

        source_modified_date = self.source_modified_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if contact_first_name is not UNSET:
            field_dict["contactFirstName"] = contact_first_name
        if contact_last_name is not UNSET:
            field_dict["contactLastName"] = contact_last_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if bank_account_ref is not UNSET:
            field_dict["bankAccountRef"] = bank_account_ref
        if website is not UNSET:
            field_dict["website"] = website
        if currency is not UNSET:
            field_dict["currency"] = currency
        if phone is not UNSET:
            field_dict["phone"] = phone
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if tax_number is not UNSET:
            field_dict["taxNumber"] = tax_number
        if status is not UNSET:
            field_dict["status"] = status
        if balance is not UNSET:
            field_dict["balance"] = balance
        if contact_type is not UNSET:
            field_dict["contactType"] = contact_type
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_account_ref import BankAccountRef
        from ..models.billing_address import BillingAddress
        from ..models.contact_person import ContactPerson
        from ..models.shipping_address import ShippingAddress

        d = src_dict.copy()
        id = d.pop("id")

        contact_name = d.pop("contactName", UNSET)

        contact_first_name = d.pop("contactFirstName", UNSET)

        contact_last_name = d.pop("contactLastName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        _bank_account_ref = d.pop("bankAccountRef", UNSET)
        bank_account_ref: Union[Unset, BankAccountRef]
        if isinstance(_bank_account_ref, Unset):
            bank_account_ref = UNSET
        else:
            bank_account_ref = BankAccountRef.from_dict(_bank_account_ref)

        website = d.pop("website", UNSET)

        currency = d.pop("currency", UNSET)

        phone = d.pop("phone", UNSET)

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
            contacts_item = ContactPerson.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        tax_number = d.pop("taxNumber", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, GetContactDataStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_get_contact_data_status(_status)

        balance = d.pop("balance", UNSET)

        _contact_type = d.pop("contactType", UNSET)
        contact_type: Union[Unset, GetContactDataContactType]
        if isinstance(_contact_type, Unset):
            contact_type = UNSET
        else:
            contact_type = check_get_contact_data_contact_type(_contact_type)

        source_modified_date = d.pop("sourceModifiedDate", UNSET)

        get_contact_data = cls(
            id=id,
            contact_name=contact_name,
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            email_address=email_address,
            bank_account_ref=bank_account_ref,
            website=website,
            currency=currency,
            phone=phone,
            billing_address=billing_address,
            shipping_address=shipping_address,
            contacts=contacts,
            tax_number=tax_number,
            status=status,
            balance=balance,
            contact_type=contact_type,
            source_modified_date=source_modified_date,
        )

        get_contact_data.additional_properties = d
        return get_contact_data

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
