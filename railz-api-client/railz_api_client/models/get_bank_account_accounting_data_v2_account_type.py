from typing import Literal, Set, cast

GetBankAccountAccountingDataV2AccountType = Literal["checking", "creditCard", "investment", "loan", "saving", "unknown"]

GET_BANK_ACCOUNT_ACCOUNTING_DATA_V2_ACCOUNT_TYPE_VALUES: Set[GetBankAccountAccountingDataV2AccountType] = {
    "checking",
    "creditCard",
    "investment",
    "loan",
    "saving",
    "unknown",
}


def check_get_bank_account_accounting_data_v2_account_type(value: str) -> GetBankAccountAccountingDataV2AccountType:
    if value in GET_BANK_ACCOUNT_ACCOUNTING_DATA_V2_ACCOUNT_TYPE_VALUES:
        return cast(GetBankAccountAccountingDataV2AccountType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_BANK_ACCOUNT_ACCOUNTING_DATA_V2_ACCOUNT_TYPE_VALUES!r}"
    )
