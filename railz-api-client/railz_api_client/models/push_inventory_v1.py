from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_inventory_v1_type import PushInventoryV1Type, check_push_inventory_v1_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_bill_invoice_line_items import InventoryBillInvoiceLineItems


T = TypeVar("T", bound="PushInventoryV1")


@_attrs_define
class PushInventoryV1:
    """
    Attributes:
        code (Union[Unset, str]):  Example: GOL-W.
        type (Union[Unset, PushInventoryV1Type]):  Example: inventory.
        name (Union[Unset, str]):  Example: White golf balls..
        quantity_on_hand (Union[Unset, float]):  Example: 200.
        subsidiary_refs (Union[Unset, List[str]]):  Example: ['2', '3hn', '1t2'].
        invoice_item (Union[Unset, InventoryBillInvoiceLineItems]):
        bill_item (Union[Unset, InventoryBillInvoiceLineItems]):
        is_bill_item (Union[Unset, bool]):  Default: True. Example: True.
        is_invoice_item (Union[Unset, bool]):  Default: True. Example: True.
    """

    code: Union[Unset, str] = UNSET
    type: Union[Unset, PushInventoryV1Type] = UNSET
    name: Union[Unset, str] = UNSET
    quantity_on_hand: Union[Unset, float] = UNSET
    subsidiary_refs: Union[Unset, List[str]] = UNSET
    invoice_item: Union[Unset, "InventoryBillInvoiceLineItems"] = UNSET
    bill_item: Union[Unset, "InventoryBillInvoiceLineItems"] = UNSET
    is_bill_item: Union[Unset, bool] = True
    is_invoice_item: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        name = self.name

        quantity_on_hand = self.quantity_on_hand

        subsidiary_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = self.subsidiary_refs

        invoice_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_item, Unset):
            invoice_item = self.invoice_item.to_dict()

        bill_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_item, Unset):
            bill_item = self.bill_item.to_dict()

        is_bill_item = self.is_bill_item

        is_invoice_item = self.is_invoice_item

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if quantity_on_hand is not UNSET:
            field_dict["quantityOnHand"] = quantity_on_hand
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if invoice_item is not UNSET:
            field_dict["invoiceItem"] = invoice_item
        if bill_item is not UNSET:
            field_dict["billItem"] = bill_item
        if is_bill_item is not UNSET:
            field_dict["isBillItem"] = is_bill_item
        if is_invoice_item is not UNSET:
            field_dict["isInvoiceItem"] = is_invoice_item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inventory_bill_invoice_line_items import InventoryBillInvoiceLineItems

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PushInventoryV1Type]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_push_inventory_v1_type(_type)

        name = d.pop("name", UNSET)

        quantity_on_hand = d.pop("quantityOnHand", UNSET)

        subsidiary_refs = cast(List[str], d.pop("subsidiaryRefs", UNSET))

        _invoice_item = d.pop("invoiceItem", UNSET)
        invoice_item: Union[Unset, InventoryBillInvoiceLineItems]
        if isinstance(_invoice_item, Unset):
            invoice_item = UNSET
        else:
            invoice_item = InventoryBillInvoiceLineItems.from_dict(_invoice_item)

        _bill_item = d.pop("billItem", UNSET)
        bill_item: Union[Unset, InventoryBillInvoiceLineItems]
        if isinstance(_bill_item, Unset):
            bill_item = UNSET
        else:
            bill_item = InventoryBillInvoiceLineItems.from_dict(_bill_item)

        is_bill_item = d.pop("isBillItem", UNSET)

        is_invoice_item = d.pop("isInvoiceItem", UNSET)

        push_inventory_v1 = cls(
            code=code,
            type=type,
            name=name,
            quantity_on_hand=quantity_on_hand,
            subsidiary_refs=subsidiary_refs,
            invoice_item=invoice_item,
            bill_item=bill_item,
            is_bill_item=is_bill_item,
            is_invoice_item=is_invoice_item,
        )

        push_inventory_v1.additional_properties = d
        return push_inventory_v1

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
