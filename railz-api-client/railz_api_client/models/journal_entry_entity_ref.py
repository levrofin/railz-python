from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.journal_entry_entity_ref_type import JournalEntryEntityRefType, check_journal_entry_entity_ref_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="JournalEntryEntityRef")


@_attrs_define
class JournalEntryEntityRef:
    """
    Attributes:
        id (str):  Example: 1.
        name (Union[Unset, str]):  Example: ABC Inc..
        type (Union[Unset, JournalEntryEntityRefType]):  Example: vendor.
    """

    id: str
    name: Union[Unset, str] = UNSET
    type: Union[Unset, JournalEntryEntityRefType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, JournalEntryEntityRefType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_journal_entry_entity_ref_type(_type)

        journal_entry_entity_ref = cls(
            id=id,
            name=name,
            type=type,
        )

        journal_entry_entity_ref.additional_properties = d
        return journal_entry_entity_ref

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
