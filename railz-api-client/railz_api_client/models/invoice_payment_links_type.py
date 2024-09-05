from typing import Literal, Set, cast

InvoicePaymentLinksType = Literal["creditNote", "invoice", "payment", "paymentOnAccount", "refund"]

INVOICE_PAYMENT_LINKS_TYPE_VALUES: Set[InvoicePaymentLinksType] = {
    "creditNote",
    "invoice",
    "payment",
    "paymentOnAccount",
    "refund",
}


def check_invoice_payment_links_type(value: str) -> InvoicePaymentLinksType:
    if value in INVOICE_PAYMENT_LINKS_TYPE_VALUES:
        return cast(InvoicePaymentLinksType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_PAYMENT_LINKS_TYPE_VALUES!r}")
