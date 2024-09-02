from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_sync_dto_data_type import DataSyncDtoDataType
from ..models.data_sync_dto_service_name import DataSyncDtoServiceName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSyncDto")


@_attrs_define
class DataSyncDto:
    """
    Attributes:
        business_name (str):  Example: Railz.
        service_name (DataSyncDtoServiceName):
        data_type (DataSyncDtoDataType):
        full_sync (Union[Unset, bool]):  Default: False.
    """

    business_name: str
    service_name: DataSyncDtoServiceName
    data_type: DataSyncDtoDataType
    full_sync: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_name = self.business_name

        service_name = self.service_name

        data_type = self.data_type

        full_sync = self.full_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "businessName": business_name,
                "serviceName": service_name,
                "dataType": data_type,
            }
        )
        if full_sync is not UNSET:
            field_dict["fullSync"] = full_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        business_name = d.pop("businessName")

        service_name = d.pop("serviceName")

        data_type = d.pop("dataType")

        full_sync = d.pop("fullSync", UNSET)

        data_sync_dto = cls(
            business_name=business_name,
            service_name=service_name,
            data_type=data_type,
            full_sync=full_sync,
        )

        data_sync_dto.additional_properties = d
        return data_sync_dto

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
