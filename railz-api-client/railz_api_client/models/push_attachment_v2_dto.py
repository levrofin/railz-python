import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.push_attachment_v2 import PushAttachmentV2


T = TypeVar("T", bound="PushAttachmentV2Dto")


@_attrs_define
class PushAttachmentV2Dto:
    """
    Attributes:
        connection_uuid (str): Unique connection identifier. Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        file (File):
        data (Union[Unset, PushAttachmentV2]):
    """

    connection_uuid: str
    file: File
    data: Union[Unset, "PushAttachmentV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        file = self.file.to_tuple()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "file": file,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        connection_uuid = (None, str(self.connection_uuid).encode(), "text/plain")

        file = self.file.to_tuple()

        data: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.data, Unset):
            data = (None, json.dumps(self.data.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "file": file,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_attachment_v2 import PushAttachmentV2

        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        file = File(payload=BytesIO(d.pop("file")))

        _data = d.pop("data", UNSET)
        data: Union[Unset, PushAttachmentV2]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PushAttachmentV2.from_dict(_data)

        push_attachment_v2_dto = cls(
            connection_uuid=connection_uuid,
            file=file,
            data=data,
        )

        push_attachment_v2_dto.additional_properties = d
        return push_attachment_v2_dto

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
