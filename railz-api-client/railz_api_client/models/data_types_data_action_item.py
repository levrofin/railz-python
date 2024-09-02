from typing import Literal

DataTypesDataActionItem = Literal[
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
