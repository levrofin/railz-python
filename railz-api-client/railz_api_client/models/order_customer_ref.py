from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderCustomerRef")


@_attrs_define
class OrderCustomerRef:
    """
    Attributes:
        id (str):  Example: 207119551.
        customer_name (Union[Unset, str]):  Example: Amelia Earhart.
        email (Union[Unset, str]):  Example: Amelia.Earhart@example.com.
    """

    id: str
    customer_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        customer_name = self.customer_name

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        customer_name = d.pop("customerName", UNSET)

        email = d.pop("email", UNSET)

        order_customer_ref = cls(
            id=id,
            customer_name=customer_name,
            email=email,
        )

        order_customer_ref.additional_properties = d
        return order_customer_ref

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
