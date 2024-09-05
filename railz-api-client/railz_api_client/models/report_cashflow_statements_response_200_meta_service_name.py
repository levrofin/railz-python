from typing import Literal, Set, cast

ReportCashflowStatementsResponse200MetaServiceName = Literal[
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

REPORT_CASHFLOW_STATEMENTS_RESPONSE_200_META_SERVICE_NAME_VALUES: Set[
    ReportCashflowStatementsResponse200MetaServiceName
] = {
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


def check_report_cashflow_statements_response_200_meta_service_name(
    value: str,
) -> ReportCashflowStatementsResponse200MetaServiceName:
    if value in REPORT_CASHFLOW_STATEMENTS_RESPONSE_200_META_SERVICE_NAME_VALUES:
        return cast(ReportCashflowStatementsResponse200MetaServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_CASHFLOW_STATEMENTS_RESPONSE_200_META_SERVICE_NAME_VALUES!r}"
    )
