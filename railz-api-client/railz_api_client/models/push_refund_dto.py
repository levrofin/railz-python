from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.push_refund_connection import PushRefundConnection
    from ..models.push_refund_data import PushRefundData


T = TypeVar("T", bound="PushRefundDto")


@_attrs_define
class PushRefundDto:
    """
    Attributes:
        connection (PushRefundConnection):
        data (PushRefundData):
    """

    connection: "PushRefundConnection"
    data: "PushRefundData"
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
        from ..models.push_refund_connection import PushRefundConnection
        from ..models.push_refund_data import PushRefundData

        d = src_dict.copy()
        connection = PushRefundConnection.from_dict(d.pop("connection"))

        data = PushRefundData.from_dict(d.pop("data"))

        push_refund_dto = cls(
            connection=connection,
            data=data,
        )

        push_refund_dto.additional_properties = d
        return push_refund_dto

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
