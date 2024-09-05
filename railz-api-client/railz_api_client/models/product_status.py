from typing import Literal, Set, cast

ProductStatus = Literal["active", "archived", "draft"]

PRODUCT_STATUS_VALUES: Set[ProductStatus] = {
    "active",
    "archived",
    "draft",
}


def check_product_status(value: str) -> ProductStatus:
    if value in PRODUCT_STATUS_VALUES:
        return cast(ProductStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_STATUS_VALUES!r}")
