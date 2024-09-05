from typing import Literal, Set, cast

PushBankTransactionV2TransactionType = Literal[
    "deposit",
    "depositFromOtherAccounts",
    "expense",
    "expenseRefund",
    "interestIncome",
    "otherIncome",
    "overPayment",
    "ownerDrawings",
    "ownersContribution",
    "payment",
    "refund",
    "salesReturn",
    "salesWithoutInvoices",
    "transfer",
    "unknown",
]

PUSH_BANK_TRANSACTION_V2_TRANSACTION_TYPE_VALUES: Set[PushBankTransactionV2TransactionType] = {
    "deposit",
    "depositFromOtherAccounts",
    "expense",
    "expenseRefund",
    "interestIncome",
    "otherIncome",
    "overPayment",
    "ownerDrawings",
    "ownersContribution",
    "payment",
    "refund",
    "salesReturn",
    "salesWithoutInvoices",
    "transfer",
    "unknown",
}


def check_push_bank_transaction_v2_transaction_type(value: str) -> PushBankTransactionV2TransactionType:
    if value in PUSH_BANK_TRANSACTION_V2_TRANSACTION_TYPE_VALUES:
        return cast(PushBankTransactionV2TransactionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSACTION_V2_TRANSACTION_TYPE_VALUES!r}")
