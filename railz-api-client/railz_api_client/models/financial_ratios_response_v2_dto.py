from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.financial_ratios_report_v2 import FinancialRatiosReportV2
    from ..models.pagination_meta_data import PaginationMetaData


T = TypeVar("T", bound="FinancialRatiosResponseV2Dto")


@_attrs_define
class FinancialRatiosResponseV2Dto:
    """
    Attributes:
        count (float):  Example: 1.
        pagination (PaginationMetaData):
        ratios (List['FinancialRatiosReportV2']):
    """

    count: float
    pagination: "PaginationMetaData"
    ratios: List["FinancialRatiosReportV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        pagination = self.pagination.to_dict()

        ratios = []
        for ratios_item_data in self.ratios:
            ratios_item = ratios_item_data.to_dict()
            ratios.append(ratios_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "pagination": pagination,
                "ratios": ratios,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.financial_ratios_report_v2 import FinancialRatiosReportV2
        from ..models.pagination_meta_data import PaginationMetaData

        d = src_dict.copy()
        count = d.pop("count")

        pagination = PaginationMetaData.from_dict(d.pop("pagination"))

        ratios = []
        _ratios = d.pop("ratios")
        for ratios_item_data in _ratios:
            ratios_item = FinancialRatiosReportV2.from_dict(ratios_item_data)

            ratios.append(ratios_item)

        financial_ratios_response_v2_dto = cls(
            count=count,
            pagination=pagination,
            ratios=ratios,
        )

        financial_ratios_response_v2_dto.additional_properties = d
        return financial_ratios_response_v2_dto

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
