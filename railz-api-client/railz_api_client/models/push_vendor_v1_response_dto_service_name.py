from typing import Literal, Set, cast

PushVendorV1ResponseDtoServiceName = Literal[
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

PUSH_VENDOR_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushVendorV1ResponseDtoServiceName] = {
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


def check_push_vendor_v1_response_dto_service_name(value: str) -> PushVendorV1ResponseDtoServiceName:
    if value in PUSH_VENDOR_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushVendorV1ResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_VENDOR_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
