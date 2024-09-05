from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_update_bills_connection_service_name import (
    PushUpdateBillsConnectionServiceName,
    check_push_update_bills_connection_service_name,
)

T = TypeVar("T", bound="PushUpdateBillsConnection")


@_attrs_define
class PushUpdateBillsConnection:
    """
    Attributes:
        business_name (str): Unique business name identifier. Example: Railz.
        service_name (PushUpdateBillsConnectionServiceName): Name of accounting platform service. Example: quickbooks.
    """

    business_name: str
    service_name: PushUpdateBillsConnectionServiceName
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_name = self.business_name

        service_name: str = self.service_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "businessName": business_name,
                "serviceName": service_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        business_name = d.pop("businessName")

        service_name = check_push_update_bills_connection_service_name(d.pop("serviceName"))

        push_update_bills_connection = cls(
            business_name=business_name,
            service_name=service_name,
        )

        push_update_bills_connection.additional_properties = d
        return push_update_bills_connection

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
