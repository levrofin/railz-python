from typing import Literal, Set, cast

BankReconciliationReportMetaDataV2ServiceName = Literal[
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

BANK_RECONCILIATION_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[BankReconciliationReportMetaDataV2ServiceName] = {
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


def check_bank_reconciliation_report_meta_data_v2_service_name(
    value: str,
) -> BankReconciliationReportMetaDataV2ServiceName:
    if value in BANK_RECONCILIATION_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(BankReconciliationReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_RECONCILIATION_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
