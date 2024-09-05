from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_financial_ratios_response_200_meta_report_frequency import (
    ReportFinancialRatiosResponse200MetaReportFrequency,
    check_report_financial_ratios_response_200_meta_report_frequency,
)
from ..models.report_financial_ratios_response_200_meta_service_name import (
    ReportFinancialRatiosResponse200MetaServiceName,
    check_report_financial_ratios_response_200_meta_service_name,
)

T = TypeVar("T", bound="ReportFinancialRatiosResponse200Meta")


@_attrs_define
class ReportFinancialRatiosResponse200Meta:
    """
    Attributes:
        report_id (List[str]):  Example: ['5fad8a342a88364234392fb5'].
        service_name (ReportFinancialRatiosResponse200MetaServiceName):  Example: xero.
        business_name (str):  Example: Railz.
        end_date (str): if report frequency is monthly, end date is maximum of 12 months from start date, if quaterly,
            its a maximum of 3 years from start date, if yearly, its maximum of 12 years from start date Example:
            2020-12-25T01:02:03Z.
        start_date (str):  Example: 2020-11-25T01:02:03Z.
        report_frequency (ReportFinancialRatiosResponse200MetaReportFrequency):  Example: month.
    """

    report_id: List[str]
    service_name: ReportFinancialRatiosResponse200MetaServiceName
    business_name: str
    end_date: str
    start_date: str
    report_frequency: ReportFinancialRatiosResponse200MetaReportFrequency
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_id = self.report_id

        service_name: str = self.service_name

        business_name = self.business_name

        end_date = self.end_date

        start_date = self.start_date

        report_frequency: str = self.report_frequency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportId": report_id,
                "serviceName": service_name,
                "businessName": business_name,
                "endDate": end_date,
                "startDate": start_date,
                "reportFrequency": report_frequency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        report_id = cast(List[str], d.pop("reportId"))

        service_name = check_report_financial_ratios_response_200_meta_service_name(d.pop("serviceName"))

        business_name = d.pop("businessName")

        end_date = d.pop("endDate")

        start_date = d.pop("startDate")

        report_frequency = check_report_financial_ratios_response_200_meta_report_frequency(d.pop("reportFrequency"))

        report_financial_ratios_response_200_meta = cls(
            report_id=report_id,
            service_name=service_name,
            business_name=business_name,
            end_date=end_date,
            start_date=start_date,
            report_frequency=report_frequency,
        )

        report_financial_ratios_response_200_meta.additional_properties = d
        return report_financial_ratios_response_200_meta

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
