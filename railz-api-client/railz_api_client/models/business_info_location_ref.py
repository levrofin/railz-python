from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_info_location_address import BusinessInfoLocationAddress
    from ..models.business_info_location_parent_ref import BusinessInfoLocationParentRef


T = TypeVar("T", bound="BusinessInfoLocationRef")


@_attrs_define
class BusinessInfoLocationRef:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 52.
        name (Union[Unset, str]):  Example: United States.
        address (Union[Unset, BusinessInfoLocationAddress]):
        parent_ref (Union[Unset, BusinessInfoLocationParentRef]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    address: Union[Unset, "BusinessInfoLocationAddress"] = UNSET
    parent_ref: Union[Unset, "BusinessInfoLocationParentRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.business_info_location_address import BusinessInfoLocationAddress
        from ..models.business_info_location_parent_ref import BusinessInfoLocationParentRef

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, BusinessInfoLocationAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = BusinessInfoLocationAddress.from_dict(_address)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, BusinessInfoLocationParentRef]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = BusinessInfoLocationParentRef.from_dict(_parent_ref)

        business_info_location_ref = cls(
            id=id,
            name=name,
            address=address,
            parent_ref=parent_ref,
        )

        business_info_location_ref.additional_properties = d
        return business_info_location_ref

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
