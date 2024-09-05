from typing import Literal, Set, cast

ReportInvoicesResponse200MetaServiceName = Literal[
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

REPORT_INVOICES_RESPONSE_200_META_SERVICE_NAME_VALUES: Set[ReportInvoicesResponse200MetaServiceName] = {
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


def check_report_invoices_response_200_meta_service_name(value: str) -> ReportInvoicesResponse200MetaServiceName:
    if value in REPORT_INVOICES_RESPONSE_200_META_SERVICE_NAME_VALUES:
        return cast(ReportInvoicesResponse200MetaServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_INVOICES_RESPONSE_200_META_SERVICE_NAME_VALUES!r}"
    )
