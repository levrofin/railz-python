from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_financial_ratios_response_200_data_liquidity_absolute_liquidity import (
        ReportFinancialRatiosResponse200DataLiquidityAbsoluteLiquidity,
    )
    from ..models.report_financial_ratios_response_200_data_liquidity_cash_ratio import (
        ReportFinancialRatiosResponse200DataLiquidityCashRatio,
    )
    from ..models.report_financial_ratios_response_200_data_liquidity_current_ratio import (
        ReportFinancialRatiosResponse200DataLiquidityCurrentRatio,
    )
    from ..models.report_financial_ratios_response_200_data_liquidity_free_cashflow_ratio import (
        ReportFinancialRatiosResponse200DataLiquidityFreeCashflowRatio,
    )
    from ..models.report_financial_ratios_response_200_data_liquidity_gross_burn import (
        ReportFinancialRatiosResponse200DataLiquidityGrossBurn,
    )
    from ..models.report_financial_ratios_response_200_data_liquidity_quick_ratio import (
        ReportFinancialRatiosResponse200DataLiquidityQuickRatio,
    )
    from ..models.report_financial_ratios_response_200_data_liquidity_runway import (
        ReportFinancialRatiosResponse200DataLiquidityRunway,
    )


T = TypeVar("T", bound="ReportFinancialRatiosResponse200DataLiquidity")


