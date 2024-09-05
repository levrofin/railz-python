from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_options_data_request_type import PushOptionsDataRequestType, check_push_options_data_request_type
from ..models.push_options_data_service_name import PushOptionsDataServiceName, check_push_options_data_service_name

if TYPE_CHECKING:
    from ..models.property_ import Property


T = TypeVar("T", bound="PushOptionsData")


@_attrs_define
class PushOptionsData:
    """
    Attributes:
        title (str):
        request_type (PushOptionsDataRequestType):  Example: accounts.
        service_name (PushOptionsDataServiceName):  Example: quickbooks.
        method (str):
        properties (Property):
    """

    title: str
    request_type: PushOptionsDataRequestType
    service_name: PushOptionsDataServiceName
    method: str
    properties: "Property"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        request_type: str = self.request_type

        service_name: str = self.service_name

        method = self.method

        properties = self.properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "requestType": request_type,
                "serviceName": service_name,
                "method": method,
                "properties": properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_ import Property

        d = src_dict.copy()
        title = d.pop("title")

        request_type = check_push_options_data_request_type(d.pop("requestType"))

        service_name = check_push_options_data_service_name(d.pop("serviceName"))

        method = d.pop("method")

        properties = Property.from_dict(d.pop("properties"))

        push_options_data = cls(
            title=title,
            request_type=request_type,
            service_name=service_name,
            method=method,
            properties=properties,
        )

        push_options_data.additional_properties = d
        return push_options_data

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
