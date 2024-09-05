from typing import Literal, Set, cast

ReportRevenueResponse200MetaServiceName = Literal[
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

REPORT_REVENUE_RESPONSE_200_META_SERVICE_NAME_VALUES: Set[ReportRevenueResponse200MetaServiceName] = {
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


def check_report_revenue_response_200_meta_service_name(value: str) -> ReportRevenueResponse200MetaServiceName:
    if value in REPORT_REVENUE_RESPONSE_200_META_SERVICE_NAME_VALUES:
        return cast(ReportRevenueResponse200MetaServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_REVENUE_RESPONSE_200_META_SERVICE_NAME_VALUES!r}"
    )
