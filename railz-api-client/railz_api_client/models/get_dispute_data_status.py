from typing import Literal

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
