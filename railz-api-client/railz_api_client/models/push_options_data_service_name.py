from typing import Literal, Set, cast

PushOptionsDataServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "myob",
    "oracleNetsuite",
    "plaid",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "shopify",
    "square",
    "wave",
    "xero",
    "zohoBooks",
]

PUSH_OPTIONS_DATA_SERVICE_NAME_VALUES: Set[PushOptionsDataServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "myob",
    "oracleNetsuite",
    "plaid",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "shopify",
    "square",
    "wave",
    "xero",
    "zohoBooks",
}


def check_push_options_data_service_name(value: str) -> PushOptionsDataServiceName:
    if value in PUSH_OPTIONS_DATA_SERVICE_NAME_VALUES:
        return cast(PushOptionsDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_OPTIONS_DATA_SERVICE_NAME_VALUES!r}")
