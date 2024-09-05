from typing import Literal, Set, cast

ReportFinancialRatiosResponse200MetaServiceName = Literal[
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

REPORT_FINANCIAL_RATIOS_RESPONSE_200_META_SERVICE_NAME_VALUES: Set[ReportFinancialRatiosResponse200MetaServiceName] = {
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


def check_report_financial_ratios_response_200_meta_service_name(
    value: str,
) -> ReportFinancialRatiosResponse200MetaServiceName:
    if value in REPORT_FINANCIAL_RATIOS_RESPONSE_200_META_SERVICE_NAME_VALUES:
        return cast(ReportFinancialRatiosResponse200MetaServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_FINANCIAL_RATIOS_RESPONSE_200_META_SERVICE_NAME_VALUES!r}"
    )
