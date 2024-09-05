from typing import Literal, Set, cast

PushPurchaseOrderV2ResponseDtoServiceName = Literal[
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

PUSH_PURCHASE_ORDER_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushPurchaseOrderV2ResponseDtoServiceName] = {
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


def check_push_purchase_order_v2_response_dto_service_name(value: str) -> PushPurchaseOrderV2ResponseDtoServiceName:
    if value in PUSH_PURCHASE_ORDER_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushPurchaseOrderV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_PURCHASE_ORDER_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
