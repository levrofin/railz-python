from typing import Literal, Set, cast

PushBillResponseV2DtoServiceName = Literal[
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

PUSH_BILL_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushBillResponseV2DtoServiceName] = {
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


def check_push_bill_response_v2_dto_service_name(value: str) -> PushBillResponseV2DtoServiceName:
    if value in PUSH_BILL_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushBillResponseV2DtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}")
