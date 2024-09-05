import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_transaction_data_payment_method_type import (
    GetTransactionDataPaymentMethodType,
    check_get_transaction_data_payment_method_type,
)
from ..models.get_transaction_data_status import GetTransactionDataStatus, check_get_transaction_data_status
from ..models.get_transaction_data_transaction_type import (
    GetTransactionDataTransactionType,
    check_get_transaction_data_transaction_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commerce_currency_ref import CommerceCurrencyRef
    from ..models.transaction_source_refs import TransactionSourceRefs


T = TypeVar("T", bound="GetTransactionData")


@_attrs_define
class GetTransactionData:
    """
    Attributes:
        id (str):  Example: 699519475.
        total_amount (float):  Example: -3.45.
        transaction_type (GetTransactionDataTransactionType):  Example: transfer.
        created_date (datetime.datetime):  Example: 2022-03-11T11:29:03-05:00.
        status (GetTransactionDataStatus):  Example: pending.
        order_id (Union[Unset, str]):  Example: 217130470.
        payment_method_type (Union[Unset, GetTransactionDataPaymentMethodType]):  Example: digital.
        currency_ref (Union[Unset, CommerceCurrencyRef]):
        transaction_source_refs (Union[Unset, List['TransactionSourceRefs']]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2022-03-11T11:29:03-05:00.
    """

    id: str
    total_amount: float
    transaction_type: GetTransactionDataTransactionType
    created_date: datetime.datetime
    status: GetTransactionDataStatus
    order_id: Union[Unset, str] = UNSET
    payment_method_type: Union[Unset, GetTransactionDataPaymentMethodType] = UNSET
    currency_ref: Union[Unset, "CommerceCurrencyRef"] = UNSET
    transaction_source_refs: Union[Unset, List["TransactionSourceRefs"]] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        total_amount = self.total_amount

        transaction_type: str = self.transaction_type

        created_date = self.created_date.isoformat()

        status: str = self.status

        order_id = self.order_id

        payment_method_type: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method_type, Unset):
            payment_method_type = self.payment_method_type

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

        transaction_source_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transaction_source_refs, Unset):
            transaction_source_refs = []
            for transaction_source_refs_item_data in self.transaction_source_refs:
                transaction_source_refs_item = transaction_source_refs_item_data.to_dict()
                transaction_source_refs.append(transaction_source_refs_item)

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "totalAmount": total_amount,
                "transactionType": transaction_type,
                "createdDate": created_date,
                "status": status,
            }
        )
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if payment_method_type is not UNSET:
            field_dict["paymentMethodType"] = payment_method_type
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref
        if transaction_source_refs is not UNSET:
            field_dict["transactionSourceRefs"] = transaction_source_refs
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commerce_currency_ref import CommerceCurrencyRef
        from ..models.transaction_source_refs import TransactionSourceRefs

        d = src_dict.copy()
        id = d.pop("id")

        total_amount = d.pop("totalAmount")

        transaction_type = check_get_transaction_data_transaction_type(d.pop("transactionType"))

        created_date = isoparse(d.pop("createdDate"))

        status = check_get_transaction_data_status(d.pop("status"))

        order_id = d.pop("orderId", UNSET)

        _payment_method_type = d.pop("paymentMethodType", UNSET)
        payment_method_type: Union[Unset, GetTransactionDataPaymentMethodType]
        if isinstance(_payment_method_type, Unset):
            payment_method_type = UNSET
        else:
            payment_method_type = check_get_transaction_data_payment_method_type(_payment_method_type)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CommerceCurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CommerceCurrencyRef.from_dict(_currency_ref)

        transaction_source_refs = []
        _transaction_source_refs = d.pop("transactionSourceRefs", UNSET)
        for transaction_source_refs_item_data in _transaction_source_refs or []:
            transaction_source_refs_item = TransactionSourceRefs.from_dict(transaction_source_refs_item_data)

            transaction_source_refs.append(transaction_source_refs_item)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_transaction_data = cls(
            id=id,
            total_amount=total_amount,
            transaction_type=transaction_type,
            created_date=created_date,
            status=status,
            order_id=order_id,
            payment_method_type=payment_method_type,
            currency_ref=currency_ref,
            transaction_source_refs=transaction_source_refs,
            source_modified_date=source_modified_date,
        )

        get_transaction_data.additional_properties = d
        return get_transaction_data

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
