from typing import Literal, Set, cast

ReportIncomeStatementsResponse200MetaReportFrequency = Literal["month", "quarter", "year"]

REPORT_INCOME_STATEMENTS_RESPONSE_200_META_REPORT_FREQUENCY_VALUES: Set[
    ReportIncomeStatementsResponse200MetaReportFrequency
] = {
    "month",
    "quarter",
    "year",
}


def check_report_income_statements_response_200_meta_report_frequency(
    value: str,
) -> ReportIncomeStatementsResponse200MetaReportFrequency:
    if value in REPORT_INCOME_STATEMENTS_RESPONSE_200_META_REPORT_FREQUENCY_VALUES:
        return cast(ReportIncomeStatementsResponse200MetaReportFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_INCOME_STATEMENTS_RESPONSE_200_META_REPORT_FREQUENCY_VALUES!r}"
    )
