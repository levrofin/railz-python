import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.disconnect_response_dto_service_name import (
    DisconnectResponseDtoServiceName,
    check_disconnect_response_dto_service_name,
)

T = TypeVar("T", bound="DisconnectResponseDto")


@_attrs_define
class DisconnectResponseDto:
    """
    Attributes:
        connection_id (str):  Example: CON-e66400c1-4d2f-4683-9bea-275799943695.
        business_name (str):  Example: Railz.
        service_name (DisconnectResponseDtoServiceName):  Example: xero.
        status (str):  Example: disconnected.
        created_at (datetime.datetime):  Example: 2020-12-25T01:02:03Z.
        updated_at (datetime.datetime):  Example: 2020-12-25T01:02:03Z.
    """

    connection_id: str
    business_name: str
    service_name: DisconnectResponseDtoServiceName
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id

        business_name = self.business_name

        service_name: str = self.service_name

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionId": connection_id,
                "businessName": business_name,
                "serviceName": service_name,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId")

        business_name = d.pop("businessName")

        service_name = check_disconnect_response_dto_service_name(d.pop("serviceName"))

        status = d.pop("status")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        disconnect_response_dto = cls(
            connection_id=connection_id,
            business_name=business_name,
            service_name=service_name,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        disconnect_response_dto.additional_properties = d
        return disconnect_response_dto

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
