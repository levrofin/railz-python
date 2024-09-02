from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialRatiosReliabilityData")


@_attrs_define
class FinancialRatiosReliabilityData:
    """
    Attributes:
        asset_quality_index (Union[Unset, float]):  Example: 0.608.
        depreciation_index (Union[Unset, float]):  Example: 0.801.
        days_sales_receivables_index (Union[Unset, float]):  Example: 0.814.
    """

    asset_quality_index: Union[Unset, float] = UNSET
    depreciation_index: Union[Unset, float] = UNSET
    days_sales_receivables_index: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_quality_index = self.asset_quality_index

        depreciation_index = self.depreciation_index

        days_sales_receivables_index = self.days_sales_receivables_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_quality_index is not UNSET:
            field_dict["assetQualityIndex"] = asset_quality_index
        if depreciation_index is not UNSET:
            field_dict["depreciationIndex"] = depreciation_index
        if days_sales_receivables_index is not UNSET:
            field_dict["daysSalesReceivablesIndex"] = days_sales_receivables_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_quality_index = d.pop("assetQualityIndex", UNSET)

        depreciation_index = d.pop("depreciationIndex", UNSET)

        days_sales_receivables_index = d.pop("daysSalesReceivablesIndex", UNSET)

        financial_ratios_reliability_data = cls(
            asset_quality_index=asset_quality_index,
            depreciation_index=depreciation_index,
            days_sales_receivables_index=days_sales_receivables_index,
        )

        financial_ratios_reliability_data.additional_properties = d
        return financial_ratios_reliability_data

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
