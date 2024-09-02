from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_transactions import BankTransactions
    from ..models.reconciled_bank_transactions import ReconciledBankTransactions


T = TypeVar("T", bound="BankReconciliationData")


@_attrs_define
class BankReconciliationData:
    """
    Attributes:
        bank_transactions_count (float):  Example: 35.
        accounting_transactions_count (float):  Example: 50.
        bank_transactions_amount (float):  Example: 105.5.
        accounting_transactions_amount (float):  Example: 750.5.
        bank_transactions_total_value (float):  Example: 109.95.
        accounting_transactions_total_value (float):  Example: 500.5.
        weighted_percentage_error (float):  Example: 1.
        accuracy_score (float):  Example: 50.5.
        bank_transactions_unreconciled_count (float):  Example: 25.
        bank_transactions_unreconciled_amount (float):  Example: 109.95.
        daily_accuracy_score (float):  Example: 0.24.
        unreconciled_bank_transactions (Union[Unset, List['BankTransactions']]):
        reconciled_bank_transactions (Union[Unset, List['ReconciledBankTransactions']]):
    """

    bank_transactions_count: float
    accounting_transactions_count: float
    bank_transactions_amount: float
    accounting_transactions_amount: float
    bank_transactions_total_value: float
    accounting_transactions_total_value: float
    weighted_percentage_error: float
    accuracy_score: float
    bank_transactions_unreconciled_count: float
    bank_transactions_unreconciled_amount: float
    daily_accuracy_score: float
    unreconciled_bank_transactions: Union[Unset, List["BankTransactions"]] = UNSET
    reconciled_bank_transactions: Union[Unset, List["ReconciledBankTransactions"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bank_transactions_count = self.bank_transactions_count

        accounting_transactions_count = self.accounting_transactions_count

        bank_transactions_amount = self.bank_transactions_amount

        accounting_transactions_amount = self.accounting_transactions_amount

        bank_transactions_total_value = self.bank_transactions_total_value

        accounting_transactions_total_value = self.accounting_transactions_total_value

        weighted_percentage_error = self.weighted_percentage_error

        accuracy_score = self.accuracy_score

        bank_transactions_unreconciled_count = self.bank_transactions_unreconciled_count

        bank_transactions_unreconciled_amount = self.bank_transactions_unreconciled_amount

        daily_accuracy_score = self.daily_accuracy_score

        unreconciled_bank_transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unreconciled_bank_transactions, Unset):
            unreconciled_bank_transactions = []
            for unreconciled_bank_transactions_item_data in self.unreconciled_bank_transactions:
                unreconciled_bank_transactions_item = unreconciled_bank_transactions_item_data.to_dict()
                unreconciled_bank_transactions.append(unreconciled_bank_transactions_item)

        reconciled_bank_transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.reconciled_bank_transactions, Unset):
            reconciled_bank_transactions = []
            for reconciled_bank_transactions_item_data in self.reconciled_bank_transactions:
                reconciled_bank_transactions_item = reconciled_bank_transactions_item_data.to_dict()
                reconciled_bank_transactions.append(reconciled_bank_transactions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bankTransactionsCount": bank_transactions_count,
                "accountingTransactionsCount": accounting_transactions_count,
                "bankTransactionsAmount": bank_transactions_amount,
                "accountingTransactionsAmount": accounting_transactions_amount,
                "bankTransactionsTotalValue": bank_transactions_total_value,
                "accountingTransactionsTotalValue": accounting_transactions_total_value,
                "weightedPercentageError": weighted_percentage_error,
                "accuracyScore": accuracy_score,
                "bankTransactionsUnreconciledCount": bank_transactions_unreconciled_count,
                "bankTransactionsUnreconciledAmount": bank_transactions_unreconciled_amount,
                "dailyAccuracyScore": daily_accuracy_score,
            }
        )
        if unreconciled_bank_transactions is not UNSET:
            field_dict["unreconciledBankTransactions"] = unreconciled_bank_transactions
        if reconciled_bank_transactions is not UNSET:
            field_dict["reconciledBankTransactions"] = reconciled_bank_transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_transactions import BankTransactions
        from ..models.reconciled_bank_transactions import ReconciledBankTransactions

        d = src_dict.copy()
        bank_transactions_count = d.pop("bankTransactionsCount")

        accounting_transactions_count = d.pop("accountingTransactionsCount")

        bank_transactions_amount = d.pop("bankTransactionsAmount")

        accounting_transactions_amount = d.pop("accountingTransactionsAmount")

        bank_transactions_total_value = d.pop("bankTransactionsTotalValue")

        accounting_transactions_total_value = d.pop("accountingTransactionsTotalValue")

        weighted_percentage_error = d.pop("weightedPercentageError")

        accuracy_score = d.pop("accuracyScore")

        bank_transactions_unreconciled_count = d.pop("bankTransactionsUnreconciledCount")

        bank_transactions_unreconciled_amount = d.pop("bankTransactionsUnreconciledAmount")

        daily_accuracy_score = d.pop("dailyAccuracyScore")

        unreconciled_bank_transactions = []
        _unreconciled_bank_transactions = d.pop("unreconciledBankTransactions", UNSET)
        for unreconciled_bank_transactions_item_data in _unreconciled_bank_transactions or []:
            unreconciled_bank_transactions_item = BankTransactions.from_dict(unreconciled_bank_transactions_item_data)

            unreconciled_bank_transactions.append(unreconciled_bank_transactions_item)

        reconciled_bank_transactions = []
        _reconciled_bank_transactions = d.pop("reconciledBankTransactions", UNSET)
        for reconciled_bank_transactions_item_data in _reconciled_bank_transactions or []:
            reconciled_bank_transactions_item = ReconciledBankTransactions.from_dict(
                reconciled_bank_transactions_item_data
            )

            reconciled_bank_transactions.append(reconciled_bank_transactions_item)

        bank_reconciliation_data = cls(
            bank_transactions_count=bank_transactions_count,
            accounting_transactions_count=accounting_transactions_count,
            bank_transactions_amount=bank_transactions_amount,
            accounting_transactions_amount=accounting_transactions_amount,
            bank_transactions_total_value=bank_transactions_total_value,
            accounting_transactions_total_value=accounting_transactions_total_value,
            weighted_percentage_error=weighted_percentage_error,
            accuracy_score=accuracy_score,
            bank_transactions_unreconciled_count=bank_transactions_unreconciled_count,
            bank_transactions_unreconciled_amount=bank_transactions_unreconciled_amount,
            daily_accuracy_score=daily_accuracy_score,
            unreconciled_bank_transactions=unreconciled_bank_transactions,
            reconciled_bank_transactions=reconciled_bank_transactions,
        )

        bank_reconciliation_data.additional_properties = d
        return bank_reconciliation_data

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
