from typing import Literal, Set, cast

AttachmentLinkV2Type = Literal[
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

ATTACHMENT_LINK_V2_TYPE_VALUES: Set[AttachmentLinkV2Type] = {
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


def check_attachment_link_v2_type(value: str) -> AttachmentLinkV2Type:
    if value in ATTACHMENT_LINK_V2_TYPE_VALUES:
        return cast(AttachmentLinkV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ATTACHMENT_LINK_V2_TYPE_VALUES!r}")
