from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.push_customer_v2 import PushCustomerV2


T = TypeVar("T", bound="BatchPushCustomerV2Dto")


@_attrs_define
class BatchPushCustomerV2Dto:
    """
    Attributes:
        connection_uuid (str): Unique connection identifier. Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        batch (List['PushCustomerV2']):
    """

    connection_uuid: str
    batch: List["PushCustomerV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        batch = []
        for batch_item_data in self.batch:
            batch_item = batch_item_data.to_dict()
            batch.append(batch_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "batch": batch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_customer_v2 import PushCustomerV2

        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        batch = []
        _batch = d.pop("batch")
        for batch_item_data in _batch:
            batch_item = PushCustomerV2.from_dict(batch_item_data)

            batch.append(batch_item)

        batch_push_customer_v2_dto = cls(
            connection_uuid=connection_uuid,
            batch=batch,
        )

        batch_push_customer_v2_dto.additional_properties = d
        return batch_push_customer_v2_dto

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
