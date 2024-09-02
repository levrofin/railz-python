from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.push_bank_transfers import PushBankTransfers
    from ..models.push_bank_transfers_connection import PushBankTransfersConnection


T = TypeVar("T", bound="PushBankTransfersDto")


@_attrs_define
class PushBankTransfersDto:
    """
    Attributes:
        connection (PushBankTransfersConnection):
        data (PushBankTransfers):
    """

    connection: "PushBankTransfersConnection"
    data: "PushBankTransfers"
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
        from ..models.push_bank_transfers import PushBankTransfers
        from ..models.push_bank_transfers_connection import PushBankTransfersConnection

        d = src_dict.copy()
        connection = PushBankTransfersConnection.from_dict(d.pop("connection"))

        data = PushBankTransfers.from_dict(d.pop("data"))

        push_bank_transfers_dto = cls(
            connection=connection,
            data=data,
        )

        push_bank_transfers_dto.additional_properties = d
        return push_bank_transfers_dto

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
