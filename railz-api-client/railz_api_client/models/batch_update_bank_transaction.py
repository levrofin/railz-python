import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.batch_update_bank_transaction_transaction_type import (
    BatchUpdateBankTransactionTransactionType,
    check_batch_update_bank_transaction_transaction_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_account_ref_dto import BankAccountRefDto
    from ..models.batch_update_bank_transaction_pass_through import BatchUpdateBankTransactionPassThrough
    from ..models.entity_ref_dto import EntityRefDto
    from ..models.update_bank_transaction_line import UpdateBankTransactionLine


T = TypeVar("T", bound="BatchUpdateBankTransaction")


@_attrs_define
class BatchUpdateBankTransaction:
    """
    Attributes:
        transaction_type (BatchUpdateBankTransactionTransactionType):  Example: payment.
        bank_transaction_ref (str): reference to the bank transaction to be updated
        pass_through (Union[Unset, BatchUpdateBankTransactionPassThrough]):  Example: {'CustomField': [{'DefinitionId':
            '1', 'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        currency (Union[Unset, str]):  Example: CAD.
        bank_account_ref (Union[Unset, BankAccountRefDto]):
        entity_ref (Union[Unset, EntityRefDto]):
        total_amount (Union[Unset, float]):  Example: 150.50.
        lines (Union[Unset, List['UpdateBankTransactionLine']]):
        memo (Union[Unset, str]):  Example: Example memo..
        posted_date (Union[Unset, datetime.datetime]):  Example: 2020-11-30.
    """

    transaction_type: BatchUpdateBankTransactionTransactionType
    bank_transaction_ref: str
    pass_through: Union[Unset, "BatchUpdateBankTransactionPassThrough"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    bank_account_ref: Union[Unset, "BankAccountRefDto"] = UNSET
    entity_ref: Union[Unset, "EntityRefDto"] = UNSET
    total_amount: Union[Unset, float] = UNSET
    lines: Union[Unset, List["UpdateBankTransactionLine"]] = UNSET
    memo: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_type: str = self.transaction_type

        bank_transaction_ref = self.bank_transaction_ref

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        currency_rate = self.currency_rate

        currency = self.currency

        bank_account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bank_account_ref, Unset):
            bank_account_ref = self.bank_account_ref.to_dict()

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

        total_amount = self.total_amount

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        memo = self.memo

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactionType": transaction_type,
                "bankTransactionRef": bank_transaction_ref,
            }
        )
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if currency is not UNSET:
            field_dict["currency"] = currency
        if bank_account_ref is not UNSET:
            field_dict["bankAccountRef"] = bank_account_ref
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if lines is not UNSET:
            field_dict["lines"] = lines
        if memo is not UNSET:
            field_dict["memo"] = memo
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_account_ref_dto import BankAccountRefDto
        from ..models.batch_update_bank_transaction_pass_through import BatchUpdateBankTransactionPassThrough
        from ..models.entity_ref_dto import EntityRefDto
        from ..models.update_bank_transaction_line import UpdateBankTransactionLine

        d = src_dict.copy()
        transaction_type = check_batch_update_bank_transaction_transaction_type(d.pop("transactionType"))

        bank_transaction_ref = d.pop("bankTransactionRef")

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, BatchUpdateBankTransactionPassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = BatchUpdateBankTransactionPassThrough.from_dict(_pass_through)

        currency_rate = d.pop("currencyRate", UNSET)

        currency = d.pop("currency", UNSET)

        _bank_account_ref = d.pop("bankAccountRef", UNSET)
        bank_account_ref: Union[Unset, BankAccountRefDto]
        if isinstance(_bank_account_ref, Unset):
            bank_account_ref = UNSET
        else:
            bank_account_ref = BankAccountRefDto.from_dict(_bank_account_ref)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, EntityRefDto]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = EntityRefDto.from_dict(_entity_ref)

        total_amount = d.pop("totalAmount", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = UpdateBankTransactionLine.from_dict(lines_item_data)

            lines.append(lines_item)

        memo = d.pop("memo", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        batch_update_bank_transaction = cls(
            transaction_type=transaction_type,
            bank_transaction_ref=bank_transaction_ref,
            pass_through=pass_through,
            currency_rate=currency_rate,
            currency=currency,
            bank_account_ref=bank_account_ref,
            entity_ref=entity_ref,
            total_amount=total_amount,
            lines=lines,
            memo=memo,
            posted_date=posted_date,
        )

        batch_update_bank_transaction.additional_properties = d
        return batch_update_bank_transaction

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
