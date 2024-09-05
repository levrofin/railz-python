import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_dispute_data_reason import GetDisputeDataReason, check_get_dispute_data_reason
from ..models.get_dispute_data_status import GetDisputeDataStatus, check_get_dispute_data_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commerce_currency_ref import CommerceCurrencyRef
    from ..models.order_ref import OrderRef


T = TypeVar("T", bound="GetDisputeData")


@_attrs_define
class GetDisputeData:
    """
    Attributes:
        id (str):  Example: 1052608616.
        total_amount (float):  Example: 100.
        status (GetDisputeDataStatus):  Example: processing.
        reason (GetDisputeDataReason):  Example: subscriptionCanceled.
        due_date (datetime.datetime):  Example: 2022-03-11T11:29:03-05:00".
        created_date (datetime.datetime):  Example: 2022-03-11T11:29:03-05:00".
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2022-03-11T11:29:03-05:00".
        order_ref (Union[Unset, OrderRef]):
        currency_ref (Union[Unset, CommerceCurrencyRef]):
    """

    id: str
    total_amount: float
    status: GetDisputeDataStatus
    reason: GetDisputeDataReason
    due_date: datetime.datetime
    created_date: datetime.datetime
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    order_ref: Union[Unset, "OrderRef"] = UNSET
    currency_ref: Union[Unset, "CommerceCurrencyRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        total_amount = self.total_amount

        status: str = self.status

        reason: str = self.reason

        due_date = self.due_date.isoformat()

        created_date = self.created_date.isoformat()

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        order_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_ref, Unset):
            order_ref = self.order_ref.to_dict()

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "totalAmount": total_amount,
                "status": status,
                "reason": reason,
                "dueDate": due_date,
                "createdDate": created_date,
            }
        )
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if order_ref is not UNSET:
            field_dict["orderRef"] = order_ref
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commerce_currency_ref import CommerceCurrencyRef
        from ..models.order_ref import OrderRef

        d = src_dict.copy()
        id = d.pop("id")

        total_amount = d.pop("totalAmount")

        status = check_get_dispute_data_status(d.pop("status"))

        reason = check_get_dispute_data_reason(d.pop("reason"))

        due_date = isoparse(d.pop("dueDate"))

        created_date = isoparse(d.pop("createdDate"))

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        _order_ref = d.pop("orderRef", UNSET)
        order_ref: Union[Unset, OrderRef]
        if isinstance(_order_ref, Unset):
            order_ref = UNSET
        else:
            order_ref = OrderRef.from_dict(_order_ref)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CommerceCurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CommerceCurrencyRef.from_dict(_currency_ref)

        get_dispute_data = cls(
            id=id,
            total_amount=total_amount,
            status=status,
            reason=reason,
            due_date=due_date,
            created_date=created_date,
            source_modified_date=source_modified_date,
            order_ref=order_ref,
            currency_ref=currency_ref,
        )

        get_dispute_data.additional_properties = d
        return get_dispute_data

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
