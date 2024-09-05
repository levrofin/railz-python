from typing import Literal, Set, cast

MetadataObjectDtoWebhookLocationItem = Literal["body", "header", "query"]

METADATA_OBJECT_DTO_WEBHOOK_LOCATION_ITEM_VALUES: Set[MetadataObjectDtoWebhookLocationItem] = {
    "body",
    "header",
    "query",
}


def check_metadata_object_dto_webhook_location_item(value: str) -> MetadataObjectDtoWebhookLocationItem:
    if value in METADATA_OBJECT_DTO_WEBHOOK_LOCATION_ITEM_VALUES:
        return cast(MetadataObjectDtoWebhookLocationItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {METADATA_OBJECT_DTO_WEBHOOK_LOCATION_ITEM_VALUES!r}")
