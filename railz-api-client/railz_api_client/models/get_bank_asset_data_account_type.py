from typing import Literal, Set, cast

GetBankAssetDataAccountType = Literal["checking", "creditCard", "investment", "loan", "saving", "unknown"]

GET_BANK_ASSET_DATA_ACCOUNT_TYPE_VALUES: Set[GetBankAssetDataAccountType] = {
    "checking",
    "creditCard",
    "investment",
    "loan",
    "saving",
    "unknown",
}


def check_get_bank_asset_data_account_type(value: str) -> GetBankAssetDataAccountType:
    if value in GET_BANK_ASSET_DATA_ACCOUNT_TYPE_VALUES:
        return cast(GetBankAssetDataAccountType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BANK_ASSET_DATA_ACCOUNT_TYPE_VALUES!r}")
