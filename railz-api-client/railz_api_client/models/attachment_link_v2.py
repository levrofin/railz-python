from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attachment_link_v2_type import AttachmentLinkV2Type

T = TypeVar("T", bound="AttachmentLinkV2")


@_attrs_define
class AttachmentLinkV2:
    """
    Attributes:
        type (AttachmentLinkV2Type):  Example: bill.
        id (str):  Example: 234.
    """

    type: AttachmentLinkV2Type
    id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        id = d.pop("id")

        attachment_link_v2 = cls(
            type=type,
            id=id,
        )

        attachment_link_v2.additional_properties = d
        return attachment_link_v2

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
