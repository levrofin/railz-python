from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_type import DataType


T = TypeVar("T", bound="DataSyncData")


@_attrs_define
class DataSyncData:
    """
    Attributes:
        connection_id (str):  Example: CON-94652dff-06ab-4b97-bd1b-f91adf7048c3.
        data_types (List['DataType']):
        sync_time (Union[Unset, float]):  Example: 1.234.
        percentage_completed (Union[Unset, float]):  Example: 75.89.
    """

    connection_id: str
    data_types: List["DataType"]
    sync_time: Union[Unset, float] = UNSET
    percentage_completed: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id

        data_types = []
        for data_types_item_data in self.data_types:
            data_types_item = data_types_item_data.to_dict()
            data_types.append(data_types_item)

        sync_time = self.sync_time

        percentage_completed = self.percentage_completed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionId": connection_id,
                "dataTypes": data_types,
            }
        )
        if sync_time is not UNSET:
            field_dict["syncTime"] = sync_time
        if percentage_completed is not UNSET:
            field_dict["percentageCompleted"] = percentage_completed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_type import DataType

        d = src_dict.copy()
        connection_id = d.pop("connectionId")

        data_types = []
        _data_types = d.pop("dataTypes")
        for data_types_item_data in _data_types:
            data_types_item = DataType.from_dict(data_types_item_data)

            data_types.append(data_types_item)

        sync_time = d.pop("syncTime", UNSET)

        percentage_completed = d.pop("percentageCompleted", UNSET)

        data_sync_data = cls(
            connection_id=connection_id,
            data_types=data_types,
            sync_time=sync_time,
            percentage_completed=percentage_completed,
        )

        data_sync_data.additional_properties = d
        return data_sync_data

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
