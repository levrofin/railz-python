from typing import Literal, Set, cast

TransactionalReportMetaDataV2ServiceName = Literal[
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

TRANSACTIONAL_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[TransactionalReportMetaDataV2ServiceName] = {
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


def check_transactional_report_meta_data_v2_service_name(value: str) -> TransactionalReportMetaDataV2ServiceName:
    if value in TRANSACTIONAL_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(TransactionalReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSACTIONAL_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
