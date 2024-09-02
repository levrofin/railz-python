from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_ref import CustomerRef
    from ..models.invoice_bill_line_items_v1 import InvoiceBillLineItemsV1
    from ..models.location_ref import LocationRef


T = TypeVar("T", bound="GetInvoiceCreditNoteDataV1")


@_attrs_define
class GetInvoiceCreditNoteDataV1:
    """
    Attributes:
        customer_ref (Union[Unset, CustomerRef]):
        location_ref (Union[Unset, LocationRef]):
        lines (Union[Unset, List['InvoiceBillLineItemsV1']]):
    """

    customer_ref: Union[Unset, "CustomerRef"] = UNSET
    location_ref: Union[Unset, "LocationRef"] = UNSET
    lines: Union[Unset, List["InvoiceBillLineItemsV1"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        location_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location_ref, Unset):
            location_ref = self.location_ref.to_dict()

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_ref import CustomerRef
        from ..models.invoice_bill_line_items_v1 import InvoiceBillLineItemsV1
        from ..models.location_ref import LocationRef

        d = src_dict.copy()
        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CustomerRef.from_dict(_customer_ref)

        _location_ref = d.pop("locationRef", UNSET)
        location_ref: Union[Unset, LocationRef]
        if isinstance(_location_ref, Unset):
            location_ref = UNSET
        else:
            location_ref = LocationRef.from_dict(_location_ref)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = InvoiceBillLineItemsV1.from_dict(lines_item_data)

            lines.append(lines_item)

        get_invoice_credit_note_data_v1 = cls(
            customer_ref=customer_ref,
            location_ref=location_ref,
            lines=lines,
        )

        get_invoice_credit_note_data_v1.additional_properties = d
        return get_invoice_credit_note_data_v1

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
