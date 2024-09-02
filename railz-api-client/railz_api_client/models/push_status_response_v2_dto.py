from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.push_status_data_v2 import PushStatusDataV2
    from ..models.push_status_meta_data_v2 import PushStatusMetaDataV2


T = TypeVar("T", bound="PushStatusResponseV2Dto")


@_attrs_define
class PushStatusResponseV2Dto:
    """
    Attributes:
        meta (PushStatusMetaDataV2):
        data (List['PushStatusDataV2']):
    """

    meta: "PushStatusMetaDataV2"
    data: List["PushStatusDataV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

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
        from ..models.push_status_data_v2 import PushStatusDataV2
        from ..models.push_status_meta_data_v2 import PushStatusMetaDataV2

        d = src_dict.copy()
        meta = PushStatusMetaDataV2.from_dict(d.pop("meta"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = PushStatusDataV2.from_dict(data_item_data)

            data.append(data_item)

        push_status_response_v2_dto = cls(
            meta=meta,
            data=data,
        )

        push_status_response_v2_dto.additional_properties = d
        return push_status_response_v2_dto

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
