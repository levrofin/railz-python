from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_payment_link_type import InvoicePaymentLinkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoicePaymentLink")


@_attrs_define
class InvoicePaymentLink:
    """
    Attributes:
        type (InvoicePaymentLinkType):
        id (Union[Unset, str]):  Example: 50.
        amount (Union[Unset, float]):
    """

    type: InvoicePaymentLinkType
    id: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        id = self.id

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        invoice_payment_link = cls(
            type=type,
            id=id,
            amount=amount,
        )

        invoice_payment_link.additional_properties = d
        return invoice_payment_link

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
