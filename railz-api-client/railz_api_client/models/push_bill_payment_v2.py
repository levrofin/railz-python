import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.push_bill_payment_v2_payment_method import PushBillPaymentV2PaymentMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.bill_payment_line_v2 import BillPaymentLineV2
    from ..models.payment_method_ref_dto import PaymentMethodRefDto
    from ..models.push_bill_payment_v2_pass_through import PushBillPaymentV2PassThrough
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto
    from ..models.vendor_ref_dto import VendorRefDto


T = TypeVar("T", bound="PushBillPaymentV2")


@_attrs_define
class PushBillPaymentV2:
    """
    Attributes:
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Bill payment memo..
        date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        total_amount (Union[Unset, float]):  Example: 200.5.
        vendor_ref (Union[Unset, VendorRefDto]):
        account_ref (Union[Unset, AccountRefDto]):
        currency (Union[Unset, str]):  Example: CAD.
        lines (Union[Unset, List['BillPaymentLineV2']]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        payment_method (Union[Unset, PushBillPaymentV2PaymentMethod]):  Example: creditCard.
        payment_method_ref (Union[Unset, PaymentMethodRefDto]):
        pass_through (Union[Unset, PushBillPaymentV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    total_amount: Union[Unset, float] = UNSET
    vendor_ref: Union[Unset, "VendorRefDto"] = UNSET
    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    currency: Union[Unset, str] = UNSET
    lines: Union[Unset, List["BillPaymentLineV2"]] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    payment_method: Union[Unset, PushBillPaymentV2PaymentMethod] = UNSET
    payment_method_ref: Union[Unset, "PaymentMethodRefDto"] = UNSET
    pass_through: Union[Unset, "PushBillPaymentV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_rate = self.currency_rate

        memo = self.memo

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        total_amount = self.total_amount

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency = self.currency

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

        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method

        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if memo is not UNSET:
            field_dict["memo"] = memo
        if date is not UNSET:
            field_dict["date"] = date
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if lines is not UNSET:
            field_dict["lines"] = lines
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.bill_payment_line_v2 import BillPaymentLineV2
        from ..models.payment_method_ref_dto import PaymentMethodRefDto
        from ..models.push_bill_payment_v2_pass_through import PushBillPaymentV2PassThrough
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto
        from ..models.vendor_ref_dto import VendorRefDto

        d = src_dict.copy()
        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        total_amount = d.pop("totalAmount", UNSET)

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

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = BillPaymentLineV2.from_dict(lines_item_data)

            lines.append(lines_item)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, PushBillPaymentV2PaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = _payment_method

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentMethodRefDto]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentMethodRefDto.from_dict(_payment_method_ref)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushBillPaymentV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushBillPaymentV2PassThrough.from_dict(_pass_through)

        push_bill_payment_v2 = cls(
            currency_rate=currency_rate,
            memo=memo,
            date=date,
            total_amount=total_amount,
            vendor_ref=vendor_ref,
            account_ref=account_ref,
            currency=currency,
            lines=lines,
            subsidiary_refs=subsidiary_refs,
            payment_method=payment_method,
            payment_method_ref=payment_method_ref,
            pass_through=pass_through,
        )

        push_bill_payment_v2.additional_properties = d
        return push_bill_payment_v2

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
