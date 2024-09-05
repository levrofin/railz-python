from typing import Literal, Set, cast

BatchUpdateChartOfAccountV2ResponseDtoServiceName = Literal[
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

BATCH_UPDATE_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[
    BatchUpdateChartOfAccountV2ResponseDtoServiceName
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


def check_batch_update_chart_of_account_v2_response_dto_service_name(
    value: str,
) -> BatchUpdateChartOfAccountV2ResponseDtoServiceName:
    if value in BATCH_UPDATE_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(BatchUpdateChartOfAccountV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_UPDATE_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
