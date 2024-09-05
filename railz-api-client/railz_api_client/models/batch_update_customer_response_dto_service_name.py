from typing import Literal, Set, cast

BatchUpdateCustomerResponseDtoServiceName = Literal[
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

BATCH_UPDATE_CUSTOMER_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[BatchUpdateCustomerResponseDtoServiceName] = {
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


def check_batch_update_customer_response_dto_service_name(value: str) -> BatchUpdateCustomerResponseDtoServiceName:
    if value in BATCH_UPDATE_CUSTOMER_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(BatchUpdateCustomerResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_UPDATE_CUSTOMER_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
