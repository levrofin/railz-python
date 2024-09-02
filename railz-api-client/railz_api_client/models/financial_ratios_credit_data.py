from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialRatiosCreditData")


@_attrs_define
class FinancialRatiosCreditData:
    """
    Attributes:
        average_collection_period (Union[Unset, float]):  Example: 36.5.
    """

    average_collection_period: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        average_collection_period = self.average_collection_period

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average_collection_period is not UNSET:
            field_dict["averageCollectionPeriod"] = average_collection_period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        average_collection_period = d.pop("averageCollectionPeriod", UNSET)

        financial_ratios_credit_data = cls(
            average_collection_period=average_collection_period,
        )

        financial_ratios_credit_data.additional_properties = d
        return financial_ratios_credit_data

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
