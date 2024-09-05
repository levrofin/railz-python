from typing import Literal, Set, cast

BusinessValuationVisualizationsReconstruct = Literal["false", "true"]

BUSINESS_VALUATION_VISUALIZATIONS_RECONSTRUCT_VALUES: Set[BusinessValuationVisualizationsReconstruct] = {
    "false",
    "true",
}


def check_business_valuation_visualizations_reconstruct(value: str) -> BusinessValuationVisualizationsReconstruct:
    if value in BUSINESS_VALUATION_VISUALIZATIONS_RECONSTRUCT_VALUES:
        return cast(BusinessValuationVisualizationsReconstruct, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUSINESS_VALUATION_VISUALIZATIONS_RECONSTRUCT_VALUES!r}"
    )
