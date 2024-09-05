from typing import Literal, Set, cast

ReportExpensesResponse200MetaReportFrequency = Literal["month", "quarter", "year"]

REPORT_EXPENSES_RESPONSE_200_META_REPORT_FREQUENCY_VALUES: Set[ReportExpensesResponse200MetaReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_report_expenses_response_200_meta_report_frequency(
    value: str,
) -> ReportExpensesResponse200MetaReportFrequency:
    if value in REPORT_EXPENSES_RESPONSE_200_META_REPORT_FREQUENCY_VALUES:
        return cast(ReportExpensesResponse200MetaReportFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_EXPENSES_RESPONSE_200_META_REPORT_FREQUENCY_VALUES!r}"
    )
