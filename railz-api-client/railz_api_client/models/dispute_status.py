from typing import Literal

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
