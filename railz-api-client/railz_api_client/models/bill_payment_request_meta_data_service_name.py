from typing import Literal, Set, cast

BillPaymentRequestMetaDataServiceName = Literal[
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

BILL_PAYMENT_REQUEST_META_DATA_SERVICE_NAME_VALUES: Set[BillPaymentRequestMetaDataServiceName] = {
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


def check_bill_payment_request_meta_data_service_name(value: str) -> BillPaymentRequestMetaDataServiceName:
    if value in BILL_PAYMENT_REQUEST_META_DATA_SERVICE_NAME_VALUES:
        return cast(BillPaymentRequestMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILL_PAYMENT_REQUEST_META_DATA_SERVICE_NAME_VALUES!r}"
    )
