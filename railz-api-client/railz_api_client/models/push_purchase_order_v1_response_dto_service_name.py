from typing import Literal, Set, cast

PushPurchaseOrderV1ResponseDtoServiceName = Literal[
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

PUSH_PURCHASE_ORDER_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushPurchaseOrderV1ResponseDtoServiceName] = {
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


def check_push_purchase_order_v1_response_dto_service_name(value: str) -> PushPurchaseOrderV1ResponseDtoServiceName:
    if value in PUSH_PURCHASE_ORDER_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushPurchaseOrderV1ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_PURCHASE_ORDER_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
