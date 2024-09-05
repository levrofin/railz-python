from typing import Literal, Set, cast

ListReportMetaDataServiceName = Literal[
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

LIST_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[ListReportMetaDataServiceName] = {
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


def check_list_report_meta_data_service_name(value: str) -> ListReportMetaDataServiceName:
    if value in LIST_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(ListReportMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_META_DATA_SERVICE_NAME_VALUES!r}")
