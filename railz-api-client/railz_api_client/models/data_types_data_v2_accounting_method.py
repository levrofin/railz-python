from typing import Literal, Set, cast

DataTypesDataV2AccountingMethod = Literal["accrual", "cash"]

DATA_TYPES_DATA_V2_ACCOUNTING_METHOD_VALUES: Set[DataTypesDataV2AccountingMethod] = {
    "accrual",
    "cash",
}


def check_data_types_data_v2_accounting_method(value: str) -> DataTypesDataV2AccountingMethod:
    if value in DATA_TYPES_DATA_V2_ACCOUNTING_METHOD_VALUES:
        return cast(DataTypesDataV2AccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_DATA_V2_ACCOUNTING_METHOD_VALUES!r}")
