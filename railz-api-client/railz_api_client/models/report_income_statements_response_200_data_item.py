from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.report_income_statements_response_200_data_item_period import (
        ReportIncomeStatementsResponse200DataItemPeriod,
    )


T = TypeVar("T", bound="ReportIncomeStatementsResponse200DataItem")


@_attrs_define
class ReportIncomeStatementsResponse200DataItem:
    """
    Attributes:
        period (ReportIncomeStatementsResponse200DataItemPeriod):
        operating_income (float):  Example: 345.
        operating_expenses (float):  Example: 345.
        cost_of_goods_sold (float):  Example: 345.
        other_income (float):  Example: 345.
        other_expenses (float):  Example: 345.
        net_income (float):  Example: 345.
    """

    period: "ReportIncomeStatementsResponse200DataItemPeriod"
    operating_income: float
    operating_expenses: float
    cost_of_goods_sold: float
    other_income: float
    other_expenses: float
    net_income: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period.to_dict()

        operating_income = self.operating_income

        operating_expenses = self.operating_expenses

        cost_of_goods_sold = self.cost_of_goods_sold

        other_income = self.other_income

        other_expenses = self.other_expenses

        net_income = self.net_income

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "operatingIncome": operating_income,
                "operatingExpenses": operating_expenses,
                "costOfGoodsSold": cost_of_goods_sold,
                "otherIncome": other_income,
                "otherExpenses": other_expenses,
                "netIncome": net_income,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_income_statements_response_200_data_item_period import (
            ReportIncomeStatementsResponse200DataItemPeriod,
        )

        d = src_dict.copy()
        period = ReportIncomeStatementsResponse200DataItemPeriod.from_dict(d.pop("period"))

        operating_income = d.pop("operatingIncome")

        operating_expenses = d.pop("operatingExpenses")

        cost_of_goods_sold = d.pop("costOfGoodsSold")

        other_income = d.pop("otherIncome")

        other_expenses = d.pop("otherExpenses")

        net_income = d.pop("netIncome")

        report_income_statements_response_200_data_item = cls(
            period=period,
            operating_income=operating_income,
            operating_expenses=operating_expenses,
            cost_of_goods_sold=cost_of_goods_sold,
            other_income=other_income,
            other_expenses=other_expenses,
            net_income=net_income,
        )

        report_income_statements_response_200_data_item.additional_properties = d
        return report_income_statements_response_200_data_item

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
