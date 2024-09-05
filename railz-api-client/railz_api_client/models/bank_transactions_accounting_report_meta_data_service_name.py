from typing import Literal, Set, cast

BankTransactionsAccountingReportMetaDataServiceName = Literal[
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

BANK_TRANSACTIONS_ACCOUNTING_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[
    BankTransactionsAccountingReportMetaDataServiceName
] = {
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


def check_bank_transactions_accounting_report_meta_data_service_name(
    value: str,
) -> BankTransactionsAccountingReportMetaDataServiceName:
    if value in BANK_TRANSACTIONS_ACCOUNTING_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(BankTransactionsAccountingReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_TRANSACTIONS_ACCOUNTING_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
