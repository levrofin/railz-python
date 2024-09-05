from typing import Literal, Set, cast

PushJournalsResponseDtoServiceName = Literal[
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

PUSH_JOURNALS_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushJournalsResponseDtoServiceName] = {
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


def check_push_journals_response_dto_service_name(value: str) -> PushJournalsResponseDtoServiceName:
    if value in PUSH_JOURNALS_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushJournalsResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_JOURNALS_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
