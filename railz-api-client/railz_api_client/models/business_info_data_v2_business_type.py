from typing import Literal, Set, cast

BusinessInfoDataV2BusinessType = Literal[
    "corporation",
    "limitedLiability",
    "notForProfit",
    "organization",
    "other",
    "partnership",
    "soleProprietorship",
    "unknown",
]

BUSINESS_INFO_DATA_V2_BUSINESS_TYPE_VALUES: Set[BusinessInfoDataV2BusinessType] = {
    "corporation",
    "limitedLiability",
    "notForProfit",
    "organization",
    "other",
    "partnership",
    "soleProprietorship",
    "unknown",
}


def check_business_info_data_v2_business_type(value: str) -> BusinessInfoDataV2BusinessType:
    if value in BUSINESS_INFO_DATA_V2_BUSINESS_TYPE_VALUES:
        return cast(BusinessInfoDataV2BusinessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUSINESS_INFO_DATA_V2_BUSINESS_TYPE_VALUES!r}")
