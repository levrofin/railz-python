from typing import Literal

UpdateBankTransactionTransactionType = Literal[
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
