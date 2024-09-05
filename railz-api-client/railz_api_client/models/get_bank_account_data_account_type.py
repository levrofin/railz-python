from typing import Literal, Set, cast

GetBankAccountDataAccountType = Literal["brokerage", "credit", "depository", "investment", "loan", "other"]

GET_BANK_ACCOUNT_DATA_ACCOUNT_TYPE_VALUES: Set[GetBankAccountDataAccountType] = {
    "brokerage",
    "credit",
    "depository",
    "investment",
    "loan",
    "other",
}


def check_get_bank_account_data_account_type(value: str) -> GetBankAccountDataAccountType:
    if value in GET_BANK_ACCOUNT_DATA_ACCOUNT_TYPE_VALUES:
        return cast(GetBankAccountDataAccountType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BANK_ACCOUNT_DATA_ACCOUNT_TYPE_VALUES!r}")
