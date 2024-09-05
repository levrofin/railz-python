from typing import Literal, Set, cast

BasicReportMetaDataV2ServiceName = Literal[
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

BASIC_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[BasicReportMetaDataV2ServiceName] = {
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


def check_basic_report_meta_data_v2_service_name(value: str) -> BasicReportMetaDataV2ServiceName:
    if value in BASIC_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(BasicReportMetaDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BASIC_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}")
