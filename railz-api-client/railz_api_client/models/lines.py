from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Lines")


@_attrs_define
class Lines:
    """
    Attributes:
        id (str):  Example: 466157049.
        variant_id (str):  Example: 39072856.
        quantity (float):  Example: 3.
        total_price (float):  Example: 199.
        product_id (Union[Unset, str]):  Example: 632910392.
        name (Union[Unset, str]):  Example: Custom Engraving Front.
        unit_price (Union[Unset, float]):  Example: 300.
        sku (Union[Unset, str]):  Example: IPOD2008GREEN.
    """

    id: str
    variant_id: str
    quantity: float
    total_price: float
    product_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    sku: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        variant_id = self.variant_id

        quantity = self.quantity

        total_price = self.total_price

        product_id = self.product_id

        name = self.name

        unit_price = self.unit_price

        sku = self.sku

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "variantId": variant_id,
                "quantity": quantity,
                "totalPrice": total_price,
            }
        )
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if name is not UNSET:
            field_dict["name"] = name
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if sku is not UNSET:
            field_dict["sku"] = sku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        variant_id = d.pop("variantId")

        quantity = d.pop("quantity")

        total_price = d.pop("totalPrice")

        product_id = d.pop("productId", UNSET)

        name = d.pop("name", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        sku = d.pop("sku", UNSET)

        lines = cls(
            id=id,
            variant_id=variant_id,
            quantity=quantity,
            total_price=total_price,
            product_id=product_id,
            name=name,
            unit_price=unit_price,
            sku=sku,
        )

        lines.additional_properties = d
        return lines

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
