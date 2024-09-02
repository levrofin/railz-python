from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_ref_dto import AccountRefDto
    from ..models.inventory_ref_dto import InventoryRefDto


T = TypeVar("T", bound="QuantityOnHandV2Dto")


@_attrs_define
class QuantityOnHandV2Dto:
    """
    Attributes:
        quantity (Union[Unset, float]):  Example: 2.5.
        location_ref (Union[Unset, InventoryRefDto]):
        account_ref (Union[Unset, AccountRefDto]):
    """

    quantity: Union[Unset, float] = UNSET
    location_ref: Union[Unset, "InventoryRefDto"] = UNSET
    account_ref: Union[Unset, "AccountRefDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity

        location_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location_ref, Unset):
            location_ref = self.location_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_ref_dto import AccountRefDto
        from ..models.inventory_ref_dto import InventoryRefDto

        d = src_dict.copy()
        quantity = d.pop("quantity", UNSET)

        _location_ref = d.pop("locationRef", UNSET)
        location_ref: Union[Unset, InventoryRefDto]
        if isinstance(_location_ref, Unset):
            location_ref = UNSET
        else:
            location_ref = InventoryRefDto.from_dict(_location_ref)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountRefDto]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountRefDto.from_dict(_account_ref)

        quantity_on_hand_v2_dto = cls(
            quantity=quantity,
            location_ref=location_ref,
            account_ref=account_ref,
        )

        quantity_on_hand_v2_dto.additional_properties = d
        return quantity_on_hand_v2_dto

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
