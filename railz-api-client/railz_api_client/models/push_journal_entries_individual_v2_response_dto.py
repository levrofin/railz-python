import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.push_journal_entries_individual_v2_response_dto_status import (
    PushJournalEntriesIndividualV2ResponseDtoStatus,
    check_push_journal_entries_individual_v2_response_dto_status,
)

if TYPE_CHECKING:
    from ..models.push_journal_entries_v2 import PushJournalEntriesV2


T = TypeVar("T", bound="PushJournalEntriesIndividualV2ResponseDto")


@_attrs_define
class PushJournalEntriesIndividualV2ResponseDto:
    """
    Attributes:
        push_communication_id (str):  Example: 60473b57f0cdd1683ca71f60.
        requested_on (datetime.datetime):  Example: 2021-03-09T08:15:22.035Z.
        status (PushJournalEntriesIndividualV2ResponseDtoStatus):  Example: pending.
        data (PushJournalEntriesV2):
    """

    push_communication_id: str
    requested_on: datetime.datetime
    status: PushJournalEntriesIndividualV2ResponseDtoStatus
    data: "PushJournalEntriesV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        push_communication_id = self.push_communication_id

        requested_on = self.requested_on.isoformat()

        status: str = self.status

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pushCommunicationId": push_communication_id,
                "requestedOn": requested_on,
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_journal_entries_v2 import PushJournalEntriesV2

        d = src_dict.copy()
        push_communication_id = d.pop("pushCommunicationId")

        requested_on = isoparse(d.pop("requestedOn"))

        status = check_push_journal_entries_individual_v2_response_dto_status(d.pop("status"))

        data = PushJournalEntriesV2.from_dict(d.pop("data"))

        push_journal_entries_individual_v2_response_dto = cls(
            push_communication_id=push_communication_id,
            requested_on=requested_on,
            status=status,
            data=data,
        )

        push_journal_entries_individual_v2_response_dto.additional_properties = d
        return push_journal_entries_individual_v2_response_dto

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
