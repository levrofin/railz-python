from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessInfoAddressV2")


@_attrs_define
class BusinessInfoAddressV2:
    """
    Attributes:
        city (Union[Unset, str]):  Example: Toronto.
        country (Union[Unset, str]):  Example: Canada.
        line1 (Union[Unset, str]):  Example: 1234 Park Street.
        line2 (Union[Unset, str]):  Example: Suite 1000.
        region (Union[Unset, str]):  Example: ON.
        postal_code (Union[Unset, str]):  Example: A0B1C2.
    """

    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    line1: Union[Unset, str] = UNSET
    line2: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city

        country = self.country

        line1 = self.line1

        line2 = self.line2

        region = self.region

        postal_code = self.postal_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if line1 is not UNSET:
            field_dict["line1"] = line1
        if line2 is not UNSET:
            field_dict["line2"] = line2
        if region is not UNSET:
            field_dict["region"] = region
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        line1 = d.pop("line1", UNSET)

        line2 = d.pop("line2", UNSET)

        region = d.pop("region", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        business_info_address_v2 = cls(
            city=city,
            country=country,
            line1=line1,
            line2=line2,
            region=region,
            postal_code=postal_code,
        )

        business_info_address_v2.additional_properties = d
        return business_info_address_v2

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
