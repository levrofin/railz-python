from typing import Literal, Set, cast

GetCustomerBankAccountDataV2Type = Literal["checking", "creditCard", "investment", "loan", "saving", "unknown"]

GET_CUSTOMER_BANK_ACCOUNT_DATA_V2_TYPE_VALUES: Set[GetCustomerBankAccountDataV2Type] = {
    "checking",
    "creditCard",
    "investment",
    "loan",
    "saving",
    "unknown",
}


def check_get_customer_bank_account_data_v2_type(value: str) -> GetCustomerBankAccountDataV2Type:
    if value in GET_CUSTOMER_BANK_ACCOUNT_DATA_V2_TYPE_VALUES:
        return cast(GetCustomerBankAccountDataV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CUSTOMER_BANK_ACCOUNT_DATA_V2_TYPE_VALUES!r}")
