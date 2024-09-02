from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_sync_data import DataSyncData
    from ..models.data_sync_meta import DataSyncMeta


T = TypeVar("T", bound="DataStatusResponseDto")


@_attrs_define
class DataStatusResponseDto:
    """
    Attributes:
        meta (DataSyncMeta):
        data (Union[Unset, List['DataSyncData']]):
    """

    meta: "DataSyncMeta"
    data: Union[Unset, List["DataSyncData"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_sync_data import DataSyncData
        from ..models.data_sync_meta import DataSyncMeta

        d = src_dict.copy()
        meta = DataSyncMeta.from_dict(d.pop("meta"))

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = DataSyncData.from_dict(data_item_data)

            data.append(data_item)

        data_status_response_dto = cls(
            meta=meta,
            data=data,
        )

        data_status_response_dto.additional_properties = d
        return data_status_response_dto

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
