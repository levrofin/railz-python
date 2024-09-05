from typing import Literal, Set, cast

ConnectionMigrationDtoServiceName = Literal[
    "dynamicsBusinessCentral", "freshbooks", "plaid", "quickbooks", "sageBusinessCloud", "wave", "xero", "zohoBooks"
]

CONNECTION_MIGRATION_DTO_SERVICE_NAME_VALUES: Set[ConnectionMigrationDtoServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "plaid",
    "quickbooks",
    "sageBusinessCloud",
    "wave",
    "xero",
    "zohoBooks",
}


def check_connection_migration_dto_service_name(value: str) -> ConnectionMigrationDtoServiceName:
    if value in CONNECTION_MIGRATION_DTO_SERVICE_NAME_VALUES:
        return cast(ConnectionMigrationDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTION_MIGRATION_DTO_SERVICE_NAME_VALUES!r}")
