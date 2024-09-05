from typing import Literal, Set, cast

EntityRefV2Type = Literal["customer", "vendor"]

ENTITY_REF_V2_TYPE_VALUES: Set[EntityRefV2Type] = {
    "customer",
    "vendor",
}


def check_entity_ref_v2_type(value: str) -> EntityRefV2Type:
    if value in ENTITY_REF_V2_TYPE_VALUES:
        return cast(EntityRefV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENTITY_REF_V2_TYPE_VALUES!r}")
