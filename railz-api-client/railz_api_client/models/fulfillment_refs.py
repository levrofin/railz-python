from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FulfillmentRefs")


@_attrs_define
class FulfillmentRefs:
    """
    Attributes:
        carrier (Union[Unset, str]):  Example: USPS.
        tracking_number (Union[Unset, str]):  Example: 1Z2345.
        service (Union[Unset, str]):  Example: manual.
        tracking_url (Union[Unset, str]):  Example:
            https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z2345.
    """

    carrier: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    tracking_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carrier = self.carrier

        tracking_number = self.tracking_number

        service = self.service

        tracking_url = self.tracking_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if service is not UNSET:
            field_dict["service"] = service
        if tracking_url is not UNSET:
            field_dict["trackingUrl"] = tracking_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        carrier = d.pop("carrier", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        service = d.pop("service", UNSET)

        tracking_url = d.pop("trackingUrl", UNSET)

        fulfillment_refs = cls(
            carrier=carrier,
            tracking_number=tracking_number,
            service=service,
            tracking_url=tracking_url,
        )

        fulfillment_refs.additional_properties = d
        return fulfillment_refs

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
