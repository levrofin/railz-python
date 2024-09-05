from typing import Literal, Set, cast

PushCustomerBankAccountResponseDtoServiceName = Literal[
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

PUSH_CUSTOMER_BANK_ACCOUNT_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushCustomerBankAccountResponseDtoServiceName] = {
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


def check_push_customer_bank_account_response_dto_service_name(
    value: str,
) -> PushCustomerBankAccountResponseDtoServiceName:
    if value in PUSH_CUSTOMER_BANK_ACCOUNT_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushCustomerBankAccountResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_CUSTOMER_BANK_ACCOUNT_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
