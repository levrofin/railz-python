from typing import Literal, Set, cast

BankAccountMetaDataServiceName = Literal[
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

BANK_ACCOUNT_META_DATA_SERVICE_NAME_VALUES: Set[BankAccountMetaDataServiceName] = {
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


def check_bank_account_meta_data_service_name(value: str) -> BankAccountMetaDataServiceName:
    if value in BANK_ACCOUNT_META_DATA_SERVICE_NAME_VALUES:
        return cast(BankAccountMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNT_META_DATA_SERVICE_NAME_VALUES!r}")
