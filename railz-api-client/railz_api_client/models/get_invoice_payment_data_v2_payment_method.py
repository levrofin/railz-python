from typing import Literal, Set, cast

GetInvoicePaymentDataV2PaymentMethod = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

GET_INVOICE_PAYMENT_DATA_V2_PAYMENT_METHOD_VALUES: Set[GetInvoicePaymentDataV2PaymentMethod] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_get_invoice_payment_data_v2_payment_method(value: str) -> GetInvoicePaymentDataV2PaymentMethod:
    if value in GET_INVOICE_PAYMENT_DATA_V2_PAYMENT_METHOD_VALUES:
        return cast(GetInvoicePaymentDataV2PaymentMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_PAYMENT_DATA_V2_PAYMENT_METHOD_VALUES!r}"
    )
