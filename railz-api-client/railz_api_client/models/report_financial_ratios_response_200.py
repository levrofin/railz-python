from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.report_financial_ratios_response_200_data import ReportFinancialRatiosResponse200Data
    from ..models.report_financial_ratios_response_200_meta import ReportFinancialRatiosResponse200Meta


T = TypeVar("T", bound="ReportFinancialRatiosResponse200")


@_attrs_define
class ReportFinancialRatiosResponse200:
    """
    Attributes:
        meta (ReportFinancialRatiosResponse200Meta):
        data (ReportFinancialRatiosResponse200Data):
    """

    meta: "ReportFinancialRatiosResponse200Meta"
    data: "ReportFinancialRatiosResponse200Data"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        data = self.data.to_dict()

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
        from ..models.report_financial_ratios_response_200_data import ReportFinancialRatiosResponse200Data
        from ..models.report_financial_ratios_response_200_meta import ReportFinancialRatiosResponse200Meta

        d = src_dict.copy()
        meta = ReportFinancialRatiosResponse200Meta.from_dict(d.pop("meta"))

        data = ReportFinancialRatiosResponse200Data.from_dict(d.pop("data"))

        report_financial_ratios_response_200 = cls(
            meta=meta,
            data=data,
        )

        report_financial_ratios_response_200.additional_properties = d
        return report_financial_ratios_response_200

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
