from typing import Literal, Set, cast

GetDisputeDataStatus = Literal[
    "chargeRefunded",
    "evidenceRequired",
    "inquiryAccepted",
    "inquiryClosed",
    "inquiryLost",
    "inquiryProcessing",
    "inquiryWon",
    "other",
    "processing",
    "unknown",
]

GET_DISPUTE_DATA_STATUS_VALUES: Set[GetDisputeDataStatus] = {
    "chargeRefunded",
    "evidenceRequired",
    "inquiryAccepted",
    "inquiryClosed",
    "inquiryLost",
    "inquiryProcessing",
    "inquiryWon",
    "other",
    "processing",
    "unknown",
}


def check_get_dispute_data_status(value: str) -> GetDisputeDataStatus:
    if value in GET_DISPUTE_DATA_STATUS_VALUES:
        return cast(GetDisputeDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_DISPUTE_DATA_STATUS_VALUES!r}")
