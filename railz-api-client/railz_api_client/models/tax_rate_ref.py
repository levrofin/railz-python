from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxRateRef")


@_attrs_define
class TaxRateRef:
    """
    Attributes:
        id (str):  Example: 1.
        name (Union[Unset, str]):  Example: HST.
        effective_tax_rate (Union[Unset, float]):  Example: 13.
    """

    id: str
    name: Union[Unset, str] = UNSET
    effective_tax_rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        effective_tax_rate = self.effective_tax_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if effective_tax_rate is not UNSET:
            field_dict["effectiveTaxRate"] = effective_tax_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        effective_tax_rate = d.pop("effectiveTaxRate", UNSET)

        tax_rate_ref = cls(
            id=id,
            name=name,
            effective_tax_rate=effective_tax_rate,
        )

        tax_rate_ref.additional_properties = d
        return tax_rate_ref

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
