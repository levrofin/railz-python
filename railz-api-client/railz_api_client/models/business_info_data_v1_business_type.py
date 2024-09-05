from typing import Literal, Set, cast

BusinessInfoDataV1BusinessType = Literal[
    "corporation",
    "limitedLiability",
    "notForProfit",
    "organization",
    "other",
    "partnership",
    "soleProprietorship",
    "unknown",
]

BUSINESS_INFO_DATA_V1_BUSINESS_TYPE_VALUES: Set[BusinessInfoDataV1BusinessType] = {
    "corporation",
    "limitedLiability",
    "notForProfit",
    "organization",
    "other",
    "partnership",
    "soleProprietorship",
    "unknown",
}


def check_business_info_data_v1_business_type(value: str) -> BusinessInfoDataV1BusinessType:
    if value in BUSINESS_INFO_DATA_V1_BUSINESS_TYPE_VALUES:
        return cast(BusinessInfoDataV1BusinessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUSINESS_INFO_DATA_V1_BUSINESS_TYPE_VALUES!r}")
