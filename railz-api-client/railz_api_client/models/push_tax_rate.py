from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_tax_rate_component import PushTaxRateComponent


T = TypeVar("T", bound="PushTaxRate")


@_attrs_define
class PushTaxRate:
    """
    Attributes:
        name (str):  Example: Name of the tax rate.
        code (Union[Unset, str]):  Example: 11200.
        effective_tax_rate (Union[Unset, float]):
        total_tax_rate (Union[Unset, float]):
        bank_name (Union[Unset, str]):  Example: TD Bank.
        components (Union[Unset, List['PushTaxRateComponent']]):
    """

    name: str
    code: Union[Unset, str] = UNSET
    effective_tax_rate: Union[Unset, float] = UNSET
    total_tax_rate: Union[Unset, float] = UNSET
    bank_name: Union[Unset, str] = UNSET
    components: Union[Unset, List["PushTaxRateComponent"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        code = self.code

        effective_tax_rate = self.effective_tax_rate

        total_tax_rate = self.total_tax_rate

        bank_name = self.bank_name

        components: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if effective_tax_rate is not UNSET:
            field_dict["effectiveTaxRate"] = effective_tax_rate
        if total_tax_rate is not UNSET:
            field_dict["totalTaxRate"] = total_tax_rate
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_tax_rate_component import PushTaxRateComponent

        d = src_dict.copy()
        name = d.pop("name")

        code = d.pop("code", UNSET)

        effective_tax_rate = d.pop("effectiveTaxRate", UNSET)

        total_tax_rate = d.pop("totalTaxRate", UNSET)

        bank_name = d.pop("bankName", UNSET)

        components = []
        _components = d.pop("components", UNSET)
        for components_item_data in _components or []:
            components_item = PushTaxRateComponent.from_dict(components_item_data)

            components.append(components_item)

        push_tax_rate = cls(
            name=name,
            code=code,
            effective_tax_rate=effective_tax_rate,
            total_tax_rate=total_tax_rate,
            bank_name=bank_name,
            components=components,
        )

        push_tax_rate.additional_properties = d
        return push_tax_rate

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
