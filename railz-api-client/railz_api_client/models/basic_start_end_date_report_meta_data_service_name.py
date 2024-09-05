from typing import Literal, Set, cast

BasicStartEndDateReportMetaDataServiceName = Literal[
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

BASIC_START_END_DATE_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[BasicStartEndDateReportMetaDataServiceName] = {
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


def check_basic_start_end_date_report_meta_data_service_name(value: str) -> BasicStartEndDateReportMetaDataServiceName:
    if value in BASIC_START_END_DATE_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(BasicStartEndDateReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASIC_START_END_DATE_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
