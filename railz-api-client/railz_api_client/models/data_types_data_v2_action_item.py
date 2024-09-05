from typing import Literal, Set, cast

DataTypesDataV2ActionItem = Literal[
    "delete",
    "pull",
    "pull_not_applicable",
    "pull_not_supported",
    "push_create",
    "push_create_batch",
    "push_not_applicable",
    "push_not_supported",
    "push_update",
    "push_update_batch",
    "push_update_not_supported",
]

DATA_TYPES_DATA_V2_ACTION_ITEM_VALUES: Set[DataTypesDataV2ActionItem] = {
    "delete",
    "pull",
    "pull_not_applicable",
    "pull_not_supported",
    "push_create",
    "push_create_batch",
    "push_not_applicable",
    "push_not_supported",
    "push_update",
    "push_update_batch",
    "push_update_not_supported",
}


def check_data_types_data_v2_action_item(value: str) -> DataTypesDataV2ActionItem:
    if value in DATA_TYPES_DATA_V2_ACTION_ITEM_VALUES:
        return cast(DataTypesDataV2ActionItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_DATA_V2_ACTION_ITEM_VALUES!r}")
