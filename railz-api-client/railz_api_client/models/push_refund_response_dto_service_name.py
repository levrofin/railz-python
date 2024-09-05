from typing import Literal, Set, cast

PushRefundResponseDtoServiceName = Literal["freshbooks", "quickbooks", "xero"]

PUSH_REFUND_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushRefundResponseDtoServiceName] = {
    "freshbooks",
    "quickbooks",
    "xero",
}


def check_push_refund_response_dto_service_name(value: str) -> PushRefundResponseDtoServiceName:
    if value in PUSH_REFUND_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushRefundResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_REFUND_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
