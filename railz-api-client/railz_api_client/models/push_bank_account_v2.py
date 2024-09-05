from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_bank_account_v2_account_type import (
    PushBankAccountV2AccountType,
    check_push_bank_account_v2_account_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PushBankAccountV2")


@_attrs_define
class PushBankAccountV2:
    """
    Attributes:
        id (Union[Unset, str]):  Example: lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDje.
        nominal_code (Union[Unset, str]):  Example: 200.
        name (Union[Unset, str]):  Example: Business Bank Account.
        account_type (Union[Unset, PushBankAccountV2AccountType]):  Example: checking.
        account_number (Union[Unset, str]):  Example: 11200.
        routing_number (Union[Unset, str]):  Example: 123456789.
        bank_code (Union[Unset, str]):  Example: TD.
        i_ban (Union[Unset, str]):  Example: CA123456789012345678901234.
        institution_name (Union[Unset, str]):  Example: TD Bank.
        currency (Union[Unset, str]):  Example: CAD.
        current_balance (Union[Unset, float]):  Example: 24.55.
        overdraft_limit (Union[Unset, float]):  Example: 8.75.
        available_balance (Union[Unset, float]):  Example: 5.55.
        is_active (Union[Unset, bool]):  Example: True.
    """

    id: Union[Unset, str] = UNSET
    nominal_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    account_type: Union[Unset, PushBankAccountV2AccountType] = UNSET
    account_number: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    bank_code: Union[Unset, str] = UNSET
    i_ban: Union[Unset, str] = UNSET
    institution_name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    current_balance: Union[Unset, float] = UNSET
    overdraft_limit: Union[Unset, float] = UNSET
    available_balance: Union[Unset, float] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        nominal_code = self.nominal_code

        name = self.name

        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type

        account_number = self.account_number

        routing_number = self.routing_number

        bank_code = self.bank_code

        i_ban = self.i_ban

        institution_name = self.institution_name

        currency = self.currency

        current_balance = self.current_balance

        overdraft_limit = self.overdraft_limit

        available_balance = self.available_balance

        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if nominal_code is not UNSET:
            field_dict["nominalCode"] = nominal_code
        if name is not UNSET:
            field_dict["name"] = name
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if bank_code is not UNSET:
            field_dict["bankCode"] = bank_code
        if i_ban is not UNSET:
            field_dict["iBan"] = i_ban
        if institution_name is not UNSET:
            field_dict["institutionName"] = institution_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if current_balance is not UNSET:
            field_dict["currentBalance"] = current_balance
        if overdraft_limit is not UNSET:
            field_dict["overdraftLimit"] = overdraft_limit
        if available_balance is not UNSET:
            field_dict["availableBalance"] = available_balance
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        nominal_code = d.pop("nominalCode", UNSET)

        name = d.pop("name", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, PushBankAccountV2AccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = check_push_bank_account_v2_account_type(_account_type)

        account_number = d.pop("accountNumber", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        bank_code = d.pop("bankCode", UNSET)

        i_ban = d.pop("iBan", UNSET)

        institution_name = d.pop("institutionName", UNSET)

        currency = d.pop("currency", UNSET)

        current_balance = d.pop("currentBalance", UNSET)

        overdraft_limit = d.pop("overdraftLimit", UNSET)

        available_balance = d.pop("availableBalance", UNSET)

        is_active = d.pop("isActive", UNSET)

        push_bank_account_v2 = cls(
            id=id,
            nominal_code=nominal_code,
            name=name,
            account_type=account_type,
            account_number=account_number,
            routing_number=routing_number,
            bank_code=bank_code,
            i_ban=i_ban,
            institution_name=institution_name,
            currency=currency,
            current_balance=current_balance,
            overdraft_limit=overdraft_limit,
            available_balance=available_balance,
            is_active=is_active,
        )

        push_bank_account_v2.additional_properties = d
        return push_bank_account_v2

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
