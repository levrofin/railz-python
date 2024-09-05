from typing import Literal, Set, cast

PushEstimateConnectionServiceName = Literal["freshbooks", "quickbooks", "xero"]

PUSH_ESTIMATE_CONNECTION_SERVICE_NAME_VALUES: Set[PushEstimateConnectionServiceName] = {
    "freshbooks",
    "quickbooks",
    "xero",
}


def check_push_estimate_connection_service_name(value: str) -> PushEstimateConnectionServiceName:
    if value in PUSH_ESTIMATE_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushEstimateConnectionServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_ESTIMATE_CONNECTION_SERVICE_NAME_VALUES!r}")
