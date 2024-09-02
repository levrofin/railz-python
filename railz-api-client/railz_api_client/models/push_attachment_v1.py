from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.push_attachment_link import PushAttachmentLink


T = TypeVar("T", bound="PushAttachmentV1")


@_attrs_define
class PushAttachmentV1:
    """
    Attributes:
        link (PushAttachmentLink):
    """

    link: "PushAttachmentLink"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_attachment_link import PushAttachmentLink

        d = src_dict.copy()
        link = PushAttachmentLink.from_dict(d.pop("link"))

        push_attachment_v1 = cls(
            link=link,
        )

        push_attachment_v1.additional_properties = d
        return push_attachment_v1

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
