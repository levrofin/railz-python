from typing import Literal, Set, cast

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

GET_DISPUTE_DATA_REASON_VALUES: Set[GetDisputeDataReason] = {
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
}


def check_get_dispute_data_reason(value: str) -> GetDisputeDataReason:
    if value in GET_DISPUTE_DATA_REASON_VALUES:
        return cast(GetDisputeDataReason, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_DISPUTE_DATA_REASON_VALUES!r}")
