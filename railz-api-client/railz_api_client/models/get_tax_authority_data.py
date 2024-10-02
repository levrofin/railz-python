import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTaxAuthorityData")


@_attrs_define
class GetTaxAuthorityData:
    """
    Attributes:
        id (str):  Example: 1.
        name (str):  Example: Dept. of Revenue.
        memo (Union[Unset, str]):
        registration_number (Union[Unset, str]):  Example: 460000000066001.
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-10T11:26:06.619Z.
    """

    id: str
    name: str
    memo: Union[Unset, str] = UNSET
    registration_number: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        memo = self.memo

        registration_number = self.registration_number

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if memo is not UNSET:
            field_dict["memo"] = memo
        if registration_number is not UNSET:
            field_dict["registrationNumber"] = registration_number
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        memo = d.pop("memo", UNSET)

        registration_number = d.pop("registrationNumber", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_tax_authority_data = cls(
            id=id,
            name=name,
            memo=memo,
            registration_number=registration_number,
            source_modified_date=source_modified_date,
        )

        get_tax_authority_data.additional_properties = d
        return get_tax_authority_data

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
