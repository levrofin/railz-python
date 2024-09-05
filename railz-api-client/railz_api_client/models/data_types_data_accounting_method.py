from typing import Literal, Set, cast

DataTypesDataAccountingMethod = Literal["accrual", "cash"]

DATA_TYPES_DATA_ACCOUNTING_METHOD_VALUES: Set[DataTypesDataAccountingMethod] = {
    "accrual",
    "cash",
}


def check_data_types_data_accounting_method(value: str) -> DataTypesDataAccountingMethod:
    if value in DATA_TYPES_DATA_ACCOUNTING_METHOD_VALUES:
        return cast(DataTypesDataAccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_DATA_ACCOUNTING_METHOD_VALUES!r}")
