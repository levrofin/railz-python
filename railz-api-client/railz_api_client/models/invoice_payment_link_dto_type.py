from typing import Literal, Set, cast

InvoicePaymentLinkDtoType = Literal["creditNote", "invoice", "payment", "paymentOnAccount", "refund"]

INVOICE_PAYMENT_LINK_DTO_TYPE_VALUES: Set[InvoicePaymentLinkDtoType] = {
    "creditNote",
    "invoice",
    "payment",
    "paymentOnAccount",
    "refund",
}


def check_invoice_payment_link_dto_type(value: str) -> InvoicePaymentLinkDtoType:
    if value in INVOICE_PAYMENT_LINK_DTO_TYPE_VALUES:
        return cast(InvoicePaymentLinkDtoType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_PAYMENT_LINK_DTO_TYPE_VALUES!r}")
