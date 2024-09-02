from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_sync_v2_dto_data_type import DataSyncV2DtoDataType
from ..models.data_sync_v2_dto_data_types_item import DataSyncV2DtoDataTypesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSyncV2Dto")


@_attrs_define
class DataSyncV2Dto:
    """
    Attributes:
        connection_uuid (str): Unique connection identifier. Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        data_type (Union[Unset, DataSyncV2DtoDataType]):
        data_types (Union[Unset, List[DataSyncV2DtoDataTypesItem]]):
        full_sync (Union[Unset, bool]):  Default: False.
    """

    connection_uuid: str
    data_type: Union[Unset, DataSyncV2DtoDataType] = UNSET
    data_types: Union[Unset, List[DataSyncV2DtoDataTypesItem]] = UNSET
    full_sync: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        data_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type

        data_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_types, Unset):
            data_types = []
            for data_types_item_data in self.data_types:
                data_types_item = data_types_item_data
                data_types.append(data_types_item)

        full_sync = self.full_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
            }
        )
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if data_types is not UNSET:
            field_dict["dataTypes"] = data_types
        if full_sync is not UNSET:
            field_dict["fullSync"] = full_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, DataSyncV2DtoDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = _data_type

        data_types = []
        _data_types = d.pop("dataTypes", UNSET)
        for data_types_item_data in _data_types or []:
            data_types_item = data_types_item_data

            data_types.append(data_types_item)

        full_sync = d.pop("fullSync", UNSET)

        data_sync_v2_dto = cls(
            connection_uuid=connection_uuid,
            data_type=data_type,
            data_types=data_types,
            full_sync=full_sync,
        )

        data_sync_v2_dto.additional_properties = d
        return data_sync_v2_dto

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
