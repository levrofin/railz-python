from typing import Literal, Set, cast

BankAccountMetaDataV2ServiceName = Literal[
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

BANK_ACCOUNT_META_DATA_V2_SERVICE_NAME_VALUES: Set[BankAccountMetaDataV2ServiceName] = {
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


def check_bank_account_meta_data_v2_service_name(value: str) -> BankAccountMetaDataV2ServiceName:
    if value in BANK_ACCOUNT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(BankAccountMetaDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNT_META_DATA_V2_SERVICE_NAME_VALUES!r}")
