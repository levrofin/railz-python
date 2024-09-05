from typing import Literal, Set, cast

DisputeStatus = Literal[
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

DISPUTE_STATUS_VALUES: Set[DisputeStatus] = {
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


def check_dispute_status(value: str) -> DisputeStatus:
    if value in DISPUTE_STATUS_VALUES:
        return cast(DisputeStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DISPUTE_STATUS_VALUES!r}")
