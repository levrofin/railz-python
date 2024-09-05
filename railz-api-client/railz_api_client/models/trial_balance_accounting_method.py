from typing import Literal, Set, cast

TrialBalanceAccountingMethod = Literal["accrual", "cash"]

TRIAL_BALANCE_ACCOUNTING_METHOD_VALUES: Set[TrialBalanceAccountingMethod] = {
    "accrual",
    "cash",
}


def check_trial_balance_accounting_method(value: str) -> TrialBalanceAccountingMethod:
    if value in TRIAL_BALANCE_ACCOUNTING_METHOD_VALUES:
        return cast(TrialBalanceAccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIAL_BALANCE_ACCOUNTING_METHOD_VALUES!r}")
