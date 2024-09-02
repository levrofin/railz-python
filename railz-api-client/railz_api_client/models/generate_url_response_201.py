from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GenerateUrlResponse201")


@_attrs_define
class GenerateUrlResponse201:
    """
    Attributes:
        url (str):  Example: https://sites.railz.ai/ux34ass113333.
        expiry_date (str):  Example: 2021-08-09 23:50:00.
    """

    url: str
    expiry_date: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        expiry_date = self.expiry_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "expiryDate": expiry_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        expiry_date = d.pop("expiryDate")

        generate_url_response_201 = cls(
            url=url,
            expiry_date=expiry_date,
        )

        generate_url_response_201.additional_properties = d
        return generate_url_response_201

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
