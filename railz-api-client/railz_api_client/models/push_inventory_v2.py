from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_inventory_v2_type import PushInventoryV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_bill_invoice_line_items_v2 import InventoryBillInvoiceLineItemsV2
    from ..models.push_inventory_v2_pass_through import PushInventoryV2PassThrough
    from ..models.quantity_on_hand_v2_dto import QuantityOnHandV2Dto
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto


T = TypeVar("T", bound="PushInventoryV2")


@_attrs_define
class PushInventoryV2:
    """
    Attributes:
        name (str):  Example: White golf balls..
        code (Union[Unset, str]):  Example: GOL-W.
        type (Union[Unset, PushInventoryV2Type]):  Example: inventory.
        quantity_on_hand (Union[Unset, List['QuantityOnHandV2Dto']]):
        bill_item (Union[Unset, InventoryBillInvoiceLineItemsV2]):
        invoice_item (Union[Unset, InventoryBillInvoiceLineItemsV2]):
        is_bill_item (Union[Unset, bool]):  Example: True.
        is_invoice_item (Union[Unset, bool]):  Example: True.
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        pass_through (Union[Unset, PushInventoryV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    name: str
    code: Union[Unset, str] = UNSET
    type: Union[Unset, PushInventoryV2Type] = UNSET
    quantity_on_hand: Union[Unset, List["QuantityOnHandV2Dto"]] = UNSET
    bill_item: Union[Unset, "InventoryBillInvoiceLineItemsV2"] = UNSET
    invoice_item: Union[Unset, "InventoryBillInvoiceLineItemsV2"] = UNSET
    is_bill_item: Union[Unset, bool] = UNSET
    is_invoice_item: Union[Unset, bool] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    pass_through: Union[Unset, "PushInventoryV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        code = self.code

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        quantity_on_hand: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quantity_on_hand, Unset):
            quantity_on_hand = []
            for quantity_on_hand_item_data in self.quantity_on_hand:
                quantity_on_hand_item = quantity_on_hand_item_data.to_dict()
                quantity_on_hand.append(quantity_on_hand_item)

        bill_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_item, Unset):
            bill_item = self.bill_item.to_dict()

        invoice_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_item, Unset):
            invoice_item = self.invoice_item.to_dict()

        is_bill_item = self.is_bill_item

        is_invoice_item = self.is_invoice_item

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if type is not UNSET:
            field_dict["type"] = type
        if quantity_on_hand is not UNSET:
            field_dict["quantityOnHand"] = quantity_on_hand
        if bill_item is not UNSET:
            field_dict["billItem"] = bill_item
        if invoice_item is not UNSET:
            field_dict["invoiceItem"] = invoice_item
        if is_bill_item is not UNSET:
            field_dict["isBillItem"] = is_bill_item
        if is_invoice_item is not UNSET:
            field_dict["isInvoiceItem"] = is_invoice_item
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inventory_bill_invoice_line_items_v2 import InventoryBillInvoiceLineItemsV2
        from ..models.push_inventory_v2_pass_through import PushInventoryV2PassThrough
        from ..models.quantity_on_hand_v2_dto import QuantityOnHandV2Dto
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto

        d = src_dict.copy()
        name = d.pop("name")

        code = d.pop("code", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PushInventoryV2Type]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = _type

        quantity_on_hand = []
        _quantity_on_hand = d.pop("quantityOnHand", UNSET)
        for quantity_on_hand_item_data in _quantity_on_hand or []:
            quantity_on_hand_item = QuantityOnHandV2Dto.from_dict(quantity_on_hand_item_data)

            quantity_on_hand.append(quantity_on_hand_item)

        _bill_item = d.pop("billItem", UNSET)
        bill_item: Union[Unset, InventoryBillInvoiceLineItemsV2]
        if isinstance(_bill_item, Unset):
            bill_item = UNSET
        else:
            bill_item = InventoryBillInvoiceLineItemsV2.from_dict(_bill_item)

        _invoice_item = d.pop("invoiceItem", UNSET)
        invoice_item: Union[Unset, InventoryBillInvoiceLineItemsV2]
        if isinstance(_invoice_item, Unset):
            invoice_item = UNSET
        else:
            invoice_item = InventoryBillInvoiceLineItemsV2.from_dict(_invoice_item)

        is_bill_item = d.pop("isBillItem", UNSET)

        is_invoice_item = d.pop("isInvoiceItem", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushInventoryV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushInventoryV2PassThrough.from_dict(_pass_through)

        push_inventory_v2 = cls(
            name=name,
            code=code,
            type=type,
            quantity_on_hand=quantity_on_hand,
            bill_item=bill_item,
            invoice_item=invoice_item,
            is_bill_item=is_bill_item,
            is_invoice_item=is_invoice_item,
            subsidiary_refs=subsidiary_refs,
            pass_through=pass_through,
        )

        push_inventory_v2.additional_properties = d
        return push_inventory_v2

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
