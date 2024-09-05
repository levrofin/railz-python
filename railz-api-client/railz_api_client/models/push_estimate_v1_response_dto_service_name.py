from typing import Literal, Set, cast

PushEstimateV1ResponseDtoServiceName = Literal[
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

PUSH_ESTIMATE_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushEstimateV1ResponseDtoServiceName] = {
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


def check_push_estimate_v1_response_dto_service_name(value: str) -> PushEstimateV1ResponseDtoServiceName:
    if value in PUSH_ESTIMATE_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushEstimateV1ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_ESTIMATE_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
