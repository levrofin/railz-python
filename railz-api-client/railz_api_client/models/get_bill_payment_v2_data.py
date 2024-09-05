import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bill_payment_v2_data_payment_method import (
    GetBillPaymentV2DataPaymentMethod,
    check_get_bill_payment_v2_data_payment_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.bill_payment_line_v2_item import BillPaymentLineV2Item
    from ..models.payment_method_ref_response import PaymentMethodRefResponse
    from ..models.subsidiary_ref import SubsidiaryRef
    from ..models.vendor_ref import VendorRef


T = TypeVar("T", bound="GetBillPaymentV2Data")


@_attrs_define
class GetBillPaymentV2Data:
    """
    Attributes:
        id (str):  Example: 1.
        total_amount (float):  Example: 200.5.
        date (datetime.datetime):  Example: 2021-03-09T10:57:54.294Z.
        vendor_ref (Union[Unset, VendorRef]):
        account_ref (Union[Unset, AccountRef]):
        currency (Union[Unset, str]):  Example: USD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Bill payment memo..
        payment_method (Union[Unset, GetBillPaymentV2DataPaymentMethod]):  Example: creditCard.
        payment_method_ref (Union[Unset, PaymentMethodRefResponse]):
        lines (Union[Unset, List['BillPaymentLineV2Item']]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
    """

    id: str
    total_amount: float
    date: datetime.datetime
    vendor_ref: Union[Unset, "VendorRef"] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    payment_method: Union[Unset, GetBillPaymentV2DataPaymentMethod] = UNSET
    payment_method_ref: Union[Unset, "PaymentMethodRefResponse"] = UNSET
    lines: Union[Unset, List["BillPaymentLineV2Item"]] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        total_amount = self.total_amount

        date = self.date.isoformat()

        vendor_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vendor_ref, Unset):
            vendor_ref = self.vendor_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency = self.currency

        currency_rate = self.currency_rate

        memo = self.memo

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

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "totalAmount": total_amount,
                "date": date,
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
        if memo is not UNSET:
            field_dict["memo"] = memo
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if lines is not UNSET:
            field_dict["lines"] = lines
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.bill_payment_line_v2_item import BillPaymentLineV2Item
        from ..models.payment_method_ref_response import PaymentMethodRefResponse
        from ..models.subsidiary_ref import SubsidiaryRef
        from ..models.vendor_ref import VendorRef

        d = src_dict.copy()
        id = d.pop("id")

        total_amount = d.pop("totalAmount")

        date = isoparse(d.pop("date"))

        _vendor_ref = d.pop("vendorRef", UNSET)
        vendor_ref: Union[Unset, VendorRef]
        if isinstance(_vendor_ref, Unset):
            vendor_ref = UNSET
        else:
            vendor_ref = VendorRef.from_dict(_vendor_ref)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, GetBillPaymentV2DataPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = check_get_bill_payment_v2_data_payment_method(_payment_method)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentMethodRefResponse]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentMethodRefResponse.from_dict(_payment_method_ref)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = BillPaymentLineV2Item.from_dict(lines_item_data)

            lines.append(lines_item)

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

        get_bill_payment_v2_data = cls(
            id=id,
            total_amount=total_amount,
            date=date,
            vendor_ref=vendor_ref,
            account_ref=account_ref,
            currency=currency,
            currency_rate=currency_rate,
            memo=memo,
            payment_method=payment_method,
            payment_method_ref=payment_method_ref,
            lines=lines,
            subsidiary_refs=subsidiary_refs,
            source_modified_date=source_modified_date,
        )

        get_bill_payment_v2_data.additional_properties = d
        return get_bill_payment_v2_data

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
