from typing import Literal, Set, cast

PushAttachmentResponseV1DtoServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
]

PUSH_ATTACHMENT_RESPONSE_V1_DTO_SERVICE_NAME_VALUES: Set[PushAttachmentResponseV1DtoServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
}


def check_push_attachment_response_v1_dto_service_name(value: str) -> PushAttachmentResponseV1DtoServiceName:
    if value in PUSH_ATTACHMENT_RESPONSE_V1_DTO_SERVICE_NAME_VALUES:
        return cast(PushAttachmentResponseV1DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_ATTACHMENT_RESPONSE_V1_DTO_SERVICE_NAME_VALUES!r}"
    )
