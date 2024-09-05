from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attachment_link_type import AttachmentLinkType, check_attachment_link_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentLink")


@_attrs_define
class AttachmentLink:
    """
    Attributes:
        type (Union[Unset, AttachmentLinkType]):  Example: bill.
        id (Union[Unset, str]):  Example: 234.
    """

    type: Union[Unset, AttachmentLinkType] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, AttachmentLinkType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_attachment_link_type(_type)

        id = d.pop("id", UNSET)

        attachment_link = cls(
            type=type,
            id=id,
        )

        attachment_link.additional_properties = d
        return attachment_link

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
