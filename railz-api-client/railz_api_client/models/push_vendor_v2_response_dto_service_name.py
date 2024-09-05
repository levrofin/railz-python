from typing import Literal, Set, cast

PushVendorV2ResponseDtoServiceName = Literal[
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

PUSH_VENDOR_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushVendorV2ResponseDtoServiceName] = {
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


def check_push_vendor_v2_response_dto_service_name(value: str) -> PushVendorV2ResponseDtoServiceName:
    if value in PUSH_VENDOR_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushVendorV2ResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_VENDOR_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
