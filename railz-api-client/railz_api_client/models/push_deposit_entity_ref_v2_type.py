from typing import Literal, Set, cast

PushDepositEntityRefV2Type = Literal["customer", "employee", "unknown"]

PUSH_DEPOSIT_ENTITY_REF_V2_TYPE_VALUES: Set[PushDepositEntityRefV2Type] = {
    "customer",
    "employee",
    "unknown",
}


def check_push_deposit_entity_ref_v2_type(value: str) -> PushDepositEntityRefV2Type:
    if value in PUSH_DEPOSIT_ENTITY_REF_V2_TYPE_VALUES:
        return cast(PushDepositEntityRefV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_DEPOSIT_ENTITY_REF_V2_TYPE_VALUES!r}")
