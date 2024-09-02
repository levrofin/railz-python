from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.financial_fraud_risk_report_v2 import FinancialFraudRiskReportV2


T = TypeVar("T", bound="FinancialFraudRiskResponseV2Dto")


@_attrs_define
class FinancialFraudRiskResponseV2Dto:
    """
    Attributes:
        count (float):  Example: 1.
        reports (List['FinancialFraudRiskReportV2']):
    """

    count: float
    reports: List["FinancialFraudRiskReportV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        reports = []
        for reports_item_data in self.reports:
            reports_item = reports_item_data.to_dict()
            reports.append(reports_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "reports": reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.financial_fraud_risk_report_v2 import FinancialFraudRiskReportV2

        d = src_dict.copy()
        count = d.pop("count")

        reports = []
        _reports = d.pop("reports")
        for reports_item_data in _reports:
            reports_item = FinancialFraudRiskReportV2.from_dict(reports_item_data)

            reports.append(reports_item)

        financial_fraud_risk_response_v2_dto = cls(
            count=count,
            reports=reports,
        )

        financial_fraud_risk_response_v2_dto.additional_properties = d
        return financial_fraud_risk_response_v2_dto

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
