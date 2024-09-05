from typing import Literal, Set, cast

PushAttachmentConnectionServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "sageBusinessCloud",
    "sageIntacct",
    "xero",
    "zohoBooks",
]

PUSH_ATTACHMENT_CONNECTION_SERVICE_NAME_VALUES: Set[PushAttachmentConnectionServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "sageBusinessCloud",
    "sageIntacct",
    "xero",
    "zohoBooks",
}


def check_push_attachment_connection_service_name(value: str) -> PushAttachmentConnectionServiceName:
    if value in PUSH_ATTACHMENT_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushAttachmentConnectionServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_ATTACHMENT_CONNECTION_SERVICE_NAME_VALUES!r}")
