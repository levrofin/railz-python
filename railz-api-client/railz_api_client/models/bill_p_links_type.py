from typing import Literal, Set, cast

BillPLinksType = Literal["bill", "billPayment", "creditNote", "other", "paymentOnAccount", "refund"]

BILL_P_LINKS_TYPE_VALUES: Set[BillPLinksType] = {
    "bill",
    "billPayment",
    "creditNote",
    "other",
    "paymentOnAccount",
    "refund",
}


def check_bill_p_links_type(value: str) -> BillPLinksType:
    if value in BILL_P_LINKS_TYPE_VALUES:
        return cast(BillPLinksType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_P_LINKS_TYPE_VALUES!r}")
