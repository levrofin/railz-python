import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.push_bank_transaction_v2_transaction_type import (
    PushBankTransactionV2TransactionType,
    check_push_bank_transaction_v2_transaction_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_account_ref_dto import BankAccountRefDto
    from ..models.entity_ref_dto import EntityRefDto
    from ..models.push_bank_transaction_line_v2 import PushBankTransactionLineV2
    from ..models.push_bank_transaction_v2_pass_through import PushBankTransactionV2PassThrough


T = TypeVar("T", bound="PushBankTransactionV2")


@_attrs_define
class PushBankTransactionV2:
    """
    Attributes:
        bank_account_ref (BankAccountRefDto):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        currency (Union[Unset, str]):  Example: CAD.
        transaction_type (Union[Unset, PushBankTransactionV2TransactionType]):  Example: payment.
        entity_ref (Union[Unset, EntityRefDto]):
        lines (Union[Unset, List['PushBankTransactionLineV2']]):
        total_amount (Union[Unset, float]):  Example: 150.50.
        memo (Union[Unset, str]):  Example: Example memo..
        posted_date (Union[Unset, datetime.date]):  Example: 2020-11-30.
        pass_through (Union[Unset, PushBankTransactionV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    bank_account_ref: "BankAccountRefDto"
    currency_rate: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    transaction_type: Union[Unset, PushBankTransactionV2TransactionType] = UNSET
    entity_ref: Union[Unset, "EntityRefDto"] = UNSET
    lines: Union[Unset, List["PushBankTransactionLineV2"]] = UNSET
    total_amount: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    pass_through: Union[Unset, "PushBankTransactionV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bank_account_ref = self.bank_account_ref.to_dict()

        currency_rate = self.currency_rate

        currency = self.currency

        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        total_amount = self.total_amount

        memo = self.memo

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bankAccountRef": bank_account_ref,
            }
        )
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if currency is not UNSET:
            field_dict["currency"] = currency
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref
        if lines is not UNSET:
            field_dict["lines"] = lines
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if memo is not UNSET:
            field_dict["memo"] = memo
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_account_ref_dto import BankAccountRefDto
        from ..models.entity_ref_dto import EntityRefDto
        from ..models.push_bank_transaction_line_v2 import PushBankTransactionLineV2
        from ..models.push_bank_transaction_v2_pass_through import PushBankTransactionV2PassThrough

        d = src_dict.copy()
        bank_account_ref = BankAccountRefDto.from_dict(d.pop("bankAccountRef"))

        currency_rate = d.pop("currencyRate", UNSET)

        currency = d.pop("currency", UNSET)

        _transaction_type = d.pop("transactionType", UNSET)
        transaction_type: Union[Unset, PushBankTransactionV2TransactionType]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = check_push_bank_transaction_v2_transaction_type(_transaction_type)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, EntityRefDto]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = EntityRefDto.from_dict(_entity_ref)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = PushBankTransactionLineV2.from_dict(lines_item_data)

            lines.append(lines_item)

        total_amount = d.pop("totalAmount", UNSET)

        memo = d.pop("memo", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushBankTransactionV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushBankTransactionV2PassThrough.from_dict(_pass_through)

        push_bank_transaction_v2 = cls(
            bank_account_ref=bank_account_ref,
            currency_rate=currency_rate,
            currency=currency,
            transaction_type=transaction_type,
            entity_ref=entity_ref,
            lines=lines,
            total_amount=total_amount,
            memo=memo,
            posted_date=posted_date,
            pass_through=pass_through,
        )

        push_bank_transaction_v2.additional_properties = d
        return push_bank_transaction_v2

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
