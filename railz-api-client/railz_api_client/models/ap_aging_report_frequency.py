from typing import Literal, Set, cast

ApAgingReportFrequency = Literal["month", "quarter", "year"]

AP_AGING_REPORT_FREQUENCY_VALUES: Set[ApAgingReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_ap_aging_report_frequency(value: str) -> ApAgingReportFrequency:
    if value in AP_AGING_REPORT_FREQUENCY_VALUES:
        return cast(ApAgingReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AP_AGING_REPORT_FREQUENCY_VALUES!r}")
