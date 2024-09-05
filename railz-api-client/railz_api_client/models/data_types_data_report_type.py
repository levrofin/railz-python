from typing import Literal, Set, cast

DataTypesDataReportType = Literal["accounting", "analytics", "banking", "commerce"]

DATA_TYPES_DATA_REPORT_TYPE_VALUES: Set[DataTypesDataReportType] = {
    "accounting",
    "analytics",
    "banking",
    "commerce",
}


def check_data_types_data_report_type(value: str) -> DataTypesDataReportType:
    if value in DATA_TYPES_DATA_REPORT_TYPE_VALUES:
        return cast(DataTypesDataReportType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_DATA_REPORT_TYPE_VALUES!r}")
