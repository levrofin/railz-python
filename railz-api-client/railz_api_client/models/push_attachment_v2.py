from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_attachment_link import PushAttachmentLink
    from ..models.push_attachment_v2_pass_through import PushAttachmentV2PassThrough


T = TypeVar("T", bound="PushAttachmentV2")


@_attrs_define
class PushAttachmentV2:
    """
    Attributes:
        pass_through (Union[Unset, PushAttachmentV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        links (Union[Unset, List['PushAttachmentLink']]):
    """

    pass_through: Union[Unset, "PushAttachmentV2PassThrough"] = UNSET
    links: Union[Unset, List["PushAttachmentLink"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_attachment_link import PushAttachmentLink
        from ..models.push_attachment_v2_pass_through import PushAttachmentV2PassThrough

        d = src_dict.copy()
        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushAttachmentV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushAttachmentV2PassThrough.from_dict(_pass_through)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = PushAttachmentLink.from_dict(links_item_data)

            links.append(links_item)

        push_attachment_v2 = cls(
            pass_through=pass_through,
            links=links,
        )

        push_attachment_v2.additional_properties = d
        return push_attachment_v2

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
