from typing import Literal, Set, cast

UpdateInventoryV1ResponseDtoServiceName = Literal[
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

UPDATE_INVENTORY_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[UpdateInventoryV1ResponseDtoServiceName] = {
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


def check_update_inventory_v1_response_dto_service_name(value: str) -> UpdateInventoryV1ResponseDtoServiceName:
    if value in UPDATE_INVENTORY_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(UpdateInventoryV1ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INVENTORY_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
