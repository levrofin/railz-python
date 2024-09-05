from typing import Literal, Set, cast

DataTypesDataV2ReportType = Literal["accounting", "analytics", "banking", "commerce"]

DATA_TYPES_DATA_V2_REPORT_TYPE_VALUES: Set[DataTypesDataV2ReportType] = {
    "accounting",
    "analytics",
    "banking",
    "commerce",
}


def check_data_types_data_v2_report_type(value: str) -> DataTypesDataV2ReportType:
    if value in DATA_TYPES_DATA_V2_REPORT_TYPE_VALUES:
        return cast(DataTypesDataV2ReportType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_DATA_V2_REPORT_TYPE_VALUES!r}")
