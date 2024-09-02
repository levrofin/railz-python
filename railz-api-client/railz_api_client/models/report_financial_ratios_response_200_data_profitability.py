from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_financial_ratios_response_200_data_profitability_ebitda import (
        ReportFinancialRatiosResponse200DataProfitabilityEbitda,
    )
    from ..models.report_financial_ratios_response_200_data_profitability_ebitda_margin import (
        ReportFinancialRatiosResponse200DataProfitabilityEbitdaMargin,
    )
    from ..models.report_financial_ratios_response_200_data_profitability_free_cash_flow import (
        ReportFinancialRatiosResponse200DataProfitabilityFreeCashFlow,
    )
    from ..models.report_financial_ratios_response_200_data_profitability_gross_margin import (
        ReportFinancialRatiosResponse200DataProfitabilityGrossMargin,
    )
    from ..models.report_financial_ratios_response_200_data_profitability_net_profit_margin import (
        ReportFinancialRatiosResponse200DataProfitabilityNetProfitMargin,
    )
    from ..models.report_financial_ratios_response_200_data_profitability_operating_margin import (
        ReportFinancialRatiosResponse200DataProfitabilityOperatingMargin,
    )
    from ..models.report_financial_ratios_response_200_data_profitability_return_on_assets import (
        ReportFinancialRatiosResponse200DataProfitabilityReturnOnAssets,
    )
    from ..models.report_financial_ratios_response_200_data_profitability_return_on_equity import (
        ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquity,
    )
    from ..models.report_financial_ratios_response_200_data_profitability_revenue_concentration_index import (
        ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndex,
    )
    from ..models.report_financial_ratios_response_200_data_profitability_working_capital import (
        ReportFinancialRatiosResponse200DataProfitabilityWorkingCapital,
    )


T = TypeVar("T", bound="ReportFinancialRatiosResponse200DataProfitability")


