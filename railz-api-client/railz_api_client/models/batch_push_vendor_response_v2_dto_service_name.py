from typing import Literal, Set, cast

BatchPushVendorResponseV2DtoServiceName = Literal[
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

BATCH_PUSH_VENDOR_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[BatchPushVendorResponseV2DtoServiceName] = {
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


def check_batch_push_vendor_response_v2_dto_service_name(value: str) -> BatchPushVendorResponseV2DtoServiceName:
    if value in BATCH_PUSH_VENDOR_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(BatchPushVendorResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_PUSH_VENDOR_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
