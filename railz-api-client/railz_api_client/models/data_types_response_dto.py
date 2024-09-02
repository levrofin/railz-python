from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_types_response_dto_service_name import DataTypesResponseDtoServiceName
from ..models.data_types_response_dto_service_type import DataTypesResponseDtoServiceType

if TYPE_CHECKING:
    from ..models.data_types_data import DataTypesData


T = TypeVar("T", bound="DataTypesResponseDto")


@_attrs_define
class DataTypesResponseDto:
    """
    Attributes:
        service_name (DataTypesResponseDtoServiceName):
        service_name_description (str):
        service_type (DataTypesResponseDtoServiceType):
        is_beta (bool):
        data_types (List['DataTypesData']):
    """

    service_name: DataTypesResponseDtoServiceName
    service_name_description: str
    service_type: DataTypesResponseDtoServiceType
    is_beta: bool
    data_types: List["DataTypesData"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_name = self.service_name

        service_name_description = self.service_name_description

        service_type = self.service_type

        is_beta = self.is_beta

        data_types = []
        for data_types_item_data in self.data_types:
            data_types_item = data_types_item_data.to_dict()
            data_types.append(data_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceName": service_name,
                "serviceNameDescription": service_name_description,
                "serviceType": service_type,
                "isBeta": is_beta,
                "dataTypes": data_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_types_data import DataTypesData

        d = src_dict.copy()
        service_name = d.pop("serviceName")

        service_name_description = d.pop("serviceNameDescription")

        service_type = d.pop("serviceType")

        is_beta = d.pop("isBeta")

        data_types = []
        _data_types = d.pop("dataTypes")
        for data_types_item_data in _data_types:
            data_types_item = DataTypesData.from_dict(data_types_item_data)

            data_types.append(data_types_item)

        data_types_response_dto = cls(
            service_name=service_name,
            service_name_description=service_name_description,
            service_type=service_type,
            is_beta=is_beta,
            data_types=data_types,
        )

        data_types_response_dto.additional_properties = d
        return data_types_response_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
