from typing import Literal, Set, cast

ReportCashflowStatementsResponse200MetaReportFrequency = Literal["month", "quarter", "year"]

REPORT_CASHFLOW_STATEMENTS_RESPONSE_200_META_REPORT_FREQUENCY_VALUES: Set[
    ReportCashflowStatementsResponse200MetaReportFrequency
] = {
    "month",
    "quarter",
    "year",
}


def check_report_cashflow_statements_response_200_meta_report_frequency(
    value: str,
) -> ReportCashflowStatementsResponse200MetaReportFrequency:
    if value in REPORT_CASHFLOW_STATEMENTS_RESPONSE_200_META_REPORT_FREQUENCY_VALUES:
        return cast(ReportCashflowStatementsResponse200MetaReportFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_CASHFLOW_STATEMENTS_RESPONSE_200_META_REPORT_FREQUENCY_VALUES!r}"
    )
