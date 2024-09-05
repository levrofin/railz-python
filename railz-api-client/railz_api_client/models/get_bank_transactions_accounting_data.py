import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bank_transactions_accounting_data_transaction_type import (
    GetBankTransactionsAccountingDataTransactionType,
    check_get_bank_transactions_accounting_data_transaction_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.bank_transactions_accounting_line_item import BankTransactionsAccountingLineItem
    from ..models.entity_ref_v2 import EntityRefV2


T = TypeVar("T", bound="GetBankTransactionsAccountingData")


@_attrs_define
class GetBankTransactionsAccountingData:
    """
    Attributes:
        id (str):  Example: 25.
        posted_date (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
        transaction_type (GetBankTransactionsAccountingDataTransactionType):  Example: payment.
        total_amount (float):  Example: 322.
        bank_account_ref (Union[Unset, AccountRef]):
        currency (Union[Unset, str]):  Example: CAD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        is_reconciled (Union[Unset, bool]):
        lines (Union[Unset, BankTransactionsAccountingLineItem]):
        memo (Union[Unset, str]):  Example: Example memo..
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        entity_ref (Union[Unset, EntityRefV2]):
    """

    id: str
    posted_date: datetime.datetime
    transaction_type: GetBankTransactionsAccountingDataTransactionType
    total_amount: float
    bank_account_ref: Union[Unset, "AccountRef"] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    is_reconciled: Union[Unset, bool] = UNSET
    lines: Union[Unset, "BankTransactionsAccountingLineItem"] = UNSET
    memo: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    entity_ref: Union[Unset, "EntityRefV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        posted_date = self.posted_date.isoformat()

        transaction_type: str = self.transaction_type

        total_amount = self.total_amount

        bank_account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bank_account_ref, Unset):
            bank_account_ref = self.bank_account_ref.to_dict()

        currency = self.currency

        currency_rate = self.currency_rate

        is_reconciled = self.is_reconciled

        lines: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = self.lines.to_dict()

        memo = self.memo

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "postedDate": posted_date,
                "transactionType": transaction_type,
                "totalAmount": total_amount,
            }
        )
        if bank_account_ref is not UNSET:
            field_dict["bankAccountRef"] = bank_account_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if is_reconciled is not UNSET:
            field_dict["isReconciled"] = is_reconciled
        if lines is not UNSET:
            field_dict["lines"] = lines
        if memo is not UNSET:
            field_dict["memo"] = memo
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.bank_transactions_accounting_line_item import BankTransactionsAccountingLineItem
        from ..models.entity_ref_v2 import EntityRefV2

        d = src_dict.copy()
        id = d.pop("id")

        posted_date = isoparse(d.pop("postedDate"))

        transaction_type = check_get_bank_transactions_accounting_data_transaction_type(d.pop("transactionType"))

        total_amount = d.pop("totalAmount")

        _bank_account_ref = d.pop("bankAccountRef", UNSET)
        bank_account_ref: Union[Unset, AccountRef]
        if isinstance(_bank_account_ref, Unset):
            bank_account_ref = UNSET
        else:
            bank_account_ref = AccountRef.from_dict(_bank_account_ref)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        is_reconciled = d.pop("isReconciled", UNSET)

        _lines = d.pop("lines", UNSET)
        lines: Union[Unset, BankTransactionsAccountingLineItem]
        if isinstance(_lines, Unset):
            lines = UNSET
        else:
            lines = BankTransactionsAccountingLineItem.from_dict(_lines)

        memo = d.pop("memo", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, EntityRefV2]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = EntityRefV2.from_dict(_entity_ref)

        get_bank_transactions_accounting_data = cls(
            id=id,
            posted_date=posted_date,
            transaction_type=transaction_type,
            total_amount=total_amount,
            bank_account_ref=bank_account_ref,
            currency=currency,
            currency_rate=currency_rate,
            is_reconciled=is_reconciled,
            lines=lines,
            memo=memo,
            source_modified_date=source_modified_date,
            entity_ref=entity_ref,
        )

        get_bank_transactions_accounting_data.additional_properties = d
        return get_bank_transactions_accounting_data

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
