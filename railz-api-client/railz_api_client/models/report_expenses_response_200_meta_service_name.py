from typing import Literal, Set, cast

ReportExpensesResponse200MetaServiceName = Literal[
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

REPORT_EXPENSES_RESPONSE_200_META_SERVICE_NAME_VALUES: Set[ReportExpensesResponse200MetaServiceName] = {
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


def check_report_expenses_response_200_meta_service_name(value: str) -> ReportExpensesResponse200MetaServiceName:
    if value in REPORT_EXPENSES_RESPONSE_200_META_SERVICE_NAME_VALUES:
        return cast(ReportExpensesResponse200MetaServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_EXPENSES_RESPONSE_200_META_SERVICE_NAME_VALUES!r}"
    )
