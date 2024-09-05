from typing import Literal, Set, cast

FireWebhookConnectionV2DtoDataRequestStatus = Literal["empty", "failed", "success"]

FIRE_WEBHOOK_CONNECTION_V2_DTO_DATA_REQUEST_STATUS_VALUES: Set[FireWebhookConnectionV2DtoDataRequestStatus] = {
    "empty",
    "failed",
    "success",
}


def check_fire_webhook_connection_v2_dto_data_request_status(value: str) -> FireWebhookConnectionV2DtoDataRequestStatus:
    if value in FIRE_WEBHOOK_CONNECTION_V2_DTO_DATA_REQUEST_STATUS_VALUES:
        return cast(FireWebhookConnectionV2DtoDataRequestStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FIRE_WEBHOOK_CONNECTION_V2_DTO_DATA_REQUEST_STATUS_VALUES!r}"
    )
