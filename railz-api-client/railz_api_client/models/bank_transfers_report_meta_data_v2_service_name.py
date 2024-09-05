from typing import Literal, Set, cast

BankTransfersReportMetaDataV2ServiceName = Literal[
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

BANK_TRANSFERS_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[BankTransfersReportMetaDataV2ServiceName] = {
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


def check_bank_transfers_report_meta_data_v2_service_name(value: str) -> BankTransfersReportMetaDataV2ServiceName:
    if value in BANK_TRANSFERS_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(BankTransfersReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_TRANSFERS_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
