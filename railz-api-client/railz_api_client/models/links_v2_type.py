from typing import Literal, Set, cast

LinksV2Type = Literal["billPayment", "journalEntry", "other", "paymentOnAccount", "transfer"]

LINKS_V2_TYPE_VALUES: Set[LinksV2Type] = {
    "billPayment",
    "journalEntry",
    "other",
    "paymentOnAccount",
    "transfer",
}


def check_links_v2_type(value: str) -> LinksV2Type:
    if value in LINKS_V2_TYPE_VALUES:
        return cast(LinksV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINKS_V2_TYPE_VALUES!r}")
