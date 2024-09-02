import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bank_asset_data_account_type import GetBankAssetDataAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.historical_balances import HistoricalBalances


T = TypeVar("T", bound="GetBankAssetData")


@_attrs_define
class GetBankAssetData:
    """
    Attributes:
        account_id (str):  Example: blgvvBlXw3cq5GMPwqB6s6q4dLKB9WcVqGDGo.
        current_balance (Union[Unset, float]):  Example: 110.
        available_balance (Union[Unset, float]):  Example: 100.
        limit (Union[Unset, float]):  Example: 200.
        currency (Union[Unset, str]):  Example: CAD.
        date (Union[Unset, datetime.datetime]):  Example: 2017-01-29.
        days_available (Union[Unset, float]):
        historical_balances (Union[Unset, List['HistoricalBalances']]):
        account_name (Union[Unset, str]):  Example: Railz Checking.
        account_type (Union[Unset, GetBankAssetDataAccountType]):  Example: checking.
        account_sub_type (Union[Unset, str]):  Example: checking.
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
    """

    account_id: str
    current_balance: Union[Unset, float] = UNSET
    available_balance: Union[Unset, float] = UNSET
    limit: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    days_available: Union[Unset, float] = UNSET
    historical_balances: Union[Unset, List["HistoricalBalances"]] = UNSET
    account_name: Union[Unset, str] = UNSET
    account_type: Union[Unset, GetBankAssetDataAccountType] = UNSET
    account_sub_type: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        current_balance = self.current_balance

        available_balance = self.available_balance

        limit = self.limit

        currency = self.currency

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        days_available = self.days_available

        historical_balances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.historical_balances, Unset):
            historical_balances = []
            for historical_balances_item_data in self.historical_balances:
                historical_balances_item = historical_balances_item_data.to_dict()
                historical_balances.append(historical_balances_item)

        account_name = self.account_name

        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type

        account_sub_type = self.account_sub_type

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
            }
        )
        if current_balance is not UNSET:
            field_dict["currentBalance"] = current_balance
        if available_balance is not UNSET:
            field_dict["availableBalance"] = available_balance
        if limit is not UNSET:
            field_dict["limit"] = limit
        if currency is not UNSET:
            field_dict["currency"] = currency
        if date is not UNSET:
            field_dict["date"] = date
        if days_available is not UNSET:
            field_dict["daysAvailable"] = days_available
        if historical_balances is not UNSET:
            field_dict["historicalBalances"] = historical_balances
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if account_sub_type is not UNSET:
            field_dict["accountSubType"] = account_sub_type
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.historical_balances import HistoricalBalances

        d = src_dict.copy()
        account_id = d.pop("accountId")

        current_balance = d.pop("currentBalance", UNSET)

        available_balance = d.pop("availableBalance", UNSET)

        limit = d.pop("limit", UNSET)

        currency = d.pop("currency", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        days_available = d.pop("daysAvailable", UNSET)

        historical_balances = []
        _historical_balances = d.pop("historicalBalances", UNSET)
        for historical_balances_item_data in _historical_balances or []:
            historical_balances_item = HistoricalBalances.from_dict(historical_balances_item_data)

            historical_balances.append(historical_balances_item)

        account_name = d.pop("accountName", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, GetBankAssetDataAccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = _account_type

        account_sub_type = d.pop("accountSubType", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_bank_asset_data = cls(
            account_id=account_id,
            current_balance=current_balance,
            available_balance=available_balance,
            limit=limit,
            currency=currency,
            date=date,
            days_available=days_available,
            historical_balances=historical_balances,
            account_name=account_name,
            account_type=account_type,
            account_sub_type=account_sub_type,
            source_modified_date=source_modified_date,
        )

        get_bank_asset_data.additional_properties = d
        return get_bank_asset_data

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
