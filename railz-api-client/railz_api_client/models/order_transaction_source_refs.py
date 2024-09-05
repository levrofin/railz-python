from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_transaction_source_refs_type import (
    OrderTransactionSourceRefsType,
    check_order_transaction_source_refs_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderTransactionSourceRefs")


@_attrs_define
class OrderTransactionSourceRefs:
    """
    Attributes:
        id (str):  Example: 699519475.
        total_amount (float):  Example: 50.00.
        type (Union[Unset, OrderTransactionSourceRefsType]):  Example: payment.
    """

    id: str
    total_amount: float
    type: Union[Unset, OrderTransactionSourceRefsType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        total_amount = self.total_amount

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "totalAmount": total_amount,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        total_amount = d.pop("totalAmount")

        _type = d.pop("type", UNSET)
        type: Union[Unset, OrderTransactionSourceRefsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_order_transaction_source_refs_type(_type)

        order_transaction_source_refs = cls(
            id=id,
            total_amount=total_amount,
            type=type,
        )

        order_transaction_source_refs.additional_properties = d
        return order_transaction_source_refs

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
