from typing import Literal

PushBankTransactionTransactionType = Literal[
    "deposit",
    "expense",
    "overpayment",
    "payment",
]
