from typing import Literal, Set, cast

PushTrackingCategoriesResponseV2DtoServiceName = Literal[
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

PUSH_TRACKING_CATEGORIES_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushTrackingCategoriesResponseV2DtoServiceName] = {
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


def check_push_tracking_categories_response_v2_dto_service_name(
    value: str,
) -> PushTrackingCategoriesResponseV2DtoServiceName:
    if value in PUSH_TRACKING_CATEGORIES_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushTrackingCategoriesResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_TRACKING_CATEGORIES_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
