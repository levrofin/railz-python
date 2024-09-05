from typing import Literal, Set, cast

BatchPushCustomerResponseV2DtoServiceName = Literal[
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

BATCH_PUSH_CUSTOMER_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[BatchPushCustomerResponseV2DtoServiceName] = {
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


def check_batch_push_customer_response_v2_dto_service_name(value: str) -> BatchPushCustomerResponseV2DtoServiceName:
    if value in BATCH_PUSH_CUSTOMER_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(BatchPushCustomerResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_PUSH_CUSTOMER_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
