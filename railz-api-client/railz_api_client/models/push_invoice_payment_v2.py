import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.push_invoice_payment_v2_payment_method import (
    PushInvoicePaymentV2PaymentMethod,
    check_push_invoice_payment_v2_payment_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.customer_ref_dto import CustomerRefDto
    from ..models.payment_method_ref_dto import PaymentMethodRefDto
    from ..models.push_invoice_payment_line_v2 import PushInvoicePaymentLineV2
    from ..models.push_invoice_payment_v2_pass_through import PushInvoicePaymentV2PassThrough
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto


T = TypeVar("T", bound="PushInvoicePaymentV2")


@_attrs_define
class PushInvoicePaymentV2:
    """
    Attributes:
        pass_through (Union[Unset, PushInvoicePaymentV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        account_ref (Union[Unset, AccountRefDto]):
        customer_ref (Union[Unset, CustomerRefDto]):
        currency (Union[Unset, str]):  Example: CAD.
        total_amount (Union[Unset, float]):  Example: 200.5.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        payment_method (Union[Unset, PushInvoicePaymentV2PaymentMethod]):  Example: creditCard.
        payment_method_ref (Union[Unset, PaymentMethodRefDto]):
        lines (Union[Unset, List['PushInvoicePaymentLineV2']]):
        date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        memo (Union[Unset, str]):  Example: Invoice payment memo..
    """

    pass_through: Union[Unset, "PushInvoicePaymentV2PassThrough"] = UNSET
    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    customer_ref: Union[Unset, "CustomerRefDto"] = UNSET
    currency: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    payment_method: Union[Unset, PushInvoicePaymentV2PaymentMethod] = UNSET
    payment_method_ref: Union[Unset, "PaymentMethodRefDto"] = UNSET
    lines: Union[Unset, List["PushInvoicePaymentLineV2"]] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    memo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        currency = self.currency

        total_amount = self.total_amount

        currency_rate = self.currency_rate

        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method

        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        memo = self.memo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if lines is not UNSET:
            field_dict["lines"] = lines
        if date is not UNSET:
            field_dict["date"] = date
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if memo is not UNSET:
            field_dict["memo"] = memo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.customer_ref_dto import CustomerRefDto
        from ..models.payment_method_ref_dto import PaymentMethodRefDto
        from ..models.push_invoice_payment_line_v2 import PushInvoicePaymentLineV2
        from ..models.push_invoice_payment_v2_pass_through import PushInvoicePaymentV2PassThrough
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto

        d = src_dict.copy()
        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushInvoicePaymentV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushInvoicePaymentV2PassThrough.from_dict(_pass_through)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRefDto]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRefDto.from_dict(_account_ref)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerRefDto]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerRefDto.from_dict(_customer_ref)

        currency = d.pop("currency", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, PushInvoicePaymentV2PaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = check_push_invoice_payment_v2_payment_method(_payment_method)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentMethodRefDto]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentMethodRefDto.from_dict(_payment_method_ref)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = PushInvoicePaymentLineV2.from_dict(lines_item_data)

            lines.append(lines_item)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        memo = d.pop("memo", UNSET)

        push_invoice_payment_v2 = cls(
            pass_through=pass_through,
            account_ref=account_ref,
            customer_ref=customer_ref,
            currency=currency,
            total_amount=total_amount,
            currency_rate=currency_rate,
            payment_method=payment_method,
            payment_method_ref=payment_method_ref,
            lines=lines,
            date=date,
            subsidiary_refs=subsidiary_refs,
            memo=memo,
        )

        push_invoice_payment_v2.additional_properties = d
        return push_invoice_payment_v2

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
