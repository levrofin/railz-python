import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.business_info_meta_data_service_name import (
    BusinessInfoMetaDataServiceName,
    check_business_info_meta_data_service_name,
)

T = TypeVar("T", bound="BusinessInfoMetaData")


@_attrs_define
class BusinessInfoMetaData:
    """
    Attributes:
        report_id (str):  Example: 5fad8a342a88364234392fb5.
        service_name (BusinessInfoMetaDataServiceName):  Example: xero.
        business_name (str):  Example: Railz.
        created_at (datetime.datetime):  Example: 2020-11-25T01:02:03Z.
        updated_at (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
    """

    report_id: str
    service_name: BusinessInfoMetaDataServiceName
    business_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_id = self.report_id

        service_name: str = self.service_name

        business_name = self.business_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportId": report_id,
                "serviceName": service_name,
                "businessName": business_name,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        report_id = d.pop("reportId")

        service_name = check_business_info_meta_data_service_name(d.pop("serviceName"))

        business_name = d.pop("businessName")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        business_info_meta_data = cls(
            report_id=report_id,
            service_name=service_name,
            business_name=business_name,
            created_at=created_at,
            updated_at=updated_at,
        )

        business_info_meta_data.additional_properties = d
        return business_info_meta_data

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
