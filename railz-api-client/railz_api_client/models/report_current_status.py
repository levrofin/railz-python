from typing import Literal, Set, cast

ReportCurrentStatus = Literal["empty", "failed", "pending", "success"]

REPORT_CURRENT_STATUS_VALUES: Set[ReportCurrentStatus] = {
    "empty",
    "failed",
    "pending",
    "success",
}


def check_report_current_status(value: str) -> ReportCurrentStatus:
    if value in REPORT_CURRENT_STATUS_VALUES:
        return cast(ReportCurrentStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_CURRENT_STATUS_VALUES!r}")
