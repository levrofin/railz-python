from typing import Literal, Set, cast

ReportBillsResponse200MetaServiceName = Literal[
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

REPORT_BILLS_RESPONSE_200_META_SERVICE_NAME_VALUES: Set[ReportBillsResponse200MetaServiceName] = {
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


def check_report_bills_response_200_meta_service_name(value: str) -> ReportBillsResponse200MetaServiceName:
    if value in REPORT_BILLS_RESPONSE_200_META_SERVICE_NAME_VALUES:
        return cast(ReportBillsResponse200MetaServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_BILLS_RESPONSE_200_META_SERVICE_NAME_VALUES!r}"
    )
