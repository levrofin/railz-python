from typing import Literal, Set, cast

FireWebhookConnectionV2DtoEvent = Literal[
    "auth", "batchPush", "connectionStatus", "customerRequest", "data", "dataPerType", "delete", "login", "push"
]

FIRE_WEBHOOK_CONNECTION_V2_DTO_EVENT_VALUES: Set[FireWebhookConnectionV2DtoEvent] = {
    "auth",
    "batchPush",
    "connectionStatus",
    "customerRequest",
    "data",
    "dataPerType",
    "delete",
    "login",
    "push",
}


def check_fire_webhook_connection_v2_dto_event(value: str) -> FireWebhookConnectionV2DtoEvent:
    if value in FIRE_WEBHOOK_CONNECTION_V2_DTO_EVENT_VALUES:
        return cast(FireWebhookConnectionV2DtoEvent, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIRE_WEBHOOK_CONNECTION_V2_DTO_EVENT_VALUES!r}")
