import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.metadata_object_dto import MetadataObjectDto


T = TypeVar("T", bound="PutBusinessesResponseDto")


@_attrs_define
class PutBusinessesResponseDto:
    """
    Attributes:
        business_name (str):  Example: Railz.
        url (str):
        metadata (List['MetadataObjectDto']):
        status (str):
        created_at (datetime.datetime):
        business_uuid (str):
        updated_at (datetime.datetime):
    """

    business_name: str
    url: str
    metadata: List["MetadataObjectDto"]
    status: str
    created_at: datetime.datetime
    business_uuid: str
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_name = self.business_name

        url = self.url

        metadata = []
        for metadata_item_data in self.metadata:
            metadata_item = metadata_item_data.to_dict()
            metadata.append(metadata_item)

        status = self.status

        created_at = self.created_at.isoformat()

        business_uuid = self.business_uuid

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "businessName": business_name,
                "url": url,
                "metadata": metadata,
                "status": status,
                "createdAt": created_at,
                "businessUUID": business_uuid,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metadata_object_dto import MetadataObjectDto

        d = src_dict.copy()
        business_name = d.pop("businessName")

        url = d.pop("url")

        metadata = []
        _metadata = d.pop("metadata")
        for metadata_item_data in _metadata:
            metadata_item = MetadataObjectDto.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        status = d.pop("status")

        created_at = isoparse(d.pop("createdAt"))

        business_uuid = d.pop("businessUUID")

        updated_at = isoparse(d.pop("updatedAt"))

        put_businesses_response_dto = cls(
            business_name=business_name,
            url=url,
            metadata=metadata,
            status=status,
            created_at=created_at,
            business_uuid=business_uuid,
            updated_at=updated_at,
        )

        put_businesses_response_dto.additional_properties = d
        return put_businesses_response_dto

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
