from typing import Literal, Set, cast

UpdateBillsResponseV1DtoServiceName = Literal[
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

UPDATE_BILLS_RESPONSE_V1_DTO_SERVICE_NAME_VALUES: Set[UpdateBillsResponseV1DtoServiceName] = {
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


def check_update_bills_response_v1_dto_service_name(value: str) -> UpdateBillsResponseV1DtoServiceName:
    if value in UPDATE_BILLS_RESPONSE_V1_DTO_SERVICE_NAME_VALUES:
        return cast(UpdateBillsResponseV1DtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BILLS_RESPONSE_V1_DTO_SERVICE_NAME_VALUES!r}")
