from typing import Literal, Set, cast

PushBankAccountV2AccountType = Literal["checking", "creditCard", "investment", "loan", "saving", "unknown"]

PUSH_BANK_ACCOUNT_V2_ACCOUNT_TYPE_VALUES: Set[PushBankAccountV2AccountType] = {
    "checking",
    "creditCard",
    "investment",
    "loan",
    "saving",
    "unknown",
}


def check_push_bank_account_v2_account_type(value: str) -> PushBankAccountV2AccountType:
    if value in PUSH_BANK_ACCOUNT_V2_ACCOUNT_TYPE_VALUES:
        return cast(PushBankAccountV2AccountType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BANK_ACCOUNT_V2_ACCOUNT_TYPE_VALUES!r}")
