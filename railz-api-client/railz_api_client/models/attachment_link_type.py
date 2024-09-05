from typing import Literal, Set, cast

AttachmentLinkType = Literal[
    "account",
    "bankTransaction",
    "bankTransfer",
    "bill",
    "billCreditNote",
    "billPayment",
    "customer",
    "deposit",
    "expense",
    "inventory",
    "invoice",
    "invoiceCreditNote",
    "invoicePayment",
    "journalEntry",
    "purchaseOrder",
    "vendor",
]

ATTACHMENT_LINK_TYPE_VALUES: Set[AttachmentLinkType] = {
    "account",
    "bankTransaction",
    "bankTransfer",
    "bill",
    "billCreditNote",
    "billPayment",
    "customer",
    "deposit",
    "expense",
    "inventory",
    "invoice",
    "invoiceCreditNote",
    "invoicePayment",
    "journalEntry",
    "purchaseOrder",
    "vendor",
}


def check_attachment_link_type(value: str) -> AttachmentLinkType:
    if value in ATTACHMENT_LINK_TYPE_VALUES:
        return cast(AttachmentLinkType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ATTACHMENT_LINK_TYPE_VALUES!r}")
