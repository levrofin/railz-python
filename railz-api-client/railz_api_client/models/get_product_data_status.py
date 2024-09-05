from typing import Literal, Set, cast

GetProductDataStatus = Literal["active", "archived", "draft"]

GET_PRODUCT_DATA_STATUS_VALUES: Set[GetProductDataStatus] = {
    "active",
    "archived",
    "draft",
}


def check_get_product_data_status(value: str) -> GetProductDataStatus:
    if value in GET_PRODUCT_DATA_STATUS_VALUES:
        return cast(GetProductDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_PRODUCT_DATA_STATUS_VALUES!r}")
