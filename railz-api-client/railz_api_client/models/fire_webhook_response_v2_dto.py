from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FireWebhookResponseV2Dto")


@_attrs_define
class FireWebhookResponseV2Dto:
    """
    Attributes:
        webhook_fired (bool):  Example: True.
        connection_uuid (str):  Example: CON-004f4cbe-e9ba-46c0-a7ef-2da661fe0e15.
        business_uuid (str):  Example: BIZ-26bc4510-8c6f-4688-996d-e87acf3e0b3f.
    """

    webhook_fired: bool
    connection_uuid: str
    business_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        webhook_fired = self.webhook_fired

        connection_uuid = self.connection_uuid

        business_uuid = self.business_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhookFired": webhook_fired,
                "connectionUuid": connection_uuid,
                "businessUuid": business_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        webhook_fired = d.pop("webhookFired")

        connection_uuid = d.pop("connectionUuid")

        business_uuid = d.pop("businessUuid")

        fire_webhook_response_v2_dto = cls(
            webhook_fired=webhook_fired,
            connection_uuid=connection_uuid,
            business_uuid=business_uuid,
        )

        fire_webhook_response_v2_dto.additional_properties = d
        return fire_webhook_response_v2_dto

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
