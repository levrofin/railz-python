from typing import Literal, Set, cast

WeightUnitOfMeasure = Literal["g", "kg", "lb", "oz"]

WEIGHT_UNIT_OF_MEASURE_VALUES: Set[WeightUnitOfMeasure] = {
    "g",
    "kg",
    "lb",
    "oz",
}


def check_weight_unit_of_measure(value: str) -> WeightUnitOfMeasure:
    if value in WEIGHT_UNIT_OF_MEASURE_VALUES:
        return cast(WeightUnitOfMeasure, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEIGHT_UNIT_OF_MEASURE_VALUES!r}")
