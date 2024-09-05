from typing import Literal, Set, cast

FireWebhookConnectionV2DtoPayloadType = Literal["full", "simple"]

FIRE_WEBHOOK_CONNECTION_V2_DTO_PAYLOAD_TYPE_VALUES: Set[FireWebhookConnectionV2DtoPayloadType] = {
    "full",
    "simple",
}


def check_fire_webhook_connection_v2_dto_payload_type(value: str) -> FireWebhookConnectionV2DtoPayloadType:
    if value in FIRE_WEBHOOK_CONNECTION_V2_DTO_PAYLOAD_TYPE_VALUES:
        return cast(FireWebhookConnectionV2DtoPayloadType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FIRE_WEBHOOK_CONNECTION_V2_DTO_PAYLOAD_TYPE_VALUES!r}"
    )
