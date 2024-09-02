from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_revenue_response_200_data_sub_sections_item import ReportRevenueResponse200DataSubSectionsItem


T = TypeVar("T", bound="ReportRevenueResponse200Data")


@_attrs_define
class ReportRevenueResponse200Data:
    """
    Attributes:
        sub_sections (List['ReportRevenueResponse200DataSubSectionsItem']): For each subsection, get its end date values
            and return the top 3 and the remaining sub section values should be summed up and indicated in the last object
            where name = 'Other'
        total_amount (float): Total of all values in the expenses section in incomeStatement results as at end date
            Example: 3500.
        percentage_change (Union[Unset, float]): Percentage change between previous period and current end date period
            Example: 15.
    """

    sub_sections: List["ReportRevenueResponse200DataSubSectionsItem"]
    total_amount: float
    percentage_change: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_sections = []
        for sub_sections_item_data in self.sub_sections:
            sub_sections_item = sub_sections_item_data.to_dict()
            sub_sections.append(sub_sections_item)

        total_amount = self.total_amount

        percentage_change = self.percentage_change

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subSections": sub_sections,
                "totalAmount": total_amount,
            }
        )
        if percentage_change is not UNSET:
            field_dict["percentageChange"] = percentage_change

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_revenue_response_200_data_sub_sections_item import (
            ReportRevenueResponse200DataSubSectionsItem,
        )

        d = src_dict.copy()
        sub_sections = []
        _sub_sections = d.pop("subSections")
        for sub_sections_item_data in _sub_sections:
            sub_sections_item = ReportRevenueResponse200DataSubSectionsItem.from_dict(sub_sections_item_data)

            sub_sections.append(sub_sections_item)

        total_amount = d.pop("totalAmount")

        percentage_change = d.pop("percentageChange", UNSET)

        report_revenue_response_200_data = cls(
            sub_sections=sub_sections,
            total_amount=total_amount,
            percentage_change=percentage_change,
        )

        report_revenue_response_200_data.additional_properties = d
        return report_revenue_response_200_data

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
