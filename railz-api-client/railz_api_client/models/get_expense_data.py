import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_expense_data_payment_method import GetExpenseDataPaymentMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_v2_dto import AccountRefV2Dto
    from ..models.expense_line_item import ExpenseLineItem
    from ..models.payment_method_ref_response import PaymentMethodRefResponse
    from ..models.vendor_ref_dto_v2 import VendorRefDtoV2


T = TypeVar("T", bound="GetExpenseData")


@_attrs_define
class GetExpenseData:
    """
    Attributes:
        id (str):  Example: 1.
        total_amount (float):  Example: 100.13.
        posted_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        vendor_ref (Union[Unset, VendorRefDtoV2]):
        account_ref (Union[Unset, AccountRefV2Dto]):
        currency (Union[Unset, str]):  Example: USD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        payment_method (Union[Unset, GetExpenseDataPaymentMethod]):  Example: creditCard.
        payment_method_ref (Union[Unset, PaymentMethodRefResponse]):
        memo (Union[Unset, str]):  Example: Example expense memo..
        lines (Union[Unset, List['ExpenseLineItem']]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-10T11:26:06.619Z.
    """

    id: str
    total_amount: float
    posted_date: datetime.datetime
    vendor_ref: Union[Unset, "VendorRefDtoV2"] = UNSET
    account_ref: Union[Unset, "AccountRefV2Dto"] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    payment_method: Union[Unset, GetExpenseDataPaymentMethod] = UNSET
    payment_method_ref: Union[Unset, "PaymentMethodRefResponse"] = UNSET
    memo: Union[Unset, str] = UNSET
    lines: Union[Unset, List["ExpenseLineItem"]] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        total_amount = self.total_amount

        posted_date = self.posted_date.isoformat()

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency = self.currency

        currency_rate = self.currency_rate

        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method

        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        memo = self.memo

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "totalAmount": total_amount,
                "postedDate": posted_date,
            }
        )
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if memo is not UNSET:
            field_dict["memo"] = memo
        if lines is not UNSET:
            field_dict["lines"] = lines
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_v2_dto import AccountRefV2Dto
        from ..models.expense_line_item import ExpenseLineItem
        from ..models.payment_method_ref_response import PaymentMethodRefResponse
        from ..models.vendor_ref_dto_v2 import VendorRefDtoV2

        d = src_dict.copy()
        id = d.pop("id")

        total_amount = d.pop("totalAmount")

        posted_date = isoparse(d.pop("postedDate"))

        _vendor_ref = d.pop("vendorRef", UNSET)
        vendor_ref: Union[Unset, VendorRefDtoV2]
        if isinstance(_vendor_ref, Unset):
            vendor_ref = UNSET
        else:
            vendor_ref = VendorRefDtoV2.from_dict(_vendor_ref)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRefV2Dto]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRefV2Dto.from_dict(_account_ref)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, GetExpenseDataPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = _payment_method

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentMethodRefResponse]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentMethodRefResponse.from_dict(_payment_method_ref)

        memo = d.pop("memo", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = ExpenseLineItem.from_dict(lines_item_data)

            lines.append(lines_item)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_expense_data = cls(
            id=id,
            total_amount=total_amount,
            posted_date=posted_date,
            vendor_ref=vendor_ref,
            account_ref=account_ref,
            currency=currency,
            currency_rate=currency_rate,
            payment_method=payment_method,
            payment_method_ref=payment_method_ref,
            memo=memo,
            lines=lines,
            source_modified_date=source_modified_date,
        )

        get_expense_data.additional_properties = d
        return get_expense_data

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
