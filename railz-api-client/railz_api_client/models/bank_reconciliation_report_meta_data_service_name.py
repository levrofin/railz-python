from typing import Literal, Set, cast

BankReconciliationReportMetaDataServiceName = Literal[
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

BANK_RECONCILIATION_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[BankReconciliationReportMetaDataServiceName] = {
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


def check_bank_reconciliation_report_meta_data_service_name(value: str) -> BankReconciliationReportMetaDataServiceName:
    if value in BANK_RECONCILIATION_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(BankReconciliationReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_RECONCILIATION_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
