from typing import Literal, Set, cast

LinkType = Literal["billPayment", "journalEntry", "other", "paymentOnAccount", "transfer"]

LINK_TYPE_VALUES: Set[LinkType] = {
    "billPayment",
    "journalEntry",
    "other",
    "paymentOnAccount",
    "transfer",
}


def check_link_type(value: str) -> LinkType:
    if value in LINK_TYPE_VALUES:
        return cast(LinkType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINK_TYPE_VALUES!r}")
