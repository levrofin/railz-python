from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_financial_ratios_response_200_data_efficiency_asset_turnover_ratio import (
        ReportFinancialRatiosResponse200DataEfficiencyAssetTurnoverRatio,
    )
    from ..models.report_financial_ratios_response_200_data_efficiency_gross_burn_rate import (
        ReportFinancialRatiosResponse200DataEfficiencyGrossBurnRate,
    )
    from ..models.report_financial_ratios_response_200_data_efficiency_inventory_turnover_ratio import (
        ReportFinancialRatiosResponse200DataEfficiencyInventoryTurnoverRatio,
    )


T = TypeVar("T", bound="ReportFinancialRatiosResponse200DataEfficiency")


@_attrs_define
class ReportFinancialRatiosResponse200DataEfficiency:
    """
    Attributes:
        gross_burn_rate (Union[Unset, ReportFinancialRatiosResponse200DataEfficiencyGrossBurnRate]):
        inventory_turnover_ratio (Union[Unset, ReportFinancialRatiosResponse200DataEfficiencyInventoryTurnoverRatio]):
        asset_turnover_ratio (Union[Unset, ReportFinancialRatiosResponse200DataEfficiencyAssetTurnoverRatio]):
    """

    gross_burn_rate: Union[Unset, "ReportFinancialRatiosResponse200DataEfficiencyGrossBurnRate"] = UNSET
    inventory_turnover_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataEfficiencyInventoryTurnoverRatio"] = (
        UNSET
    )
    asset_turnover_ratio: Union[Unset, "ReportFinancialRatiosResponse200DataEfficiencyAssetTurnoverRatio"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gross_burn_rate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gross_burn_rate, Unset):
            gross_burn_rate = self.gross_burn_rate.to_dict()

        inventory_turnover_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_turnover_ratio, Unset):
            inventory_turnover_ratio = self.inventory_turnover_ratio.to_dict()

        asset_turnover_ratio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.asset_turnover_ratio, Unset):
            asset_turnover_ratio = self.asset_turnover_ratio.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gross_burn_rate is not UNSET:
            field_dict["grossBurnRate"] = gross_burn_rate
        if inventory_turnover_ratio is not UNSET:
            field_dict["inventoryTurnoverRatio"] = inventory_turnover_ratio
        if asset_turnover_ratio is not UNSET:
            field_dict["assetTurnoverRatio"] = asset_turnover_ratio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_financial_ratios_response_200_data_efficiency_asset_turnover_ratio import (
            ReportFinancialRatiosResponse200DataEfficiencyAssetTurnoverRatio,
        )
        from ..models.report_financial_ratios_response_200_data_efficiency_gross_burn_rate import (
            ReportFinancialRatiosResponse200DataEfficiencyGrossBurnRate,
        )
        from ..models.report_financial_ratios_response_200_data_efficiency_inventory_turnover_ratio import (
            ReportFinancialRatiosResponse200DataEfficiencyInventoryTurnoverRatio,
        )

        d = src_dict.copy()
        _gross_burn_rate = d.pop("grossBurnRate", UNSET)
        gross_burn_rate: Union[Unset, ReportFinancialRatiosResponse200DataEfficiencyGrossBurnRate]
        if isinstance(_gross_burn_rate, Unset):
            gross_burn_rate = UNSET
        else:
            gross_burn_rate = ReportFinancialRatiosResponse200DataEfficiencyGrossBurnRate.from_dict(_gross_burn_rate)

        _inventory_turnover_ratio = d.pop("inventoryTurnoverRatio", UNSET)
        inventory_turnover_ratio: Union[Unset, ReportFinancialRatiosResponse200DataEfficiencyInventoryTurnoverRatio]
        if isinstance(_inventory_turnover_ratio, Unset):
            inventory_turnover_ratio = UNSET
        else:
            inventory_turnover_ratio = ReportFinancialRatiosResponse200DataEfficiencyInventoryTurnoverRatio.from_dict(
                _inventory_turnover_ratio
            )

        _asset_turnover_ratio = d.pop("assetTurnoverRatio", UNSET)
        asset_turnover_ratio: Union[Unset, ReportFinancialRatiosResponse200DataEfficiencyAssetTurnoverRatio]
        if isinstance(_asset_turnover_ratio, Unset):
            asset_turnover_ratio = UNSET
        else:
            asset_turnover_ratio = ReportFinancialRatiosResponse200DataEfficiencyAssetTurnoverRatio.from_dict(
                _asset_turnover_ratio
            )

        report_financial_ratios_response_200_data_efficiency = cls(
            gross_burn_rate=gross_burn_rate,
            inventory_turnover_ratio=inventory_turnover_ratio,
            asset_turnover_ratio=asset_turnover_ratio,
        )

        report_financial_ratios_response_200_data_efficiency.additional_properties = d
        return report_financial_ratios_response_200_data_efficiency

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
