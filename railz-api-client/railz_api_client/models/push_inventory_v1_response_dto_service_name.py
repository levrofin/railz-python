from typing import Literal, Set, cast

PushInventoryV1ResponseDtoServiceName = Literal[
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

PUSH_INVENTORY_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushInventoryV1ResponseDtoServiceName] = {
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


def check_push_inventory_v1_response_dto_service_name(value: str) -> PushInventoryV1ResponseDtoServiceName:
    if value in PUSH_INVENTORY_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushInventoryV1ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_INVENTORY_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
