import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.currency_ref import CurrencyRef
    from ..models.customer_ref import CustomerRef
    from ..models.invoice_payment_line_item import InvoicePaymentLineItem
    from ..models.subsidiary_ref import SubsidiaryRef


T = TypeVar("T", bound="GetInvoicePaymentData")


@_attrs_define
class GetInvoicePaymentData:
    """
    Attributes:
        id (str):  Example: 1.
        date (datetime.datetime):  Example: 2021-03-10T11:17:23.155Z.
        customer_ref (Union[Unset, CustomerRef]):
        account_ref (Union[Unset, AccountRef]):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Invoice payment memo..
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-10T11:17:23.155Z.
        total_amount (Union[Unset, float]):  Example: 200.5.
        currency_ref (Union[Unset, CurrencyRef]):
        lines (Union[Unset, List['InvoicePaymentLineItem']]):
    """

    id: str
    date: datetime.datetime
    customer_ref: Union[Unset, "CustomerRef"] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    total_amount: Union[Unset, float] = UNSET
    currency_ref: Union[Unset, "CurrencyRef"] = UNSET
    lines: Union[Unset, List["InvoicePaymentLineItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

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

        total_amount = self.total_amount

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

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
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.currency_ref import CurrencyRef
        from ..models.customer_ref import CustomerRef
        from ..models.invoice_payment_line_item import InvoicePaymentLineItem
        from ..models.subsidiary_ref import SubsidiaryRef

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

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

        total_amount = d.pop("totalAmount", UNSET)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CurrencyRef.from_dict(_currency_ref)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = InvoicePaymentLineItem.from_dict(lines_item_data)

            lines.append(lines_item)

        get_invoice_payment_data = cls(
            id=id,
            date=date,
            customer_ref=customer_ref,
            account_ref=account_ref,
            currency_rate=currency_rate,
            memo=memo,
            subsidiary_refs=subsidiary_refs,
            source_modified_date=source_modified_date,
            total_amount=total_amount,
            currency_ref=currency_ref,
            lines=lines,
        )

        get_invoice_payment_data.additional_properties = d
        return get_invoice_payment_data

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
