import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.financial_statement_report_meta_data_v2_accounting_method import (
    FinancialStatementReportMetaDataV2AccountingMethod,
)
from ..models.financial_statement_report_meta_data_v2_service_name import FinancialStatementReportMetaDataV2ServiceName
from ..models.financial_statement_report_meta_data_v2_status import FinancialStatementReportMetaDataV2Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialStatementReportMetaDataV2")


@_attrs_define
class FinancialStatementReportMetaDataV2:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (str):  Example: Railz.
        service_name (FinancialStatementReportMetaDataV2ServiceName):  Example: xero.
        report_id (str):  Example: 5fad8a342a88364234392fb5.
        status (FinancialStatementReportMetaDataV2Status):  Example: success.
        report_frequency (str):  Example: month.
        created_at (datetime.datetime):  Example: 2020-11-25T01:02:03Z.
        updated_at (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
        start_date (str):  Example: 2020-11-25T01:02:03Z.
        end_date (str):  Example: 2020-12-25T01:02:03Z.
        accounting_method (FinancialStatementReportMetaDataV2AccountingMethod):  Example: accrual.
        currency (Union[Unset, str]):  Example: USD.
    """

    connection_uuid: str
    business_name: str
    service_name: FinancialStatementReportMetaDataV2ServiceName
    report_id: str
    status: FinancialStatementReportMetaDataV2Status
    report_frequency: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    start_date: str
    end_date: str
    accounting_method: FinancialStatementReportMetaDataV2AccountingMethod
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        business_name = self.business_name

        service_name = self.service_name

        report_id = self.report_id

        status = self.status

        report_frequency = self.report_frequency

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        start_date = self.start_date

        end_date = self.end_date

        accounting_method = self.accounting_method

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "businessName": business_name,
                "serviceName": service_name,
                "reportId": report_id,
                "status": status,
                "reportFrequency": report_frequency,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "startDate": start_date,
                "endDate": end_date,
                "accountingMethod": accounting_method,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName")

        service_name = d.pop("serviceName")

        report_id = d.pop("reportId")

        status = d.pop("status")

        report_frequency = d.pop("reportFrequency")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        start_date = d.pop("startDate")

        end_date = d.pop("endDate")

        accounting_method = d.pop("accountingMethod")

        currency = d.pop("currency", UNSET)

        financial_statement_report_meta_data_v2 = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
            report_id=report_id,
            status=status,
            report_frequency=report_frequency,
            created_at=created_at,
            updated_at=updated_at,
            start_date=start_date,
            end_date=end_date,
            accounting_method=accounting_method,
            currency=currency,
        )

        financial_statement_report_meta_data_v2.additional_properties = d
        return financial_statement_report_meta_data_v2

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
