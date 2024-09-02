from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_financial_ratios_response_200_data_leverage_debt_service_coverage_ratio import (
        ReportFinancialRatiosResponse200DataLeverageDebtServiceCoverageRatio,
    )
    from ..models.report_financial_ratios_response_200_data_leverage_debt_to_assets_ratio import (
        ReportFinancialRatiosResponse200DataLeverageDebtToAssetsRatio,
    )
    from ..models.report_financial_ratios_response_200_data_leverage_debt_to_equity_ratio import (
        ReportFinancialRatiosResponse200DataLeverageDebtToEquityRatio,
    )
    from ..models.report_financial_ratios_response_200_data_leverage_equity_to_lt_assets import (
        ReportFinancialRatiosResponse200DataLeverageEquityToLTAssets,
    )
    from ..models.report_financial_ratios_response_200_data_leverage_interest_bank_loan import (
        ReportFinancialRatiosResponse200DataLeverageInterestBankLoan,
    )
    from ..models.report_financial_ratios_response_200_data_leverage_interest_coverage_ratio import (
        ReportFinancialRatiosResponse200DataLeverageInterestCoverageRatio,
    )
    from ..models.report_financial_ratios_response_200_data_leverage_short_debt_to_equity_ratio import (
        ReportFinancialRatiosResponse200DataLeverageShortDebtToEquityRatio,
    )


T = TypeVar("T", bound="ReportFinancialRatiosResponse200DataLeverage")


