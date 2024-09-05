from typing import Literal, Set, cast

ReportBalanceSheetsResponse200MetaServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
]

REPORT_BALANCE_SHEETS_RESPONSE_200_META_SERVICE_NAME_VALUES: Set[ReportBalanceSheetsResponse200MetaServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
}


def check_report_balance_sheets_response_200_meta_service_name(
    value: str,
) -> ReportBalanceSheetsResponse200MetaServiceName:
    if value in REPORT_BALANCE_SHEETS_RESPONSE_200_META_SERVICE_NAME_VALUES:
        return cast(ReportBalanceSheetsResponse200MetaServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_BALANCE_SHEETS_RESPONSE_200_META_SERVICE_NAME_VALUES!r}"
    )
