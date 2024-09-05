from typing import Literal, Set, cast

FireWebhookConnectionV1DtoServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "myob",
    "oracleNetsuite",
    "plaid",
    "quickbooks",
    "quickbooksDesktop",
    "railzSandbox",
    "sageBusinessCloud",
    "sageIntacct",
    "shopify",
    "square",
    "wave",
    "xero",
    "zohoBooks",
]

FIRE_WEBHOOK_CONNECTION_V1_DTO_SERVICE_NAME_VALUES: Set[FireWebhookConnectionV1DtoServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "myob",
    "oracleNetsuite",
    "plaid",
    "quickbooks",
    "quickbooksDesktop",
    "railzSandbox",
    "sageBusinessCloud",
    "sageIntacct",
    "shopify",
    "square",
    "wave",
    "xero",
    "zohoBooks",
}


def check_fire_webhook_connection_v1_dto_service_name(value: str) -> FireWebhookConnectionV1DtoServiceName:
    if value in FIRE_WEBHOOK_CONNECTION_V1_DTO_SERVICE_NAME_VALUES:
        return cast(FireWebhookConnectionV1DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FIRE_WEBHOOK_CONNECTION_V1_DTO_SERVICE_NAME_VALUES!r}"
    )
