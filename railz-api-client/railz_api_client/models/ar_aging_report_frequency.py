from typing import Literal, Set, cast

ArAgingReportFrequency = Literal["month", "quarter", "year"]

AR_AGING_REPORT_FREQUENCY_VALUES: Set[ArAgingReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_ar_aging_report_frequency(value: str) -> ArAgingReportFrequency:
    if value in AR_AGING_REPORT_FREQUENCY_VALUES:
        return cast(ArAgingReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AR_AGING_REPORT_FREQUENCY_VALUES!r}")
