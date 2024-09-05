from typing import Literal, Set, cast

PutVendorV1ResponseDtoServiceName = Literal[
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

PUT_VENDOR_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PutVendorV1ResponseDtoServiceName] = {
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


def check_put_vendor_v1_response_dto_service_name(value: str) -> PutVendorV1ResponseDtoServiceName:
    if value in PUT_VENDOR_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PutVendorV1ResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUT_VENDOR_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
