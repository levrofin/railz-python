from typing import Literal, Set, cast

ListReportMetaDataV2ServiceName = Literal[
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

LIST_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[ListReportMetaDataV2ServiceName] = {
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


def check_list_report_meta_data_v2_service_name(value: str) -> ListReportMetaDataV2ServiceName:
    if value in LIST_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(ListReportMetaDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}")
