from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_bills_v2 import UpdateBillsV2


T = TypeVar("T", bound="UpdateBillsV2Dto")


@_attrs_define
class UpdateBillsV2Dto:
    """
    Attributes:
        connection_uuid (str): Unique connection identifier. Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        data (UpdateBillsV2):
    """

    connection_uuid: str
    data: "UpdateBillsV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_bills_v2 import UpdateBillsV2

        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        data = UpdateBillsV2.from_dict(d.pop("data"))

        update_bills_v2_dto = cls(
            connection_uuid=connection_uuid,
            data=data,
        )

        update_bills_v2_dto.additional_properties = d
        return update_bills_v2_dto

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
