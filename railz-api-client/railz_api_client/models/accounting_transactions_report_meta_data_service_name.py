from typing import Literal, Set, cast

AccountingTransactionsReportMetaDataServiceName = Literal[
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

ACCOUNTING_TRANSACTIONS_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[AccountingTransactionsReportMetaDataServiceName] = {
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


def check_accounting_transactions_report_meta_data_service_name(
    value: str,
) -> AccountingTransactionsReportMetaDataServiceName:
    if value in ACCOUNTING_TRANSACTIONS_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(AccountingTransactionsReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTIONS_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
