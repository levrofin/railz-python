from typing import Literal, Set, cast

LinkRefDtoType = Literal["bill", "billPayment", "creditNote", "other", "paymentOnAccount", "refund"]

LINK_REF_DTO_TYPE_VALUES: Set[LinkRefDtoType] = {
    "bill",
    "billPayment",
    "creditNote",
    "other",
    "paymentOnAccount",
    "refund",
}


def check_link_ref_dto_type(value: str) -> LinkRefDtoType:
    if value in LINK_REF_DTO_TYPE_VALUES:
        return cast(LinkRefDtoType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINK_REF_DTO_TYPE_VALUES!r}")
