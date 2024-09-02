from typing import Literal

GetBankTransactionsDataTransactionType = Literal[
    "adjustment",
    "atm",
    "bankCharge",
    "billPayment",
    "cash",
    "cashback",
    "cheque",
    "directDebit",
    "interest",
    "purchase",
    "standingOrder",
    "transfer",
]
