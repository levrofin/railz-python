from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.weight_unit_of_measure import WeightUnitOfMeasure
from ..types import UNSET, Unset

T = TypeVar("T", bound="Weight")


@_attrs_define
class Weight:
    """
    Attributes:
        value (Union[Unset, float]):  Example: 1.25.
        unit_of_measure (Union[Unset, WeightUnitOfMeasure]):  Example: lb.
    """

    value: Union[Unset, float] = UNSET
    unit_of_measure: Union[Unset, WeightUnitOfMeasure] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        unit_of_measure: Union[Unset, str] = UNSET
        if not isinstance(self.unit_of_measure, Unset):
            unit_of_measure = self.unit_of_measure

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        _unit_of_measure = d.pop("unitOfMeasure", UNSET)
        unit_of_measure: Union[Unset, WeightUnitOfMeasure]
        if isinstance(_unit_of_measure, Unset):
            unit_of_measure = UNSET
        else:
            unit_of_measure = _unit_of_measure

        weight = cls(
            value=value,
            unit_of_measure=unit_of_measure,
        )

        weight.additional_properties = d
        return weight

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
