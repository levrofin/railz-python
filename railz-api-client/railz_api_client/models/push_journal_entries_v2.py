import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_journal_ref_dto import BaseJournalRefDto
    from ..models.journal_entry_line_items_v2 import JournalEntryLineItemsV2
    from ..models.push_journal_entries_v2_pass_through import PushJournalEntriesV2PassThrough
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto


T = TypeVar("T", bound="PushJournalEntriesV2")


@_attrs_define
class PushJournalEntriesV2:
    """
    Attributes:
        lines (List['JournalEntryLineItemsV2']):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        memo (Union[Unset, str]):  Example: Services rendered..
        currency (Union[Unset, str]):  Example: CAD.
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        journal_ref (Union[Unset, BaseJournalRefDto]):
        created_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        journal_number (Union[Unset, str]):  Example: 1857648.
        pass_through (Union[Unset, PushJournalEntriesV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    lines: List["JournalEntryLineItemsV2"]
    currency_rate: Union[Unset, float] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    journal_ref: Union[Unset, "BaseJournalRefDto"] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    journal_number: Union[Unset, str] = UNSET
    pass_through: Union[Unset, "PushJournalEntriesV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        currency_rate = self.currency_rate

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        memo = self.memo

        currency = self.currency

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        journal_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.journal_ref, Unset):
            journal_ref = self.journal_ref.to_dict()

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        journal_number = self.journal_number

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lines": lines,
            }
        )
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if memo is not UNSET:
            field_dict["memo"] = memo
        if currency is not UNSET:
            field_dict["currency"] = currency
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if journal_ref is not UNSET:
            field_dict["journalRef"] = journal_ref
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if journal_number is not UNSET:
            field_dict["journalNumber"] = journal_number
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_journal_ref_dto import BaseJournalRefDto
        from ..models.journal_entry_line_items_v2 import JournalEntryLineItemsV2
        from ..models.push_journal_entries_v2_pass_through import PushJournalEntriesV2PassThrough
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto

        d = src_dict.copy()
        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = JournalEntryLineItemsV2.from_dict(lines_item_data)

            lines.append(lines_item)

        currency_rate = d.pop("currencyRate", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _journal_ref = d.pop("journalRef", UNSET)
        journal_ref: Union[Unset, BaseJournalRefDto]
        if isinstance(_journal_ref, Unset):
            journal_ref = UNSET
        else:
            journal_ref = BaseJournalRefDto.from_dict(_journal_ref)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        journal_number = d.pop("journalNumber", UNSET)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushJournalEntriesV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushJournalEntriesV2PassThrough.from_dict(_pass_through)

        push_journal_entries_v2 = cls(
            lines=lines,
            currency_rate=currency_rate,
            posted_date=posted_date,
            memo=memo,
            currency=currency,
            subsidiary_refs=subsidiary_refs,
            journal_ref=journal_ref,
            created_date=created_date,
            journal_number=journal_number,
            pass_through=pass_through,
        )

        push_journal_entries_v2.additional_properties = d
        return push_journal_entries_v2

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
