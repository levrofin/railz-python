from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_vendor_push_address_v2_type import CustomerVendorPushAddressV2Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerVendorPushAddressV2")


@_attrs_define
class CustomerVendorPushAddressV2:
    """
    Attributes:
        line1 (Union[Unset, str]):  Example: 1234 Park Street.
        line2 (Union[Unset, str]):  Example: Suite 1000.
        city (Union[Unset, str]):  Example: Toronto.
        region (Union[Unset, str]):  Example: ON.
        country (Union[Unset, str]):  Example: CAN.
        postal_code (Union[Unset, str]):  Example: A0B1C2.
        type (Union[Unset, CustomerVendorPushAddressV2Type]):  Example: billing.
    """

    line1: Union[Unset, str] = UNSET
    line2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    type: Union[Unset, CustomerVendorPushAddressV2Type] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line1 = self.line1

        line2 = self.line2

        city = self.city

        region = self.region

        country = self.country

        postal_code = self.postal_code

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line1 is not UNSET:
            field_dict["line1"] = line1
        if line2 is not UNSET:
            field_dict["line2"] = line2
        if city is not UNSET:
            field_dict["city"] = city
        if region is not UNSET:
            field_dict["region"] = region
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line1 = d.pop("line1", UNSET)

        line2 = d.pop("line2", UNSET)

        city = d.pop("city", UNSET)

        region = d.pop("region", UNSET)

        country = d.pop("country", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CustomerVendorPushAddressV2Type]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = _type

        customer_vendor_push_address_v2 = cls(
            line1=line1,
            line2=line2,
            city=city,
            region=region,
            country=country,
            postal_code=postal_code,
            type=type,
        )

        customer_vendor_push_address_v2.additional_properties = d
        return customer_vendor_push_address_v2

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
