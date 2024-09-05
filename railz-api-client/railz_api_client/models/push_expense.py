import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.push_expense_payment_method import PushExpensePaymentMethod, check_push_expense_payment_method
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.expense_line_dto import ExpenseLineDto
    from ..models.payment_method_ref_dto import PaymentMethodRefDto
    from ..models.push_expense_pass_through import PushExpensePassThrough
    from ..models.vendor_ref_dto import VendorRefDto


T = TypeVar("T", bound="PushExpense")


@_attrs_define
class PushExpense:
    """
    Attributes:
        pass_through (Union[Unset, PushExpensePassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        vendor_ref (Union[Unset, VendorRefDto]):
        account_ref (Union[Unset, AccountRefDto]):
        currency (Union[Unset, str]):  Example: CAD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        payment_method (Union[Unset, PushExpensePaymentMethod]):  Example: creditCard.
        payment_method_ref (Union[Unset, PaymentMethodRefDto]):
        memo (Union[Unset, str]):  Example: Example memo..
        lines (Union[Unset, List['ExpenseLineDto']]):
    """

    pass_through: Union[Unset, "PushExpensePassThrough"] = UNSET
    vendor_ref: Union[Unset, "VendorRefDto"] = UNSET
    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    payment_method: Union[Unset, PushExpensePaymentMethod] = UNSET
    payment_method_ref: Union[Unset, "PaymentMethodRefDto"] = UNSET
    memo: Union[Unset, str] = UNSET
    lines: Union[Unset, List["ExpenseLineDto"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency = self.currency

        currency_rate = self.currency_rate

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if memo is not UNSET:
            field_dict["memo"] = memo
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.expense_line_dto import ExpenseLineDto
        from ..models.payment_method_ref_dto import PaymentMethodRefDto
        from ..models.push_expense_pass_through import PushExpensePassThrough
        from ..models.vendor_ref_dto import VendorRefDto

        d = src_dict.copy()
        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushExpensePassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushExpensePassThrough.from_dict(_pass_through)

        _vendor_ref = d.pop("vendorRef", UNSET)
        vendor_ref: Union[Unset, VendorRefDto]
        if isinstance(_vendor_ref, Unset):
            vendor_ref = UNSET
        else:
            vendor_ref = VendorRefDto.from_dict(_vendor_ref)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRefDto]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRefDto.from_dict(_account_ref)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, PushExpensePaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = check_push_expense_payment_method(_payment_method)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentMethodRefDto]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentMethodRefDto.from_dict(_payment_method_ref)

        memo = d.pop("memo", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = ExpenseLineDto.from_dict(lines_item_data)

            lines.append(lines_item)

        push_expense = cls(
            pass_through=pass_through,
            vendor_ref=vendor_ref,
            account_ref=account_ref,
            currency=currency,
            currency_rate=currency_rate,
            posted_date=posted_date,
            payment_method=payment_method,
            payment_method_ref=payment_method_ref,
            memo=memo,
            lines=lines,
        )

        push_expense.additional_properties = d
        return push_expense

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
