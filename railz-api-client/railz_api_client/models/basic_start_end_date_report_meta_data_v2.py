import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.basic_start_end_date_report_meta_data_v2_service_name import (
    BasicStartEndDateReportMetaDataV2ServiceName,
    check_basic_start_end_date_report_meta_data_v2_service_name,
)

T = TypeVar("T", bound="BasicStartEndDateReportMetaDataV2")


@_attrs_define
class BasicStartEndDateReportMetaDataV2:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (str):  Example: Railz.
        service_name (BasicStartEndDateReportMetaDataV2ServiceName):  Example: xero.
        report_id (List[str]):  Example: ['5fad8a342a88364234392fb5'].
        created_at (datetime.datetime):  Example: 2020-11-25T01:02:03Z.
        updated_at (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
        start_date (datetime.datetime):  Example: 2020-11-25T01:02:03Z.
        end_date (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
    """

    connection_uuid: str
    business_name: str
    service_name: BasicStartEndDateReportMetaDataV2ServiceName
    report_id: List[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    start_date: datetime.datetime
    end_date: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        business_name = self.business_name

        service_name: str = self.service_name

        report_id = self.report_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "businessName": business_name,
                "serviceName": service_name,
                "reportId": report_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "startDate": start_date,
                "endDate": end_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName")

        service_name = check_basic_start_end_date_report_meta_data_v2_service_name(d.pop("serviceName"))

        report_id = cast(List[str], d.pop("reportId"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        basic_start_end_date_report_meta_data_v2 = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
            report_id=report_id,
            created_at=created_at,
            updated_at=updated_at,
            start_date=start_date,
            end_date=end_date,
        )

        basic_start_end_date_report_meta_data_v2.additional_properties = d
        return basic_start_end_date_report_meta_data_v2

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
