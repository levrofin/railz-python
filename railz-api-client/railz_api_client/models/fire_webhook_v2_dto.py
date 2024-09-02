from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fire_webhook_connection_v2_dto import FireWebhookConnectionV2Dto


T = TypeVar("T", bound="FireWebhookV2Dto")


@_attrs_define
class FireWebhookV2Dto:
    """
    Attributes:
        connection (FireWebhookConnectionV2Dto):
    """

    connection: "FireWebhookConnectionV2Dto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection = self.connection.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection": connection,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fire_webhook_connection_v2_dto import FireWebhookConnectionV2Dto

        d = src_dict.copy()
        connection = FireWebhookConnectionV2Dto.from_dict(d.pop("connection"))

        fire_webhook_v2_dto = cls(
            connection=connection,
        )

        fire_webhook_v2_dto.additional_properties = d
        return fire_webhook_v2_dto

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
