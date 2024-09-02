from typing import Literal

FireWebhookConnectionV1DtoEvent = Literal[
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
