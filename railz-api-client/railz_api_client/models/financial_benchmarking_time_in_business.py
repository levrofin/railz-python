from typing import Literal, Set, cast

FinancialBenchmarkingTimeInBusiness = Literal[1, 2, 3, 4, 5, 10, 99]

FINANCIAL_BENCHMARKING_TIME_IN_BUSINESS_VALUES: Set[FinancialBenchmarkingTimeInBusiness] = {
    1,
    2,
    3,
    4,
    5,
    10,
    99,
}


def check_financial_benchmarking_time_in_business(value: int) -> FinancialBenchmarkingTimeInBusiness:
    if value in FINANCIAL_BENCHMARKING_TIME_IN_BUSINESS_VALUES:
        return cast(FinancialBenchmarkingTimeInBusiness, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_BENCHMARKING_TIME_IN_BUSINESS_VALUES!r}")
