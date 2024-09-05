from typing import Literal, Set, cast

TrialBalanceReportFrequency = Literal["month", "quarter", "year"]

TRIAL_BALANCE_REPORT_FREQUENCY_VALUES: Set[TrialBalanceReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_trial_balance_report_frequency(value: str) -> TrialBalanceReportFrequency:
    if value in TRIAL_BALANCE_REPORT_FREQUENCY_VALUES:
        return cast(TrialBalanceReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIAL_BALANCE_REPORT_FREQUENCY_VALUES!r}")
