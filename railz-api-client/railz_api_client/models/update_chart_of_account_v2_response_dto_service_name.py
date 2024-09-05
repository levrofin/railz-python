from typing import Literal, Set, cast

UpdateChartOfAccountV2ResponseDtoServiceName = Literal[
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

UPDATE_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[UpdateChartOfAccountV2ResponseDtoServiceName] = {
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


def check_update_chart_of_account_v2_response_dto_service_name(
    value: str,
) -> UpdateChartOfAccountV2ResponseDtoServiceName:
    if value in UPDATE_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(UpdateChartOfAccountV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
