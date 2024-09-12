import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_account_ref_dto import BankAccountRefDto
    from ..models.bill_payment_request_links import BillPaymentRequestLinks
    from ..models.payment_request_payment_method_ref_dto import PaymentRequestPaymentMethodRefDto
    from ..models.vendor_ref_dto import VendorRefDto


T = TypeVar("T", bound="PostBillPaymentRequestV2")


@_attrs_define
class PostBillPaymentRequestV2:
    """
    Attributes:
        bank_account_ref (BankAccountRefDto):
        links (List['BillPaymentRequestLinks']):
        vendor_ref (Union[Unset, VendorRefDto]):
        payment_number (Union[Unset, str]):  Example: 456.
        payment_code (Union[Unset, str]):  Example: 1234.
        payment_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        currency (Union[Unset, str]):  Example: USD.
        total_amount (Union[Unset, float]):  Example: 43.5.
        payment_method_ref (Union[Unset, PaymentRequestPaymentMethodRefDto]):
        memo (Union[Unset, str]):
    """

    bank_account_ref: "BankAccountRefDto"
    links: List["BillPaymentRequestLinks"]
    vendor_ref: Union[Unset, "VendorRefDto"] = UNSET
    payment_number: Union[Unset, str] = UNSET
    payment_code: Union[Unset, str] = UNSET
    payment_date: Union[Unset, datetime.date] = UNSET
    currency: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    payment_method_ref: Union[Unset, "PaymentRequestPaymentMethodRefDto"] = UNSET
    memo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bank_account_ref = self.bank_account_ref.to_dict()

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

        payment_number = self.payment_number

        payment_code = self.payment_code

        payment_date: Union[Unset, str] = UNSET
        if not isinstance(self.payment_date, Unset):
            payment_date = self.payment_date.isoformat()

        currency = self.currency

        total_amount = self.total_amount

        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        memo = self.memo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bankAccountRef": bank_account_ref,
                "links": links,
            }
        )
        if vendor_ref is not UNSET:
            field_dict["vendorRef"] = vendor_ref
        if payment_number is not UNSET:
            field_dict["paymentNumber"] = payment_number
        if payment_code is not UNSET:
            field_dict["paymentCode"] = payment_code
        if payment_date is not UNSET:
            field_dict["paymentDate"] = payment_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if memo is not UNSET:
            field_dict["memo"] = memo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_account_ref_dto import BankAccountRefDto
        from ..models.bill_payment_request_links import BillPaymentRequestLinks
        from ..models.payment_request_payment_method_ref_dto import PaymentRequestPaymentMethodRefDto
        from ..models.vendor_ref_dto import VendorRefDto

        d = src_dict.copy()
        bank_account_ref = BankAccountRefDto.from_dict(d.pop("bankAccountRef"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = BillPaymentRequestLinks.from_dict(links_item_data)

            links.append(links_item)

        _vendor_ref = d.pop("vendorRef", UNSET)
        vendor_ref: Union[Unset, VendorRefDto]
        if isinstance(_vendor_ref, Unset):
            vendor_ref = UNSET
        else:
            vendor_ref = VendorRefDto.from_dict(_vendor_ref)

        payment_number = d.pop("paymentNumber", UNSET)

        payment_code = d.pop("paymentCode", UNSET)

        _payment_date = d.pop("paymentDate", UNSET)
        payment_date: Union[Unset, datetime.date]
        if isinstance(_payment_date, Unset):
            payment_date = UNSET
        else:
            payment_date = isoparse(_payment_date).date()

        currency = d.pop("currency", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentRequestPaymentMethodRefDto]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentRequestPaymentMethodRefDto.from_dict(_payment_method_ref)

        memo = d.pop("memo", UNSET)

        post_bill_payment_request_v2 = cls(
            bank_account_ref=bank_account_ref,
            links=links,
            vendor_ref=vendor_ref,
            payment_number=payment_number,
            payment_code=payment_code,
            payment_date=payment_date,
            currency=currency,
            total_amount=total_amount,
            payment_method_ref=payment_method_ref,
            memo=memo,
        )

        post_bill_payment_request_v2.additional_properties = d
        return post_bill_payment_request_v2

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
