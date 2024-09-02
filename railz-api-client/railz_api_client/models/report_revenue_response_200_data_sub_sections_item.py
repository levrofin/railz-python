from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportRevenueResponse200DataSubSectionsItem")


@_attrs_define
class ReportRevenueResponse200DataSubSectionsItem:
    """
    Example:
        [{'name': 'Utilities', 'amount': 2300}, {'name': 'Service Fee Income', 'amount': 1000}, {'name': 'Other',
            'amount': 200}]

    Attributes:
        name (str): Sub section with the largest amount Example: Operating Expenses.
        amount (float): Total of all values in the expenses section in incomeStatement results Example: 1200.
    """

    name: str
    amount: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        amount = d.pop("amount")

        report_revenue_response_200_data_sub_sections_item = cls(
            name=name,
            amount=amount,
        )

        report_revenue_response_200_data_sub_sections_item.additional_properties = d
        return report_revenue_response_200_data_sub_sections_item

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
