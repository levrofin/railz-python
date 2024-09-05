from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_object_dto_webhook_location_item import (
    MetadataObjectDtoWebhookLocationItem,
    check_metadata_object_dto_webhook_location_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataObjectDto")


@_attrs_define
class MetadataObjectDto:
    """
    Attributes:
        name (str):
        value (str):
        webhook_location (Union[Unset, List[MetadataObjectDtoWebhookLocationItem]]):
    """

    name: str
    value: str
    webhook_location: Union[Unset, List[MetadataObjectDtoWebhookLocationItem]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        value = self.value

        webhook_location: Union[Unset, List[str]] = UNSET
        if not isinstance(self.webhook_location, Unset):
            webhook_location = []
            for webhook_location_item_data in self.webhook_location:
                webhook_location_item: str = webhook_location_item_data
                webhook_location.append(webhook_location_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if webhook_location is not UNSET:
            field_dict["webhookLocation"] = webhook_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        value = d.pop("value")

        webhook_location = []
        _webhook_location = d.pop("webhookLocation", UNSET)
        for webhook_location_item_data in _webhook_location or []:
            webhook_location_item = check_metadata_object_dto_webhook_location_item(webhook_location_item_data)

            webhook_location.append(webhook_location_item)

        metadata_object_dto = cls(
            name=name,
            value=value,
            webhook_location=webhook_location,
        )

        metadata_object_dto.additional_properties = d
        return metadata_object_dto

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
