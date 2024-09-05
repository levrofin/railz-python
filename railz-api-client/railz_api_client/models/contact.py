from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_status import ContactStatus, check_contact_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        status (ContactStatus):
        name (Union[Unset, str]):  Example: John Smith.
        email (Union[Unset, str]):  Example: jsmith@company.com.
        phone (Union[Unset, str]):  Example: 8887779999.
        address (Union[Unset, Address]):
        modified_date (Union[Unset, str]):  Example: 2021-03-09T08:49:36.035Z.
    """

    status: ContactStatus
    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    address: Union[Unset, "Address"] = UNSET
    modified_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: str = self.status

        name = self.name

        email = self.email

        phone = self.phone

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        modified_date = self.modified_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if address is not UNSET:
            field_dict["address"] = address
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        status = check_contact_status(d.pop("status"))

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        modified_date = d.pop("modifiedDate", UNSET)

        contact = cls(
            status=status,
            name=name,
            email=email,
            phone=phone,
            address=address,
            modified_date=modified_date,
        )

        contact.additional_properties = d
        return contact

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
