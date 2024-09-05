from typing import Literal, Set, cast

ConnectionMigrationDtoLocation = Literal["au", "ca", "com", "eu", "in", "jp"]

CONNECTION_MIGRATION_DTO_LOCATION_VALUES: Set[ConnectionMigrationDtoLocation] = {
    "au",
    "ca",
    "com",
    "eu",
    "in",
    "jp",
}


def check_connection_migration_dto_location(value: str) -> ConnectionMigrationDtoLocation:
    if value in CONNECTION_MIGRATION_DTO_LOCATION_VALUES:
        return cast(ConnectionMigrationDtoLocation, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTION_MIGRATION_DTO_LOCATION_VALUES!r}")
