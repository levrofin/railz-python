from typing import Literal

FireWebhookConnectionV2DtoEvent = Literal[
    "auth",
    "batchPush",
    "connectionStatus",
    "customerRequest",
    "data",
    "dataPerType",
    "delete",
    "login",
    "push",
]
