import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bank_account_accounting_data_v2_account_type import (
    GetBankAccountAccountingDataV2AccountType,
    check_get_bank_account_accounting_data_v2_account_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBankAccountAccountingDataV2")


@_attrs_define
class GetBankAccountAccountingDataV2:
    """
    Attributes:
        id (str):  Example: lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDje.
        account_type (GetBankAccountAccountingDataV2AccountType):  Example: checking.
        nominal_code (Union[Unset, str]):  Example: 200.
        name (Union[Unset, str]):  Example: Business Bank Account.
        account_number (Union[Unset, str]):  Example: 11200.
        routing_number (Union[Unset, str]):  Example: 123456789.
        ach_id (Union[Unset, str]):  Example: 123456789.
        bank_code (Union[Unset, str]):  Example: TD.
        i_ban (Union[Unset, str]):  Example: CA123456789012345678901234.
        institution_name (Union[Unset, str]):  Example: TD Bank.
        currency (Union[Unset, str]):  Example: CAD.
        current_balance (Union[Unset, float]):  Example: 24.55.
        overdraft_limit (Union[Unset, float]):  Example: 8.75.
        available_balance (Union[Unset, float]):  Example: 5.55.
        is_active (Union[Unset, bool]):  Example: True.
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2022-03-11T11:29:03-05:00".
    """

    id: str
    account_type: GetBankAccountAccountingDataV2AccountType
    nominal_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    ach_id: Union[Unset, str] = UNSET
    bank_code: Union[Unset, str] = UNSET
    i_ban: Union[Unset, str] = UNSET
    institution_name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    current_balance: Union[Unset, float] = UNSET
    overdraft_limit: Union[Unset, float] = UNSET
    available_balance: Union[Unset, float] = UNSET
    is_active: Union[Unset, bool] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        account_type: str = self.account_type

        nominal_code = self.nominal_code

        name = self.name

        account_number = self.account_number

        routing_number = self.routing_number

        ach_id = self.ach_id

        bank_code = self.bank_code

        i_ban = self.i_ban

        institution_name = self.institution_name

        currency = self.currency

        current_balance = self.current_balance

        overdraft_limit = self.overdraft_limit

        available_balance = self.available_balance

        is_active = self.is_active

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "accountType": account_type,
            }
        )
        if nominal_code is not UNSET:
            field_dict["nominalCode"] = nominal_code
        if name is not UNSET:
            field_dict["name"] = name
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if ach_id is not UNSET:
            field_dict["achId"] = ach_id
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
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        account_type = check_get_bank_account_accounting_data_v2_account_type(d.pop("accountType"))

        nominal_code = d.pop("nominalCode", UNSET)

        name = d.pop("name", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        ach_id = d.pop("achId", UNSET)

        bank_code = d.pop("bankCode", UNSET)

        i_ban = d.pop("iBan", UNSET)

        institution_name = d.pop("institutionName", UNSET)

        currency = d.pop("currency", UNSET)

        current_balance = d.pop("currentBalance", UNSET)

        overdraft_limit = d.pop("overdraftLimit", UNSET)

        available_balance = d.pop("availableBalance", UNSET)

        is_active = d.pop("isActive", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_bank_account_accounting_data_v2 = cls(
            id=id,
            account_type=account_type,
            nominal_code=nominal_code,
            name=name,
            account_number=account_number,
            routing_number=routing_number,
            ach_id=ach_id,
            bank_code=bank_code,
            i_ban=i_ban,
            institution_name=institution_name,
            currency=currency,
            current_balance=current_balance,
            overdraft_limit=overdraft_limit,
            available_balance=available_balance,
            is_active=is_active,
            source_modified_date=source_modified_date,
        )

        get_bank_account_accounting_data_v2.additional_properties = d
        return get_bank_account_accounting_data_v2

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
