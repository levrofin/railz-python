from typing import Literal, Set, cast

BatchUpdateVendorResponseV2DtoServiceName = Literal[
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

BATCH_UPDATE_VENDOR_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[BatchUpdateVendorResponseV2DtoServiceName] = {
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


def check_batch_update_vendor_response_v2_dto_service_name(value: str) -> BatchUpdateVendorResponseV2DtoServiceName:
    if value in BATCH_UPDATE_VENDOR_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(BatchUpdateVendorResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_UPDATE_VENDOR_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
