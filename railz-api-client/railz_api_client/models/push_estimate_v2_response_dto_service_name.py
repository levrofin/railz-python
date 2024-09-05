from typing import Literal, Set, cast

PushEstimateV2ResponseDtoServiceName = Literal[
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

PUSH_ESTIMATE_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushEstimateV2ResponseDtoServiceName] = {
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


def check_push_estimate_v2_response_dto_service_name(value: str) -> PushEstimateV2ResponseDtoServiceName:
    if value in PUSH_ESTIMATE_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushEstimateV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_ESTIMATE_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
