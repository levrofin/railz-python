from typing import Literal, Set, cast

PushPurchaseOrderV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_PURCHASE_ORDER_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushPurchaseOrderV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_purchase_order_v1_response_dto_status(value: str) -> PushPurchaseOrderV1ResponseDtoStatus:
    if value in PUSH_PURCHASE_ORDER_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushPurchaseOrderV1ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_PURCHASE_ORDER_V1_RESPONSE_DTO_STATUS_VALUES!r}"
    )
