from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessValuationData")


@_attrs_define
class BusinessValuationData:
    """
    Attributes:
        liquidation_value (Union[Unset, float]):  Example: 100000.
        discounted_cashflow_value (Union[Unset, float]):  Example: 100000.
        discount_rate (Union[Unset, float]):  Example: 0.12.
        revenue_multiple (Union[Unset, float]):  Example: 1.6.
        multiple_to_revenue_value (Union[Unset, float]):  Example: 100000.
        first_chicago_value (Union[Unset, float]):  Example: 100000.
    """

    liquidation_value: Union[Unset, float] = UNSET
    discounted_cashflow_value: Union[Unset, float] = UNSET
    discount_rate: Union[Unset, float] = UNSET
    revenue_multiple: Union[Unset, float] = UNSET
    multiple_to_revenue_value: Union[Unset, float] = UNSET
    first_chicago_value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        liquidation_value = self.liquidation_value

        discounted_cashflow_value = self.discounted_cashflow_value

        discount_rate = self.discount_rate

        revenue_multiple = self.revenue_multiple

        multiple_to_revenue_value = self.multiple_to_revenue_value

        first_chicago_value = self.first_chicago_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if liquidation_value is not UNSET:
            field_dict["liquidationValue"] = liquidation_value
        if discounted_cashflow_value is not UNSET:
            field_dict["discountedCashflowValue"] = discounted_cashflow_value
        if discount_rate is not UNSET:
            field_dict["discountRate"] = discount_rate
        if revenue_multiple is not UNSET:
            field_dict["revenueMultiple"] = revenue_multiple
        if multiple_to_revenue_value is not UNSET:
            field_dict["multipleToRevenueValue"] = multiple_to_revenue_value
        if first_chicago_value is not UNSET:
            field_dict["firstChicagoValue"] = first_chicago_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        liquidation_value = d.pop("liquidationValue", UNSET)

        discounted_cashflow_value = d.pop("discountedCashflowValue", UNSET)

        discount_rate = d.pop("discountRate", UNSET)

        revenue_multiple = d.pop("revenueMultiple", UNSET)

        multiple_to_revenue_value = d.pop("multipleToRevenueValue", UNSET)

        first_chicago_value = d.pop("firstChicagoValue", UNSET)

        business_valuation_data = cls(
            liquidation_value=liquidation_value,
            discounted_cashflow_value=discounted_cashflow_value,
            discount_rate=discount_rate,
            revenue_multiple=revenue_multiple,
            multiple_to_revenue_value=multiple_to_revenue_value,
            first_chicago_value=first_chicago_value,
        )

        business_valuation_data.additional_properties = d
        return business_valuation_data

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
