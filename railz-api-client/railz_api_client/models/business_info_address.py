from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessInfoAddress")


@_attrs_define
class BusinessInfoAddress:
    """
    Attributes:
        street_number (Union[Unset, str]):  Example: 5100.
        street_name (Union[Unset, str]):  Example: York Street.
        city (Union[Unset, str]):  Example: Toronto.
        state (Union[Unset, str]):  Example: Ontario.
        country (Union[Unset, str]):  Example: Canada.
        zip_ (Union[Unset, str]):  Example: M5J0B1.
        line1 (Union[Unset, str]):  Example: 1234 Park Street.
        line2 (Union[Unset, str]):  Example: Suite 1000.
        region (Union[Unset, str]):  Example: ON.
        postal_code (Union[Unset, str]):  Example: A0B1C2.
    """

    street_number: Union[Unset, str] = UNSET
    street_name: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    zip_: Union[Unset, str] = UNSET
    line1: Union[Unset, str] = UNSET
    line2: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        street_number = self.street_number

        street_name = self.street_name

        city = self.city

        state = self.state

        country = self.country

        zip_ = self.zip_

        line1 = self.line1

        line2 = self.line2

        region = self.region

        postal_code = self.postal_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
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
        street_number = d.pop("streetNumber", UNSET)

        street_name = d.pop("streetName", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        zip_ = d.pop("zip", UNSET)

        line1 = d.pop("line1", UNSET)

        line2 = d.pop("line2", UNSET)

        region = d.pop("region", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        business_info_address = cls(
            street_number=street_number,
            street_name=street_name,
            city=city,
            state=state,
            country=country,
            zip_=zip_,
            line1=line1,
            line2=line2,
            region=region,
            postal_code=postal_code,
        )

        business_info_address.additional_properties = d
        return business_info_address

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
