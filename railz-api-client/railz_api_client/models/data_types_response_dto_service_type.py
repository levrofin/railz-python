from typing import Literal, Set, cast

DataTypesResponseDtoServiceType = Literal["accounting", "banking", "commerce"]

DATA_TYPES_RESPONSE_DTO_SERVICE_TYPE_VALUES: Set[DataTypesResponseDtoServiceType] = {
    "accounting",
    "banking",
    "commerce",
}


def check_data_types_response_dto_service_type(value: str) -> DataTypesResponseDtoServiceType:
    if value in DATA_TYPES_RESPONSE_DTO_SERVICE_TYPE_VALUES:
        return cast(DataTypesResponseDtoServiceType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_RESPONSE_DTO_SERVICE_TYPE_VALUES!r}")
