from typing import Literal, Set, cast

BalanceSheetsReportFrequency = Literal["month", "quarter", "year"]

BALANCE_SHEETS_REPORT_FREQUENCY_VALUES: Set[BalanceSheetsReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_balance_sheets_report_frequency(value: str) -> BalanceSheetsReportFrequency:
    if value in BALANCE_SHEETS_REPORT_FREQUENCY_VALUES:
        return cast(BalanceSheetsReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_SHEETS_REPORT_FREQUENCY_VALUES!r}")
