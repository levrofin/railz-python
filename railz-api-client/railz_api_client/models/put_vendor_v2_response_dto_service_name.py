from typing import Literal, Set, cast

PutVendorV2ResponseDtoServiceName = Literal[
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

PUT_VENDOR_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PutVendorV2ResponseDtoServiceName] = {
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


def check_put_vendor_v2_response_dto_service_name(value: str) -> PutVendorV2ResponseDtoServiceName:
    if value in PUT_VENDOR_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PutVendorV2ResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUT_VENDOR_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
