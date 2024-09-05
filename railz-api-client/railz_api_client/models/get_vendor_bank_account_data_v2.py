from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_vendor_bank_account_data_v2_type import (
    GetVendorBankAccountDataV2Type,
    check_get_vendor_bank_account_data_v2_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_address import BaseAddress
    from ..models.vendor_ref import VendorRef


T = TypeVar("T", bound="GetVendorBankAccountDataV2")


@_attrs_define
class GetVendorBankAccountDataV2:
    """
    Attributes:
        id (str):  Example: lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDje.
        name (Union[Unset, str]):  Example: Business Bank Account.
        type (Union[Unset, GetVendorBankAccountDataV2Type]):  Example: checking.
        account_number (Union[Unset, str]):  Example: 11200.
        routing_number (Union[Unset, str]):  Example: 123456789.
        bank_name (Union[Unset, str]):  Example: TD Bank.
        supports_ach (Union[Unset, bool]):  Example: True.
        supports_wire (Union[Unset, bool]):  Example: True.
        supports_check (Union[Unset, bool]):  Example: True.
        address (Union[Unset, BaseAddress]):
        contact_name (Union[Unset, str]):
        vendor_ref (Union[Unset, VendorRef]):
        currency (Union[Unset, str]):  Example: USD.
        source_modified_date (Union[Unset, str]):  Example: 2021-03-09T08:49:36.035Z.
    """

    id: str
    name: Union[Unset, str] = UNSET
    type: Union[Unset, GetVendorBankAccountDataV2Type] = UNSET
    account_number: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    supports_ach: Union[Unset, bool] = UNSET
    supports_wire: Union[Unset, bool] = UNSET
    supports_check: Union[Unset, bool] = UNSET
    address: Union[Unset, "BaseAddress"] = UNSET
    contact_name: Union[Unset, str] = UNSET
    vendor_ref: Union[Unset, "VendorRef"] = UNSET
    currency: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
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

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

        currency = self.currency

        source_modified_date = self.source_modified_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
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
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_address import BaseAddress
        from ..models.vendor_ref import VendorRef

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GetVendorBankAccountDataV2Type]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_get_vendor_bank_account_data_v2_type(_type)

        account_number = d.pop("accountNumber", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        bank_name = d.pop("bankName", UNSET)

        supports_ach = d.pop("supportsAch", UNSET)

        supports_wire = d.pop("supportsWire", UNSET)

        supports_check = d.pop("supportsCheck", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, BaseAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = BaseAddress.from_dict(_address)

        contact_name = d.pop("contactName", UNSET)

        _vendor_ref = d.pop("vendorRef", UNSET)
        vendor_ref: Union[Unset, VendorRef]
        if isinstance(_vendor_ref, Unset):
            vendor_ref = UNSET
        else:
            vendor_ref = VendorRef.from_dict(_vendor_ref)

        currency = d.pop("currency", UNSET)

        source_modified_date = d.pop("sourceModifiedDate", UNSET)

        get_vendor_bank_account_data_v2 = cls(
            id=id,
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
            vendor_ref=vendor_ref,
            currency=currency,
            source_modified_date=source_modified_date,
        )

        get_vendor_bank_account_data_v2.additional_properties = d
        return get_vendor_bank_account_data_v2

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
