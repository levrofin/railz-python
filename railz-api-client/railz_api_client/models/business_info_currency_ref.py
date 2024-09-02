from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessInfoCurrencyRef")


@_attrs_define
class BusinessInfoCurrencyRef:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 21.
        is_active (Union[Unset, bool]):
        is_base_currency (Union[Unset, bool]):  Example: True.
        symbol (Union[Unset, str]):  Example: USD.
        name (Union[Unset, str]):  Example: USA.
    """

    id: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_base_currency: Union[Unset, bool] = UNSET
    symbol: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        is_active = self.is_active

        is_base_currency = self.is_base_currency

        symbol = self.symbol

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_base_currency is not UNSET:
            field_dict["isBaseCurrency"] = is_base_currency
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_active = d.pop("isActive", UNSET)

        is_base_currency = d.pop("isBaseCurrency", UNSET)

        symbol = d.pop("symbol", UNSET)

        name = d.pop("name", UNSET)

        business_info_currency_ref = cls(
            id=id,
            is_active=is_active,
            is_base_currency=is_base_currency,
            symbol=symbol,
            name=name,
        )

        business_info_currency_ref.additional_properties = d
        return business_info_currency_ref

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
