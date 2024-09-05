from typing import Literal, Set, cast

BasicReportMetaDataServiceName = Literal[
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

BASIC_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[BasicReportMetaDataServiceName] = {
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


def check_basic_report_meta_data_service_name(value: str) -> BasicReportMetaDataServiceName:
    if value in BASIC_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(BasicReportMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BASIC_REPORT_META_DATA_SERVICE_NAME_VALUES!r}")
