import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_transfer_from_account_ref import BankTransferFromAccountRef
    from ..models.bank_transfer_to_account_ref import BankTransferToAccountRef
    from ..models.currency_ref import CurrencyRef


T = TypeVar("T", bound="GetBankTransferDataV1")


@_attrs_define
class GetBankTransferDataV1:
    """
    Attributes:
        id (str):  Example: 123.
        date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        total_amount (float):  Example: 1000.5.
        from_account_ref (BankTransferFromAccountRef):
        to_account_ref (BankTransferToAccountRef):
        from_bank_transaction_id (str):  Example: b11794bc.
        to_bank_transaction_id (str):  Example: b11794cd.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Reference to bank transfer..
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency_ref (Union[Unset, CurrencyRef]):
    """

    id: str
    date: datetime.datetime
    total_amount: float
    from_account_ref: "BankTransferFromAccountRef"
    to_account_ref: "BankTransferToAccountRef"
    from_bank_transaction_id: str
    to_bank_transaction_id: str
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    currency_ref: Union[Unset, "CurrencyRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        total_amount = self.total_amount

        from_account_ref = self.from_account_ref.to_dict()

        to_account_ref = self.to_account_ref.to_dict()

        from_bank_transaction_id = self.from_bank_transaction_id

        to_bank_transaction_id = self.to_bank_transaction_id

        currency_rate = self.currency_rate

        memo = self.memo

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "totalAmount": total_amount,
                "fromAccountRef": from_account_ref,
                "toAccountRef": to_account_ref,
                "fromBankTransactionId": from_bank_transaction_id,
                "toBankTransactionId": to_bank_transaction_id,
            }
        )
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if memo is not UNSET:
            field_dict["memo"] = memo
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_transfer_from_account_ref import BankTransferFromAccountRef
        from ..models.bank_transfer_to_account_ref import BankTransferToAccountRef
        from ..models.currency_ref import CurrencyRef

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        total_amount = d.pop("totalAmount")

        from_account_ref = BankTransferFromAccountRef.from_dict(d.pop("fromAccountRef"))

        to_account_ref = BankTransferToAccountRef.from_dict(d.pop("toAccountRef"))

        from_bank_transaction_id = d.pop("fromBankTransactionId")

        to_bank_transaction_id = d.pop("toBankTransactionId")

        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CurrencyRef.from_dict(_currency_ref)

        get_bank_transfer_data_v1 = cls(
            id=id,
            date=date,
            total_amount=total_amount,
            from_account_ref=from_account_ref,
            to_account_ref=to_account_ref,
            from_bank_transaction_id=from_bank_transaction_id,
            to_bank_transaction_id=to_bank_transaction_id,
            currency_rate=currency_rate,
            memo=memo,
            source_modified_date=source_modified_date,
            currency_ref=currency_ref,
        )

        get_bank_transfer_data_v1.additional_properties = d
        return get_bank_transfer_data_v1

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
