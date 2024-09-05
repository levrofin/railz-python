import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.basic_start_end_date_report_meta_data_service_name import (
    BasicStartEndDateReportMetaDataServiceName,
    check_basic_start_end_date_report_meta_data_service_name,
)

T = TypeVar("T", bound="BasicStartEndDateReportMetaData")


@_attrs_define
class BasicStartEndDateReportMetaData:
    """
    Attributes:
        report_id (List[str]):  Example: ['5fad8a342a88364234392fb5'].
        service_name (BasicStartEndDateReportMetaDataServiceName):  Example: xero.
        business_name (str):  Example: Railz.
        created_at (datetime.datetime):  Example: 2020-11-25T01:02:03Z.
        updated_at (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
        start_date (datetime.datetime):  Example: 2020-11-25T01:02:03Z.
        end_date (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
    """

    report_id: List[str]
    service_name: BasicStartEndDateReportMetaDataServiceName
    business_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    start_date: datetime.datetime
    end_date: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_id = self.report_id

        service_name: str = self.service_name

        business_name = self.business_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportId": report_id,
                "serviceName": service_name,
                "businessName": business_name,
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
        report_id = cast(List[str], d.pop("reportId"))

        service_name = check_basic_start_end_date_report_meta_data_service_name(d.pop("serviceName"))

        business_name = d.pop("businessName")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        basic_start_end_date_report_meta_data = cls(
            report_id=report_id,
            service_name=service_name,
            business_name=business_name,
            created_at=created_at,
            updated_at=updated_at,
            start_date=start_date,
            end_date=end_date,
        )

        basic_start_end_date_report_meta_data.additional_properties = d
        return basic_start_end_date_report_meta_data

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
