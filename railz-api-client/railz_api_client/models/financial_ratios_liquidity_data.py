from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialRatiosLiquidityData")


@_attrs_define
class FinancialRatiosLiquidityData:
    """
    Attributes:
        quick_ratio (Union[Unset, float]):  Example: 0.88811223.
        absolute_liquidity (Union[Unset, float]):  Example: 530167.93.
        current_ratio (Union[Unset, float]):  Example: 1.10856651.
        gross_burn (Union[Unset, float]):  Example: 382071.92.
        runway (Union[Unset, float]):  Example: 12.84898122.
        cash_ratio (Union[Unset, float]):  Example: 0.73314452.
        free_cashflow_ratio (Union[Unset, float]):  Example: 0.45151529.
        cash_flow_coverage_ratio (Union[Unset, float]):  Example: 0.09030305.
    """

    quick_ratio: Union[Unset, float] = UNSET
    absolute_liquidity: Union[Unset, float] = UNSET
    current_ratio: Union[Unset, float] = UNSET
    gross_burn: Union[Unset, float] = UNSET
    runway: Union[Unset, float] = UNSET
    cash_ratio: Union[Unset, float] = UNSET
    free_cashflow_ratio: Union[Unset, float] = UNSET
    cash_flow_coverage_ratio: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quick_ratio = self.quick_ratio

        absolute_liquidity = self.absolute_liquidity

        current_ratio = self.current_ratio

        gross_burn = self.gross_burn

        runway = self.runway

        cash_ratio = self.cash_ratio

        free_cashflow_ratio = self.free_cashflow_ratio

        cash_flow_coverage_ratio = self.cash_flow_coverage_ratio

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
        if cash_flow_coverage_ratio is not UNSET:
            field_dict["cashFlowCoverageRatio"] = cash_flow_coverage_ratio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quick_ratio = d.pop("quickRatio", UNSET)

        absolute_liquidity = d.pop("absoluteLiquidity", UNSET)

        current_ratio = d.pop("currentRatio", UNSET)

        gross_burn = d.pop("grossBurn", UNSET)

        runway = d.pop("runway", UNSET)

        cash_ratio = d.pop("cashRatio", UNSET)

        free_cashflow_ratio = d.pop("freeCashflowRatio", UNSET)

        cash_flow_coverage_ratio = d.pop("cashFlowCoverageRatio", UNSET)

        financial_ratios_liquidity_data = cls(
            quick_ratio=quick_ratio,
            absolute_liquidity=absolute_liquidity,
            current_ratio=current_ratio,
            gross_burn=gross_burn,
            runway=runway,
            cash_ratio=cash_ratio,
            free_cashflow_ratio=free_cashflow_ratio,
            cash_flow_coverage_ratio=cash_flow_coverage_ratio,
        )

        financial_ratios_liquidity_data.additional_properties = d
        return financial_ratios_liquidity_data

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
