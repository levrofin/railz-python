from typing import Literal, Set, cast

PushAttachmentResponseV1DtoStatus = Literal["failed", "pending", "success"]

PUSH_ATTACHMENT_RESPONSE_V1_DTO_STATUS_VALUES: Set[PushAttachmentResponseV1DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_attachment_response_v1_dto_status(value: str) -> PushAttachmentResponseV1DtoStatus:
    if value in PUSH_ATTACHMENT_RESPONSE_V1_DTO_STATUS_VALUES:
        return cast(PushAttachmentResponseV1DtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_ATTACHMENT_RESPONSE_V1_DTO_STATUS_VALUES!r}")
