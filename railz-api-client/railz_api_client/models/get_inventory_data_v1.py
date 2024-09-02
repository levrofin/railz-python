import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_inventory_data_v1_item_status import GetInventoryDataV1ItemStatus
from ..models.get_inventory_data_v1_type import GetInventoryDataV1Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_or_invoice_item import BillOrInvoiceItem
    from ..models.inventory_subsidiary_ref import InventorySubsidiaryRef
    from ..models.quantity_on_hand_data import QuantityOnHandData


T = TypeVar("T", bound="GetInventoryDataV1")


@_attrs_define
class GetInventoryDataV1:
    """
    Attributes:
        id (str):  Example: 1.
        item_status (GetInventoryDataV1ItemStatus):  Example: active.
        name (Union[Unset, str]):  Example: Product Services.
        code (Union[Unset, str]):  Example: 100.
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        bill_item (Union[Unset, BillOrInvoiceItem]):
        invoice_item (Union[Unset, BillOrInvoiceItem]):
        is_invoice_item (Union[Unset, bool]):  Example: True.
        is_bill_item (Union[Unset, bool]):  Example: True.
        subsidiary_refs (Union[Unset, List['InventorySubsidiaryRef']]):
        quantity_on_hand (Union[Unset, List['QuantityOnHandData']]):
        type (Union[Unset, GetInventoryDataV1Type]):  Example: inventory.
        quantity_on_hand_per_location (Union[Unset, List['QuantityOnHandData']]):
    """

    id: str
    item_status: GetInventoryDataV1ItemStatus
    name: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    bill_item: Union[Unset, "BillOrInvoiceItem"] = UNSET
    invoice_item: Union[Unset, "BillOrInvoiceItem"] = UNSET
    is_invoice_item: Union[Unset, bool] = UNSET
    is_bill_item: Union[Unset, bool] = UNSET
    subsidiary_refs: Union[Unset, List["InventorySubsidiaryRef"]] = UNSET
    quantity_on_hand: Union[Unset, List["QuantityOnHandData"]] = UNSET
    type: Union[Unset, GetInventoryDataV1Type] = UNSET
    quantity_on_hand_per_location: Union[Unset, List["QuantityOnHandData"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        item_status = self.item_status

        name = self.name

        code = self.code

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        bill_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_item, Unset):
            bill_item = self.bill_item.to_dict()

        invoice_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_item, Unset):
            invoice_item = self.invoice_item.to_dict()

        is_invoice_item = self.is_invoice_item

        is_bill_item = self.is_bill_item

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        quantity_on_hand: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quantity_on_hand, Unset):
            quantity_on_hand = []
            for quantity_on_hand_item_data in self.quantity_on_hand:
                quantity_on_hand_item = quantity_on_hand_item_data.to_dict()
                quantity_on_hand.append(quantity_on_hand_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        quantity_on_hand_per_location: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quantity_on_hand_per_location, Unset):
            quantity_on_hand_per_location = []
            for quantity_on_hand_per_location_item_data in self.quantity_on_hand_per_location:
                quantity_on_hand_per_location_item = quantity_on_hand_per_location_item_data.to_dict()
                quantity_on_hand_per_location.append(quantity_on_hand_per_location_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "itemStatus": item_status,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if bill_item is not UNSET:
            field_dict["billItem"] = bill_item
        if invoice_item is not UNSET:
            field_dict["invoiceItem"] = invoice_item
        if is_invoice_item is not UNSET:
            field_dict["isInvoiceItem"] = is_invoice_item
        if is_bill_item is not UNSET:
            field_dict["isBillItem"] = is_bill_item
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if quantity_on_hand is not UNSET:
            field_dict["quantityOnHand"] = quantity_on_hand
        if type is not UNSET:
            field_dict["type"] = type
        if quantity_on_hand_per_location is not UNSET:
            field_dict["quantityOnHandPerLocation"] = quantity_on_hand_per_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bill_or_invoice_item import BillOrInvoiceItem
        from ..models.inventory_subsidiary_ref import InventorySubsidiaryRef
        from ..models.quantity_on_hand_data import QuantityOnHandData

        d = src_dict.copy()
        id = d.pop("id")

        item_status = d.pop("itemStatus")

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        _bill_item = d.pop("billItem", UNSET)
        bill_item: Union[Unset, BillOrInvoiceItem]
        if isinstance(_bill_item, Unset):
            bill_item = UNSET
        else:
            bill_item = BillOrInvoiceItem.from_dict(_bill_item)

        _invoice_item = d.pop("invoiceItem", UNSET)
        invoice_item: Union[Unset, BillOrInvoiceItem]
        if isinstance(_invoice_item, Unset):
            invoice_item = UNSET
        else:
            invoice_item = BillOrInvoiceItem.from_dict(_invoice_item)

        is_invoice_item = d.pop("isInvoiceItem", UNSET)

        is_bill_item = d.pop("isBillItem", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = InventorySubsidiaryRef.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        quantity_on_hand = []
        _quantity_on_hand = d.pop("quantityOnHand", UNSET)
        for quantity_on_hand_item_data in _quantity_on_hand or []:
            quantity_on_hand_item = QuantityOnHandData.from_dict(quantity_on_hand_item_data)

            quantity_on_hand.append(quantity_on_hand_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GetInventoryDataV1Type]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = _type

        quantity_on_hand_per_location = []
        _quantity_on_hand_per_location = d.pop("quantityOnHandPerLocation", UNSET)
        for quantity_on_hand_per_location_item_data in _quantity_on_hand_per_location or []:
            quantity_on_hand_per_location_item = QuantityOnHandData.from_dict(quantity_on_hand_per_location_item_data)

            quantity_on_hand_per_location.append(quantity_on_hand_per_location_item)

        get_inventory_data_v1 = cls(
            id=id,
            item_status=item_status,
            name=name,
            code=code,
            source_modified_date=source_modified_date,
            bill_item=bill_item,
            invoice_item=invoice_item,
            is_invoice_item=is_invoice_item,
            is_bill_item=is_bill_item,
            subsidiary_refs=subsidiary_refs,
            quantity_on_hand=quantity_on_hand,
            type=type,
            quantity_on_hand_per_location=quantity_on_hand_per_location,
        )

        get_inventory_data_v1.additional_properties = d
        return get_inventory_data_v1

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
