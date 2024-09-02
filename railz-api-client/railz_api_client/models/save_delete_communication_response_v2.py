import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.save_delete_communication_response_v2_service_name import SaveDeleteCommunicationResponseV2ServiceName
from ..models.save_delete_communication_response_v2_status import SaveDeleteCommunicationResponseV2Status

T = TypeVar("T", bound="SaveDeleteCommunicationResponseV2")


@_attrs_define
class SaveDeleteCommunicationResponseV2:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (str):  Example: Railz.
        service_name (SaveDeleteCommunicationResponseV2ServiceName):  Example: xero.
        delete_communication_id (str):  Example: 645102bca1b57c57cc241173.
        requested_on (datetime.datetime):  Example: 2022-06-24T09:40:11.088Z.
        status (SaveDeleteCommunicationResponseV2Status):  Example: pending.
    """

    connection_uuid: str
    business_name: str
    service_name: SaveDeleteCommunicationResponseV2ServiceName
    delete_communication_id: str
    requested_on: datetime.datetime
    status: SaveDeleteCommunicationResponseV2Status
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        business_name = self.business_name

        service_name = self.service_name

        delete_communication_id = self.delete_communication_id

        requested_on = self.requested_on.isoformat()

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "businessName": business_name,
                "serviceName": service_name,
                "deleteCommunicationId": delete_communication_id,
                "requestedOn": requested_on,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName")

        service_name = d.pop("serviceName")

        delete_communication_id = d.pop("deleteCommunicationId")

        requested_on = isoparse(d.pop("requestedOn"))

        status = d.pop("status")

        save_delete_communication_response_v2 = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
            delete_communication_id=delete_communication_id,
            requested_on=requested_on,
            status=status,
        )

        save_delete_communication_response_v2.additional_properties = d
        return save_delete_communication_response_v2

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
