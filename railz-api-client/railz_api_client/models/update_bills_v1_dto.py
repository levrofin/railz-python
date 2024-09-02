from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.push_update_bills_connection import PushUpdateBillsConnection
    from ..models.update_bills_v1 import UpdateBillsV1


T = TypeVar("T", bound="UpdateBillsV1Dto")


@_attrs_define
class UpdateBillsV1Dto:
    """
    Attributes:
        connection (PushUpdateBillsConnection):
        data (UpdateBillsV1):
    """

    connection: "PushUpdateBillsConnection"
    data: "UpdateBillsV1"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection = self.connection.to_dict()

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection": connection,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_update_bills_connection import PushUpdateBillsConnection
        from ..models.update_bills_v1 import UpdateBillsV1

        d = src_dict.copy()
        connection = PushUpdateBillsConnection.from_dict(d.pop("connection"))

        data = UpdateBillsV1.from_dict(d.pop("data"))

        update_bills_v1_dto = cls(
            connection=connection,
            data=data,
        )

        update_bills_v1_dto.additional_properties = d
        return update_bills_v1_dto

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
