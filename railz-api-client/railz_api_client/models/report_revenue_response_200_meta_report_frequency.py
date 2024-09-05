from typing import Literal, Set, cast

ReportRevenueResponse200MetaReportFrequency = Literal["month", "quarter", "year"]

REPORT_REVENUE_RESPONSE_200_META_REPORT_FREQUENCY_VALUES: Set[ReportRevenueResponse200MetaReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_report_revenue_response_200_meta_report_frequency(value: str) -> ReportRevenueResponse200MetaReportFrequency:
    if value in REPORT_REVENUE_RESPONSE_200_META_REPORT_FREQUENCY_VALUES:
        return cast(ReportRevenueResponse200MetaReportFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_REVENUE_RESPONSE_200_META_REPORT_FREQUENCY_VALUES!r}"
    )
