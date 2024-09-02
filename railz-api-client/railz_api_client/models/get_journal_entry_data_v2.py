import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_journal_entry_line_items_v2 import GetJournalEntryLineItemsV2
    from ..models.journal_ref_dto import JournalRefDto
    from ..models.subsidiary_ref import SubsidiaryRef


T = TypeVar("T", bound="GetJournalEntryDataV2")


@_attrs_define
class GetJournalEntryDataV2:
    """
    Attributes:
        id (str):  Example: 1.
        lines (List['GetJournalEntryLineItemsV2']):
        posted_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        created_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        memo (Union[Unset, str]):  Example: Example bill memo..
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        total_credit (Union[Unset, float]):  Example: 129.99.
        total_debit (Union[Unset, float]):  Example: 129.99.
        journal_number (Union[Unset, str]):  Example: 123.
        currency (Union[Unset, str]):  Example: USD.
        journal_ref (Union[Unset, JournalRefDto]):
    """

    id: str
    lines: List["GetJournalEntryLineItemsV2"]
    posted_date: Union[Unset, datetime.datetime] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    memo: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    total_credit: Union[Unset, float] = UNSET
    total_debit: Union[Unset, float] = UNSET
    journal_number: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    journal_ref: Union[Unset, "JournalRefDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        currency_rate = self.currency_rate

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        memo = self.memo

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        total_credit = self.total_credit

        total_debit = self.total_debit

        journal_number = self.journal_number

        currency = self.currency

        journal_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.journal_ref, Unset):
            journal_ref = self.journal_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "lines": lines,
            }
        )
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if memo is not UNSET:
            field_dict["memo"] = memo
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if total_credit is not UNSET:
            field_dict["totalCredit"] = total_credit
        if total_debit is not UNSET:
            field_dict["totalDebit"] = total_debit
        if journal_number is not UNSET:
            field_dict["journalNumber"] = journal_number
        if currency is not UNSET:
            field_dict["currency"] = currency
        if journal_ref is not UNSET:
            field_dict["journalRef"] = journal_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_journal_entry_line_items_v2 import GetJournalEntryLineItemsV2
        from ..models.journal_ref_dto import JournalRefDto
        from ..models.subsidiary_ref import SubsidiaryRef

        d = src_dict.copy()
        id = d.pop("id")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = GetJournalEntryLineItemsV2.from_dict(lines_item_data)

            lines.append(lines_item)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        currency_rate = d.pop("currencyRate", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRef.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        memo = d.pop("memo", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        total_credit = d.pop("totalCredit", UNSET)

        total_debit = d.pop("totalDebit", UNSET)

        journal_number = d.pop("journalNumber", UNSET)

        currency = d.pop("currency", UNSET)

        _journal_ref = d.pop("journalRef", UNSET)
        journal_ref: Union[Unset, JournalRefDto]
        if isinstance(_journal_ref, Unset):
            journal_ref = UNSET
        else:
            journal_ref = JournalRefDto.from_dict(_journal_ref)

        get_journal_entry_data_v2 = cls(
            id=id,
            lines=lines,
            posted_date=posted_date,
            created_date=created_date,
            currency_rate=currency_rate,
            subsidiary_refs=subsidiary_refs,
            memo=memo,
            source_modified_date=source_modified_date,
            total_credit=total_credit,
            total_debit=total_debit,
            journal_number=journal_number,
            currency=currency,
            journal_ref=journal_ref,
        )

        get_journal_entry_data_v2.additional_properties = d
        return get_journal_entry_data_v2

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
