from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_payment_link_dto_type import InvoicePaymentLinkDtoType, check_invoice_payment_link_dto_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoicePaymentLinkDto")


@_attrs_define
class InvoicePaymentLinkDto:
    """
    Attributes:
        id (str):  Example: 133.
        type (Union[Unset, InvoicePaymentLinkDtoType]):
    """

    id: str
    type: Union[Unset, InvoicePaymentLinkDtoType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _type = d.pop("type", UNSET)
        type: Union[Unset, InvoicePaymentLinkDtoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_invoice_payment_link_dto_type(_type)

        invoice_payment_link_dto = cls(
            id=id,
            type=type,
        )

        invoice_payment_link_dto.additional_properties = d
        return invoice_payment_link_dto

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
