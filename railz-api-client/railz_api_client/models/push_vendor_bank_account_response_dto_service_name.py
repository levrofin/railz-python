from typing import Literal, Set, cast

PushVendorBankAccountResponseDtoServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
]

PUSH_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushVendorBankAccountResponseDtoServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
}


def check_push_vendor_bank_account_response_dto_service_name(value: str) -> PushVendorBankAccountResponseDtoServiceName:
    if value in PUSH_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushVendorBankAccountResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
