import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BankTransactions")


@_attrs_define
class BankTransactions:
    """
    Attributes:
        id (str):  Example: lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDje.
        date (datetime.datetime):  Example: 2017-01-29.
        amount (float):  Example: 1000.
        account_id (str):  Example: onD7kPQJ98cDejlnXpZeHeqp1qBlX5TogLqxW.
        account_type (Union[Unset, str]):  Example: investment, credit, depository, loan, brokerage, other.
        description (Union[Unset, str]):  Example: BMO Bank of Montreal.
    """

    id: str
    date: datetime.datetime
    amount: float
    account_id: str
    account_type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        amount = self.amount

        account_id = self.account_id

        account_type = self.account_type

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "amount": amount,
                "accountId": account_id,
            }
        )
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        amount = d.pop("amount")

        account_id = d.pop("accountId")

        account_type = d.pop("accountType", UNSET)

        description = d.pop("description", UNSET)

        bank_transactions = cls(
            id=id,
            date=date,
            amount=amount,
            account_id=account_id,
            account_type=account_type,
            description=description,
        )

        bank_transactions.additional_properties = d
        return bank_transactions

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
