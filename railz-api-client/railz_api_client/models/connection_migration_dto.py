from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_migration_dto_location import ConnectionMigrationDtoLocation
from ..models.connection_migration_dto_service_name import ConnectionMigrationDtoServiceName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionMigrationDto")


@_attrs_define
class ConnectionMigrationDto:
    """
    Attributes:
        service_name (ConnectionMigrationDtoServiceName):
        access_token (Union[Unset, str]):
        refresh_token (Union[Unset, str]):
        account_id (Union[Unset, str]):
        location (Union[Unset, ConnectionMigrationDtoLocation]):
    """

    service_name: ConnectionMigrationDtoServiceName
    access_token: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    location: Union[Unset, ConnectionMigrationDtoLocation] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_name = self.service_name

        access_token = self.access_token

        refresh_token = self.refresh_token

        account_id = self.account_id

        location: Union[Unset, str] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceName": service_name,
            }
        )
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if refresh_token is not UNSET:
            field_dict["refreshToken"] = refresh_token
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_name = d.pop("serviceName")

        access_token = d.pop("accessToken", UNSET)

        refresh_token = d.pop("refreshToken", UNSET)

        account_id = d.pop("accountId", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, ConnectionMigrationDtoLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = _location

        connection_migration_dto = cls(
            service_name=service_name,
            access_token=access_token,
            refresh_token=refresh_token,
            account_id=account_id,
            location=location,
        )

        connection_migration_dto.additional_properties = d
        return connection_migration_dto

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
