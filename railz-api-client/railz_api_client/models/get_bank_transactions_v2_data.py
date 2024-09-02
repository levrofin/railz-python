import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bank_transactions_v2_data_payment_channel import GetBankTransactionsV2DataPaymentChannel
from ..models.get_bank_transactions_v2_data_section import GetBankTransactionsV2DataSection
from ..models.get_bank_transactions_v2_data_sub_section import GetBankTransactionsV2DataSubSection
from ..models.get_bank_transactions_v2_data_transaction_type import GetBankTransactionsV2DataTransactionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_location_data import BankLocationData


T = TypeVar("T", bound="GetBankTransactionsV2Data")


@_attrs_define
class GetBankTransactionsV2Data:
    """
    Attributes:
        id (str):  Example: lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDje.
        account_id (str):  Example: blgvvBlXw3cq5GMPwqB6s6q4dLKB9WcVqGDGo.
        date (datetime.datetime):  Example: 2017-01-29.
        is_pending (bool):
        amount (float):  Example: 100.
        currency (str):  Example: CAD.
        payment_channel (GetBankTransactionsV2DataPaymentChannel):  Example: online.
        description (str):  Example: Apple Store.
        authorized_on_date (Union[Unset, datetime.datetime]):  Example: 2017-01-29.
        transaction_type (Union[Unset, GetBankTransactionsV2DataTransactionType]):  Example: directDebit.
        categories (Union[Unset, List[str]]):  Example: ['Shops', 'Computers and Electronics'].
        merchant_name (Union[Unset, str]):  Example: Apple.
        merchant_store_number (Union[Unset, str]):  Example: 1235.
        location (Union[Unset, BankLocationData]):
        section (Union[Unset, GetBankTransactionsV2DataSection]):  Example: Assets.
        sub_section (Union[Unset, GetBankTransactionsV2DataSubSection]):  Example: Current Assets.
        group (Union[Unset, str]):  Example: Office General Administrative Expenses.
        sub_group (Union[Unset, str]):  Example: Office Supplies & Software.
        account_type (Union[Unset, str]):
        account_sub_type (Union[Unset, str]):
    """

    id: str
    account_id: str
    date: datetime.datetime
    is_pending: bool
    amount: float
    currency: str
    payment_channel: GetBankTransactionsV2DataPaymentChannel
    description: str
    authorized_on_date: Union[Unset, datetime.datetime] = UNSET
    transaction_type: Union[Unset, GetBankTransactionsV2DataTransactionType] = UNSET
    categories: Union[Unset, List[str]] = UNSET
    merchant_name: Union[Unset, str] = UNSET
    merchant_store_number: Union[Unset, str] = UNSET
    location: Union[Unset, "BankLocationData"] = UNSET
    section: Union[Unset, GetBankTransactionsV2DataSection] = UNSET
    sub_section: Union[Unset, GetBankTransactionsV2DataSubSection] = UNSET
    group: Union[Unset, str] = UNSET
    sub_group: Union[Unset, str] = UNSET
    account_type: Union[Unset, str] = UNSET
    account_sub_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        account_id = self.account_id

        date = self.date.isoformat()

        is_pending = self.is_pending

        amount = self.amount

        currency = self.currency

        payment_channel = self.payment_channel

        description = self.description

        authorized_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.authorized_on_date, Unset):
            authorized_on_date = self.authorized_on_date.isoformat()

        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type

        categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        merchant_name = self.merchant_name

        merchant_store_number = self.merchant_store_number

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        section: Union[Unset, str] = UNSET
        if not isinstance(self.section, Unset):
            section = self.section

        sub_section: Union[Unset, str] = UNSET
        if not isinstance(self.sub_section, Unset):
            sub_section = self.sub_section

        group = self.group

        sub_group = self.sub_group

        account_type = self.account_type

        account_sub_type = self.account_sub_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "accountId": account_id,
                "date": date,
                "isPending": is_pending,
                "amount": amount,
                "currency": currency,
                "paymentChannel": payment_channel,
                "description": description,
            }
        )
        if authorized_on_date is not UNSET:
            field_dict["authorizedOnDate"] = authorized_on_date
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type
        if categories is not UNSET:
            field_dict["categories"] = categories
        if merchant_name is not UNSET:
            field_dict["merchantName"] = merchant_name
        if merchant_store_number is not UNSET:
            field_dict["merchantStoreNumber"] = merchant_store_number
        if location is not UNSET:
            field_dict["location"] = location
        if section is not UNSET:
            field_dict["section"] = section
        if sub_section is not UNSET:
            field_dict["subSection"] = sub_section
        if group is not UNSET:
            field_dict["group"] = group
        if sub_group is not UNSET:
            field_dict["subGroup"] = sub_group
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if account_sub_type is not UNSET:
            field_dict["accountSubType"] = account_sub_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_location_data import BankLocationData

        d = src_dict.copy()
        id = d.pop("id")

        account_id = d.pop("accountId")

        date = isoparse(d.pop("date"))

        is_pending = d.pop("isPending")

        amount = d.pop("amount")

        currency = d.pop("currency")

        payment_channel = d.pop("paymentChannel")

        description = d.pop("description")

        _authorized_on_date = d.pop("authorizedOnDate", UNSET)
        authorized_on_date: Union[Unset, datetime.datetime]
        if isinstance(_authorized_on_date, Unset):
            authorized_on_date = UNSET
        else:
            authorized_on_date = isoparse(_authorized_on_date)

        _transaction_type = d.pop("transactionType", UNSET)
        transaction_type: Union[Unset, GetBankTransactionsV2DataTransactionType]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = _transaction_type

        categories = cast(List[str], d.pop("categories", UNSET))

        merchant_name = d.pop("merchantName", UNSET)

        merchant_store_number = d.pop("merchantStoreNumber", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, BankLocationData]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = BankLocationData.from_dict(_location)

        _section = d.pop("section", UNSET)
        section: Union[Unset, GetBankTransactionsV2DataSection]
        if isinstance(_section, Unset):
            section = UNSET
        else:
            section = _section

        _sub_section = d.pop("subSection", UNSET)
        sub_section: Union[Unset, GetBankTransactionsV2DataSubSection]
        if isinstance(_sub_section, Unset):
            sub_section = UNSET
        else:
            sub_section = _sub_section

        group = d.pop("group", UNSET)

        sub_group = d.pop("subGroup", UNSET)

        account_type = d.pop("accountType", UNSET)

        account_sub_type = d.pop("accountSubType", UNSET)

        get_bank_transactions_v2_data = cls(
            id=id,
            account_id=account_id,
            date=date,
            is_pending=is_pending,
            amount=amount,
            currency=currency,
            payment_channel=payment_channel,
            description=description,
            authorized_on_date=authorized_on_date,
            transaction_type=transaction_type,
            categories=categories,
            merchant_name=merchant_name,
            merchant_store_number=merchant_store_number,
            location=location,
            section=section,
            sub_section=sub_section,
            group=group,
            sub_group=sub_group,
            account_type=account_type,
            account_sub_type=account_sub_type,
        )

        get_bank_transactions_v2_data.additional_properties = d
        return get_bank_transactions_v2_data

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
