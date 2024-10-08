import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ap_aging_meta_data_service_name import ApAgingMetaDataServiceName, check_ap_aging_meta_data_service_name

T = TypeVar("T", bound="ApAgingMetaData")


@_attrs_define
class ApAgingMetaData:
    """
    Attributes:
        report_id (List[str]):  Example: ['5fad8a342a88364234392fb5'].
        service_name (ApAgingMetaDataServiceName):  Example: xero.
        business_name (str):  Example: Railz.
        start_date (datetime.datetime):  Example: 2020-11-25T01:02:03Z.
        end_date (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
        created_at (datetime.datetime):  Example: 2020-11-25T01:02:03Z.
        updated_at (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
        report_frequency (str):  Example: month.
    """

    report_id: List[str]
    service_name: ApAgingMetaDataServiceName
    business_name: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    report_frequency: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_id = self.report_id

        service_name: str = self.service_name

        business_name = self.business_name

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        report_frequency = self.report_frequency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportId": report_id,
                "serviceName": service_name,
                "businessName": business_name,
                "startDate": start_date,
                "endDate": end_date,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "reportFrequency": report_frequency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        report_id = cast(List[str], d.pop("reportId"))

        service_name = check_ap_aging_meta_data_service_name(d.pop("serviceName"))

        business_name = d.pop("businessName")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        report_frequency = d.pop("reportFrequency")

        ap_aging_meta_data = cls(
            report_id=report_id,
            service_name=service_name,
            business_name=business_name,
            start_date=start_date,
            end_date=end_date,
            created_at=created_at,
            updated_at=updated_at,
            report_frequency=report_frequency,
        )

        ap_aging_meta_data.additional_properties = d
        return ap_aging_meta_data

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
