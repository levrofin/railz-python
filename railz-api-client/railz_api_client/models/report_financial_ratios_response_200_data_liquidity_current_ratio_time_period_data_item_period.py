from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportFinancialRatiosResponse200DataLiquidityCurrentRatioTimePeriodDataItemPeriod")


@_attrs_define
class ReportFinancialRatiosResponse200DataLiquidityCurrentRatioTimePeriodDataItemPeriod:
    """
    Attributes:
        year (float):  Example: 2020.
        month (float):  Example: 8.
        quarter (float):  Example: 3.
        day (float):  Example: 31.
        date (str):  Example: 2020-08-31T00:00:00.000Z.
    """

    year: float
    month: float
    quarter: float
    day: float
    date: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year

        month = self.month

        quarter = self.quarter

        day = self.day

        date = self.date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "month": month,
                "quarter": quarter,
                "day": day,
                "date": date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year")

        month = d.pop("month")

        quarter = d.pop("quarter")

        day = d.pop("day")

        date = d.pop("date")

        report_financial_ratios_response_200_data_liquidity_current_ratio_time_period_data_item_period = cls(
            year=year,
            month=month,
            quarter=quarter,
            day=day,
            date=date,
        )

        report_financial_ratios_response_200_data_liquidity_current_ratio_time_period_data_item_period.additional_properties = d
        return report_financial_ratios_response_200_data_liquidity_current_ratio_time_period_data_item_period

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
