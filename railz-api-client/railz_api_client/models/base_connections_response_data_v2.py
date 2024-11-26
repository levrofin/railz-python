import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        connection_uuid (Union[None, Unset, str]):  Example: CON-e66400c1-4d2f-4683-9bea-275799943695.
        first_record_date (Union[None, Unset, datetime.datetime]):  Example: 2020-12-25T01:02:03Z.
        service_name (Union[Unset, BaseConnectionsResponseDataV2ServiceName]):  Example: xero.
        description (Union[None, Unset, str]):  Example: TD Bank.
        status (Union[None, Unset, str]):  Example: active.
        created_at (Union[None, Unset, datetime.datetime]):  Example: 2020-12-25T01:02:03Z.
        updated_at (Union[None, Unset, datetime.datetime]):  Example: 2020-12-25T01:02:03Z.
        disconnect_reason (Union[None, Unset, str]):  Example: disconnectedByCustomer.
        sync_time (Union[None, Unset, float]):  Example: 1.3092.
        institution (Union['ConnectionsInstitutionData', None, Unset]):  Example: {'name': 'Citizens bank', 'logo':
            'https://serverlogo.url'}.
        is_mock_data (Union[None, Unset, bool]):  Example: True.
        service_account_ref (Union['ServiceAccountRefType', None, Unset]):  Example: {'id': '12345', 'entityRef': {'id':
            '100'}}.
    """

    connection_uuid: Union[None, Unset, str] = UNSET
    first_record_date: Union[None, Unset, datetime.datetime] = UNSET
    service_name: Union[Unset, BaseConnectionsResponseDataV2ServiceName] = UNSET
    description: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    disconnect_reason: Union[None, Unset, str] = UNSET
    sync_time: Union[None, Unset, float] = UNSET
    institution: Union["ConnectionsInstitutionData", None, Unset] = UNSET
    is_mock_data: Union[None, Unset, bool] = UNSET
    service_account_ref: Union["ServiceAccountRefType", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.connections_institution_data import ConnectionsInstitutionData
        from ..models.service_account_ref_type import ServiceAccountRefType

        connection_uuid: Union[None, Unset, str]
        if isinstance(self.connection_uuid, Unset):
            connection_uuid = UNSET
        else:
            connection_uuid = self.connection_uuid

        first_record_date: Union[None, Unset, str]
        if isinstance(self.first_record_date, Unset):
            first_record_date = UNSET
        elif isinstance(self.first_record_date, datetime.datetime):
            first_record_date = self.first_record_date.isoformat()
        else:
            first_record_date = self.first_record_date

        service_name: Union[Unset, str] = UNSET
        if not isinstance(self.service_name, Unset):
            service_name = self.service_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        disconnect_reason: Union[None, Unset, str]
        if isinstance(self.disconnect_reason, Unset):
            disconnect_reason = UNSET
        else:
            disconnect_reason = self.disconnect_reason

        sync_time: Union[None, Unset, float]
        if isinstance(self.sync_time, Unset):
            sync_time = UNSET
        else:
            sync_time = self.sync_time

        institution: Union[Dict[str, Any], None, Unset]
        if isinstance(self.institution, Unset):
            institution = UNSET
        elif isinstance(self.institution, ConnectionsInstitutionData):
            institution = self.institution.to_dict()
        else:
            institution = self.institution

        is_mock_data: Union[None, Unset, bool]
        if isinstance(self.is_mock_data, Unset):
            is_mock_data = UNSET
        else:
            is_mock_data = self.is_mock_data

        service_account_ref: Union[Dict[str, Any], None, Unset]
        if isinstance(self.service_account_ref, Unset):
            service_account_ref = UNSET
        elif isinstance(self.service_account_ref, ServiceAccountRefType):
            service_account_ref = self.service_account_ref.to_dict()
        else:
            service_account_ref = self.service_account_ref

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

        def _parse_connection_uuid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        connection_uuid = _parse_connection_uuid(d.pop("connectionUuid", UNSET))

        def _parse_first_record_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_record_date_type_0 = isoparse(data)

                return first_record_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        first_record_date = _parse_first_record_date(d.pop("firstRecordDate", UNSET))

        _service_name = d.pop("serviceName", UNSET)
        service_name: Union[Unset, BaseConnectionsResponseDataV2ServiceName]
        if isinstance(_service_name, Unset):
            service_name = UNSET
        else:
            service_name = check_base_connections_response_data_v2_service_name(_service_name)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_disconnect_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disconnect_reason = _parse_disconnect_reason(d.pop("disconnectReason", UNSET))

        def _parse_sync_time(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sync_time = _parse_sync_time(d.pop("syncTime", UNSET))

        def _parse_institution(data: object) -> Union["ConnectionsInstitutionData", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                institution_type_1 = ConnectionsInstitutionData.from_dict(data)

                return institution_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ConnectionsInstitutionData", None, Unset], data)

        institution = _parse_institution(d.pop("institution", UNSET))

        def _parse_is_mock_data(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_mock_data = _parse_is_mock_data(d.pop("isMockData", UNSET))

        def _parse_service_account_ref(data: object) -> Union["ServiceAccountRefType", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                service_account_ref_type_1 = ServiceAccountRefType.from_dict(data)

                return service_account_ref_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ServiceAccountRefType", None, Unset], data)

        service_account_ref = _parse_service_account_ref(d.pop("serviceAccountRef", UNSET))

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
