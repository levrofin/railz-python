from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref import AccountRef
    from ..models.inventory_location_ref import InventoryLocationRef


T = TypeVar("T", bound="QuantityOnHandData")


@_attrs_define
class QuantityOnHandData:
    """
    Attributes:
        location_ref (Union[Unset, InventoryLocationRef]):
        quantity (Union[Unset, float]):  Example: 2.5.
        account_ref (Union[Unset, AccountRef]):
    """

    location_ref: Union[Unset, "InventoryLocationRef"] = UNSET
    quantity: Union[Unset, float] = UNSET
    account_ref: Union[Unset, "AccountRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location_ref, Unset):
            location_ref = self.location_ref.to_dict()

        quantity = self.quantity

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref import AccountRef
        from ..models.inventory_location_ref import InventoryLocationRef

        d = src_dict.copy()
        _location_ref = d.pop("locationRef", UNSET)
        location_ref: Union[Unset, InventoryLocationRef]
        if isinstance(_location_ref, Unset):
            location_ref = UNSET
        else:
            location_ref = InventoryLocationRef.from_dict(_location_ref)

        quantity = d.pop("quantity", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRef.from_dict(_account_ref)

        quantity_on_hand_data = cls(
            location_ref=location_ref,
            quantity=quantity,
            account_ref=account_ref,
        )

        quantity_on_hand_data.additional_properties = d
        return quantity_on_hand_data

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
