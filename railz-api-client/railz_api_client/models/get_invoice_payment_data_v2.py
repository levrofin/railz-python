import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_invoice_payment_data_v2_payment_method import (
    GetInvoicePaymentDataV2PaymentMethod,
    check_get_invoice_payment_data_v2_payment_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.customer_ref import CustomerRef
    from ..models.invoice_payment_line_item_v2 import InvoicePaymentLineItemV2
    from ..models.payment_method_ref_response import PaymentMethodRefResponse
    from ..models.subsidiary_ref import SubsidiaryRef


T = TypeVar("T", bound="GetInvoicePaymentDataV2")


@_attrs_define
class GetInvoicePaymentDataV2:
    """
    Attributes:
        id (str):  Example: 1.
        date (datetime.datetime):  Example: 2021-03-10T11:17:23.155Z.
        total_amount (float):  Example: 200.5.
        customer_ref (Union[Unset, CustomerRef]):
        account_ref (Union[Unset, AccountRef]):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Invoice payment memo..
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-10T11:17:23.155Z.
        currency (Union[Unset, str]):  Example: USD.
        payment_method (Union[Unset, GetInvoicePaymentDataV2PaymentMethod]):  Example: creditCard.
        payment_method_ref (Union[Unset, PaymentMethodRefResponse]):
        lines (Union[Unset, List['InvoicePaymentLineItemV2']]):
    """

    id: str
    date: datetime.datetime
    total_amount: float
    customer_ref: Union[Unset, "CustomerRef"] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    payment_method: Union[Unset, GetInvoicePaymentDataV2PaymentMethod] = UNSET
    payment_method_ref: Union[Unset, "PaymentMethodRefResponse"] = UNSET
    lines: Union[Unset, List["InvoicePaymentLineItemV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        total_amount = self.total_amount

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency_rate = self.currency_rate

        memo = self.memo

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        currency = self.currency

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "totalAmount": total_amount,
            }
        )
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if memo is not UNSET:
            field_dict["memo"] = memo
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.customer_ref import CustomerRef
        from ..models.invoice_payment_line_item_v2 import InvoicePaymentLineItemV2
        from ..models.payment_method_ref_response import PaymentMethodRefResponse
        from ..models.subsidiary_ref import SubsidiaryRef

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        total_amount = d.pop("totalAmount")

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerRef.from_dict(_customer_ref)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRef.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        currency = d.pop("currency", UNSET)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, GetInvoicePaymentDataV2PaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = check_get_invoice_payment_data_v2_payment_method(_payment_method)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentMethodRefResponse]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentMethodRefResponse.from_dict(_payment_method_ref)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = InvoicePaymentLineItemV2.from_dict(lines_item_data)

            lines.append(lines_item)

        get_invoice_payment_data_v2 = cls(
            id=id,
            date=date,
            total_amount=total_amount,
            customer_ref=customer_ref,
            account_ref=account_ref,
            currency_rate=currency_rate,
            memo=memo,
            subsidiary_refs=subsidiary_refs,
            source_modified_date=source_modified_date,
            currency=currency,
            payment_method=payment_method,
            payment_method_ref=payment_method_ref,
            lines=lines,
        )

        get_invoice_payment_data_v2.additional_properties = d
        return get_invoice_payment_data_v2

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
