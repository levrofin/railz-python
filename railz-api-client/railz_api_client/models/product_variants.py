import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory import Inventory
    from ..models.weight import Weight


T = TypeVar("T", bound="ProductVariants")


@_attrs_define
class ProductVariants:
    """
    Attributes:
        id (str):  Example: 808950810.
        name (str):  Example: Pink.
        unit_price (float):  Example: 199.
        created_date (datetime.datetime):  Example: 2022-03-11T11:29:03-05:00.
        is_tax_enabled (Union[Unset, bool]):  Example: True.
        sku (Union[Unset, str]):  Example: IPOD2008PINK.
        barcode (Union[Unset, str]):  Example: 1234_pink.
        weight (Union[Unset, Weight]):
        inventory (Union[Unset, Inventory]):
        is_shipping_required (Union[Unset, bool]):  Example: True.
    """

    id: str
    name: str
    unit_price: float
    created_date: datetime.datetime
    is_tax_enabled: Union[Unset, bool] = UNSET
    sku: Union[Unset, str] = UNSET
    barcode: Union[Unset, str] = UNSET
    weight: Union[Unset, "Weight"] = UNSET
    inventory: Union[Unset, "Inventory"] = UNSET
    is_shipping_required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        unit_price = self.unit_price

        created_date = self.created_date.isoformat()

        is_tax_enabled = self.is_tax_enabled

        sku = self.sku

        barcode = self.barcode

        weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        inventory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = self.inventory.to_dict()

        is_shipping_required = self.is_shipping_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "unitPrice": unit_price,
                "createdDate": created_date,
            }
        )
        if is_tax_enabled is not UNSET:
            field_dict["isTaxEnabled"] = is_tax_enabled
        if sku is not UNSET:
            field_dict["sku"] = sku
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if weight is not UNSET:
            field_dict["weight"] = weight
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if is_shipping_required is not UNSET:
            field_dict["isShippingRequired"] = is_shipping_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inventory import Inventory
        from ..models.weight import Weight

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        unit_price = d.pop("unitPrice")

        created_date = isoparse(d.pop("createdDate"))

        is_tax_enabled = d.pop("isTaxEnabled", UNSET)

        sku = d.pop("sku", UNSET)

        barcode = d.pop("barcode", UNSET)

        _weight = d.pop("weight", UNSET)
        weight: Union[Unset, Weight]
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = Weight.from_dict(_weight)

        _inventory = d.pop("inventory", UNSET)
        inventory: Union[Unset, Inventory]
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = Inventory.from_dict(_inventory)

        is_shipping_required = d.pop("isShippingRequired", UNSET)

        product_variants = cls(
            id=id,
            name=name,
            unit_price=unit_price,
            created_date=created_date,
            is_tax_enabled=is_tax_enabled,
            sku=sku,
            barcode=barcode,
            weight=weight,
            inventory=inventory,
            is_shipping_required=is_shipping_required,
        )

        product_variants.additional_properties = d
        return product_variants

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
