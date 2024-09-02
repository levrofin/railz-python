import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_sync_response_v2_dto_service_name import DataSyncResponseV2DtoServiceName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSyncResponseV2Dto")


@_attrs_define
class DataSyncResponseV2Dto:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (str):  Example: Railz.
        service_name (DataSyncResponseV2DtoServiceName):  Example: xero.
        requested_on (datetime.datetime):  Example: 2021-03-18T08:16:51.233Z.
        request_id (str):  Example: 94652dff-06ab-4b97-bd1b-f91adf7048c3.
        data_type (Union[Unset, str]):  Example: balanceSheet.
        data_types (Union[Unset, List[str]]):  Example: ['balanceSheet'].
    """

    connection_uuid: str
    business_name: str
    service_name: DataSyncResponseV2DtoServiceName
    requested_on: datetime.datetime
    request_id: str
    data_type: Union[Unset, str] = UNSET
    data_types: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        business_name = self.business_name

        service_name = self.service_name

        requested_on = self.requested_on.isoformat()

        request_id = self.request_id

        data_type = self.data_type

        data_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_types, Unset):
            data_types = self.data_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "businessName": business_name,
                "serviceName": service_name,
                "requestedOn": requested_on,
                "requestId": request_id,
            }
        )
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if data_types is not UNSET:
            field_dict["dataTypes"] = data_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName")

        service_name = d.pop("serviceName")

        requested_on = isoparse(d.pop("requestedOn"))

        request_id = d.pop("requestId")

        data_type = d.pop("dataType", UNSET)

        data_types = cast(List[str], d.pop("dataTypes", UNSET))

        data_sync_response_v2_dto = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
            requested_on=requested_on,
            request_id=request_id,
            data_type=data_type,
            data_types=data_types,
        )

        data_sync_response_v2_dto.additional_properties = d
        return data_sync_response_v2_dto

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
