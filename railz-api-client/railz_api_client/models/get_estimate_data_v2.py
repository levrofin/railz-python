import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_estimate_data_v2_status import GetEstimateDataV2Status, check_get_estimate_data_v2_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_address import BaseAddress
    from ..models.customer_ref import CustomerRef
    from ..models.estimate_line_item_v2 import EstimateLineItemV2
    from ..models.get_estimate_data_v2_pass_through import GetEstimateDataV2PassThrough


T = TypeVar("T", bound="GetEstimateDataV2")


@_attrs_define
class GetEstimateDataV2:
    """
    Attributes:
        id (str):  Example: 1.
        posted_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        lines (List['EstimateLineItemV2']):
        total_amount (float):  Example: 322.
        status (GetEstimateDataV2Status):
        pass_through (Union[Unset, GetEstimateDataV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        customer_ref (Union[Unset, CustomerRef]):
        due_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        accepted_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        expiry_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency (Union[Unset, str]):  Example: USD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        total_discount (Union[Unset, float]):  Example: 322.
        discount_percentage (Union[Unset, float]):  Example: 322.
        sub_total (Union[Unset, float]):  Example: 301.5.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        memo (Union[Unset, str]):  Example: Example bill memo..
        shipping_address (Union[Unset, BaseAddress]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
    """

    id: str
    posted_date: datetime.datetime
    lines: List["EstimateLineItemV2"]
    total_amount: float
    status: GetEstimateDataV2Status
    pass_through: Union[Unset, "GetEstimateDataV2PassThrough"] = UNSET
    customer_ref: Union[Unset, "CustomerRef"] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    accepted_date: Union[Unset, datetime.datetime] = UNSET
    expiry_date: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    shipping_address: Union[Unset, "BaseAddress"] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        posted_date = self.posted_date.isoformat()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        total_amount = self.total_amount

        status: str = self.status

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        accepted_date: Union[Unset, str] = UNSET
        if not isinstance(self.accepted_date, Unset):
            accepted_date = self.accepted_date.isoformat()

        expiry_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat()

        currency = self.currency

        currency_rate = self.currency_rate

        total_discount = self.total_discount

        discount_percentage = self.discount_percentage

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        memo = self.memo

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "postedDate": posted_date,
                "lines": lines,
                "totalAmount": total_amount,
                "status": status,
            }
        )
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if accepted_date is not UNSET:
            field_dict["acceptedDate"] = accepted_date
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if currency is not UNSET:
            field_dict["currency"] = currency
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
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_address import BaseAddress
        from ..models.customer_ref import CustomerRef
        from ..models.estimate_line_item_v2 import EstimateLineItemV2
        from ..models.get_estimate_data_v2_pass_through import GetEstimateDataV2PassThrough

        d = src_dict.copy()
        id = d.pop("id")

        posted_date = isoparse(d.pop("postedDate"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = EstimateLineItemV2.from_dict(lines_item_data)

            lines.append(lines_item)

        total_amount = d.pop("totalAmount")

        status = check_get_estimate_data_v2_status(d.pop("status"))

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, GetEstimateDataV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = GetEstimateDataV2PassThrough.from_dict(_pass_through)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerRef.from_dict(_customer_ref)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _accepted_date = d.pop("acceptedDate", UNSET)
        accepted_date: Union[Unset, datetime.datetime]
        if isinstance(_accepted_date, Unset):
            accepted_date = UNSET
        else:
            accepted_date = isoparse(_accepted_date)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, datetime.datetime]
        if isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        memo = d.pop("memo", UNSET)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, BaseAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = BaseAddress.from_dict(_shipping_address)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_estimate_data_v2 = cls(
            id=id,
            posted_date=posted_date,
            lines=lines,
            total_amount=total_amount,
            status=status,
            pass_through=pass_through,
            customer_ref=customer_ref,
            due_date=due_date,
            accepted_date=accepted_date,
            expiry_date=expiry_date,
            currency=currency,
            currency_rate=currency_rate,
            total_discount=total_discount,
            discount_percentage=discount_percentage,
            sub_total=sub_total,
            tax_amount=tax_amount,
            memo=memo,
            shipping_address=shipping_address,
            source_modified_date=source_modified_date,
        )

        get_estimate_data_v2.additional_properties = d
        return get_estimate_data_v2

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
