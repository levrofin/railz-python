import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reconciled_bank_transactions_accounting_transaction_type import (
    ReconciledBankTransactionsAccountingTransactionType,
    check_reconciled_bank_transactions_accounting_transaction_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_ref import EntityRef
    from ..models.reconcilation_account_ref import ReconcilationAccountRef


T = TypeVar("T", bound="ReconciledBankTransactions")


@_attrs_define
class ReconciledBankTransactions:
    """
    Attributes:
        id (str):  Example: lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDje.
        date (datetime.datetime):  Example: 2017-01-29.
        amount (float):  Example: 1000.
        account_id (str):  Example: onD7kPQJ98cDejlnXpZeHeqp1qBlX5TogLqxW.
        accounting_transaction_id (str):  Example: 13.
        account_ref (ReconcilationAccountRef):
        account_type (Union[Unset, str]):  Example: investment, credit, depository, loan, brokerage, other.
        description (Union[Unset, str]):  Example: BMO Bank of Montreal.
        accounting_transaction_type (Union[Unset, ReconciledBankTransactionsAccountingTransactionType]):
        is_posting (Union[Unset, bool]):  Example: true.
        is_split_transaction (Union[Unset, bool]):  Example: true.
        sub_total (Union[Unset, float]):  Example: 300.5.
        transaction_number (Union[Unset, str]):  Example: INV-001.
        transaction_report_id (Union[Unset, str]):  Example: 5fad8a342a88364234392fb6.
        entity_ref (Union[Unset, EntityRef]):
    """

    id: str
    date: datetime.datetime
    amount: float
    account_id: str
    accounting_transaction_id: str
    account_ref: "ReconcilationAccountRef"
    account_type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    accounting_transaction_type: Union[Unset, ReconciledBankTransactionsAccountingTransactionType] = UNSET
    is_posting: Union[Unset, bool] = UNSET
    is_split_transaction: Union[Unset, bool] = UNSET
    sub_total: Union[Unset, float] = UNSET
    transaction_number: Union[Unset, str] = UNSET
    transaction_report_id: Union[Unset, str] = UNSET
    entity_ref: Union[Unset, "EntityRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        amount = self.amount

        account_id = self.account_id

        accounting_transaction_id = self.accounting_transaction_id

        account_ref = self.account_ref.to_dict()

        account_type = self.account_type

        description = self.description

        accounting_transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.accounting_transaction_type, Unset):
            accounting_transaction_type = self.accounting_transaction_type

        is_posting = self.is_posting

        is_split_transaction = self.is_split_transaction

        sub_total = self.sub_total

        transaction_number = self.transaction_number

        transaction_report_id = self.transaction_report_id

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "amount": amount,
                "accountId": account_id,
                "accountingTransactionId": accounting_transaction_id,
                "accountRef": account_ref,
            }
        )
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if description is not UNSET:
            field_dict["description"] = description
        if accounting_transaction_type is not UNSET:
            field_dict["accountingTransactionType"] = accounting_transaction_type
        if is_posting is not UNSET:
            field_dict["isPosting"] = is_posting
        if is_split_transaction is not UNSET:
            field_dict["isSplitTransaction"] = is_split_transaction
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if transaction_number is not UNSET:
            field_dict["transactionNumber"] = transaction_number
        if transaction_report_id is not UNSET:
            field_dict["transactionReportId"] = transaction_report_id
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_ref import EntityRef
        from ..models.reconcilation_account_ref import ReconcilationAccountRef

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        amount = d.pop("amount")

        account_id = d.pop("accountId")

        accounting_transaction_id = d.pop("accountingTransactionId")

        account_ref = ReconcilationAccountRef.from_dict(d.pop("accountRef"))

        account_type = d.pop("accountType", UNSET)

        description = d.pop("description", UNSET)

        _accounting_transaction_type = d.pop("accountingTransactionType", UNSET)
        accounting_transaction_type: Union[Unset, ReconciledBankTransactionsAccountingTransactionType]
        if isinstance(_accounting_transaction_type, Unset):
            accounting_transaction_type = UNSET
        else:
            accounting_transaction_type = check_reconciled_bank_transactions_accounting_transaction_type(
                _accounting_transaction_type
            )

        is_posting = d.pop("isPosting", UNSET)

        is_split_transaction = d.pop("isSplitTransaction", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        transaction_number = d.pop("transactionNumber", UNSET)

        transaction_report_id = d.pop("transactionReportId", UNSET)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, EntityRef]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = EntityRef.from_dict(_entity_ref)

        reconciled_bank_transactions = cls(
            id=id,
            date=date,
            amount=amount,
            account_id=account_id,
            accounting_transaction_id=accounting_transaction_id,
            account_ref=account_ref,
            account_type=account_type,
            description=description,
            accounting_transaction_type=accounting_transaction_type,
            is_posting=is_posting,
            is_split_transaction=is_split_transaction,
            sub_total=sub_total,
            transaction_number=transaction_number,
            transaction_report_id=transaction_report_id,
            entity_ref=entity_ref,
        )

        reconciled_bank_transactions.additional_properties = d
        return reconciled_bank_transactions

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
