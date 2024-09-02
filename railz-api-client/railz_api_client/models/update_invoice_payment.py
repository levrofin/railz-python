import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_invoice_payment_payment_method import UpdateInvoicePaymentPaymentMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.customer_ref_dto import CustomerRefDto
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto
    from ..models.update_invoice_payment_line_v2 import UpdateInvoicePaymentLineV2
    from ..models.update_invoice_payment_pass_through import UpdateInvoicePaymentPassThrough


T = TypeVar("T", bound="UpdateInvoicePayment")


@_attrs_define
class UpdateInvoicePayment:
    """
    Attributes:
        pass_through (Union[Unset, UpdateInvoicePaymentPassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        account_ref (Union[Unset, AccountRefDto]):
        customer_ref (Union[Unset, CustomerRefDto]):
        total_amount (Union[Unset, float]):  Example: 200.5.
        currency (Union[Unset, str]):  Example: CAD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        payment_method (Union[Unset, UpdateInvoicePaymentPaymentMethod]):
        memo (Union[Unset, str]):  Example: Invoice payment memo..
        lines (Union[Unset, List['UpdateInvoicePaymentLineV2']]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
    """

    pass_through: Union[Unset, "UpdateInvoicePaymentPassThrough"] = UNSET
    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    customer_ref: Union[Unset, "CustomerRefDto"] = UNSET
    total_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    payment_method: Union[Unset, UpdateInvoicePaymentPaymentMethod] = UNSET
    memo: Union[Unset, str] = UNSET
    lines: Union[Unset, List["UpdateInvoicePaymentLineV2"]] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
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

        total_amount = self.total_amount

        currency = self.currency

        currency_rate = self.currency_rate

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method

        memo = self.memo

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if date is not UNSET:
            field_dict["date"] = date
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if memo is not UNSET:
            field_dict["memo"] = memo
        if lines is not UNSET:
            field_dict["lines"] = lines
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.customer_ref_dto import CustomerRefDto
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto
        from ..models.update_invoice_payment_line_v2 import UpdateInvoicePaymentLineV2
        from ..models.update_invoice_payment_pass_through import UpdateInvoicePaymentPassThrough

        d = src_dict.copy()
        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, UpdateInvoicePaymentPassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = UpdateInvoicePaymentPassThrough.from_dict(_pass_through)

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

        total_amount = d.pop("totalAmount", UNSET)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, UpdateInvoicePaymentPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = _payment_method

        memo = d.pop("memo", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = UpdateInvoicePaymentLineV2.from_dict(lines_item_data)

            lines.append(lines_item)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        update_invoice_payment = cls(
            pass_through=pass_through,
            account_ref=account_ref,
            customer_ref=customer_ref,
            total_amount=total_amount,
            currency=currency,
            currency_rate=currency_rate,
            date=date,
            payment_method=payment_method,
            memo=memo,
            lines=lines,
            subsidiary_refs=subsidiary_refs,
        )

        update_invoice_payment.additional_properties = d
        return update_invoice_payment

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
