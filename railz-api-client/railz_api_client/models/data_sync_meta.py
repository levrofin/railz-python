from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_sync_meta_service_name import DataSyncMetaServiceName

T = TypeVar("T", bound="DataSyncMeta")


@_attrs_define
class DataSyncMeta:
    """
    Attributes:
        service_name (DataSyncMetaServiceName):  Example: xero.
        business_name (str):  Example: Demo Business.
    """

    service_name: DataSyncMetaServiceName
    business_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_name = self.service_name

        business_name = self.business_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceName": service_name,
                "businessName": business_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_name = d.pop("serviceName")

        business_name = d.pop("businessName")

        data_sync_meta = cls(
            service_name=service_name,
            business_name=business_name,
        )

        data_sync_meta.additional_properties = d
        return data_sync_meta

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
