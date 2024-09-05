from typing import Literal, Set, cast

BankTransfersReportMetaDataServiceName = Literal[
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

BANK_TRANSFERS_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[BankTransfersReportMetaDataServiceName] = {
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


def check_bank_transfers_report_meta_data_service_name(value: str) -> BankTransfersReportMetaDataServiceName:
    if value in BANK_TRANSFERS_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(BankTransfersReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_TRANSFERS_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
