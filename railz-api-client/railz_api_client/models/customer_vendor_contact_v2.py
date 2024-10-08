from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_vendor_contact_v2_status import (
    CustomerVendorContactV2Status,
    check_customer_vendor_contact_v2_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_vendor_address import CustomerVendorAddress


T = TypeVar("T", bound="CustomerVendorContactV2")


@_attrs_define
class CustomerVendorContactV2:
    """
    Attributes:
        name (Union[Unset, str]):  Example: John Smith.
        email (Union[Unset, str]):  Example: jsmith@company.com.
        phone (Union[Unset, str]):  Example: 8887779999.
        address (Union[Unset, CustomerVendorAddress]):
        status (Union[Unset, CustomerVendorContactV2Status]):
    """

    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    address: Union[Unset, "CustomerVendorAddress"] = UNSET
    status: Union[Unset, CustomerVendorContactV2Status] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        email = self.email

        phone = self.phone

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

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
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_vendor_address import CustomerVendorAddress

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, CustomerVendorAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = CustomerVendorAddress.from_dict(_address)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CustomerVendorContactV2Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_customer_vendor_contact_v2_status(_status)

        customer_vendor_contact_v2 = cls(
            name=name,
            email=email,
            phone=phone,
            address=address,
            status=status,
        )

        customer_vendor_contact_v2.additional_properties = d
        return customer_vendor_contact_v2

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
