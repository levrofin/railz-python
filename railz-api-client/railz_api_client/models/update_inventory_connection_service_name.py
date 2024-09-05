from typing import Literal, Set, cast

UpdateInventoryConnectionServiceName = Literal[
    "dynamicsBusinessCentral", "freshbooks", "oracleNetsuite", "quickbooks", "sageIntacct", "wave", "xero"
]

UPDATE_INVENTORY_CONNECTION_SERVICE_NAME_VALUES: Set[UpdateInventoryConnectionServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "sageIntacct",
    "wave",
    "xero",
}


def check_update_inventory_connection_service_name(value: str) -> UpdateInventoryConnectionServiceName:
    if value in UPDATE_INVENTORY_CONNECTION_SERVICE_NAME_VALUES:
        return cast(UpdateInventoryConnectionServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INVENTORY_CONNECTION_SERVICE_NAME_VALUES!r}")
