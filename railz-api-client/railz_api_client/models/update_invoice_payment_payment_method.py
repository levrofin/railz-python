from typing import Literal, Set, cast

UpdateInvoicePaymentPaymentMethod = Literal["cash", "check", "creditCard", "other"]

UPDATE_INVOICE_PAYMENT_PAYMENT_METHOD_VALUES: Set[UpdateInvoicePaymentPaymentMethod] = {
    "cash",
    "check",
    "creditCard",
    "other",
}


def check_update_invoice_payment_payment_method(value: str) -> UpdateInvoicePaymentPaymentMethod:
    if value in UPDATE_INVOICE_PAYMENT_PAYMENT_METHOD_VALUES:
        return cast(UpdateInvoicePaymentPaymentMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INVOICE_PAYMENT_PAYMENT_METHOD_VALUES!r}")
