from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_journals_data_status import PushJournalsDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_journals_data_pass_through import PushJournalsDataPassThrough


T = TypeVar("T", bound="PushJournalsData")


@_attrs_define
class PushJournalsData:
    """
    Attributes:
        journal_code (str):  Example: GL.
        name (str):  Example: General Ledger.
        status (PushJournalsDataStatus):
        pass_through (Union[Unset, PushJournalsDataPassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    journal_code: str
    name: str
    status: PushJournalsDataStatus
    pass_through: Union[Unset, "PushJournalsDataPassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        journal_code = self.journal_code

        name = self.name

        status = self.status

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "journalCode": journal_code,
                "name": name,
                "status": status,
            }
        )
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_journals_data_pass_through import PushJournalsDataPassThrough

        d = src_dict.copy()
        journal_code = d.pop("journalCode")

        name = d.pop("name")

        status = d.pop("status")

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushJournalsDataPassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushJournalsDataPassThrough.from_dict(_pass_through)

        push_journals_data = cls(
            journal_code=journal_code,
            name=name,
            status=status,
            pass_through=pass_through,
        )

        push_journals_data.additional_properties = d
        return push_journals_data

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
