from typing import Literal, Set, cast

PushRefundResponseV2DtoServiceName = Literal[
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

PUSH_REFUND_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushRefundResponseV2DtoServiceName] = {
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


def check_push_refund_response_v2_dto_service_name(value: str) -> PushRefundResponseV2DtoServiceName:
    if value in PUSH_REFUND_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushRefundResponseV2DtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_REFUND_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}")
