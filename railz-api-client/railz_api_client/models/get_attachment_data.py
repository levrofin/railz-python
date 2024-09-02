from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_link import AttachmentLink


T = TypeVar("T", bound="GetAttachmentData")


@_attrs_define
class GetAttachmentData:
    """
    Attributes:
        id (str):  Example: 1.
        url (str):  Example: https://api.railz.ai/Attachments/Image00394.png.
        file_name (Union[Unset, str]):  Example: image00394.png.
        content_type (Union[Unset, str]):  Example: image/jpeg.
        upload_date (Union[Unset, str]):  Example: 2020-11-25T01:02:03Z.
        file_size (Union[Unset, float]):  Example: 10495.
        source_modified_date (Union[Unset, str]):  Example: 2021-03-09T08:49:36.035Z.
        link (Union[Unset, AttachmentLink]):
    """

    id: str
    url: str
    file_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    upload_date: Union[Unset, str] = UNSET
    file_size: Union[Unset, float] = UNSET
    source_modified_date: Union[Unset, str] = UNSET
    link: Union[Unset, "AttachmentLink"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        url = self.url

        file_name = self.file_name

        content_type = self.content_type

        upload_date = self.upload_date

        file_size = self.file_size

        source_modified_date = self.source_modified_date

        link: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
            }
        )
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if upload_date is not UNSET:
            field_dict["uploadDate"] = upload_date
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment_link import AttachmentLink

        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        file_name = d.pop("fileName", UNSET)

        content_type = d.pop("contentType", UNSET)

        upload_date = d.pop("uploadDate", UNSET)

        file_size = d.pop("fileSize", UNSET)

        source_modified_date = d.pop("sourceModifiedDate", UNSET)

        _link = d.pop("link", UNSET)
        link: Union[Unset, AttachmentLink]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = AttachmentLink.from_dict(_link)

        get_attachment_data = cls(
            id=id,
            url=url,
            file_name=file_name,
            content_type=content_type,
            upload_date=upload_date,
            file_size=file_size,
            source_modified_date=source_modified_date,
            link=link,
        )

        get_attachment_data.additional_properties = d
        return get_attachment_data

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
