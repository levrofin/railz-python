from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialRatiosMarketData")


@_attrs_define
class FinancialRatiosMarketData:
    """
    Attributes:
        debt_to_enterprise_value (Union[Unset, float]):  Example: 0.19155987.
    """

    debt_to_enterprise_value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        debt_to_enterprise_value = self.debt_to_enterprise_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if debt_to_enterprise_value is not UNSET:
            field_dict["debtToEnterpriseValue"] = debt_to_enterprise_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        debt_to_enterprise_value = d.pop("debtToEnterpriseValue", UNSET)

        financial_ratios_market_data = cls(
            debt_to_enterprise_value=debt_to_enterprise_value,
        )

        financial_ratios_market_data.additional_properties = d
        return financial_ratios_market_data

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
