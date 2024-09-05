from typing import Literal, Set, cast

TransactionalReportMetaDataServiceName = Literal[
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

TRANSACTIONAL_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[TransactionalReportMetaDataServiceName] = {
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


def check_transactional_report_meta_data_service_name(value: str) -> TransactionalReportMetaDataServiceName:
    if value in TRANSACTIONAL_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(TransactionalReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSACTIONAL_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
