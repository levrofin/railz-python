from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_statistics_data import SummaryStatisticsData


T = TypeVar("T", bound="PortfolioMetricsReportData")


@_attrs_define
class PortfolioMetricsReportData:
    """
    Attributes:
        section ('SummaryStatisticsData'):
        sub_section ('SummaryStatisticsData'):
        group ('SummaryStatisticsData'):
        sub_group ('SummaryStatisticsData'):
        ratios (Union['SummaryStatisticsData', Unset]):
        pds (Union['SummaryStatisticsData', Unset]):
        credit_scores (Union['SummaryStatisticsData', Unset]):
    """

    section: "SummaryStatisticsData"
    sub_section: "SummaryStatisticsData"
    group: "SummaryStatisticsData"
    sub_group: "SummaryStatisticsData"
    ratios: Union["SummaryStatisticsData", Unset] = UNSET
    pds: Union["SummaryStatisticsData", Unset] = UNSET
    credit_scores: Union["SummaryStatisticsData", Unset] = UNSET
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

        ratios: Union[Dict[str, Any], Unset]
        if isinstance(self.ratios, Unset):
            ratios = UNSET
        else:
            ratios = self.ratios.to_dict()

        pds: Union[Dict[str, Any], Unset]
        if isinstance(self.pds, Unset):
            pds = UNSET
        else:
            pds = self.pds.to_dict()

        credit_scores: Union[Dict[str, Any], Unset]
        if isinstance(self.credit_scores, Unset):
            credit_scores = UNSET
        else:
            credit_scores = self.credit_scores.to_dict()

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
        if ratios is not UNSET:
            field_dict["ratios"] = ratios
        if pds is not UNSET:
            field_dict["pds"] = pds
        if credit_scores is not UNSET:
            field_dict["creditScores"] = credit_scores

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

        def _parse_ratios(data: object) -> Union["SummaryStatisticsData", Unset]:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            ratios_type_0 = SummaryStatisticsData.from_dict(data)

            return ratios_type_0

        ratios = _parse_ratios(d.pop("ratios", UNSET))

        def _parse_pds(data: object) -> Union["SummaryStatisticsData", Unset]:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            pds_type_0 = SummaryStatisticsData.from_dict(data)

            return pds_type_0

        pds = _parse_pds(d.pop("pds", UNSET))

        def _parse_credit_scores(data: object) -> Union["SummaryStatisticsData", Unset]:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            credit_scores_type_0 = SummaryStatisticsData.from_dict(data)

            return credit_scores_type_0

        credit_scores = _parse_credit_scores(d.pop("creditScores", UNSET))

        portfolio_metrics_report_data = cls(
            section=section,
            sub_section=sub_section,
            group=group,
            sub_group=sub_group,
            ratios=ratios,
            pds=pds,
            credit_scores=credit_scores,
        )

        portfolio_metrics_report_data.additional_properties = d
        return portfolio_metrics_report_data

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
