from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.report_financial_ratios_response_200_data_profitability_revenue_concentration_index_time_period_data_item import (
        ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndexTimePeriodDataItem,
    )


T = TypeVar("T", bound="ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndex")


@_attrs_define
class ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndex:
    """
    Attributes:
        current_value (float): Return on Assets - EBITDA calculation (a decimal value) Example: 10.
        percentage_change (float): EBITDA (a dollar value) Example: 10.
        time_period_data
            (List['ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndexTimePeriodDataItem']):
    """

    current_value: float
    percentage_change: float
    time_period_data: List[
        "ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndexTimePeriodDataItem"
    ]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_value = self.current_value

        percentage_change = self.percentage_change

        time_period_data = []
        for time_period_data_item_data in self.time_period_data:
            time_period_data_item = time_period_data_item_data.to_dict()
            time_period_data.append(time_period_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentValue": current_value,
                "percentageChange": percentage_change,
                "timePeriodData": time_period_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_financial_ratios_response_200_data_profitability_revenue_concentration_index_time_period_data_item import (
            ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndexTimePeriodDataItem,
        )

        d = src_dict.copy()
        current_value = d.pop("currentValue")

        percentage_change = d.pop("percentageChange")

        time_period_data = []
        _time_period_data = d.pop("timePeriodData")
        for time_period_data_item_data in _time_period_data:
            time_period_data_item = (
                ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndexTimePeriodDataItem.from_dict(
                    time_period_data_item_data
                )
            )

            time_period_data.append(time_period_data_item)

        report_financial_ratios_response_200_data_profitability_revenue_concentration_index = cls(
            current_value=current_value,
            percentage_change=percentage_change,
            time_period_data=time_period_data,
        )

        report_financial_ratios_response_200_data_profitability_revenue_concentration_index.additional_properties = d
        return report_financial_ratios_response_200_data_profitability_revenue_concentration_index

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
