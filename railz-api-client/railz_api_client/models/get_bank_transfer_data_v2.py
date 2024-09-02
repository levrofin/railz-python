import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_transfer_from_account_ref import BankTransferFromAccountRef
    from ..models.bank_transfer_to_account_ref import BankTransferToAccountRef


T = TypeVar("T", bound="GetBankTransferDataV2")


@_attrs_define
class GetBankTransferDataV2:
    """
    Attributes:
        id (str):  Example: 123.
        date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        total_amount (float):  Example: 1000.5.
        from_account_ref (BankTransferFromAccountRef):
        to_account_ref (BankTransferToAccountRef):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        from_bank_transaction_id (Union[Unset, str]):  Example: b11794bc.
        to_bank_transaction_id (Union[Unset, str]):  Example: b11794cd.
        memo (Union[Unset, str]):  Example: Reference to bank transfer..
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency (Union[Unset, str]):  Example: USD.
    """

    id: str
    date: datetime.datetime
    total_amount: float
    from_account_ref: "BankTransferFromAccountRef"
    to_account_ref: "BankTransferToAccountRef"
    currency_rate: Union[Unset, float] = UNSET
    from_bank_transaction_id: Union[Unset, str] = UNSET
    to_bank_transaction_id: Union[Unset, str] = UNSET
    memo: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        total_amount = self.total_amount

        from_account_ref = self.from_account_ref.to_dict()

        to_account_ref = self.to_account_ref.to_dict()

        currency_rate = self.currency_rate

        from_bank_transaction_id = self.from_bank_transaction_id

        to_bank_transaction_id = self.to_bank_transaction_id

        memo = self.memo

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "totalAmount": total_amount,
                "fromAccountRef": from_account_ref,
                "toAccountRef": to_account_ref,
            }
        )
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if from_bank_transaction_id is not UNSET:
            field_dict["fromBankTransactionId"] = from_bank_transaction_id
        if to_bank_transaction_id is not UNSET:
            field_dict["toBankTransactionId"] = to_bank_transaction_id
        if memo is not UNSET:
            field_dict["memo"] = memo
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_transfer_from_account_ref import BankTransferFromAccountRef
        from ..models.bank_transfer_to_account_ref import BankTransferToAccountRef

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        total_amount = d.pop("totalAmount")

        from_account_ref = BankTransferFromAccountRef.from_dict(d.pop("fromAccountRef"))

        to_account_ref = BankTransferToAccountRef.from_dict(d.pop("toAccountRef"))

        currency_rate = d.pop("currencyRate", UNSET)

        from_bank_transaction_id = d.pop("fromBankTransactionId", UNSET)

        to_bank_transaction_id = d.pop("toBankTransactionId", UNSET)

        memo = d.pop("memo", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        currency = d.pop("currency", UNSET)

        get_bank_transfer_data_v2 = cls(
            id=id,
            date=date,
            total_amount=total_amount,
            from_account_ref=from_account_ref,
            to_account_ref=to_account_ref,
            currency_rate=currency_rate,
            from_bank_transaction_id=from_bank_transaction_id,
            to_bank_transaction_id=to_bank_transaction_id,
            memo=memo,
            source_modified_date=source_modified_date,
            currency=currency,
        )

        get_bank_transfer_data_v2.additional_properties = d
        return get_bank_transfer_data_v2

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