@_attrs_define
class ReportFinancialRatiosResponse200DataLeverage:
    """
    Attributes:
        equity_to_lt_assets (Union[Unset, ReportFinancialRatiosResponse200DataLeverageEquityToLTAssets]):
        short_debt_to_equity_ratio (Union[Unset, ReportFinancialRatiosResponse200DataLeverageShortDebtToEquityRatio]):
        debt_to_equity_ratio (Union[Unset, ReportFinancialRatiosResponse200DataLeverageDebtToEquityRatio]):
        interest_bank_loan (Union[Unset, ReportFinancialRatiosResponse200DataLeverageInterestBankLoan]):
        interest_coverage_ratio (Union[Unset, ReportFinancialRatiosResponse200DataLeverageInterestCoverageRatio]):
        debt_to_assets_ratio (Union[Unset, ReportFinancialRatiosResponse200DataLeverageDebtToAssetsRatio]):
        debt_service_coverage_ratio (Union[Unset,
            ReportFinancialRatiosResponse200DataLeverageDebtServiceCoverageRatio]):
    """

    equity_to_lt_assets: Union[Unset, "ReportFinancialRatiosResponse200DataLeverageEquityToLTAssets"] = UNSET
    short_debt_to_equity_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataLeverageShortDebtToEquityRatio"] = (
        UNSET
    )
    debt_to_equity_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataLeverageDebtToEquityRatio"] = UNSET
    interest_bank_loan: Union[Unset, "ReportFinancialRatiosResponse200DataLeverageInterestBankLoan"] = UNSET
    interest_coverage_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataLeverageInterestCoverageRatio"] = UNSET
    debt_to_assets_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataLeverageDebtToAssetsRatio"] = UNSET
    debt_service_coverage_ratio: Union[
        Unset, "ReportFinancialRatiosResponse200DataLeverageDebtServiceCoverageRatio"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        equity_to_lt_assets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.equity_to_lt_assets, Unset):
            equity_to_lt_assets = self.equity_to_lt_assets.to_dict()

        short_debt_to_equity_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.short_debt_to_equity_ratio, Unset):
            short_debt_to_equity_ratio = self.short_debt_to_equity_ratio.to_dict()

        debt_to_equity_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.debt_to_equity_ratio, Unset):
            debt_to_equity_ratio = self.debt_to_equity_ratio.to_dict()

        interest_bank_loan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interest_bank_loan, Unset):
            interest_bank_loan = self.interest_bank_loan.to_dict()

        interest_coverage_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interest_coverage_ratio, Unset):
            interest_coverage_ratio = self.interest_coverage_ratio.to_dict()

        debt_to_assets_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.debt_to_assets_ratio, Unset):
            debt_to_assets_ratio = self.debt_to_assets_ratio.to_dict()

        debt_service_coverage_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.debt_service_coverage_ratio, Unset):
            debt_service_coverage_ratio = self.debt_service_coverage_ratio.to_dict()

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_financial_ratios_response_200_data_leverage_debt_service_coverage_ratio import (
            ReportFinancialRatiosResponse200DataLeverageDebtServiceCoverageRatio,
        )
        from ..models.report_financial_ratios_response_200_data_leverage_debt_to_assets_ratio import (
            ReportFinancialRatiosResponse200DataLeverageDebtToAssetsRatio,
        )
        from ..models.report_financial_ratios_response_200_data_leverage_debt_to_equity_ratio import (
            ReportFinancialRatiosResponse200DataLeverageDebtToEquityRatio,
        )
        from ..models.report_financial_ratios_response_200_data_leverage_equity_to_lt_assets import (
            ReportFinancialRatiosResponse200DataLeverageEquityToLTAssets,
        )
        from ..models.report_financial_ratios_response_200_data_leverage_interest_bank_loan import (
            ReportFinancialRatiosResponse200DataLeverageInterestBankLoan,
        )
        from ..models.report_financial_ratios_response_200_data_leverage_interest_coverage_ratio import (
            ReportFinancialRatiosResponse200DataLeverageInterestCoverageRatio,
        )
        from ..models.report_financial_ratios_response_200_data_leverage_short_debt_to_equity_ratio import (
            ReportFinancialRatiosResponse200DataLeverageShortDebtToEquityRatio,
        )

        d = src_dict.copy()
        _equity_to_lt_assets = d.pop("equityToLTAssets", UNSET)
        equity_to_lt_assets: Union[Unset, ReportFinancialRatiosResponse200DataLeverageEquityToLTAssets]
        if isinstance(_equity_to_lt_assets, Unset):
            equity_to_lt_assets = UNSET
        else:
            equity_to_lt_assets = ReportFinancialRatiosResponse200DataLeverageEquityToLTAssets.from_dict(
                _equity_to_lt_assets
            )

        _short_debt_to_equity_ratio = d.pop("shortDebtToEquityRatio", UNSET)
        short_debt_to_equity_ratio: Union[Unset, ReportFinancialRatiosResponse200DataLeverageShortDebtToEquityRatio]
        if isinstance(_short_debt_to_equity_ratio, Unset):
            short_debt_to_equity_ratio = UNSET
        else:
            short_debt_to_equity_ratio = ReportFinancialRatiosResponse200DataLeverageShortDebtToEquityRatio.from_dict(
                _short_debt_to_equity_ratio
            )

        _debt_to_equity_ratio = d.pop("debtToEquityRatio", UNSET)
        debt_to_equity_ratio: Union[Unset, ReportFinancialRatiosResponse200DataLeverageDebtToEquityRatio]
        if isinstance(_debt_to_equity_ratio, Unset):
            debt_to_equity_ratio = UNSET
        else:
            debt_to_equity_ratio = ReportFinancialRatiosResponse200DataLeverageDebtToEquityRatio.from_dict(
                _debt_to_equity_ratio
            )

        _interest_bank_loan = d.pop("interestBankLoan", UNSET)
        interest_bank_loan: Union[Unset, ReportFinancialRatiosResponse200DataLeverageInterestBankLoan]
        if isinstance(_interest_bank_loan, Unset):
            interest_bank_loan = UNSET
        else:
            interest_bank_loan = ReportFinancialRatiosResponse200DataLeverageInterestBankLoan.from_dict(
                _interest_bank_loan
            )

        _interest_coverage_ratio = d.pop("interestCoverageRatio", UNSET)
        interest_coverage_ratio: Union[Unset, ReportFinancialRatiosResponse200DataLeverageInterestCoverageRatio]
        if isinstance(_interest_coverage_ratio, Unset):
            interest_coverage_ratio = UNSET
        else:
            interest_coverage_ratio = ReportFinancialRatiosResponse200DataLeverageInterestCoverageRatio.from_dict(
                _interest_coverage_ratio
            )

        _debt_to_assets_ratio = d.pop("debtToAssetsRatio", UNSET)
        debt_to_assets_ratio: Union[Unset, ReportFinancialRatiosResponse200DataLeverageDebtToAssetsRatio]
        if isinstance(_debt_to_assets_ratio, Unset):
            debt_to_assets_ratio = UNSET
        else:
            debt_to_assets_ratio = ReportFinancialRatiosResponse200DataLeverageDebtToAssetsRatio.from_dict(
                _debt_to_assets_ratio
            )

        _debt_service_coverage_ratio = d.pop("debtServiceCoverageRatio", UNSET)
        debt_service_coverage_ratio: Union[Unset, ReportFinancialRatiosResponse200DataLeverageDebtServiceCoverageRatio]
        if isinstance(_debt_service_coverage_ratio, Unset):
            debt_service_coverage_ratio = UNSET
        else:
            debt_service_coverage_ratio = (
                ReportFinancialRatiosResponse200DataLeverageDebtServiceCoverageRatio.from_dict(
                    _debt_service_coverage_ratio
                )
            )

        report_financial_ratios_response_200_data_leverage = cls(
            equity_to_lt_assets=equity_to_lt_assets,
            short_debt_to_equity_ratio=short_debt_to_equity_ratio,
            debt_to_equity_ratio=debt_to_equity_ratio,
            interest_bank_loan=interest_bank_loan,
            interest_coverage_ratio=interest_coverage_ratio,
            debt_to_assets_ratio=debt_to_assets_ratio,
            debt_service_coverage_ratio=debt_service_coverage_ratio,
        )

        report_financial_ratios_response_200_data_leverage.additional_properties = d
        return report_financial_ratios_response_200_data_leverage

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
