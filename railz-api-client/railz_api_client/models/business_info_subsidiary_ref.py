from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_info_subsidiary_ref_currency_ref import BusinessInfoSubsidiaryRefCurrencyRef
    from ..models.business_info_subsidiary_ref_location_ref import BusinessInfoSubsidiaryRefLocationRef
    from ..models.business_info_subsidiary_ref_parent_ref import BusinessInfoSubsidiaryRefParentRef


T = TypeVar("T", bound="BusinessInfoSubsidiaryRef")


@_attrs_define
class BusinessInfoSubsidiaryRef:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 8.
        name (Union[Unset, str]):  Example: Honeywell.
        parent_ref (Union[Unset, BusinessInfoSubsidiaryRefParentRef]):
        currencies (Union[Unset, List['BusinessInfoSubsidiaryRefCurrencyRef']]):
        locations (Union[Unset, List['BusinessInfoSubsidiaryRefLocationRef']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    parent_ref: Union[Unset, "BusinessInfoSubsidiaryRefParentRef"] = UNSET
    currencies: Union[Unset, List["BusinessInfoSubsidiaryRefCurrencyRef"]] = UNSET
    locations: Union[Unset, List["BusinessInfoSubsidiaryRefLocationRef"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        currencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.currencies, Unset):
            currencies = []
            for currencies_item_data in self.currencies:
                currencies_item = currencies_item_data.to_dict()
                currencies.append(currencies_item)

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if currencies is not UNSET:
            field_dict["currencies"] = currencies
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.business_info_subsidiary_ref_currency_ref import BusinessInfoSubsidiaryRefCurrencyRef
        from ..models.business_info_subsidiary_ref_location_ref import BusinessInfoSubsidiaryRefLocationRef
        from ..models.business_info_subsidiary_ref_parent_ref import BusinessInfoSubsidiaryRefParentRef

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, BusinessInfoSubsidiaryRefParentRef]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = BusinessInfoSubsidiaryRefParentRef.from_dict(_parent_ref)

        currencies = []
        _currencies = d.pop("currencies", UNSET)
        for currencies_item_data in _currencies or []:
            currencies_item = BusinessInfoSubsidiaryRefCurrencyRef.from_dict(currencies_item_data)

            currencies.append(currencies_item)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = BusinessInfoSubsidiaryRefLocationRef.from_dict(locations_item_data)

            locations.append(locations_item)

        business_info_subsidiary_ref = cls(
            id=id,
            name=name,
            parent_ref=parent_ref,
            currencies=currencies,
            locations=locations,
        )

        business_info_subsidiary_ref.additional_properties = d
        return business_info_subsidiary_ref

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
