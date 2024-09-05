from typing import Literal, Set, cast

InvoicePaymentLinkType = Literal["creditNote", "invoice", "payment", "paymentOnAccount", "refund"]

INVOICE_PAYMENT_LINK_TYPE_VALUES: Set[InvoicePaymentLinkType] = {
    "creditNote",
    "invoice",
    "payment",
    "paymentOnAccount",
    "refund",
}


def check_invoice_payment_link_type(value: str) -> InvoicePaymentLinkType:
    if value in INVOICE_PAYMENT_LINK_TYPE_VALUES:
        return cast(InvoicePaymentLinkType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_PAYMENT_LINK_TYPE_VALUES!r}")
