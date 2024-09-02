from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_ratios_credit_data import FinancialRatiosCreditData
    from ..models.financial_ratios_efficiency_data import FinancialRatiosEfficiencyData
    from ..models.financial_ratios_leverage_data import FinancialRatiosLeverageData
    from ..models.financial_ratios_liquidity_data import FinancialRatiosLiquidityData
    from ..models.financial_ratios_market_data import FinancialRatiosMarketData
    from ..models.financial_ratios_profitability_data import FinancialRatiosProfitabilityData
    from ..models.financial_ratios_reliability_data import FinancialRatiosReliabilityData


T = TypeVar("T", bound="FinancialRatiosData")


@_attrs_define
class FinancialRatiosData:
    """
    Attributes:
        credit (Union[Unset, FinancialRatiosCreditData]):
        efficiency (Union[Unset, FinancialRatiosEfficiencyData]):
        leverage (Union[Unset, FinancialRatiosLeverageData]):
        liquidity (Union[Unset, FinancialRatiosLiquidityData]):
        market (Union[Unset, FinancialRatiosMarketData]):
        profitability (Union[Unset, FinancialRatiosProfitabilityData]):
        reliability (Union[Unset, FinancialRatiosReliabilityData]):
    """

    credit: Union[Unset, "FinancialRatiosCreditData"] = UNSET
    efficiency: Union[Unset, "FinancialRatiosEfficiencyData"] = UNSET
    leverage: Union[Unset, "FinancialRatiosLeverageData"] = UNSET
    liquidity: Union[Unset, "FinancialRatiosLiquidityData"] = UNSET
    market: Union[Unset, "FinancialRatiosMarketData"] = UNSET
    profitability: Union[Unset, "FinancialRatiosProfitabilityData"] = UNSET
    reliability: Union[Unset, "FinancialRatiosReliabilityData"] = UNSET
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

        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        profitability: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profitability, Unset):
            profitability = self.profitability.to_dict()

        reliability: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reliability, Unset):
            reliability = self.reliability.to_dict()

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
        if market is not UNSET:
            field_dict["market"] = market
        if profitability is not UNSET:
            field_dict["profitability"] = profitability
        if reliability is not UNSET:
            field_dict["reliability"] = reliability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.financial_ratios_credit_data import FinancialRatiosCreditData
        from ..models.financial_ratios_efficiency_data import FinancialRatiosEfficiencyData
        from ..models.financial_ratios_leverage_data import FinancialRatiosLeverageData
        from ..models.financial_ratios_liquidity_data import FinancialRatiosLiquidityData
        from ..models.financial_ratios_market_data import FinancialRatiosMarketData
        from ..models.financial_ratios_profitability_data import FinancialRatiosProfitabilityData
        from ..models.financial_ratios_reliability_data import FinancialRatiosReliabilityData

        d = src_dict.copy()
        _credit = d.pop("credit", UNSET)
        credit: Union[Unset, FinancialRatiosCreditData]
        if isinstance(_credit, Unset):
            credit = UNSET
        else:
            credit = FinancialRatiosCreditData.from_dict(_credit)

        _efficiency = d.pop("efficiency", UNSET)
        efficiency: Union[Unset, FinancialRatiosEfficiencyData]
        if isinstance(_efficiency, Unset):
            efficiency = UNSET
        else:
            efficiency = FinancialRatiosEfficiencyData.from_dict(_efficiency)

        _leverage = d.pop("leverage", UNSET)
        leverage: Union[Unset, FinancialRatiosLeverageData]
        if isinstance(_leverage, Unset):
            leverage = UNSET
        else:
            leverage = FinancialRatiosLeverageData.from_dict(_leverage)

        _liquidity = d.pop("liquidity", UNSET)
        liquidity: Union[Unset, FinancialRatiosLiquidityData]
        if isinstance(_liquidity, Unset):
            liquidity = UNSET
        else:
            liquidity = FinancialRatiosLiquidityData.from_dict(_liquidity)

        _market = d.pop("market", UNSET)
        market: Union[Unset, FinancialRatiosMarketData]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = FinancialRatiosMarketData.from_dict(_market)

        _profitability = d.pop("profitability", UNSET)
        profitability: Union[Unset, FinancialRatiosProfitabilityData]
        if isinstance(_profitability, Unset):
            profitability = UNSET
        else:
            profitability = FinancialRatiosProfitabilityData.from_dict(_profitability)

        _reliability = d.pop("reliability", UNSET)
        reliability: Union[Unset, FinancialRatiosReliabilityData]
        if isinstance(_reliability, Unset):
            reliability = UNSET
        else:
            reliability = FinancialRatiosReliabilityData.from_dict(_reliability)

        financial_ratios_data = cls(
            credit=credit,
            efficiency=efficiency,
            leverage=leverage,
            liquidity=liquidity,
            market=market,
            profitability=profitability,
            reliability=reliability,
        )

        financial_ratios_data.additional_properties = d
        return financial_ratios_data

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
