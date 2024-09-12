from typing import Literal, Set, cast

PostBillPaymentRequestResponseV2DtoServiceName = Literal[
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

POST_BILL_PAYMENT_REQUEST_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PostBillPaymentRequestResponseV2DtoServiceName] = {
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


def check_post_bill_payment_request_response_v2_dto_service_name(
    value: str,
) -> PostBillPaymentRequestResponseV2DtoServiceName:
    if value in POST_BILL_PAYMENT_REQUEST_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PostBillPaymentRequestResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_BILL_PAYMENT_REQUEST_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
