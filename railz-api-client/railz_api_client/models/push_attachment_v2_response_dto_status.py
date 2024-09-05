from typing import Literal, Set, cast

PushAttachmentV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_ATTACHMENT_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushAttachmentV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_attachment_v2_response_dto_status(value: str) -> PushAttachmentV2ResponseDtoStatus:
    if value in PUSH_ATTACHMENT_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushAttachmentV2ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_ATTACHMENT_V2_RESPONSE_DTO_STATUS_VALUES!r}")
