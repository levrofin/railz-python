import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PortfolioMetricsReportMetaData")


@_attrs_define
class PortfolioMetricsReportMetaData:
    """
    Attributes:
        start_date (datetime.datetime):  Example: 2020-11-01T01:02:03Z.
        end_date (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
        report_frequency (str):  Example: month.
        created_at (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
    """

    start_date: datetime.datetime
    end_date: datetime.datetime
    report_frequency: str
    created_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        report_frequency = self.report_frequency

        created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startDate": start_date,
                "endDate": end_date,
                "reportFrequency": report_frequency,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        report_frequency = d.pop("reportFrequency")

        created_at = isoparse(d.pop("createdAt"))

        portfolio_metrics_report_meta_data = cls(
            start_date=start_date,
            end_date=end_date,
            report_frequency=report_frequency,
            created_at=created_at,
        )

        portfolio_metrics_report_meta_data.additional_properties = d
        return portfolio_metrics_report_meta_data

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
