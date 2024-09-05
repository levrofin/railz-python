from typing import Literal, Set, cast

PushExpenseeResponseDtoServiceName = Literal[
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

PUSH_EXPENSEE_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushExpenseeResponseDtoServiceName] = {
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


def check_push_expensee_response_dto_service_name(value: str) -> PushExpenseeResponseDtoServiceName:
    if value in PUSH_EXPENSEE_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushExpenseeResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_EXPENSEE_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
