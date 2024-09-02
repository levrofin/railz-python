from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quantity_per_location import QuantityPerLocation


T = TypeVar("T", bound="Inventory")


@_attrs_define
class Inventory:
    """
    Attributes:
        total_quantity (Union[Unset, float]):  Example: 10.
        quantity_per_location (Union[Unset, List['QuantityPerLocation']]):
    """

    total_quantity: Union[Unset, float] = UNSET
    quantity_per_location: Union[Unset, List["QuantityPerLocation"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_quantity = self.total_quantity

        quantity_per_location: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quantity_per_location, Unset):
            quantity_per_location = []
            for quantity_per_location_item_data in self.quantity_per_location:
                quantity_per_location_item = quantity_per_location_item_data.to_dict()
                quantity_per_location.append(quantity_per_location_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity
        if quantity_per_location is not UNSET:
            field_dict["quantityPerLocation"] = quantity_per_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.quantity_per_location import QuantityPerLocation

        d = src_dict.copy()
        total_quantity = d.pop("totalQuantity", UNSET)

        quantity_per_location = []
        _quantity_per_location = d.pop("quantityPerLocation", UNSET)
        for quantity_per_location_item_data in _quantity_per_location or []:
            quantity_per_location_item = QuantityPerLocation.from_dict(quantity_per_location_item_data)

            quantity_per_location.append(quantity_per_location_item)

        inventory = cls(
            total_quantity=total_quantity,
            quantity_per_location=quantity_per_location,
        )

        inventory.additional_properties = d
        return inventory

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
