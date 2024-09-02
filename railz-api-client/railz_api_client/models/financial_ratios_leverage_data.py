from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialRatiosLeverageData")


@_attrs_define
class FinancialRatiosLeverageData:
    """
    Attributes:
        equity_to_lt_assets (Union[Unset, float]):  Example: 0.26784885.
        short_debt_to_equity_ratio (Union[Unset, float]):  Example: 0.87117832.
        debt_to_equity_ratio (Union[Unset, float]):  Example: 1.03899521.
        interest_bank_loan (Union[Unset, float]):  Example: 1.03899521.
        interest_coverage_ratio (Union[Unset, float]):  Example: 3.48778221.
        debt_to_assets_ratio (Union[Unset, float]):  Example: 0.89995561.
        debt_service_coverage_ratio (Union[Unset, float]):  Example: 4.20509522.
        leverage_index (Union[Unset, float]):  Example: 0.878.
        leverage_ratio (Union[Unset, float]):  Example: 0.067.
    """

    equity_to_lt_assets: Union[Unset, float] = UNSET
    short_debt_to_equity_ratio: Union[Unset, float] = UNSET
    debt_to_equity_ratio: Union[Unset, float] = UNSET
    interest_bank_loan: Union[Unset, float] = UNSET
    interest_coverage_ratio: Union[Unset, float] = UNSET
    debt_to_assets_ratio: Union[Unset, float] = UNSET
    debt_service_coverage_ratio: Union[Unset, float] = UNSET
    leverage_index: Union[Unset, float] = UNSET
    leverage_ratio: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        equity_to_lt_assets = self.equity_to_lt_assets

        short_debt_to_equity_ratio = self.short_debt_to_equity_ratio

        debt_to_equity_ratio = self.debt_to_equity_ratio

        interest_bank_loan = self.interest_bank_loan

        interest_coverage_ratio = self.interest_coverage_ratio

        debt_to_assets_ratio = self.debt_to_assets_ratio

        debt_service_coverage_ratio = self.debt_service_coverage_ratio

        leverage_index = self.leverage_index

        leverage_ratio = self.leverage_ratio

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if equity_to_lt_assets is not UNSET:
            field_dict["equityToLTAssets"] = equity_to_lt_assets
        if short_debt_to_equity_ratio is not UNSET:
            field_dict["shortDebtToEquityRatio"] = short_debt_to_equity_ratio
        if debt_to_equity_ratio is not UNSET:
            field_dict["debtToEquityRatio"] = debt_to_equity_ratio
        if interest_bank_loan is not UNSET:
            field_dict["interestBankLoan"] = interest_bank_loan
        if interest_coverage_ratio is not UNSET:
            field_dict["interestCoverageRatio"] = interest_coverage_ratio
        if debt_to_assets_ratio is not UNSET:
            field_dict["debtToAssetsRatio"] = debt_to_assets_ratio
        if debt_service_coverage_ratio is not UNSET:
            field_dict["debtServiceCoverageRatio"] = debt_service_coverage_ratio
        if leverage_index is not UNSET:
            field_dict["leverageIndex"] = leverage_index
        if leverage_ratio is not UNSET:
            field_dict["leverageRatio"] = leverage_ratio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        equity_to_lt_assets = d.pop("equityToLTAssets", UNSET)

        short_debt_to_equity_ratio = d.pop("shortDebtToEquityRatio", UNSET)

        debt_to_equity_ratio = d.pop("debtToEquityRatio", UNSET)

        interest_bank_loan = d.pop("interestBankLoan", UNSET)

        interest_coverage_ratio = d.pop("interestCoverageRatio", UNSET)

        debt_to_assets_ratio = d.pop("debtToAssetsRatio", UNSET)

        debt_service_coverage_ratio = d.pop("debtServiceCoverageRatio", UNSET)

        leverage_index = d.pop("leverageIndex", UNSET)

        leverage_ratio = d.pop("leverageRatio", UNSET)

        financial_ratios_leverage_data = cls(
            equity_to_lt_assets=equity_to_lt_assets,
            short_debt_to_equity_ratio=short_debt_to_equity_ratio,
            debt_to_equity_ratio=debt_to_equity_ratio,
            interest_bank_loan=interest_bank_loan,
            interest_coverage_ratio=interest_coverage_ratio,
            debt_to_assets_ratio=debt_to_assets_ratio,
            debt_service_coverage_ratio=debt_service_coverage_ratio,
            leverage_index=leverage_index,
            leverage_ratio=leverage_ratio,
        )

        financial_ratios_leverage_data.additional_properties = d
        return financial_ratios_leverage_data

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
