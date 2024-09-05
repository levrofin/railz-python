from typing import Literal, Set, cast

ReportIncomeStatementsResponse200MetaServiceName = Literal[
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

REPORT_INCOME_STATEMENTS_RESPONSE_200_META_SERVICE_NAME_VALUES: Set[
    ReportIncomeStatementsResponse200MetaServiceName
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


def check_report_income_statements_response_200_meta_service_name(
    value: str,
) -> ReportIncomeStatementsResponse200MetaServiceName:
    if value in REPORT_INCOME_STATEMENTS_RESPONSE_200_META_SERVICE_NAME_VALUES:
        return cast(ReportIncomeStatementsResponse200MetaServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_INCOME_STATEMENTS_RESPONSE_200_META_SERVICE_NAME_VALUES!r}"
    )
