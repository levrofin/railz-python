from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.report_financial_ratios_response_200_data_profitability_return_on_equity_time_period_data_item_period import (
        ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquityTimePeriodDataItemPeriod,
    )


T = TypeVar("T", bound="ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquityTimePeriodDataItem")


@_attrs_define
class ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquityTimePeriodDataItem:
    """
    Attributes:
        period (ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquityTimePeriodDataItemPeriod):
        value (float):  Example: 1000.
    """

    period: "ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquityTimePeriodDataItemPeriod"
    value: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period.to_dict()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_financial_ratios_response_200_data_profitability_return_on_equity_time_period_data_item_period import (
            ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquityTimePeriodDataItemPeriod,
        )

        d = src_dict.copy()
        period = ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquityTimePeriodDataItemPeriod.from_dict(
            d.pop("period")
        )

        value = d.pop("value")

        report_financial_ratios_response_200_data_profitability_return_on_equity_time_period_data_item = cls(
            period=period,
            value=value,
        )

        report_financial_ratios_response_200_data_profitability_return_on_equity_time_period_data_item.additional_properties = d
        return report_financial_ratios_response_200_data_profitability_return_on_equity_time_period_data_item

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
