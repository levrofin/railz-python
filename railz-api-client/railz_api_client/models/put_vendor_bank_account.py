from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_base_address import PushBaseAddress
    from ..models.vendor_ref_dto import VendorRefDto


T = TypeVar("T", bound="PutVendorBankAccount")


@_attrs_define
class PutVendorBankAccount:
    """
    Attributes:
        name (Union[Unset, str]):  Example: Business Bank Account.
        type (Union[Unset, str]):  Example: checking.
        account_number (Union[Unset, str]):  Example: 11200.
        routing_number (Union[Unset, str]):  Example: 123456789.
        bank_name (Union[Unset, str]):  Example: TD Bank.
        supports_ach (Union[Unset, bool]):  Example: True.
        supports_wire (Union[Unset, bool]):  Example: True.
        supports_check (Union[Unset, bool]):  Example: True.
        address (Union[Unset, PushBaseAddress]):
        contact_name (Union[Unset, str]):  Example: Jane Smith.
        currency (Union[Unset, str]):  Example: CAD.
        vendor_ref (Union[Unset, VendorRefDto]):
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    supports_ach: Union[Unset, bool] = UNSET
    supports_wire: Union[Unset, bool] = UNSET
    supports_check: Union[Unset, bool] = UNSET
    address: Union[Unset, "PushBaseAddress"] = UNSET
    contact_name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    vendor_ref: Union[Unset, "VendorRefDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type = self.type

        account_number = self.account_number

        routing_number = self.routing_number

        bank_name = self.bank_name

        supports_ach = self.supports_ach

        supports_wire = self.supports_wire

        supports_check = self.supports_check

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        contact_name = self.contact_name

        currency = self.currency

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if supports_ach is not UNSET:
            field_dict["supportsAch"] = supports_ach
        if supports_wire is not UNSET:
            field_dict["supportsWire"] = supports_wire
        if supports_check is not UNSET:
            field_dict["supportsCheck"] = supports_check
        if address is not UNSET:
            field_dict["address"] = address
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_base_address import PushBaseAddress
        from ..models.vendor_ref_dto import VendorRefDto

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        bank_name = d.pop("bankName", UNSET)

        supports_ach = d.pop("supportsAch", UNSET)

        supports_wire = d.pop("supportsWire", UNSET)

        supports_check = d.pop("supportsCheck", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, PushBaseAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = PushBaseAddress.from_dict(_address)

        contact_name = d.pop("contactName", UNSET)

        currency = d.pop("currency", UNSET)

        _vendor_ref = d.pop("vendorRef", UNSET)
        vendor_ref: Union[Unset, VendorRefDto]
        if isinstance(_vendor_ref, Unset):
            vendor_ref = UNSET
        else:
            vendor_ref = VendorRefDto.from_dict(_vendor_ref)

        put_vendor_bank_account = cls(
            name=name,
            type=type,
            account_number=account_number,
            routing_number=routing_number,
            bank_name=bank_name,
            supports_ach=supports_ach,
            supports_wire=supports_wire,
            supports_check=supports_check,
            address=address,
            contact_name=contact_name,
            currency=currency,
            vendor_ref=vendor_ref,
        )

        put_vendor_bank_account.additional_properties = d
        return put_vendor_bank_account

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
