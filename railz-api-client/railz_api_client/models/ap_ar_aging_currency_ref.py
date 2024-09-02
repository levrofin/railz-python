from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApArAgingCurrencyRef")


@_attrs_define
class ApArAgingCurrencyRef:
    """
    Attributes:
        id (str):  Example: CAD.
        name (Union[Unset, str]):  Example: Canadian Dollar.
        symbol (Union[Unset, str]):  Example: USD,CAD.
    """

    id: str
    name: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        ap_ar_aging_currency_ref = cls(
            id=id,
            name=name,
            symbol=symbol,
        )

        ap_ar_aging_currency_ref.additional_properties = d
        return ap_ar_aging_currency_ref

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
