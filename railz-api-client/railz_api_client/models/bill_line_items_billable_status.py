from typing import Literal

BillLineItemsBillableStatus = Literal[
    "billable",
    "hasBeenBilled",
    "notBillable",
]
