from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_financial_ratios_response_200_data_credit import ReportFinancialRatiosResponse200DataCredit
    from ..models.report_financial_ratios_response_200_data_efficiency import (
        ReportFinancialRatiosResponse200DataEfficiency,
    )
    from ..models.report_financial_ratios_response_200_data_leverage import ReportFinancialRatiosResponse200DataLeverage
    from ..models.report_financial_ratios_response_200_data_liquidity import (
        ReportFinancialRatiosResponse200DataLiquidity,
    )
    from ..models.report_financial_ratios_response_200_data_profitability import (
        ReportFinancialRatiosResponse200DataProfitability,
    )


T = TypeVar("T", bound="ReportFinancialRatiosResponse200Data")


@_attrs_define
class ReportFinancialRatiosResponse200Data:
    """
    Attributes:
        credit (Union[Unset, ReportFinancialRatiosResponse200DataCredit]):
        efficiency (Union[Unset, ReportFinancialRatiosResponse200DataEfficiency]):
        leverage (Union[Unset, ReportFinancialRatiosResponse200DataLeverage]):
        liquidity (Union[Unset, ReportFinancialRatiosResponse200DataLiquidity]):
        profitability (Union[Unset, ReportFinancialRatiosResponse200DataProfitability]):
    """

    credit: Union[Unset, "ReportFinancialRatiosResponse200DataCredit"] = UNSET
    efficiency: Union[Unset, "ReportFinancialRatiosResponse200DataEfficiency"] = UNSET
    leverage: Union[Unset, "ReportFinancialRatiosResponse200DataLeverage"] = UNSET
    liquidity: Union[Unset, "ReportFinancialRatiosResponse200DataLiquidity"] = UNSET
    profitability: Union[Unset, "ReportFinancialRatiosResponse200DataProfitability"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credit, Unset):
            credit = self.credit.to_dict()

        efficiency: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.efficiency, Unset):
            efficiency = self.efficiency.to_dict()

        leverage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leverage, Unset):
            leverage = self.leverage.to_dict()

        liquidity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.liquidity, Unset):
            liquidity = self.liquidity.to_dict()

        profitability: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profitability, Unset):
            profitability = self.profitability.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit is not UNSET:
            field_dict["credit"] = credit
        if efficiency is not UNSET:
            field_dict["efficiency"] = efficiency
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity
        if profitability is not UNSET:
            field_dict["profitability"] = profitability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_financial_ratios_response_200_data_credit import ReportFinancialRatiosResponse200DataCredit
        from ..models.report_financial_ratios_response_200_data_efficiency import (
            ReportFinancialRatiosResponse200DataEfficiency,
        )
        from ..models.report_financial_ratios_response_200_data_leverage import (
            ReportFinancialRatiosResponse200DataLeverage,
        )
        from ..models.report_financial_ratios_response_200_data_liquidity import (
            ReportFinancialRatiosResponse200DataLiquidity,
        )
        from ..models.report_financial_ratios_response_200_data_profitability import (
            ReportFinancialRatiosResponse200DataProfitability,
        )

        d = src_dict.copy()
        _credit = d.pop("credit", UNSET)
        credit: Union[Unset, ReportFinancialRatiosResponse200DataCredit]
        if isinstance(_credit, Unset):
            credit = UNSET
        else:
            credit = ReportFinancialRatiosResponse200DataCredit.from_dict(_credit)

        _efficiency = d.pop("efficiency", UNSET)
        efficiency: Union[Unset, ReportFinancialRatiosResponse200DataEfficiency]
        if isinstance(_efficiency, Unset):
            efficiency = UNSET
        else:
            efficiency = ReportFinancialRatiosResponse200DataEfficiency.from_dict(_efficiency)

        _leverage = d.pop("leverage", UNSET)
        leverage: Union[Unset, ReportFinancialRatiosResponse200DataLeverage]
        if isinstance(_leverage, Unset):
            leverage = UNSET
        else:
            leverage = ReportFinancialRatiosResponse200DataLeverage.from_dict(_leverage)

        _liquidity = d.pop("liquidity", UNSET)
        liquidity: Union[Unset, ReportFinancialRatiosResponse200DataLiquidity]
        if isinstance(_liquidity, Unset):
            liquidity = UNSET
        else:
            liquidity = ReportFinancialRatiosResponse200DataLiquidity.from_dict(_liquidity)

        _profitability = d.pop("profitability", UNSET)
        profitability: Union[Unset, ReportFinancialRatiosResponse200DataProfitability]
        if isinstance(_profitability, Unset):
            profitability = UNSET
        else:
            profitability = ReportFinancialRatiosResponse200DataProfitability.from_dict(_profitability)

        report_financial_ratios_response_200_data = cls(
            credit=credit,
            efficiency=efficiency,
            leverage=leverage,
            liquidity=liquidity,
            profitability=profitability,
        )

        report_financial_ratios_response_200_data.additional_properties = d
        return report_financial_ratios_response_200_data

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
