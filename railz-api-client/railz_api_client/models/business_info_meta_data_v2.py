import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.business_info_meta_data_v2_service_name import BusinessInfoMetaDataV2ServiceName
from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessInfoMetaDataV2")


@_attrs_define
class BusinessInfoMetaDataV2:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        report_id (str):  Example: 5fad8a342a88364234392fb5.
        created_at (datetime.datetime):  Example: 2020-11-25T01:02:03Z.
        updated_at (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
        business_name (Union[Unset, str]):  Example: Railz.
        service_name (Union[Unset, BusinessInfoMetaDataV2ServiceName]):  Example: xero.
    """

    connection_uuid: str
    report_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    business_name: Union[Unset, str] = UNSET
    service_name: Union[Unset, BusinessInfoMetaDataV2ServiceName] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        report_id = self.report_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        business_name = self.business_name

        service_name: Union[Unset, str] = UNSET
        if not isinstance(self.service_name, Unset):
            service_name = self.service_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "reportId": report_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        report_id = d.pop("reportId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        business_name = d.pop("businessName", UNSET)

        _service_name = d.pop("serviceName", UNSET)
        service_name: Union[Unset, BusinessInfoMetaDataV2ServiceName]
        if isinstance(_service_name, Unset):
            service_name = UNSET
        else:
            service_name = _service_name

        business_info_meta_data_v2 = cls(
            connection_uuid=connection_uuid,
            report_id=report_id,
            created_at=created_at,
            updated_at=updated_at,
            business_name=business_name,
            service_name=service_name,
        )

        business_info_meta_data_v2.additional_properties = d
        return business_info_meta_data_v2

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
