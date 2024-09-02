from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.report_cashflow_statements_response_200_data_item_period import (
        ReportCashflowStatementsResponse200DataItemPeriod,
    )


T = TypeVar("T", bound="ReportCashflowStatementsResponse200DataItem")


@_attrs_define
class ReportCashflowStatementsResponse200DataItem:
    """
    Attributes:
        period (ReportCashflowStatementsResponse200DataItemPeriod):
        operating_activities (float):  Example: 345.
        financing_activities (float):  Example: 345.
        investing_activities (float):  Example: 345.
        net_cash (float):  Example: 345.
    """

    period: "ReportCashflowStatementsResponse200DataItemPeriod"
    operating_activities: float
    financing_activities: float
    investing_activities: float
    net_cash: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period.to_dict()

        operating_activities = self.operating_activities

        financing_activities = self.financing_activities

        investing_activities = self.investing_activities

        net_cash = self.net_cash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "operatingActivities": operating_activities,
                "financingActivities": financing_activities,
                "investingActivities": investing_activities,
                "netCash": net_cash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_cashflow_statements_response_200_data_item_period import (
            ReportCashflowStatementsResponse200DataItemPeriod,
        )

        d = src_dict.copy()
        period = ReportCashflowStatementsResponse200DataItemPeriod.from_dict(d.pop("period"))

        operating_activities = d.pop("operatingActivities")

        financing_activities = d.pop("financingActivities")

        investing_activities = d.pop("investingActivities")

        net_cash = d.pop("netCash")

        report_cashflow_statements_response_200_data_item = cls(
            period=period,
            operating_activities=operating_activities,
            financing_activities=financing_activities,
            investing_activities=investing_activities,
            net_cash=net_cash,
        )

        report_cashflow_statements_response_200_data_item.additional_properties = d
        return report_cashflow_statements_response_200_data_item

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
