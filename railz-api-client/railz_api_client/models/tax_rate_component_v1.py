from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxRateComponentV1")


@_attrs_define
class TaxRateComponentV1:
    """
    Attributes:
        name (Union[Unset, str]):  Example: HST.
        rate (Union[Unset, float]):  Example: 13.
        is_compound (Union[Unset, bool]):
        is_purchases_tax (Union[Unset, bool]):
        is_sales_tax (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    is_compound: Union[Unset, bool] = UNSET
    is_purchases_tax: Union[Unset, bool] = UNSET
    is_sales_tax: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        rate = self.rate

        is_compound = self.is_compound

        is_purchases_tax = self.is_purchases_tax

        is_sales_tax = self.is_sales_tax

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if rate is not UNSET:
            field_dict["rate"] = rate
        if is_compound is not UNSET:
            field_dict["isCompound"] = is_compound
        if is_purchases_tax is not UNSET:
            field_dict["isPurchasesTax"] = is_purchases_tax
        if is_sales_tax is not UNSET:
            field_dict["isSalesTax"] = is_sales_tax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        rate = d.pop("rate", UNSET)

        is_compound = d.pop("isCompound", UNSET)

        is_purchases_tax = d.pop("isPurchasesTax", UNSET)

        is_sales_tax = d.pop("isSalesTax", UNSET)

        tax_rate_component_v1 = cls(
            name=name,
            rate=rate,
            is_compound=is_compound,
            is_purchases_tax=is_purchases_tax,
            is_sales_tax=is_sales_tax,
        )

        tax_rate_component_v1.additional_properties = d
        return tax_rate_component_v1

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
