from typing import Literal

GetBankTransactionsV2DataTransactionType = Literal[
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
