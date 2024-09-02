from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.summary_statistics_data import SummaryStatisticsData


T = TypeVar("T", bound="TaxBenchmarkingsData")


@_attrs_define
class TaxBenchmarkingsData:
    """
    Attributes:
        section ('SummaryStatisticsData'):
        sub_section ('SummaryStatisticsData'):
        group ('SummaryStatisticsData'):
        sub_group ('SummaryStatisticsData'):
    """

    section: "SummaryStatisticsData"
    sub_section: "SummaryStatisticsData"
    group: "SummaryStatisticsData"
    sub_group: "SummaryStatisticsData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.summary_statistics_data import SummaryStatisticsData

        section: Dict[str, Any]
        if isinstance(self.section, SummaryStatisticsData):
            section = self.section.to_dict()

        sub_section: Dict[str, Any]
        if isinstance(self.sub_section, SummaryStatisticsData):
            sub_section = self.sub_section.to_dict()

        group: Dict[str, Any]
        if isinstance(self.group, SummaryStatisticsData):
            group = self.group.to_dict()

        sub_group: Dict[str, Any]
        if isinstance(self.sub_group, SummaryStatisticsData):
            sub_group = self.sub_group.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "section": section,
                "subSection": sub_section,
                "group": group,
                "subGroup": sub_group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.summary_statistics_data import SummaryStatisticsData

        d = src_dict.copy()

        def _parse_section(data: object) -> "SummaryStatisticsData":
            if not isinstance(data, dict):
                raise TypeError()
            section_type_0 = SummaryStatisticsData.from_dict(data)

            return section_type_0

        section = _parse_section(d.pop("section"))

        def _parse_sub_section(data: object) -> "SummaryStatisticsData":
            if not isinstance(data, dict):
                raise TypeError()
            sub_section_type_0 = SummaryStatisticsData.from_dict(data)

            return sub_section_type_0

        sub_section = _parse_sub_section(d.pop("subSection"))

        def _parse_group(data: object) -> "SummaryStatisticsData":
            if not isinstance(data, dict):
                raise TypeError()
            group_type_0 = SummaryStatisticsData.from_dict(data)

            return group_type_0

        group = _parse_group(d.pop("group"))

        def _parse_sub_group(data: object) -> "SummaryStatisticsData":
            if not isinstance(data, dict):
                raise TypeError()
            sub_group_type_0 = SummaryStatisticsData.from_dict(data)

            return sub_group_type_0

        sub_group = _parse_sub_group(d.pop("subGroup"))

        tax_benchmarkings_data = cls(
            section=section,
            sub_section=sub_section,
            group=group,
            sub_group=sub_group,
        )

        tax_benchmarkings_data.additional_properties = d
        return tax_benchmarkings_data

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
