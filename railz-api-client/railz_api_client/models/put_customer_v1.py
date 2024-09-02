from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.addresses import Addresses


T = TypeVar("T", bound="PutCustomerV1")


@_attrs_define
class PutCustomerV1:
    """
    Attributes:
        contact_first_name (Union[Unset, str]):  Example: Jane.
        contact_last_name (Union[Unset, str]):  Example: Smith.
        email_address (Union[Unset, str]):  Example: email@acme.com.
        phone (Union[Unset, str]):  Example: 8889990000.
        website (Union[Unset, str]):  Example: www.acme.com.
        is_person (Union[Unset, bool]):
        customer_name (Union[Unset, str]):  Example: ACME Inc..
        addresses (Union[Unset, List['Addresses']]):
        default_currency (Union[Unset, str]):  Example: CAD.
        subsidiary_refs (Union[Unset, List[str]]):  Example: ['1', '3'].
    """

    contact_first_name: Union[Unset, str] = UNSET
    contact_last_name: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    is_person: Union[Unset, bool] = UNSET
    customer_name: Union[Unset, str] = UNSET
    addresses: Union[Unset, List["Addresses"]] = UNSET
    default_currency: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact_first_name = self.contact_first_name

        contact_last_name = self.contact_last_name

        email_address = self.email_address

        phone = self.phone

        website = self.website

        is_person = self.is_person

        customer_name = self.customer_name

        addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        default_currency = self.default_currency

        subsidiary_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = self.subsidiary_refs

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
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.addresses import Addresses

        d = src_dict.copy()
        contact_first_name = d.pop("contactFirstName", UNSET)

        contact_last_name = d.pop("contactLastName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        phone = d.pop("phone", UNSET)

        website = d.pop("website", UNSET)

        is_person = d.pop("isPerson", UNSET)

        customer_name = d.pop("customerName", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = Addresses.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        default_currency = d.pop("defaultCurrency", UNSET)

        subsidiary_refs = cast(List[str], d.pop("subsidiaryRefs", UNSET))

        put_customer_v1 = cls(
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            email_address=email_address,
            phone=phone,
            website=website,
            is_person=is_person,
            customer_name=customer_name,
            addresses=addresses,
            default_currency=default_currency,
            subsidiary_refs=subsidiary_refs,
        )

        put_customer_v1.additional_properties = d
        return put_customer_v1

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
