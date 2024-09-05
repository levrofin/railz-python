import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bank_account_data_account_type import (
    GetBankAccountDataAccountType,
    check_get_bank_account_data_account_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBankAccountData")


@_attrs_define
class GetBankAccountData:
    """
    Attributes:
        institution_name (str):  Example: TD Bank.
        account_id (str):  Example: blgvvBlXw3cq5GMPwqB6s6q4dLKB9WcVqGDGo.
        currency (str):  Example: CAD.
        account_name (str):  Example: Railz Checking.
        account_type (GetBankAccountDataAccountType):  Example: depository.
        current_balance (Union[Unset, float]):  Example: 110.
        available_balance (Union[Unset, float]):  Example: 100.
        limit (Union[Unset, float]):  Example: 200.
        masked_account_number (Union[Unset, str]):  Example: 4445.
        official_account_name (Union[Unset, str]):  Example: Railz Gold Standard 0% Interest Checking.
        account_sub_type (Union[Unset, str]):  Example: checking.
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
    """

    institution_name: str
    account_id: str
    currency: str
    account_name: str
    account_type: GetBankAccountDataAccountType
    current_balance: Union[Unset, float] = UNSET
    available_balance: Union[Unset, float] = UNSET
    limit: Union[Unset, float] = UNSET
    masked_account_number: Union[Unset, str] = UNSET
    official_account_name: Union[Unset, str] = UNSET
    account_sub_type: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        institution_name = self.institution_name

        account_id = self.account_id

        currency = self.currency

        account_name = self.account_name

        account_type: str = self.account_type

        current_balance = self.current_balance

        available_balance = self.available_balance

        limit = self.limit

        masked_account_number = self.masked_account_number

        official_account_name = self.official_account_name

        account_sub_type = self.account_sub_type

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "institutionName": institution_name,
                "accountId": account_id,
                "currency": currency,
                "accountName": account_name,
                "accountType": account_type,
            }
        )
        if current_balance is not UNSET:
            field_dict["currentBalance"] = current_balance
        if available_balance is not UNSET:
            field_dict["availableBalance"] = available_balance
        if limit is not UNSET:
            field_dict["limit"] = limit
        if masked_account_number is not UNSET:
            field_dict["maskedAccountNumber"] = masked_account_number
        if official_account_name is not UNSET:
            field_dict["officialAccountName"] = official_account_name
        if account_sub_type is not UNSET:
            field_dict["accountSubType"] = account_sub_type
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        institution_name = d.pop("institutionName")

        account_id = d.pop("accountId")

        currency = d.pop("currency")

        account_name = d.pop("accountName")

        account_type = check_get_bank_account_data_account_type(d.pop("accountType"))

        current_balance = d.pop("currentBalance", UNSET)

        available_balance = d.pop("availableBalance", UNSET)

        limit = d.pop("limit", UNSET)

        masked_account_number = d.pop("maskedAccountNumber", UNSET)

        official_account_name = d.pop("officialAccountName", UNSET)

        account_sub_type = d.pop("accountSubType", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_bank_account_data = cls(
            institution_name=institution_name,
            account_id=account_id,
            currency=currency,
            account_name=account_name,
            account_type=account_type,
            current_balance=current_balance,
            available_balance=available_balance,
            limit=limit,
            masked_account_number=masked_account_number,
            official_account_name=official_account_name,
            account_sub_type=account_sub_type,
            source_modified_date=source_modified_date,
        )

        get_bank_account_data.additional_properties = d
        return get_bank_account_data

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
