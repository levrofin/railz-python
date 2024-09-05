from typing import Literal, Set, cast

UpdateBillsResponseV2DtoServiceName = Literal[
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

UPDATE_BILLS_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[UpdateBillsResponseV2DtoServiceName] = {
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


def check_update_bills_response_v2_dto_service_name(value: str) -> UpdateBillsResponseV2DtoServiceName:
    if value in UPDATE_BILLS_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(UpdateBillsResponseV2DtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BILLS_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}")
