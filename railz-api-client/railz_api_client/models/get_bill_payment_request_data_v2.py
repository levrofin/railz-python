import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_bill_payment_request_data_v2_state import GetBillPaymentRequestDataV2State
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.bill_p_links import BillPLinks
    from ..models.payment_request_payment_method_ref_dto import PaymentRequestPaymentMethodRefDto
    from ..models.vendor_ref import VendorRef


T = TypeVar("T", bound="GetBillPaymentRequestDataV2")


@_attrs_define
class GetBillPaymentRequestDataV2:
    """
    Attributes:
        id (str):  Example: 1.
        vendor_ref (VendorRef):
        payment_amount (float):  Example: 301.5.
        state (GetBillPaymentRequestDataV2State):  Example: approved.
        batch_id (Union[Unset, str]):  Example: 1.
        bank_account_ref (Union[Unset, AccountRef]):
        payment_number (Union[Unset, str]):  Example: 1.
        payment_code (Union[Unset, str]):  Example: 1.
        payment_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        posted_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency (Union[Unset, str]):  Example: 1.
        total_amount (Union[Unset, float]):  Example: 20.5.
        total_paid (Union[Unset, float]):  Example: 322.
        amount_due (Union[Unset, float]):  Example: 322.
        links (Union[Unset, List['BillPLinks']]):
        payment_method_ref (Union[Unset, PaymentRequestPaymentMethodRefDto]):
        memo (Union[Unset, str]):  Example: Example bill memo..
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
    """

    id: str
    vendor_ref: "VendorRef"
    payment_amount: float
    state: GetBillPaymentRequestDataV2State
    batch_id: Union[Unset, str] = UNSET
    bank_account_ref: Union[Unset, "AccountRef"] = UNSET
    payment_number: Union[Unset, str] = UNSET
    payment_code: Union[Unset, str] = UNSET
    payment_date: Union[Unset, datetime.datetime] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    total_paid: Union[Unset, float] = UNSET
    amount_due: Union[Unset, float] = UNSET
    links: Union[Unset, List["BillPLinks"]] = UNSET
    payment_method_ref: Union[Unset, "PaymentRequestPaymentMethodRefDto"] = UNSET
    memo: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        vendor_ref = self.vendor_ref.to_dict()

        payment_amount = self.payment_amount

        state = self.state

        batch_id = self.batch_id

        bank_account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bank_account_ref, Unset):
            bank_account_ref = self.bank_account_ref.to_dict()

        payment_number = self.payment_number

        payment_code = self.payment_code

        payment_date: Union[Unset, str] = UNSET
        if not isinstance(self.payment_date, Unset):
            payment_date = self.payment_date.isoformat()

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        currency = self.currency

        total_amount = self.total_amount

        total_paid = self.total_paid

        amount_due = self.amount_due

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        memo = self.memo

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "vendorRef": vendor_ref,
                "paymentAmount": payment_amount,
                "state": state,
            }
        )
        if batch_id is not UNSET:
            field_dict["batchId"] = batch_id
        if bank_account_ref is not UNSET:
            field_dict["bankAccountRef"] = bank_account_ref
        if payment_number is not UNSET:
            field_dict["paymentNumber"] = payment_number
        if payment_code is not UNSET:
            field_dict["paymentCode"] = payment_code
        if payment_date is not UNSET:
            field_dict["paymentDate"] = payment_date
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_paid is not UNSET:
            field_dict["totalPaid"] = total_paid
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
        if links is not UNSET:
            field_dict["links"] = links
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if memo is not UNSET:
            field_dict["memo"] = memo
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.bill_p_links import BillPLinks
        from ..models.payment_request_payment_method_ref_dto import PaymentRequestPaymentMethodRefDto
        from ..models.vendor_ref import VendorRef

        d = src_dict.copy()
        id = d.pop("id")

        vendor_ref = VendorRef.from_dict(d.pop("vendorRef"))

        payment_amount = d.pop("paymentAmount")

        state = d.pop("state")

        batch_id = d.pop("batchId", UNSET)

        _bank_account_ref = d.pop("bankAccountRef", UNSET)
        bank_account_ref: Union[Unset, AccountRef]
        if isinstance(_bank_account_ref, Unset):
            bank_account_ref = UNSET
        else:
            bank_account_ref = AccountRef.from_dict(_bank_account_ref)

        payment_number = d.pop("paymentNumber", UNSET)

        payment_code = d.pop("paymentCode", UNSET)

        _payment_date = d.pop("paymentDate", UNSET)
        payment_date: Union[Unset, datetime.datetime]
        if isinstance(_payment_date, Unset):
            payment_date = UNSET
        else:
            payment_date = isoparse(_payment_date)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        currency = d.pop("currency", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        total_paid = d.pop("totalPaid", UNSET)

        amount_due = d.pop("amountDue", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = BillPLinks.from_dict(links_item_data)

            links.append(links_item)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, PaymentRequestPaymentMethodRefDto]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = PaymentRequestPaymentMethodRefDto.from_dict(_payment_method_ref)

        memo = d.pop("memo", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_bill_payment_request_data_v2 = cls(
            id=id,
            vendor_ref=vendor_ref,
            payment_amount=payment_amount,
            state=state,
            batch_id=batch_id,
            bank_account_ref=bank_account_ref,
            payment_number=payment_number,
            payment_code=payment_code,
            payment_date=payment_date,
            posted_date=posted_date,
            currency=currency,
            total_amount=total_amount,
            total_paid=total_paid,
            amount_due=amount_due,
            links=links,
            payment_method_ref=payment_method_ref,
            memo=memo,
            source_modified_date=source_modified_date,
        )

        get_bill_payment_request_data_v2.additional_properties = d
        return get_bill_payment_request_data_v2

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
