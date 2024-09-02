from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.connection_metadata import ConnectionMetadata
    from ..models.sync_info import SyncInfo


T = TypeVar("T", bound="SyncInfoResponseV2Dto")


@_attrs_define
class SyncInfoResponseV2Dto:
    """
    Attributes:
        meta (ConnectionMetadata):
        data (SyncInfo):
    """

    meta: "ConnectionMetadata"
    data: "SyncInfo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.connection_metadata import ConnectionMetadata
        from ..models.sync_info import SyncInfo

        d = src_dict.copy()
        meta = ConnectionMetadata.from_dict(d.pop("meta"))

        data = SyncInfo.from_dict(d.pop("data"))

        sync_info_response_v2_dto = cls(
            meta=meta,
            data=data,
        )

        sync_info_response_v2_dto.additional_properties = d
        return sync_info_response_v2_dto

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
