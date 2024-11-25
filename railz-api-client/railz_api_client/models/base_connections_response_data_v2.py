import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.base_connections_response_data_v2_service_name import (
    BaseConnectionsResponseDataV2ServiceName,
    check_base_connections_response_data_v2_service_name,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connections_institution_data import ConnectionsInstitutionData
    from ..models.service_account_ref_type import ServiceAccountRefType


T = TypeVar("T", bound="BaseConnectionsResponseDataV2")


@_attrs_define
class BaseConnectionsResponseDataV2:
    """
    Attributes:
        connection_uuid (Union[Unset, str]):  Example: CON-e66400c1-4d2f-4683-9bea-275799943695.
        first_record_date (Union[Unset, datetime.datetime]):  Example: 2020-12-25T01:02:03Z.
        service_name (Union[Unset, BaseConnectionsResponseDataV2ServiceName]):  Example: xero.
        description (Union[Unset, str]):  Example: TD Bank.
        status (Union[Unset, str]):  Example: active.
        created_at (Union[Unset, datetime.datetime]):  Example: 2020-12-25T01:02:03Z.
        updated_at (Union[Unset, datetime.datetime]):  Example: 2020-12-25T01:02:03Z.
        disconnect_reason (Union[Unset, str]):  Example: disconnectedByCustomer.
        sync_time (Union[Unset, float]):  Example: 1.3092.
        institution (Union[Unset, ConnectionsInstitutionData]):
        is_mock_data (Union[Unset, bool]):  Example: True.
        service_account_ref (Union[Unset, ServiceAccountRefType]):
    """

    connection_uuid: Union[Unset, str] = UNSET
    first_record_date: Union[Unset, datetime.datetime] = UNSET
    service_name: Union[Unset, BaseConnectionsResponseDataV2ServiceName] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    disconnect_reason: Union[Unset, str] = UNSET
    sync_time: Union[Unset, float] = UNSET
    institution: Union[Unset, "ConnectionsInstitutionData"] = UNSET
    is_mock_data: Union[Unset, bool] = UNSET
    service_account_ref: Union[Unset, "ServiceAccountRefType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        first_record_date: Union[Unset, str] = UNSET
        if not isinstance(self.first_record_date, Unset):
            first_record_date = self.first_record_date.isoformat()

        service_name: Union[Unset, str] = UNSET
        if not isinstance(self.service_name, Unset):
            service_name = self.service_name

        description = self.description

        status = self.status

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        disconnect_reason = self.disconnect_reason

        sync_time = self.sync_time

        institution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.institution, Unset):
            institution = self.institution.to_dict()

        is_mock_data = self.is_mock_data

        service_account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_account_ref, Unset):
            service_account_ref = self.service_account_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_uuid is not UNSET:
            field_dict["connectionUuid"] = connection_uuid
        if first_record_date is not UNSET:
            field_dict["firstRecordDate"] = first_record_date
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if disconnect_reason is not UNSET:
            field_dict["disconnectReason"] = disconnect_reason
        if sync_time is not UNSET:
            field_dict["syncTime"] = sync_time
        if institution is not UNSET:
            field_dict["institution"] = institution
        if is_mock_data is not UNSET:
            field_dict["isMockData"] = is_mock_data
        if service_account_ref is not UNSET:
            field_dict["serviceAccountRef"] = service_account_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.connections_institution_data import ConnectionsInstitutionData
        from ..models.service_account_ref_type import ServiceAccountRefType

        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid", UNSET)

        _first_record_date = d.pop("firstRecordDate", UNSET)
        first_record_date: Union[Unset, datetime.datetime]
        if isinstance(_first_record_date, Unset):
            first_record_date = UNSET
        else:
            first_record_date = isoparse(_first_record_date)

        _service_name = d.pop("serviceName", UNSET)
        service_name: Union[Unset, BaseConnectionsResponseDataV2ServiceName]
        if isinstance(_service_name, Unset):
            service_name = UNSET
        else:
            service_name = check_base_connections_response_data_v2_service_name(_service_name)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        disconnect_reason = d.pop("disconnectReason", UNSET)

        sync_time = d.pop("syncTime", UNSET)

        _institution = d.pop("institution", UNSET)
        institution: Union[Unset, ConnectionsInstitutionData]
        if isinstance(_institution, Unset):
            institution = UNSET
        else:
            institution = ConnectionsInstitutionData.from_dict(_institution)

        is_mock_data = d.pop("isMockData", UNSET)

        _service_account_ref = d.pop("serviceAccountRef", UNSET)
        service_account_ref: Union[Unset, ServiceAccountRefType]
        if isinstance(_service_account_ref, Unset):
            service_account_ref = UNSET
        else:
            service_account_ref = ServiceAccountRefType.from_dict(_service_account_ref)

        base_connections_response_data_v2 = cls(
            connection_uuid=connection_uuid,
            first_record_date=first_record_date,
            service_name=service_name,
            description=description,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            disconnect_reason=disconnect_reason,
            sync_time=sync_time,
            institution=institution,
            is_mock_data=is_mock_data,
            service_account_ref=service_account_ref,
        )

        base_connections_response_data_v2.additional_properties = d
        return base_connections_response_data_v2

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
