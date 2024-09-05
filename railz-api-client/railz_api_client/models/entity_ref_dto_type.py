from typing import Literal, Set, cast

EntityRefDtoType = Literal["customer", "vendor"]

ENTITY_REF_DTO_TYPE_VALUES: Set[EntityRefDtoType] = {
    "customer",
    "vendor",
}


def check_entity_ref_dto_type(value: str) -> EntityRefDtoType:
    if value in ENTITY_REF_DTO_TYPE_VALUES:
        return cast(EntityRefDtoType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENTITY_REF_DTO_TYPE_VALUES!r}")
