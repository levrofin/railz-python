from typing import Literal, Set, cast

PushTaxRateResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_TAX_RATE_RESPONSE_DTO_STATUS_VALUES: Set[PushTaxRateResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_tax_rate_response_dto_status(value: str) -> PushTaxRateResponseDtoStatus:
    if value in PUSH_TAX_RATE_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushTaxRateResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_TAX_RATE_RESPONSE_DTO_STATUS_VALUES!r}")
