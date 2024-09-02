from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialRatiosEfficiencyData")


@_attrs_define
class FinancialRatiosEfficiencyData:
    """
    Attributes:
        gross_burn_rate (Union[Unset, float]):  Example: 56223.25.
        inventory_turnover_ratio (Union[Unset, float]):  Example: 2.78891542.
        asset_turnover_ratio (Union[Unset, float]):  Example: 3.83548112.
        payables_conversion_period (Union[Unset, float]):  Example: 83.
        accounts_receivable_turnover_ratio (Union[Unset, float]):  Example: 15.55.
        accounts_payable_turnover_ratio (Union[Unset, float]):  Example: 8.99.
        days_payable_outstanding (Union[Unset, float]):  Example: 42.26.
        days_sales_outstanding (Union[Unset, float]):  Example: 34.19.
        average_outstanding_payables_balance (Union[Unset, float]):  Example: 100.99.
        average_outstanding_receivables_balance (Union[Unset, float]):  Example: 29.01.
        churn_rate (Union[Unset, float]):  Example: 1.
    """

    gross_burn_rate: Union[Unset, float] = UNSET
    inventory_turnover_ratio: Union[Unset, float] = UNSET
    asset_turnover_ratio: Union[Unset, float] = UNSET
    payables_conversion_period: Union[Unset, float] = UNSET
    accounts_receivable_turnover_ratio: Union[Unset, float] = UNSET
    accounts_payable_turnover_ratio: Union[Unset, float] = UNSET
    days_payable_outstanding: Union[Unset, float] = UNSET
    days_sales_outstanding: Union[Unset, float] = UNSET
    average_outstanding_payables_balance: Union[Unset, float] = UNSET
    average_outstanding_receivables_balance: Union[Unset, float] = UNSET
    churn_rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gross_burn_rate = self.gross_burn_rate

        inventory_turnover_ratio = self.inventory_turnover_ratio

        asset_turnover_ratio = self.asset_turnover_ratio

        payables_conversion_period = self.payables_conversion_period

        accounts_receivable_turnover_ratio = self.accounts_receivable_turnover_ratio

        accounts_payable_turnover_ratio = self.accounts_payable_turnover_ratio

        days_payable_outstanding = self.days_payable_outstanding

        days_sales_outstanding = self.days_sales_outstanding

        average_outstanding_payables_balance = self.average_outstanding_payables_balance

        average_outstanding_receivables_balance = self.average_outstanding_receivables_balance

        churn_rate = self.churn_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gross_burn_rate is not UNSET:
            field_dict["grossBurnRate"] = gross_burn_rate
        if inventory_turnover_ratio is not UNSET:
            field_dict["inventoryTurnoverRatio"] = inventory_turnover_ratio
        if asset_turnover_ratio is not UNSET:
            field_dict["assetTurnoverRatio"] = asset_turnover_ratio
        if payables_conversion_period is not UNSET:
            field_dict["payablesConversionPeriod"] = payables_conversion_period
        if accounts_receivable_turnover_ratio is not UNSET:
            field_dict["accountsReceivableTurnoverRatio"] = accounts_receivable_turnover_ratio
        if accounts_payable_turnover_ratio is not UNSET:
            field_dict["accountsPayableTurnoverRatio"] = accounts_payable_turnover_ratio
        if days_payable_outstanding is not UNSET:
            field_dict["daysPayableOutstanding"] = days_payable_outstanding
        if days_sales_outstanding is not UNSET:
            field_dict["daysSalesOutstanding"] = days_sales_outstanding
        if average_outstanding_payables_balance is not UNSET:
            field_dict["averageOutstandingPayablesBalance"] = average_outstanding_payables_balance
        if average_outstanding_receivables_balance is not UNSET:
            field_dict["averageOutstandingReceivablesBalance"] = average_outstanding_receivables_balance
        if churn_rate is not UNSET:
            field_dict["churnRate"] = churn_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gross_burn_rate = d.pop("grossBurnRate", UNSET)

        inventory_turnover_ratio = d.pop("inventoryTurnoverRatio", UNSET)

        asset_turnover_ratio = d.pop("assetTurnoverRatio", UNSET)

        payables_conversion_period = d.pop("payablesConversionPeriod", UNSET)

        accounts_receivable_turnover_ratio = d.pop("accountsReceivableTurnoverRatio", UNSET)

        accounts_payable_turnover_ratio = d.pop("accountsPayableTurnoverRatio", UNSET)

        days_payable_outstanding = d.pop("daysPayableOutstanding", UNSET)

        days_sales_outstanding = d.pop("daysSalesOutstanding", UNSET)

        average_outstanding_payables_balance = d.pop("averageOutstandingPayablesBalance", UNSET)

        average_outstanding_receivables_balance = d.pop("averageOutstandingReceivablesBalance", UNSET)

        churn_rate = d.pop("churnRate", UNSET)

        financial_ratios_efficiency_data = cls(
            gross_burn_rate=gross_burn_rate,
            inventory_turnover_ratio=inventory_turnover_ratio,
            asset_turnover_ratio=asset_turnover_ratio,
            payables_conversion_period=payables_conversion_period,
            accounts_receivable_turnover_ratio=accounts_receivable_turnover_ratio,
            accounts_payable_turnover_ratio=accounts_payable_turnover_ratio,
            days_payable_outstanding=days_payable_outstanding,
            days_sales_outstanding=days_sales_outstanding,
            average_outstanding_payables_balance=average_outstanding_payables_balance,
            average_outstanding_receivables_balance=average_outstanding_receivables_balance,
            churn_rate=churn_rate,
        )

        financial_ratios_efficiency_data.additional_properties = d
        return financial_ratios_efficiency_data

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
