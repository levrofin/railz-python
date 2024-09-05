from typing import Literal, Set, cast

PushInventoryV2ResponseDtoServiceName = Literal[
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

PUSH_INVENTORY_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushInventoryV2ResponseDtoServiceName] = {
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


def check_push_inventory_v2_response_dto_service_name(value: str) -> PushInventoryV2ResponseDtoServiceName:
    if value in PUSH_INVENTORY_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushInventoryV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_INVENTORY_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
