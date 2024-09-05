from typing import Literal, Set, cast

PushTrackingCategoriesConnectionServiceName = Literal["quickbooks", "xero"]

PUSH_TRACKING_CATEGORIES_CONNECTION_SERVICE_NAME_VALUES: Set[PushTrackingCategoriesConnectionServiceName] = {
    "quickbooks",
    "xero",
}


def check_push_tracking_categories_connection_service_name(value: str) -> PushTrackingCategoriesConnectionServiceName:
    if value in PUSH_TRACKING_CATEGORIES_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushTrackingCategoriesConnectionServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_TRACKING_CATEGORIES_CONNECTION_SERVICE_NAME_VALUES!r}"
    )
