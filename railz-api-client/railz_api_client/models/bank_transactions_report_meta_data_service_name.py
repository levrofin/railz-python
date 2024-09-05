from typing import Literal, Set, cast

BankTransactionsReportMetaDataServiceName = Literal[
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

BANK_TRANSACTIONS_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[BankTransactionsReportMetaDataServiceName] = {
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


def check_bank_transactions_report_meta_data_service_name(value: str) -> BankTransactionsReportMetaDataServiceName:
    if value in BANK_TRANSACTIONS_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(BankTransactionsReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_TRANSACTIONS_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
