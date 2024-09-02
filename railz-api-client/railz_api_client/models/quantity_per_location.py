from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_location_ref import ProductLocationRef


T = TypeVar("T", bound="QuantityPerLocation")


@_attrs_define
class QuantityPerLocation:
    """
    Attributes:
        quantity (Union[Unset, float]):
        location_ref (Union[Unset, ProductLocationRef]):
    """

    quantity: Union[Unset, float] = UNSET
    location_ref: Union[Unset, "ProductLocationRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity

        location_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location_ref, Unset):
            location_ref = self.location_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_location_ref import ProductLocationRef

        d = src_dict.copy()
        quantity = d.pop("quantity", UNSET)

        _location_ref = d.pop("locationRef", UNSET)
        location_ref: Union[Unset, ProductLocationRef]
        if isinstance(_location_ref, Unset):
            location_ref = UNSET
        else:
            location_ref = ProductLocationRef.from_dict(_location_ref)

        quantity_per_location = cls(
            quantity=quantity,
            location_ref=location_ref,
        )

        quantity_per_location.additional_properties = d
        return quantity_per_location

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
