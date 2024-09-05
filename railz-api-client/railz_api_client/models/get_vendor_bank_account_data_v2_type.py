from typing import Literal, Set, cast

GetVendorBankAccountDataV2Type = Literal["checking", "creditCard", "investment", "loan", "saving", "unknown"]

GET_VENDOR_BANK_ACCOUNT_DATA_V2_TYPE_VALUES: Set[GetVendorBankAccountDataV2Type] = {
    "checking",
    "creditCard",
    "investment",
    "loan",
    "saving",
    "unknown",
}


def check_get_vendor_bank_account_data_v2_type(value: str) -> GetVendorBankAccountDataV2Type:
    if value in GET_VENDOR_BANK_ACCOUNT_DATA_V2_TYPE_VALUES:
        return cast(GetVendorBankAccountDataV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_VENDOR_BANK_ACCOUNT_DATA_V2_TYPE_VALUES!r}")
