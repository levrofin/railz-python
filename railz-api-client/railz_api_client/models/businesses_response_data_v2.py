import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.base_connections_response_data_v2 import BaseConnectionsResponseDataV2


T = TypeVar("T", bound="BusinessesResponseDataV2")


@_attrs_define
class BusinessesResponseDataV2:
    """
    Attributes:
        business_uuid (str):  Example: BIZ-0f1ef788-54eb-4ed1-a7d3-5605febe6d84.
        business_name (str):  Example: Railz.
        status (str):  Example: active.
        created_at (datetime.datetime):  Example: 2020-12-25T01:02:03Z.
        updated_at (datetime.datetime):  Example: 2020-12-25T01:02:03Z.
        metadata (List[str]):  Example: [{'name': 'new business1', 'value': 'canada', 'webhookLocation': ['header',
            'body']}].
        connections (List['BaseConnectionsResponseDataV2']):
    """

    business_uuid: str
    business_name: str
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata: List[str]
    connections: List["BaseConnectionsResponseDataV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_uuid = self.business_uuid

        business_name = self.business_name

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        metadata = self.metadata

        connections = []
        for connections_item_data in self.connections:
            connections_item = connections_item_data.to_dict()
            connections.append(connections_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "businessUuid": business_uuid,
                "businessName": business_name,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "metadata": metadata,
                "connections": connections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_connections_response_data_v2 import BaseConnectionsResponseDataV2

        d = src_dict.copy()
        business_uuid = d.pop("businessUuid")

        business_name = d.pop("businessName")

        status = d.pop("status")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        metadata = cast(List[str], d.pop("metadata"))

        connections = []
        _connections = d.pop("connections")
        for connections_item_data in _connections:
            connections_item = BaseConnectionsResponseDataV2.from_dict(connections_item_data)

            connections.append(connections_item)

        businesses_response_data_v2 = cls(
            business_uuid=business_uuid,
            business_name=business_name,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            metadata=metadata,
            connections=connections,
        )

        businesses_response_data_v2.additional_properties = d
        return businesses_response_data_v2

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
