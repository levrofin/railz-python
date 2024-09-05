from typing import Literal, Set, cast

LinksType = Literal["billPayment", "journalEntry", "other", "paymentOnAccount", "transfer"]

LINKS_TYPE_VALUES: Set[LinksType] = {
    "billPayment",
    "journalEntry",
    "other",
    "paymentOnAccount",
    "transfer",
}


def check_links_type(value: str) -> LinksType:
    if value in LINKS_TYPE_VALUES:
        return cast(LinksType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINKS_TYPE_VALUES!r}")
