from typing import Literal, Set, cast

InvoicePaymentLinksV2Type = Literal["creditNote", "invoice", "payment", "paymentOnAccount", "refund"]

INVOICE_PAYMENT_LINKS_V2_TYPE_VALUES: Set[InvoicePaymentLinksV2Type] = {
    "creditNote",
    "invoice",
    "payment",
    "paymentOnAccount",
    "refund",
}


def check_invoice_payment_links_v2_type(value: str) -> InvoicePaymentLinksV2Type:
    if value in INVOICE_PAYMENT_LINKS_V2_TYPE_VALUES:
        return cast(InvoicePaymentLinksV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_PAYMENT_LINKS_V2_TYPE_VALUES!r}")
