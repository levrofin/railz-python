from typing import Literal, Set, cast

CreditNoteTrackingCategoryRefDtoType = Literal["class", "department", "location", "unknown"]

CREDIT_NOTE_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES: Set[CreditNoteTrackingCategoryRefDtoType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_credit_note_tracking_category_ref_dto_type(value: str) -> CreditNoteTrackingCategoryRefDtoType:
    if value in CREDIT_NOTE_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES:
        return cast(CreditNoteTrackingCategoryRefDtoType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDIT_NOTE_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES!r}"
    )
