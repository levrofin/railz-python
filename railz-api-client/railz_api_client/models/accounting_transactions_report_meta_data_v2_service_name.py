from typing import Literal, Set, cast

AccountingTransactionsReportMetaDataV2ServiceName = Literal[
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

ACCOUNTING_TRANSACTIONS_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[
    AccountingTransactionsReportMetaDataV2ServiceName
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


def check_accounting_transactions_report_meta_data_v2_service_name(
    value: str,
) -> AccountingTransactionsReportMetaDataV2ServiceName:
    if value in ACCOUNTING_TRANSACTIONS_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(AccountingTransactionsReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTIONS_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