@_attrs_define
class ReportFinancialRatiosResponse200DataProfitability:
    """
    Attributes:
        return_on_assets (Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityReturnOnAssets]):
        ebitda (Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityEbitda]):
        ebitda_margin (Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityEbitdaMargin]):
        working_capital (Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityWorkingCapital]):
        free_cash_flow (Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityFreeCashFlow]):
        gross_margin (Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityGrossMargin]):
        net_profit_margin (Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityNetProfitMargin]):
        operating_margin (Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityOperatingMargin]):
        return_on_equity (Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquity]):
        revenue_concentration_index (Union[Unset,
            ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndex]):
    """

    return_on_assets: Union[Unset, "ReportFinancialRatiosResponse200DataProfitabilityReturnOnAssets"] = UNSET
    ebitda: Union[Unset, "ReportFinancialRatiosResponse200DataProfitabilityEbitda"] = UNSET
    ebitda_margin: Union[Unset, "ReportFinancialRatiosResponse200DataProfitabilityEbitdaMargin"] = UNSET
    working_capital: Union[Unset, "ReportFinancialRatiosResponse200DataProfitabilityWorkingCapital"] = UNSET
    free_cash_flow: Union[Unset, "ReportFinancialRatiosResponse200DataProfitabilityFreeCashFlow"] = UNSET
    gross_margin: Union[Unset, "ReportFinancialRatiosResponse200DataProfitabilityGrossMargin"] = UNSET
    net_profit_margin: Union[Unset, "ReportFinancialRatiosResponse200DataProfitabilityNetProfitMargin"] = UNSET
    operating_margin: Union[Unset, "ReportFinancialRatiosResponse200DataProfitabilityOperatingMargin"] = UNSET
    return_on_equity: Union[Unset, "ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquity"] = UNSET
    revenue_concentration_index: Union[
        Unset, "ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndex"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_on_assets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_on_assets, Unset):
            return_on_assets = self.return_on_assets.to_dict()

        ebitda: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ebitda, Unset):
            ebitda = self.ebitda.to_dict()

        ebitda_margin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ebitda_margin, Unset):
            ebitda_margin = self.ebitda_margin.to_dict()

        working_capital: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.working_capital, Unset):
            working_capital = self.working_capital.to_dict()

        free_cash_flow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.free_cash_flow, Unset):
            free_cash_flow = self.free_cash_flow.to_dict()

        gross_margin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gross_margin, Unset):
            gross_margin = self.gross_margin.to_dict()

        net_profit_margin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.net_profit_margin, Unset):
            net_profit_margin = self.net_profit_margin.to_dict()

        operating_margin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operating_margin, Unset):
            operating_margin = self.operating_margin.to_dict()

        return_on_equity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_on_equity, Unset):
            return_on_equity = self.return_on_equity.to_dict()

        revenue_concentration_index: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revenue_concentration_index, Unset):
            revenue_concentration_index = self.revenue_concentration_index.to_dict()

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_financial_ratios_response_200_data_profitability_ebitda import (
            ReportFinancialRatiosResponse200DataProfitabilityEbitda,
        )
        from ..models.report_financial_ratios_response_200_data_profitability_ebitda_margin import (
            ReportFinancialRatiosResponse200DataProfitabilityEbitdaMargin,
        )
        from ..models.report_financial_ratios_response_200_data_profitability_free_cash_flow import (
            ReportFinancialRatiosResponse200DataProfitabilityFreeCashFlow,
        )
        from ..models.report_financial_ratios_response_200_data_profitability_gross_margin import (
            ReportFinancialRatiosResponse200DataProfitabilityGrossMargin,
        )
        from ..models.report_financial_ratios_response_200_data_profitability_net_profit_margin import (
            ReportFinancialRatiosResponse200DataProfitabilityNetProfitMargin,
        )
        from ..models.report_financial_ratios_response_200_data_profitability_operating_margin import (
            ReportFinancialRatiosResponse200DataProfitabilityOperatingMargin,
        )
        from ..models.report_financial_ratios_response_200_data_profitability_return_on_assets import (
            ReportFinancialRatiosResponse200DataProfitabilityReturnOnAssets,
        )
        from ..models.report_financial_ratios_response_200_data_profitability_return_on_equity import (
            ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquity,
        )
        from ..models.report_financial_ratios_response_200_data_profitability_revenue_concentration_index import (
            ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndex,
        )
        from ..models.report_financial_ratios_response_200_data_profitability_working_capital import (
            ReportFinancialRatiosResponse200DataProfitabilityWorkingCapital,
        )

        d = src_dict.copy()
        _return_on_assets = d.pop("returnOnAssets", UNSET)
        return_on_assets: Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityReturnOnAssets]
        if isinstance(_return_on_assets, Unset):
            return_on_assets = UNSET
        else:
            return_on_assets = ReportFinancialRatiosResponse200DataProfitabilityReturnOnAssets.from_dict(
                _return_on_assets
            )

        _ebitda = d.pop("ebitda", UNSET)
        ebitda: Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityEbitda]
        if isinstance(_ebitda, Unset):
            ebitda = UNSET
        else:
            ebitda = ReportFinancialRatiosResponse200DataProfitabilityEbitda.from_dict(_ebitda)

        _ebitda_margin = d.pop("ebitdaMargin", UNSET)
        ebitda_margin: Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityEbitdaMargin]
        if isinstance(_ebitda_margin, Unset):
            ebitda_margin = UNSET
        else:
            ebitda_margin = ReportFinancialRatiosResponse200DataProfitabilityEbitdaMargin.from_dict(_ebitda_margin)

        _working_capital = d.pop("workingCapital", UNSET)
        working_capital: Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityWorkingCapital]
        if isinstance(_working_capital, Unset):
            working_capital = UNSET
        else:
            working_capital = ReportFinancialRatiosResponse200DataProfitabilityWorkingCapital.from_dict(
                _working_capital
            )

        _free_cash_flow = d.pop("freeCashFlow", UNSET)
        free_cash_flow: Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityFreeCashFlow]
        if isinstance(_free_cash_flow, Unset):
            free_cash_flow = UNSET
        else:
            free_cash_flow = ReportFinancialRatiosResponse200DataProfitabilityFreeCashFlow.from_dict(_free_cash_flow)

        _gross_margin = d.pop("grossMargin", UNSET)
        gross_margin: Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityGrossMargin]
        if isinstance(_gross_margin, Unset):
            gross_margin = UNSET
        else:
            gross_margin = ReportFinancialRatiosResponse200DataProfitabilityGrossMargin.from_dict(_gross_margin)

        _net_profit_margin = d.pop("netProfitMargin", UNSET)
        net_profit_margin: Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityNetProfitMargin]
        if isinstance(_net_profit_margin, Unset):
            net_profit_margin = UNSET
        else:
            net_profit_margin = ReportFinancialRatiosResponse200DataProfitabilityNetProfitMargin.from_dict(
                _net_profit_margin
            )

        _operating_margin = d.pop("operatingMargin", UNSET)
        operating_margin: Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityOperatingMargin]
        if isinstance(_operating_margin, Unset):
            operating_margin = UNSET
        else:
            operating_margin = ReportFinancialRatiosResponse200DataProfitabilityOperatingMargin.from_dict(
                _operating_margin
            )

        _return_on_equity = d.pop("returnOnEquity", UNSET)
        return_on_equity: Union[Unset, ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquity]
        if isinstance(_return_on_equity, Unset):
            return_on_equity = UNSET
        else:
            return_on_equity = ReportFinancialRatiosResponse200DataProfitabilityReturnOnEquity.from_dict(
                _return_on_equity
            )

        _revenue_concentration_index = d.pop("revenueConcentrationIndex", UNSET)
        revenue_concentration_index: Union[
            Unset, ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndex
        ]
        if isinstance(_revenue_concentration_index, Unset):
            revenue_concentration_index = UNSET
        else:
            revenue_concentration_index = (
                ReportFinancialRatiosResponse200DataProfitabilityRevenueConcentrationIndex.from_dict(
                    _revenue_concentration_index
                )
            )

        report_financial_ratios_response_200_data_profitability = cls(
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
        )

        report_financial_ratios_response_200_data_profitability.additional_properties = d
        return report_financial_ratios_response_200_data_profitability

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
