from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.report_income_statements_response_200_data_item import ReportIncomeStatementsResponse200DataItem
    from ..models.report_income_statements_response_200_meta import ReportIncomeStatementsResponse200Meta


T = TypeVar("T", bound="ReportIncomeStatementsResponse200")


@_attrs_define
class ReportIncomeStatementsResponse200:
    """
    Attributes:
        meta (ReportIncomeStatementsResponse200Meta):
        data (List['ReportIncomeStatementsResponse200DataItem']):
    """

    meta: "ReportIncomeStatementsResponse200Meta"
    data: List["ReportIncomeStatementsResponse200DataItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_income_statements_response_200_data_item import ReportIncomeStatementsResponse200DataItem
        from ..models.report_income_statements_response_200_meta import ReportIncomeStatementsResponse200Meta

        d = src_dict.copy()
        meta = ReportIncomeStatementsResponse200Meta.from_dict(d.pop("meta"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ReportIncomeStatementsResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        report_income_statements_response_200 = cls(
            meta=meta,
            data=data,
        )

        report_income_statements_response_200.additional_properties = d
        return report_income_statements_response_200

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
