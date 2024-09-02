from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_sync_meta_v2_service_name import DataSyncMetaV2ServiceName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSyncMetaV2")


@_attrs_define
class DataSyncMetaV2:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (Union[Unset, str]):  Example: Railz.
        service_name (Union[Unset, DataSyncMetaV2ServiceName]):  Example: xero.
        sync_time (Union[Unset, float]):  Example: 1.234.
        percentage_completed (Union[Unset, float]):  Example: 75.89.
    """

    connection_uuid: str
    business_name: Union[Unset, str] = UNSET
    service_name: Union[Unset, DataSyncMetaV2ServiceName] = UNSET
    sync_time: Union[Unset, float] = UNSET
    percentage_completed: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        business_name = self.business_name

        service_name: Union[Unset, str] = UNSET
        if not isinstance(self.service_name, Unset):
            service_name = self.service_name

        sync_time = self.sync_time

        percentage_completed = self.percentage_completed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
            }
        )
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if sync_time is not UNSET:
            field_dict["syncTime"] = sync_time
        if percentage_completed is not UNSET:
            field_dict["percentageCompleted"] = percentage_completed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName", UNSET)

        _service_name = d.pop("serviceName", UNSET)
        service_name: Union[Unset, DataSyncMetaV2ServiceName]
        if isinstance(_service_name, Unset):
            service_name = UNSET
        else:
            service_name = _service_name

        sync_time = d.pop("syncTime", UNSET)

        percentage_completed = d.pop("percentageCompleted", UNSET)

        data_sync_meta_v2 = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
            sync_time=sync_time,
            percentage_completed=percentage_completed,
        )

        data_sync_meta_v2.additional_properties = d
        return data_sync_meta_v2

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
