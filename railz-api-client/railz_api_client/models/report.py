from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_current_status import ReportCurrentStatus, check_report_current_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    """
    Attributes:
        start_date (Union[Unset, str]):  Example: 2021-03-01T00:00:00Z.
        end_date (Union[Unset, str]):  Example: 2021-03-31T00:00:00Z.
        last_successful_sync (Union[Unset, str]):  Example: 2021-04-01T00:31:00Z.
        report_frequency (Union[Unset, str]):  Example: month.
        current_status (Union[Unset, ReportCurrentStatus]):  Example: success.
        latest_report_id (Union[Unset, str]):  Example: 6070149d1d685e6cf0583e36.
        latest_successful_report_id (Union[Unset, str]):  Example: 601077f5914dac670966f660.
        accounting_method (Union[Unset, str]):  Example: accrual.
        reconstructed (Union[Unset, bool]):  Example: True.
    """

    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    last_successful_sync: Union[Unset, str] = UNSET
    report_frequency: Union[Unset, str] = UNSET
    current_status: Union[Unset, ReportCurrentStatus] = UNSET
    latest_report_id: Union[Unset, str] = UNSET
    latest_successful_report_id: Union[Unset, str] = UNSET
    accounting_method: Union[Unset, str] = UNSET
    reconstructed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date

        end_date = self.end_date

        last_successful_sync = self.last_successful_sync

        report_frequency = self.report_frequency

        current_status: Union[Unset, str] = UNSET
        if not isinstance(self.current_status, Unset):
            current_status = self.current_status

        latest_report_id = self.latest_report_id

        latest_successful_report_id = self.latest_successful_report_id

        accounting_method = self.accounting_method

        reconstructed = self.reconstructed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if last_successful_sync is not UNSET:
            field_dict["lastSuccessfulSync"] = last_successful_sync
        if report_frequency is not UNSET:
            field_dict["reportFrequency"] = report_frequency
        if current_status is not UNSET:
            field_dict["currentStatus"] = current_status
        if latest_report_id is not UNSET:
            field_dict["latestReportId"] = latest_report_id
        if latest_successful_report_id is not UNSET:
            field_dict["latestSuccessfulReportId"] = latest_successful_report_id
        if accounting_method is not UNSET:
            field_dict["accountingMethod"] = accounting_method
        if reconstructed is not UNSET:
            field_dict["reconstructed"] = reconstructed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date = d.pop("startDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        last_successful_sync = d.pop("lastSuccessfulSync", UNSET)

        report_frequency = d.pop("reportFrequency", UNSET)

        _current_status = d.pop("currentStatus", UNSET)
        current_status: Union[Unset, ReportCurrentStatus]
        if isinstance(_current_status, Unset):
            current_status = UNSET
        else:
            current_status = check_report_current_status(_current_status)

        latest_report_id = d.pop("latestReportId", UNSET)

        latest_successful_report_id = d.pop("latestSuccessfulReportId", UNSET)

        accounting_method = d.pop("accountingMethod", UNSET)

        reconstructed = d.pop("reconstructed", UNSET)

        report = cls(
            start_date=start_date,
            end_date=end_date,
            last_successful_sync=last_successful_sync,
            report_frequency=report_frequency,
            current_status=current_status,
            latest_report_id=latest_report_id,
            latest_successful_report_id=latest_successful_report_id,
            accounting_method=accounting_method,
            reconstructed=reconstructed,
        )

        report.additional_properties = d
        return report

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
