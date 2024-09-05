from typing import Literal, Set, cast

BillPaymentLinkType = Literal["bill", "billPayment", "creditNote", "other", "paymentOnAccount", "refund"]

BILL_PAYMENT_LINK_TYPE_VALUES: Set[BillPaymentLinkType] = {
    "bill",
    "billPayment",
    "creditNote",
    "other",
    "paymentOnAccount",
    "refund",
}


def check_bill_payment_link_type(value: str) -> BillPaymentLinkType:
    if value in BILL_PAYMENT_LINK_TYPE_VALUES:
        return cast(BillPaymentLinkType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_PAYMENT_LINK_TYPE_VALUES!r}")
