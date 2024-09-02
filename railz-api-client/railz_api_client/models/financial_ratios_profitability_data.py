from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialRatiosProfitabilityData")


@_attrs_define
class FinancialRatiosProfitabilityData:
    """
    Attributes:
        return_on_assets (Union[Unset, float]):  Example: 0.09109873.
        ebitda (Union[Unset, float]):  Example: 278309.39.
        ebitda_margin (Union[Unset, float]):  Example: 0.32309803.
        working_capital (Union[Unset, float]):  Example: 78903.24.
        free_cash_flow (Union[Unset, float]):  Example: 129834.37.
        gross_margin (Union[Unset, float]):  Example: 0.48199755.
        net_profit_margin (Union[Unset, float]):  Example: 0.16412058.
        operating_margin (Union[Unset, float]):  Example: 0.06156661.
        return_on_equity (Union[Unset, float]):  Example: 0.15532511.
        revenue_concentration_index (Union[Unset, float]):  Example: 2.58889925.
        total_accruals_total_assets (Union[Unset, float]):  Example: 0.044.
        sga_expenses_index (Union[Unset, float]):  Example: 1.11.
        sales_growth_index (Union[Unset, float]):  Example: 0.755.
        gross_margin_index (Union[Unset, float]):  Example: 1.556.
        annual_recurring_revenue (Union[Unset, float]):  Example: 0.814.
        annual_recurring_revenue_rate (Union[Unset, float]):  Example: 0.266.
        monthly_recurring_revenue (Union[Unset, float]):  Example: 1.556.
        monthly_recurring_revenue_rate (Union[Unset, float]):  Example: 0.389.
    """

    return_on_assets: Union[Unset, float] = UNSET
    ebitda: Union[Unset, float] = UNSET
    ebitda_margin: Union[Unset, float] = UNSET
    working_capital: Union[Unset, float] = UNSET
    free_cash_flow: Union[Unset, float] = UNSET
    gross_margin: Union[Unset, float] = UNSET
    net_profit_margin: Union[Unset, float] = UNSET
    operating_margin: Union[Unset, float] = UNSET
    return_on_equity: Union[Unset, float] = UNSET
    revenue_concentration_index: Union[Unset, float] = UNSET
    total_accruals_total_assets: Union[Unset, float] = UNSET
    sga_expenses_index: Union[Unset, float] = UNSET
    sales_growth_index: Union[Unset, float] = UNSET
    gross_margin_index: Union[Unset, float] = UNSET
    annual_recurring_revenue: Union[Unset, float] = UNSET
    annual_recurring_revenue_rate: Union[Unset, float] = UNSET
    monthly_recurring_revenue: Union[Unset, float] = UNSET
    monthly_recurring_revenue_rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_on_assets = self.return_on_assets

        ebitda = self.ebitda

        ebitda_margin = self.ebitda_margin

        working_capital = self.working_capital

        free_cash_flow = self.free_cash_flow

        gross_margin = self.gross_margin

        net_profit_margin = self.net_profit_margin

        operating_margin = self.operating_margin

        return_on_equity = self.return_on_equity

        revenue_concentration_index = self.revenue_concentration_index

        total_accruals_total_assets = self.total_accruals_total_assets

        sga_expenses_index = self.sga_expenses_index

        sales_growth_index = self.sales_growth_index

        gross_margin_index = self.gross_margin_index

        annual_recurring_revenue = self.annual_recurring_revenue

        annual_recurring_revenue_rate = self.annual_recurring_revenue_rate

        monthly_recurring_revenue = self.monthly_recurring_revenue

        monthly_recurring_revenue_rate = self.monthly_recurring_revenue_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_on_assets is not UNSET:
            field_dict["returnOnAssets"] = return_on_assets
        if ebitda is not UNSET:
            field_dict["ebitda"] = ebitda
        if ebitda_margin is not UNSET:
            field_dict["ebitdaMargin"] = ebitda_margin
        if working_capital is not UNSET:
            field_dict["workingCapital"] = working_capital
        if free_cash_flow is not UNSET:
            field_dict["freeCashFlow"] = free_cash_flow
        if gross_margin is not UNSET:
            field_dict["grossMargin"] = gross_margin
        if net_profit_margin is not UNSET:
            field_dict["netProfitMargin"] = net_profit_margin
        if operating_margin is not UNSET:
            field_dict["operatingMargin"] = operating_margin
        if return_on_equity is not UNSET:
            field_dict["returnOnEquity"] = return_on_equity
        if revenue_concentration_index is not UNSET:
            field_dict["revenueConcentrationIndex"] = revenue_concentration_index
        if total_accruals_total_assets is not UNSET:
            field_dict["totalAccrualsTotalAssets"] = total_accruals_total_assets
        if sga_expenses_index is not UNSET:
            field_dict["sgaExpensesIndex"] = sga_expenses_index
        if sales_growth_index is not UNSET:
            field_dict["salesGrowthIndex"] = sales_growth_index
        if gross_margin_index is not UNSET:
            field_dict["grossMarginIndex"] = gross_margin_index
        if annual_recurring_revenue is not UNSET:
            field_dict["annualRecurringRevenue"] = annual_recurring_revenue
        if annual_recurring_revenue_rate is not UNSET:
            field_dict["annualRecurringRevenueRate"] = annual_recurring_revenue_rate
        if monthly_recurring_revenue is not UNSET:
            field_dict["monthlyRecurringRevenue"] = monthly_recurring_revenue
        if monthly_recurring_revenue_rate is not UNSET:
            field_dict["monthlyRecurringRevenueRate"] = monthly_recurring_revenue_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_on_assets = d.pop("returnOnAssets", UNSET)

        ebitda = d.pop("ebitda", UNSET)

        ebitda_margin = d.pop("ebitdaMargin", UNSET)

        working_capital = d.pop("workingCapital", UNSET)

        free_cash_flow = d.pop("freeCashFlow", UNSET)

        gross_margin = d.pop("grossMargin", UNSET)

        net_profit_margin = d.pop("netProfitMargin", UNSET)

        operating_margin = d.pop("operatingMargin", UNSET)

        return_on_equity = d.pop("returnOnEquity", UNSET)

        revenue_concentration_index = d.pop("revenueConcentrationIndex", UNSET)

        total_accruals_total_assets = d.pop("totalAccrualsTotalAssets", UNSET)

        sga_expenses_index = d.pop("sgaExpensesIndex", UNSET)

        sales_growth_index = d.pop("salesGrowthIndex", UNSET)

        gross_margin_index = d.pop("grossMarginIndex", UNSET)

        annual_recurring_revenue = d.pop("annualRecurringRevenue", UNSET)

        annual_recurring_revenue_rate = d.pop("annualRecurringRevenueRate", UNSET)

        monthly_recurring_revenue = d.pop("monthlyRecurringRevenue", UNSET)

        monthly_recurring_revenue_rate = d.pop("monthlyRecurringRevenueRate", UNSET)

        financial_ratios_profitability_data = cls(
            return_on_assets=return_on_assets,
            ebitda=ebitda,
            ebitda_margin=ebitda_margin,
            working_capital=working_capital,
            free_cash_flow=free_cash_flow,
            gross_margin=gross_margin,
            net_profit_margin=net_profit_margin,
            operating_margin=operating_margin,
            return_on_equity=return_on_equity,
            revenue_concentration_index=revenue_concentration_index,
            total_accruals_total_assets=total_accruals_total_assets,
            sga_expenses_index=sga_expenses_index,
            sales_growth_index=sales_growth_index,
            gross_margin_index=gross_margin_index,
            annual_recurring_revenue=annual_recurring_revenue,
            annual_recurring_revenue_rate=annual_recurring_revenue_rate,
            monthly_recurring_revenue=monthly_recurring_revenue,
            monthly_recurring_revenue_rate=monthly_recurring_revenue_rate,
        )

        financial_ratios_profitability_data.additional_properties = d
        return financial_ratios_profitability_data

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
