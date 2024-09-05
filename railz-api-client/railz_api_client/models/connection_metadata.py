from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_metadata_service_name import (
    ConnectionMetadataServiceName,
    check_connection_metadata_service_name,
)

T = TypeVar("T", bound="ConnectionMetadata")


@_attrs_define
class ConnectionMetadata:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (str):  Example: Railz.
        service_name (ConnectionMetadataServiceName):  Example: xero.
    """

    connection_uuid: str
    business_name: str
    service_name: ConnectionMetadataServiceName
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        business_name = self.business_name

        service_name: str = self.service_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "businessName": business_name,
                "serviceName": service_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName")

        service_name = check_connection_metadata_service_name(d.pop("serviceName"))

        connection_metadata = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
        )

        connection_metadata.additional_properties = d
        return connection_metadata

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
