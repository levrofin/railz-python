from typing import Literal, Set, cast

PushChartOfAccountV1ResponseDtoServiceName = Literal[
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

PUSH_CHART_OF_ACCOUNT_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushChartOfAccountV1ResponseDtoServiceName] = {
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


def check_push_chart_of_account_v1_response_dto_service_name(value: str) -> PushChartOfAccountV1ResponseDtoServiceName:
    if value in PUSH_CHART_OF_ACCOUNT_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushChartOfAccountV1ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_CHART_OF_ACCOUNT_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
