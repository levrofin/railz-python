import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.base_address import BaseAddress
    from ..models.currency_ref import CurrencyRef
    from ..models.customer_ref import CustomerRef
    from ..models.refund_line_item_v1 import RefundLineItemV1


T = TypeVar("T", bound="GetRefundDataV1")


@_attrs_define
class GetRefundDataV1:
    """
    Attributes:
        id (str):  Example: 1.
        total_amount (float):  Example: 322.
        date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        customer_ref (Union[Unset, CustomerRef]):
        account_ref (Union[Unset, AccountRef]):
        currency_rate (Union[Unset, float]):  Example: 1.13.
        total_discount (Union[Unset, float]):  Example: 322.
        discount_percentage (Union[Unset, float]):  Example: 322.
        sub_total (Union[Unset, float]):  Example: 301.5.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        memo (Union[Unset, str]):  Example: Example bill memo..
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        shipping_address (Union[Unset, BaseAddress]):
        currency_ref (Union[Unset, CurrencyRef]):
        lines (Union[Unset, List['RefundLineItemV1']]):
    """

    id: str
    total_amount: float
    date: datetime.datetime
    customer_ref: Union[Unset, "CustomerRef"] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    shipping_address: Union[Unset, "BaseAddress"] = UNSET
    currency_ref: Union[Unset, "CurrencyRef"] = UNSET
    lines: Union[Unset, List["RefundLineItemV1"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        total_amount = self.total_amount

        date = self.date.isoformat()

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency_rate = self.currency_rate

        total_discount = self.total_discount

        discount_percentage = self.discount_percentage

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        memo = self.memo

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

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
                "totalAmount": total_amount,
                "date": date,
            }
        )
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if memo is not UNSET:
            field_dict["memo"] = memo
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.base_address import BaseAddress
        from ..models.currency_ref import CurrencyRef
        from ..models.customer_ref import CustomerRef
        from ..models.refund_line_item_v1 import RefundLineItemV1

        d = src_dict.copy()
        id = d.pop("id")

        total_amount = d.pop("totalAmount")

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

        total_discount = d.pop("totalDiscount", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        memo = d.pop("memo", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, BaseAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = BaseAddress.from_dict(_shipping_address)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CurrencyRef.from_dict(_currency_ref)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = RefundLineItemV1.from_dict(lines_item_data)

            lines.append(lines_item)

        get_refund_data_v1 = cls(
            id=id,
            total_amount=total_amount,
            date=date,
            customer_ref=customer_ref,
            account_ref=account_ref,
            currency_rate=currency_rate,
            total_discount=total_discount,
            discount_percentage=discount_percentage,
            sub_total=sub_total,
            tax_amount=tax_amount,
            memo=memo,
            source_modified_date=source_modified_date,
            shipping_address=shipping_address,
            currency_ref=currency_ref,
            lines=lines,
        )

        get_refund_data_v1.additional_properties = d
        return get_refund_data_v1

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
