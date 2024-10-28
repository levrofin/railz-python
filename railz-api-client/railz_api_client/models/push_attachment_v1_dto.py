from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

if TYPE_CHECKING:
    from ..models.push_attachment_connection import PushAttachmentConnection
    from ..models.push_attachment_v1 import PushAttachmentV1


T = TypeVar("T", bound="PushAttachmentV1Dto")


@_attrs_define
class PushAttachmentV1Dto:
    """
    Attributes:
        connection (PushAttachmentConnection):
        file (File):
        data (PushAttachmentV1):
    """

    connection: "PushAttachmentConnection"
    file: File
    data: "PushAttachmentV1"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection = self.connection.to_dict()

        file = self.file.to_json()

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection": connection,
                "file": file,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_attachment_connection import PushAttachmentConnection
        from ..models.push_attachment_v1 import PushAttachmentV1

        d = src_dict.copy()
        connection = PushAttachmentConnection.from_dict(d.pop("connection"))

        file = File(payload=BytesIO(d.pop("file")))

        data = PushAttachmentV1.from_dict(d.pop("data"))

        push_attachment_v1_dto = cls(
            connection=connection,
            file=file,
            data=data,
        )

        push_attachment_v1_dto.additional_properties = d
        return push_attachment_v1_dto

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
