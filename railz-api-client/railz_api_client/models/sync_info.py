import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sync_info_status import SyncInfoStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncInfo")


@_attrs_define
class SyncInfo:
    """
    Attributes:
        status (SyncInfoStatus):
        created_at (datetime.datetime):  Example: 2021-03-09T08:49:36.035Z.
        first_sync_date (datetime.datetime):  Example: 2021-04-11T08:49:36.035Z.
        queue_time (Union[Unset, float]):
        sync_time (Union[Unset, float]):
        sync_type (Union[Unset, str]):
        percentage_completed (Union[Unset, float]):
    """

    status: SyncInfoStatus
    created_at: datetime.datetime
    first_sync_date: datetime.datetime
    queue_time: Union[Unset, float] = UNSET
    sync_time: Union[Unset, float] = UNSET
    sync_type: Union[Unset, str] = UNSET
    percentage_completed: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        created_at = self.created_at.isoformat()

        first_sync_date = self.first_sync_date.isoformat()

        queue_time = self.queue_time

        sync_time = self.sync_time

        sync_type = self.sync_type

        percentage_completed = self.percentage_completed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "createdAt": created_at,
                "firstSyncDate": first_sync_date,
            }
        )
        if queue_time is not UNSET:
            field_dict["queueTime"] = queue_time
        if sync_time is not UNSET:
            field_dict["syncTime"] = sync_time
        if sync_type is not UNSET:
            field_dict["syncType"] = sync_type
        if percentage_completed is not UNSET:
            field_dict["percentageCompleted"] = percentage_completed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        created_at = isoparse(d.pop("createdAt"))

        first_sync_date = isoparse(d.pop("firstSyncDate"))

        queue_time = d.pop("queueTime", UNSET)

        sync_time = d.pop("syncTime", UNSET)

        sync_type = d.pop("syncType", UNSET)

        percentage_completed = d.pop("percentageCompleted", UNSET)

        sync_info = cls(
            status=status,
            created_at=created_at,
            first_sync_date=first_sync_date,
            queue_time=queue_time,
            sync_time=sync_time,
            sync_type=sync_type,
            percentage_completed=percentage_completed,
        )

        sync_info.additional_properties = d
        return sync_info

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
