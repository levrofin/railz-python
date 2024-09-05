from typing import Literal, Set, cast

BankAssetMetaDataServiceName = Literal[
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

BANK_ASSET_META_DATA_SERVICE_NAME_VALUES: Set[BankAssetMetaDataServiceName] = {
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


def check_bank_asset_meta_data_service_name(value: str) -> BankAssetMetaDataServiceName:
    if value in BANK_ASSET_META_DATA_SERVICE_NAME_VALUES:
        return cast(BankAssetMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_ASSET_META_DATA_SERVICE_NAME_VALUES!r}")
