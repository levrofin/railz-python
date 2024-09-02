import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_sync_response_dto_service_name import DataSyncResponseDtoServiceName

T = TypeVar("T", bound="DataSyncResponseDto")


@_attrs_define
class DataSyncResponseDto:
    """
    Attributes:
        connection_id (str):  Example: CON-94652dff-06ab-4b97-bd1b-f91adf7048c3.
        business_name (str):  Example: Railz.
        service_name (DataSyncResponseDtoServiceName):  Example: quickbooks.
        data_type (str):  Example: balanceSheet.
        requested_on (datetime.datetime):  Example: 2021-03-18T08:16:51.233Z.
    """

    connection_id: str
    business_name: str
    service_name: DataSyncResponseDtoServiceName
    data_type: str
    requested_on: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id

        business_name = self.business_name

        service_name = self.service_name

        data_type = self.data_type

        requested_on = self.requested_on.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionId": connection_id,
                "businessName": business_name,
                "serviceName": service_name,
                "dataType": data_type,
                "requestedOn": requested_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId")

        business_name = d.pop("businessName")

        service_name = d.pop("serviceName")

        data_type = d.pop("dataType")

        requested_on = isoparse(d.pop("requestedOn"))

        data_sync_response_dto = cls(
            connection_id=connection_id,
            business_name=business_name,
            service_name=service_name,
            data_type=data_type,
            requested_on=requested_on,
        )

        data_sync_response_dto.additional_properties = d
        return data_sync_response_dto

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
