import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_journal_data_status import GetJournalDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.journal_parent_ref import JournalParentRef


T = TypeVar("T", bound="GetJournalData")


@_attrs_define
class GetJournalData:
    """
    Attributes:
        id (str):  Example: 1234.
        name (str):  Example: General Ledger.
        status (GetJournalDataStatus):
        journal_code (Union[Unset, str]):  Example: GL.
        parent_ref (Union[Unset, JournalParentRef]):
        type (Union[Unset, str]):  Example: General.
        has_children (Union[Unset, bool]):  Example: True.
        created_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
    """

    id: str
    name: str
    status: GetJournalDataStatus
    journal_code: Union[Unset, str] = UNSET
    parent_ref: Union[Unset, "JournalParentRef"] = UNSET
    type: Union[Unset, str] = UNSET
    has_children: Union[Unset, bool] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        journal_code = self.journal_code

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        type = self.type

        has_children = self.has_children

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
            }
        )
        if journal_code is not UNSET:
            field_dict["journalCode"] = journal_code
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if type is not UNSET:
            field_dict["type"] = type
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.journal_parent_ref import JournalParentRef

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = d.pop("status")

        journal_code = d.pop("journalCode", UNSET)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, JournalParentRef]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = JournalParentRef.from_dict(_parent_ref)

        type = d.pop("type", UNSET)

        has_children = d.pop("hasChildren", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_journal_data = cls(
            id=id,
            name=name,
            status=status,
            journal_code=journal_code,
            parent_ref=parent_ref,
            type=type,
            has_children=has_children,
            created_date=created_date,
            source_modified_date=source_modified_date,
        )

        get_journal_data.additional_properties = d
        return get_journal_data

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
