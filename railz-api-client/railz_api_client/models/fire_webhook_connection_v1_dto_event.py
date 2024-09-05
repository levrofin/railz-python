from typing import Literal, Set, cast

FireWebhookConnectionV1DtoEvent = Literal[
    "auth", "batchPush", "connectionStatus", "customerRequest", "data", "dataPerType", "delete", "login", "push"
]

FIRE_WEBHOOK_CONNECTION_V1_DTO_EVENT_VALUES: Set[FireWebhookConnectionV1DtoEvent] = {
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


def check_fire_webhook_connection_v1_dto_event(value: str) -> FireWebhookConnectionV1DtoEvent:
    if value in FIRE_WEBHOOK_CONNECTION_V1_DTO_EVENT_VALUES:
        return cast(FireWebhookConnectionV1DtoEvent, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIRE_WEBHOOK_CONNECTION_V1_DTO_EVENT_VALUES!r}")
