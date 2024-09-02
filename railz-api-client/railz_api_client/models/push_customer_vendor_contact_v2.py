from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_vendor_push_address_v2 import CustomerVendorPushAddressV2


T = TypeVar("T", bound="PushCustomerVendorContactV2")


@_attrs_define
class PushCustomerVendorContactV2:
    """
    Attributes:
        name (Union[Unset, str]):  Example: John Smith.
        email (Union[Unset, str]):  Example: jsmith@company.com.
        phone (Union[Unset, str]):  Example: 8887779999.
        address (Union[Unset, CustomerVendorPushAddressV2]):
    """

    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    address: Union[Unset, "CustomerVendorPushAddressV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        email = self.email

        phone = self.phone

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_vendor_push_address_v2 import CustomerVendorPushAddressV2

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, CustomerVendorPushAddressV2]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = CustomerVendorPushAddressV2.from_dict(_address)

        push_customer_vendor_contact_v2 = cls(
            name=name,
            email=email,
            phone=phone,
            address=address,
        )

        push_customer_vendor_contact_v2.additional_properties = d
        return push_customer_vendor_contact_v2

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
