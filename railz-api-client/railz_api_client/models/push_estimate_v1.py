import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.estimate_line_v1 import EstimateLineV1
    from ..models.push_estimate_v1_pass_through import PushEstimateV1PassThrough
    from ..models.shipping_address_dto import ShippingAddressDto


T = TypeVar("T", bound="PushEstimateV1")


@_attrs_define
class PushEstimateV1:
    """
    Attributes:
        customer_ref (str):  Example: 645.
        lines (List['EstimateLineV1']):
        pass_through (Union[Unset, PushEstimateV1PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        due_date (Union[Unset, datetime.date]):  Example: 2021-03-09.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-09.
        accepted_date (Union[Unset, datetime.date]):  Example: 2021-03-09.
        expiry_date (Union[Unset, datetime.date]):  Example: 2021-03-09.
        currency (Union[Unset, str]):  Example: CAD.
        ship_to_address (Union[Unset, ShippingAddressDto]):
        memo (Union[Unset, str]):  Example: Example memo..
    """

    customer_ref: str
    lines: List["EstimateLineV1"]
    pass_through: Union[Unset, "PushEstimateV1PassThrough"] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    accepted_date: Union[Unset, datetime.date] = UNSET
    expiry_date: Union[Unset, datetime.date] = UNSET
    currency: Union[Unset, str] = UNSET
    ship_to_address: Union[Unset, "ShippingAddressDto"] = UNSET
    memo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_ref = self.customer_ref

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        currency_rate = self.currency_rate

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        accepted_date: Union[Unset, str] = UNSET
        if not isinstance(self.accepted_date, Unset):
            accepted_date = self.accepted_date.isoformat()

        expiry_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat()

        currency = self.currency

        ship_to_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_address, Unset):
            ship_to_address = self.ship_to_address.to_dict()

        memo = self.memo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerRef": customer_ref,
                "lines": lines,
            }
        )
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if accepted_date is not UNSET:
            field_dict["acceptedDate"] = accepted_date
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if ship_to_address is not UNSET:
            field_dict["shipToAddress"] = ship_to_address
        if memo is not UNSET:
            field_dict["memo"] = memo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.estimate_line_v1 import EstimateLineV1
        from ..models.push_estimate_v1_pass_through import PushEstimateV1PassThrough
        from ..models.shipping_address_dto import ShippingAddressDto

        d = src_dict.copy()
        customer_ref = d.pop("customerRef")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = EstimateLineV1.from_dict(lines_item_data)

            lines.append(lines_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushEstimateV1PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushEstimateV1PassThrough.from_dict(_pass_through)

        currency_rate = d.pop("currencyRate", UNSET)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        _accepted_date = d.pop("acceptedDate", UNSET)
        accepted_date: Union[Unset, datetime.date]
        if isinstance(_accepted_date, Unset):
            accepted_date = UNSET
        else:
            accepted_date = isoparse(_accepted_date).date()

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, datetime.date]
        if isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date).date()

        currency = d.pop("currency", UNSET)

        _ship_to_address = d.pop("shipToAddress", UNSET)
        ship_to_address: Union[Unset, ShippingAddressDto]
        if isinstance(_ship_to_address, Unset):
            ship_to_address = UNSET
        else:
            ship_to_address = ShippingAddressDto.from_dict(_ship_to_address)

        memo = d.pop("memo", UNSET)

        push_estimate_v1 = cls(
            customer_ref=customer_ref,
            lines=lines,
            pass_through=pass_through,
            currency_rate=currency_rate,
            due_date=due_date,
            posted_date=posted_date,
            accepted_date=accepted_date,
            expiry_date=expiry_date,
            currency=currency,
            ship_to_address=ship_to_address,
            memo=memo,
        )

        push_estimate_v1.additional_properties = d
        return push_estimate_v1

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
