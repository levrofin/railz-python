from typing import Literal, Set, cast

ReportBalanceSheetsResponse200MetaReportFrequency = Literal["month", "quarter", "year"]

REPORT_BALANCE_SHEETS_RESPONSE_200_META_REPORT_FREQUENCY_VALUES: Set[
    ReportBalanceSheetsResponse200MetaReportFrequency
] = {
    "month",
    "quarter",
    "year",
}


def check_report_balance_sheets_response_200_meta_report_frequency(
    value: str,
) -> ReportBalanceSheetsResponse200MetaReportFrequency:
    if value in REPORT_BALANCE_SHEETS_RESPONSE_200_META_REPORT_FREQUENCY_VALUES:
        return cast(ReportBalanceSheetsResponse200MetaReportFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_BALANCE_SHEETS_RESPONSE_200_META_REPORT_FREQUENCY_VALUES!r}"
    )
