from typing import Literal, Set, cast

PushAttachmentLinkType = Literal[
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

PUSH_ATTACHMENT_LINK_TYPE_VALUES: Set[PushAttachmentLinkType] = {
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


def check_push_attachment_link_type(value: str) -> PushAttachmentLinkType:
    if value in PUSH_ATTACHMENT_LINK_TYPE_VALUES:
        return cast(PushAttachmentLinkType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_ATTACHMENT_LINK_TYPE_VALUES!r}")
