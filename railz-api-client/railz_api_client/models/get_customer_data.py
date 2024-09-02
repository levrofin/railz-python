from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_customer_data_status import GetCustomerDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.contact import Contact
    from ..models.currency_ref import CurrencyRef
    from ..models.parent_ref import ParentRef
    from ..models.subsidiary_ref import SubsidiaryRef


T = TypeVar("T", bound="GetCustomerData")


@_attrs_define
class GetCustomerData:
    """
    Attributes:
        id (str):  Example: 1.
        customer_name (str):  Example: ACME Inc..
        status (GetCustomerDataStatus):
        contact_name (Union[Unset, str]):  Example: Jane Smith.
        email_address (Union[Unset, str]):  Example: email@acme.com.
        website (Union[Unset, str]):  Example: www.acme.com.
        phone (Union[Unset, str]):  Example: 8889990000.
        tax_number (Union[Unset, str]):  Example: 987654321.
        balance (Union[Unset, float]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        source_modified_date (Union[Unset, str]):  Example: 2021-03-09T08:49:36.035Z.
        parent_ref (Union[Unset, ParentRef]):
        contacts (Union[Unset, List['Contact']]):
        default_currency (Union[Unset, CurrencyRef]):
        addresses (Union[Unset, List['Address']]):
    """

    id: str
    customer_name: str
    status: GetCustomerDataStatus
    contact_name: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    tax_number: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    source_modified_date: Union[Unset, str] = UNSET
    parent_ref: Union[Unset, "ParentRef"] = UNSET
    contacts: Union[Unset, List["Contact"]] = UNSET
    default_currency: Union[Unset, "CurrencyRef"] = UNSET
    addresses: Union[Unset, List["Address"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        customer_name = self.customer_name

        status = self.status

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

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        default_currency: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_currency, Unset):
            default_currency = self.default_currency.to_dict()

        addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "customerName": customer_name,
                "status": status,
            }
        )
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
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.contact import Contact
        from ..models.currency_ref import CurrencyRef
        from ..models.parent_ref import ParentRef
        from ..models.subsidiary_ref import SubsidiaryRef

        d = src_dict.copy()
        id = d.pop("id")

        customer_name = d.pop("customerName")

        status = d.pop("status")

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

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = Contact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        _default_currency = d.pop("defaultCurrency", UNSET)
        default_currency: Union[Unset, CurrencyRef]
        if isinstance(_default_currency, Unset):
            default_currency = UNSET
        else:
            default_currency = CurrencyRef.from_dict(_default_currency)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = Address.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        get_customer_data = cls(
            id=id,
            customer_name=customer_name,
            status=status,
            contact_name=contact_name,
            email_address=email_address,
            website=website,
            phone=phone,
            tax_number=tax_number,
            balance=balance,
            subsidiary_refs=subsidiary_refs,
            source_modified_date=source_modified_date,
            parent_ref=parent_ref,
            contacts=contacts,
            default_currency=default_currency,
            addresses=addresses,
        )

        get_customer_data.additional_properties = d
        return get_customer_data

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
