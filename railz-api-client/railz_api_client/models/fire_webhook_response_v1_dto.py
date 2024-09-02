from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FireWebhookResponseV1Dto")


@_attrs_define
class FireWebhookResponseV1Dto:
    """
    Attributes:
        webhook_fired (bool):  Example: True.
    """

    webhook_fired: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        webhook_fired = self.webhook_fired

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhookFired": webhook_fired,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        webhook_fired = d.pop("webhookFired")

        fire_webhook_response_v1_dto = cls(
            webhook_fired=webhook_fired,
        )

        fire_webhook_response_v1_dto.additional_properties = d
        return fire_webhook_response_v1_dto

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
