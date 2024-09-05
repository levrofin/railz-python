from typing import Literal, Set, cast

UpdateInventoryV2ResponseDtoServiceName = Literal[
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

UPDATE_INVENTORY_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[UpdateInventoryV2ResponseDtoServiceName] = {
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


def check_update_inventory_v2_response_dto_service_name(value: str) -> UpdateInventoryV2ResponseDtoServiceName:
    if value in UPDATE_INVENTORY_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(UpdateInventoryV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INVENTORY_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
