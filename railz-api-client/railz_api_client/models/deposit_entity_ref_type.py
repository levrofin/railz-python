from typing import Literal, Set, cast

DepositEntityRefType = Literal["customer", "employee", "unknown"]

DEPOSIT_ENTITY_REF_TYPE_VALUES: Set[DepositEntityRefType] = {
    "customer",
    "employee",
    "unknown",
}


def check_deposit_entity_ref_type(value: str) -> DepositEntityRefType:
    if value in DEPOSIT_ENTITY_REF_TYPE_VALUES:
        return cast(DepositEntityRefType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DEPOSIT_ENTITY_REF_TYPE_VALUES!r}")
