from typing import Literal, Set, cast

DataTypesResponseV2DtoServiceType = Literal["accounting", "banking", "commerce"]

DATA_TYPES_RESPONSE_V2_DTO_SERVICE_TYPE_VALUES: Set[DataTypesResponseV2DtoServiceType] = {
    "accounting",
    "banking",
    "commerce",
}


def check_data_types_response_v2_dto_service_type(value: str) -> DataTypesResponseV2DtoServiceType:
    if value in DATA_TYPES_RESPONSE_V2_DTO_SERVICE_TYPE_VALUES:
        return cast(DataTypesResponseV2DtoServiceType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_RESPONSE_V2_DTO_SERVICE_TYPE_VALUES!r}")
