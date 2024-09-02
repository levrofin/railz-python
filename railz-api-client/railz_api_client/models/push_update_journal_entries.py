import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_update_journal_entry_line_items import PushUpdateJournalEntryLineItems


T = TypeVar("T", bound="PushUpdateJournalEntries")


@_attrs_define
class PushUpdateJournalEntries:
    """
    Attributes:
        currency_rate (Union[Unset, float]):  Example: 1.13.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-09.
        memo (Union[Unset, str]):  Example: Services rendered..
        currency (Union[Unset, str]):  Example: CAD.
        lines (Union[Unset, List['PushUpdateJournalEntryLineItems']]):
        subsidiary_refs (Union[Unset, List[str]]):  Example: ['1', '3'].
    """

    currency_rate: Union[Unset, float] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    lines: Union[Unset, List["PushUpdateJournalEntryLineItems"]] = UNSET
    subsidiary_refs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_rate = self.currency_rate

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        memo = self.memo

        currency = self.currency

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        subsidiary_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = self.subsidiary_refs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if memo is not UNSET:
            field_dict["memo"] = memo
        if currency is not UNSET:
            field_dict["currency"] = currency
        if lines is not UNSET:
            field_dict["lines"] = lines
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_update_journal_entry_line_items import PushUpdateJournalEntryLineItems

        d = src_dict.copy()
        currency_rate = d.pop("currencyRate", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = PushUpdateJournalEntryLineItems.from_dict(lines_item_data)

            lines.append(lines_item)

        subsidiary_refs = cast(List[str], d.pop("subsidiaryRefs", UNSET))

        push_update_journal_entries = cls(
            currency_rate=currency_rate,
            posted_date=posted_date,
            memo=memo,
            currency=currency,
            lines=lines,
            subsidiary_refs=subsidiary_refs,
        )

        push_update_journal_entries.additional_properties = d
        return push_update_journal_entries

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
