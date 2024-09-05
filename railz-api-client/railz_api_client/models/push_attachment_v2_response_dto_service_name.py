from typing import Literal, Set, cast

PushAttachmentV2ResponseDtoServiceName = Literal[
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

PUSH_ATTACHMENT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushAttachmentV2ResponseDtoServiceName] = {
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


def check_push_attachment_v2_response_dto_service_name(value: str) -> PushAttachmentV2ResponseDtoServiceName:
    if value in PUSH_ATTACHMENT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushAttachmentV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_ATTACHMENT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
