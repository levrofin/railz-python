from typing import Literal, Set, cast

BasicStartEndDateReportMetaDataV2ServiceName = Literal[
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

BASIC_START_END_DATE_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[BasicStartEndDateReportMetaDataV2ServiceName] = {
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


def check_basic_start_end_date_report_meta_data_v2_service_name(
    value: str,
) -> BasicStartEndDateReportMetaDataV2ServiceName:
    if value in BASIC_START_END_DATE_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(BasicStartEndDateReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASIC_START_END_DATE_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
