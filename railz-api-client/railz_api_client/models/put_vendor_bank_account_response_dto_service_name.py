from typing import Literal, Set, cast

PutVendorBankAccountResponseDtoServiceName = Literal[
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

PUT_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PutVendorBankAccountResponseDtoServiceName] = {
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


def check_put_vendor_bank_account_response_dto_service_name(value: str) -> PutVendorBankAccountResponseDtoServiceName:
    if value in PUT_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PutVendorBankAccountResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUT_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
