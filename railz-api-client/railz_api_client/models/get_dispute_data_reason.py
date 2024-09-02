from typing import Literal

GetDisputeDataReason = Literal[
    "bankNotProcessed",
    "creditNotProcessed",
    "debitNotAuthorized",
    "duplicate",
    "fraudulent",
    "general",
    "incorrectAccountDetails",
    "insufficientFunds",
    "other",
    "productNotReceived",
    "productUnacceptable",
    "subscriptionCanceled",
    "unknown",
    "unrecognized",
]
