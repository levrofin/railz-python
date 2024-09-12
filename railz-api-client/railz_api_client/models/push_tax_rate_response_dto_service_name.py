from typing import Literal, Set, cast

PushTaxRateResponseDtoServiceName = Literal[
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

PUSH_TAX_RATE_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushTaxRateResponseDtoServiceName] = {
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


def check_push_tax_rate_response_dto_service_name(value: str) -> PushTaxRateResponseDtoServiceName:
    if value in PUSH_TAX_RATE_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushTaxRateResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_TAX_RATE_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
