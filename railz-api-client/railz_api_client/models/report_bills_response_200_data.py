from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportBillsResponse200Data")


@_attrs_define
class ReportBillsResponse200Data:
    """
    Attributes:
        unpaid_amount (float): sum of amount due
        paid_amount (float): sum (latestAmount - amountDue) Example: 1000.
        overdue_amount (float): where current Date > dueDate, sum amountDue
    """

    unpaid_amount: float
    paid_amount: float
    overdue_amount: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unpaid_amount = self.unpaid_amount

        paid_amount = self.paid_amount

        overdue_amount = self.overdue_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unpaidAmount": unpaid_amount,
                "paidAmount": paid_amount,
                "overdueAmount": overdue_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unpaid_amount = d.pop("unpaidAmount")

        paid_amount = d.pop("paidAmount")

        overdue_amount = d.pop("overdueAmount")

        report_bills_response_200_data = cls(
            unpaid_amount=unpaid_amount,
            paid_amount=paid_amount,
            overdue_amount=overdue_amount,
        )

        report_bills_response_200_data.additional_properties = d
        return report_bills_response_200_data

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
