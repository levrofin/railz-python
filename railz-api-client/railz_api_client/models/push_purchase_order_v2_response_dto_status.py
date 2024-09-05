from typing import Literal, Set, cast

PushPurchaseOrderV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_PURCHASE_ORDER_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushPurchaseOrderV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_purchase_order_v2_response_dto_status(value: str) -> PushPurchaseOrderV2ResponseDtoStatus:
    if value in PUSH_PURCHASE_ORDER_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushPurchaseOrderV2ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_PURCHASE_ORDER_V2_RESPONSE_DTO_STATUS_VALUES!r}"
    )
