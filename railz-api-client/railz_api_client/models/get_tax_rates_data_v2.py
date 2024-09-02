import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_rate_component_v2 import TaxRateComponentV2


T = TypeVar("T", bound="GetTaxRatesDataV2")


@_attrs_define
class GetTaxRatesDataV2:
    """
    Attributes:
        id (str):  Example: 1.
        name (str):  Example: Harmonized sales tax.
        code (Union[Unset, str]):  Example: HST.
        effective_tax_rate (Union[Unset, float]):
        total_tax_rate (Union[Unset, float]):  Example: 13.
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-10T11:26:06.619Z.
        components (Union[Unset, List['TaxRateComponentV2']]):
    """

    id: str
    name: str
    code: Union[Unset, str] = UNSET
    effective_tax_rate: Union[Unset, float] = UNSET
    total_tax_rate: Union[Unset, float] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    components: Union[Unset, List["TaxRateComponentV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        code = self.code

        effective_tax_rate = self.effective_tax_rate

        total_tax_rate = self.total_tax_rate

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

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
                "id": id,
                "name": name,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if effective_tax_rate is not UNSET:
            field_dict["effectiveTaxRate"] = effective_tax_rate
        if total_tax_rate is not UNSET:
            field_dict["totalTaxRate"] = total_tax_rate
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_rate_component_v2 import TaxRateComponentV2

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        code = d.pop("code", UNSET)

        effective_tax_rate = d.pop("effectiveTaxRate", UNSET)

        total_tax_rate = d.pop("totalTaxRate", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        components = []
        _components = d.pop("components", UNSET)
        for components_item_data in _components or []:
            components_item = TaxRateComponentV2.from_dict(components_item_data)

            components.append(components_item)

        get_tax_rates_data_v2 = cls(
            id=id,
            name=name,
            code=code,
            effective_tax_rate=effective_tax_rate,
            total_tax_rate=total_tax_rate,
            source_modified_date=source_modified_date,
            components=components,
        )

        get_tax_rates_data_v2.additional_properties = d
        return get_tax_rates_data_v2

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