@_attrs_define
class ReportFinancialRatiosResponse200DataLiquidity:
    """
    Attributes:
        quick_ratio (Union[Unset, ReportFinancialRatiosResponse200DataLiquidityQuickRatio]):
        absolute_liquidity (Union[Unset, ReportFinancialRatiosResponse200DataLiquidityAbsoluteLiquidity]):
        current_ratio (Union[Unset, ReportFinancialRatiosResponse200DataLiquidityCurrentRatio]):
        gross_burn (Union[Unset, ReportFinancialRatiosResponse200DataLiquidityGrossBurn]):
        runway (Union[Unset, ReportFinancialRatiosResponse200DataLiquidityRunway]):
        cash_ratio (Union[Unset, ReportFinancialRatiosResponse200DataLiquidityCashRatio]):
        free_cashflow_ratio (Union[Unset, ReportFinancialRatiosResponse200DataLiquidityFreeCashflowRatio]):
    """

    quick_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataLiquidityQuickRatio"] = UNSET
    absolute_liquidity: Union[Unset, "ReportFinancialRatiosResponse200DataLiquidityAbsoluteLiquidity"] = UNSET
    current_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataLiquidityCurrentRatio"] = UNSET
    gross_burn: Union[Unset, "ReportFinancialRatiosResponse200DataLiquidityGrossBurn"] = UNSET
    runway: Union[Unset, "ReportFinancialRatiosResponse200DataLiquidityRunway"] = UNSET
    cash_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataLiquidityCashRatio"] = UNSET
    free_cashflow_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataLiquidityFreeCashflowRatio"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quick_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quick_ratio, Unset):
            quick_ratio = self.quick_ratio.to_dict()

        absolute_liquidity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.absolute_liquidity, Unset):
            absolute_liquidity = self.absolute_liquidity.to_dict()

        current_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_ratio, Unset):
            current_ratio = self.current_ratio.to_dict()

        gross_burn: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gross_burn, Unset):
            gross_burn = self.gross_burn.to_dict()

        runway: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.runway, Unset):
            runway = self.runway.to_dict()

        cash_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cash_ratio, Unset):
            cash_ratio = self.cash_ratio.to_dict()

        free_cashflow_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.free_cashflow_ratio, Unset):
            free_cashflow_ratio = self.free_cashflow_ratio.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quick_ratio is not UNSET:
            field_dict["quickRatio"] = quick_ratio
        if absolute_liquidity is not UNSET:
            field_dict["absoluteLiquidity"] = absolute_liquidity
        if current_ratio is not UNSET:
            field_dict["currentRatio"] = current_ratio
        if gross_burn is not UNSET:
            field_dict["grossBurn"] = gross_burn
        if runway is not UNSET:
            field_dict["runway"] = runway
        if cash_ratio is not UNSET:
            field_dict["cashRatio"] = cash_ratio
        if free_cashflow_ratio is not UNSET:
            field_dict["freeCashflowRatio"] = free_cashflow_ratio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_financial_ratios_response_200_data_liquidity_absolute_liquidity import (
            ReportFinancialRatiosResponse200DataLiquidityAbsoluteLiquidity,
        )
        from ..models.report_financial_ratios_response_200_data_liquidity_cash_ratio import (
            ReportFinancialRatiosResponse200DataLiquidityCashRatio,
        )
        from ..models.report_financial_ratios_response_200_data_liquidity_current_ratio import (
            ReportFinancialRatiosResponse200DataLiquidityCurrentRatio,
        )
        from ..models.report_financial_ratios_response_200_data_liquidity_free_cashflow_ratio import (
            ReportFinancialRatiosResponse200DataLiquidityFreeCashflowRatio,
        )
        from ..models.report_financial_ratios_response_200_data_liquidity_gross_burn import (
            ReportFinancialRatiosResponse200DataLiquidityGrossBurn,
        )
        from ..models.report_financial_ratios_response_200_data_liquidity_quick_ratio import (
            ReportFinancialRatiosResponse200DataLiquidityQuickRatio,
        )
        from ..models.report_financial_ratios_response_200_data_liquidity_runway import (
            ReportFinancialRatiosResponse200DataLiquidityRunway,
        )

        d = src_dict.copy()
        _quick_ratio = d.pop("quickRatio", UNSET)
        quick_ratio: Union[Unset, ReportFinancialRatiosResponse200DataLiquidityQuickRatio]
        if isinstance(_quick_ratio, Unset):
            quick_ratio = UNSET
        else:
            quick_ratio = ReportFinancialRatiosResponse200DataLiquidityQuickRatio.from_dict(_quick_ratio)

        _absolute_liquidity = d.pop("absoluteLiquidity", UNSET)
        absolute_liquidity: Union[Unset, ReportFinancialRatiosResponse200DataLiquidityAbsoluteLiquidity]
        if isinstance(_absolute_liquidity, Unset):
            absolute_liquidity = UNSET
        else:
            absolute_liquidity = ReportFinancialRatiosResponse200DataLiquidityAbsoluteLiquidity.from_dict(
                _absolute_liquidity
            )

        _current_ratio = d.pop("currentRatio", UNSET)
        current_ratio: Union[Unset, ReportFinancialRatiosResponse200DataLiquidityCurrentRatio]
        if isinstance(_current_ratio, Unset):
            current_ratio = UNSET
        else:
            current_ratio = ReportFinancialRatiosResponse200DataLiquidityCurrentRatio.from_dict(_current_ratio)

        _gross_burn = d.pop("grossBurn", UNSET)
        gross_burn: Union[Unset, ReportFinancialRatiosResponse200DataLiquidityGrossBurn]
        if isinstance(_gross_burn, Unset):
            gross_burn = UNSET
        else:
            gross_burn = ReportFinancialRatiosResponse200DataLiquidityGrossBurn.from_dict(_gross_burn)

        _runway = d.pop("runway", UNSET)
        runway: Union[Unset, ReportFinancialRatiosResponse200DataLiquidityRunway]
        if isinstance(_runway, Unset):
            runway = UNSET
        else:
            runway = ReportFinancialRatiosResponse200DataLiquidityRunway.from_dict(_runway)

        _cash_ratio = d.pop("cashRatio", UNSET)
        cash_ratio: Union[Unset, ReportFinancialRatiosResponse200DataLiquidityCashRatio]
        if isinstance(_cash_ratio, Unset):
            cash_ratio = UNSET
        else:
            cash_ratio = ReportFinancialRatiosResponse200DataLiquidityCashRatio.from_dict(_cash_ratio)

        _free_cashflow_ratio = d.pop("freeCashflowRatio", UNSET)
        free_cashflow_ratio: Union[Unset, ReportFinancialRatiosResponse200DataLiquidityFreeCashflowRatio]
        if isinstance(_free_cashflow_ratio, Unset):
            free_cashflow_ratio = UNSET
        else:
            free_cashflow_ratio = ReportFinancialRatiosResponse200DataLiquidityFreeCashflowRatio.from_dict(
                _free_cashflow_ratio
            )

        report_financial_ratios_response_200_data_liquidity = cls(
            quick_ratio=quick_ratio,
            absolute_liquidity=absolute_liquidity,
            current_ratio=current_ratio,
            gross_burn=gross_burn,
            runway=runway,
            cash_ratio=cash_ratio,
            free_cashflow_ratio=free_cashflow_ratio,
        )

        report_financial_ratios_response_200_data_liquidity.additional_properties = d
        return report_financial_ratios_response_200_data_liquidity

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
