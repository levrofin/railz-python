from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_balance_sheets_response_200_data_item_period import (
        ReportBalanceSheetsResponse200DataItemPeriod,
    )


T = TypeVar("T", bound="ReportBalanceSheetsResponse200DataItem")


@_attrs_define
class ReportBalanceSheetsResponse200DataItem:
    """
    Attributes:
        period (ReportBalanceSheetsResponse200DataItemPeriod):
        equity (float):  Example: 345.
        current_assets (Union[Unset, float]):  Example: 345.
        non_current_assets (Union[Unset, float]):  Example: 345.
        current_liabilities (Union[Unset, float]):  Example: 345.
        non_current_liabilities (Union[Unset, float]):  Example: 345.
    """

    period: "ReportBalanceSheetsResponse200DataItemPeriod"
    equity: float
    current_assets: Union[Unset, float] = UNSET
    non_current_assets: Union[Unset, float] = UNSET
    current_liabilities: Union[Unset, float] = UNSET
    non_current_liabilities: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period.to_dict()

        equity = self.equity

        current_assets = self.current_assets

        non_current_assets = self.non_current_assets

        current_liabilities = self.current_liabilities

        non_current_liabilities = self.non_current_liabilities

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "equity": equity,
            }
        )
        if current_assets is not UNSET:
            field_dict["currentAssets"] = current_assets
        if non_current_assets is not UNSET:
            field_dict["nonCurrentAssets"] = non_current_assets
        if current_liabilities is not UNSET:
            field_dict["currentLiabilities"] = current_liabilities
        if non_current_liabilities is not UNSET:
            field_dict["nonCurrentLiabilities"] = non_current_liabilities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_balance_sheets_response_200_data_item_period import (
            ReportBalanceSheetsResponse200DataItemPeriod,
        )

        d = src_dict.copy()
        period = ReportBalanceSheetsResponse200DataItemPeriod.from_dict(d.pop("period"))

        equity = d.pop("equity")

        current_assets = d.pop("currentAssets", UNSET)

        non_current_assets = d.pop("nonCurrentAssets", UNSET)

        current_liabilities = d.pop("currentLiabilities", UNSET)

        non_current_liabilities = d.pop("nonCurrentLiabilities", UNSET)

        report_balance_sheets_response_200_data_item = cls(
            period=period,
            equity=equity,
            current_assets=current_assets,
            non_current_assets=non_current_assets,
            current_liabilities=current_liabilities,
            non_current_liabilities=non_current_liabilities,
        )

        report_balance_sheets_response_200_data_item.additional_properties = d
        return report_balance_sheets_response_200_data_item

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
