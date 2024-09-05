from typing import Literal, Set, cast

BatchPushChartOfAccountV2ResponseDtoServiceName = Literal[
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

BATCH_PUSH_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[
    BatchPushChartOfAccountV2ResponseDtoServiceName
] = {
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


def check_batch_push_chart_of_account_v2_response_dto_service_name(
    value: str,
) -> BatchPushChartOfAccountV2ResponseDtoServiceName:
    if value in BATCH_PUSH_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(BatchPushChartOfAccountV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_PUSH_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
