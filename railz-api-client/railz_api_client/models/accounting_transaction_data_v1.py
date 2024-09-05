import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.accounting_transaction_data_v1_type import (
    AccountingTransactionDataV1Type,
    check_accounting_transaction_data_v1_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accounting_transaction_account_ref import AccountingTransactionAccountRef
    from ..models.accounting_transaction_currency import AccountingTransactionCurrency
    from ..models.accounting_transaction_entity_ref import AccountingTransactionEntityRef
    from ..models.tracking_category_ref import TrackingCategoryRef


T = TypeVar("T", bound="AccountingTransactionDataV1")


@_attrs_define
class AccountingTransactionDataV1:
    """
    Attributes:
        posted_date (datetime.date):  Example: 2020-11-25.
        type (AccountingTransactionDataV1Type):  Example: invoice.
        is_posting (bool):  Example: True.
        is_reconciled (Union[Unset, bool]):  Example: True.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        is_split_transaction (Union[Unset, bool]):  Example: True.
        parent_transaction_id (Union[Unset, str]):  Example: 1043.
        sub_total (Union[Unset, float]):  Example: 300.5.
        tax_amount (Union[Unset, float]):  Example: 10.5.
        total_amount (Union[Unset, float]):  Example: 311.
        memo (Union[Unset, str]):  Example: Transaction reference.
        source_modified_date (Union[Unset, datetime.date]):  Example: 2021-03-09T10:18:29.985Z.
        id (Union[Unset, str]):  Example: 1045.
        transaction_number (Union[Unset, str]):  Example: INV-001.
        entity_ref (Union[Unset, AccountingTransactionEntityRef]):
        tracking_category_ref (Union[Unset, TrackingCategoryRef]):
        account_ref (Union[Unset, AccountingTransactionAccountRef]):
        currency_ref (Union[Unset, AccountingTransactionCurrency]):
    """

    posted_date: datetime.date
    type: AccountingTransactionDataV1Type
    is_posting: bool
    is_reconciled: Union[Unset, bool] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    is_split_transaction: Union[Unset, bool] = UNSET
    parent_transaction_id: Union[Unset, str] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.date] = UNSET
    id: Union[Unset, str] = UNSET
    transaction_number: Union[Unset, str] = UNSET
    entity_ref: Union[Unset, "AccountingTransactionEntityRef"] = UNSET
    tracking_category_ref: Union[Unset, "TrackingCategoryRef"] = UNSET
    account_ref: Union[Unset, "AccountingTransactionAccountRef"] = UNSET
    currency_ref: Union[Unset, "AccountingTransactionCurrency"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date = self.posted_date.isoformat()

        type: str = self.type

        is_posting = self.is_posting

        is_reconciled = self.is_reconciled

        currency_rate = self.currency_rate

        is_split_transaction = self.is_split_transaction

        parent_transaction_id = self.parent_transaction_id

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        total_amount = self.total_amount

        memo = self.memo

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        id = self.id

        transaction_number = self.transaction_number

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

        tracking_category_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracking_category_ref, Unset):
            tracking_category_ref = self.tracking_category_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "postedDate": posted_date,
                "type": type,
                "isPosting": is_posting,
            }
        )
        if is_reconciled is not UNSET:
            field_dict["isReconciled"] = is_reconciled
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if is_split_transaction is not UNSET:
            field_dict["isSplitTransaction"] = is_split_transaction
        if parent_transaction_id is not UNSET:
            field_dict["parentTransactionId"] = parent_transaction_id
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if memo is not UNSET:
            field_dict["memo"] = memo
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if id is not UNSET:
            field_dict["id"] = id
        if transaction_number is not UNSET:
            field_dict["transactionNumber"] = transaction_number
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref
        if tracking_category_ref is not UNSET:
            field_dict["trackingCategoryRef"] = tracking_category_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.accounting_transaction_account_ref import AccountingTransactionAccountRef
        from ..models.accounting_transaction_currency import AccountingTransactionCurrency
        from ..models.accounting_transaction_entity_ref import AccountingTransactionEntityRef
        from ..models.tracking_category_ref import TrackingCategoryRef

        d = src_dict.copy()
        posted_date = isoparse(d.pop("postedDate")).date()

        type = check_accounting_transaction_data_v1_type(d.pop("type"))

        is_posting = d.pop("isPosting")

        is_reconciled = d.pop("isReconciled", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        is_split_transaction = d.pop("isSplitTransaction", UNSET)

        parent_transaction_id = d.pop("parentTransactionId", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        memo = d.pop("memo", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.date]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date).date()

        id = d.pop("id", UNSET)

        transaction_number = d.pop("transactionNumber", UNSET)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, AccountingTransactionEntityRef]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = AccountingTransactionEntityRef.from_dict(_entity_ref)

        _tracking_category_ref = d.pop("trackingCategoryRef", UNSET)
        tracking_category_ref: Union[Unset, TrackingCategoryRef]
        if isinstance(_tracking_category_ref, Unset):
            tracking_category_ref = UNSET
        else:
            tracking_category_ref = TrackingCategoryRef.from_dict(_tracking_category_ref)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountingTransactionAccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountingTransactionAccountRef.from_dict(_account_ref)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, AccountingTransactionCurrency]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = AccountingTransactionCurrency.from_dict(_currency_ref)

        accounting_transaction_data_v1 = cls(
            posted_date=posted_date,
            type=type,
            is_posting=is_posting,
            is_reconciled=is_reconciled,
            currency_rate=currency_rate,
            is_split_transaction=is_split_transaction,
            parent_transaction_id=parent_transaction_id,
            sub_total=sub_total,
            tax_amount=tax_amount,
            total_amount=total_amount,
            memo=memo,
            source_modified_date=source_modified_date,
            id=id,
            transaction_number=transaction_number,
            entity_ref=entity_ref,
            tracking_category_ref=tracking_category_ref,
            account_ref=account_ref,
            currency_ref=currency_ref,
        )

        accounting_transaction_data_v1.additional_properties = d
        return accounting_transaction_data_v1

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
