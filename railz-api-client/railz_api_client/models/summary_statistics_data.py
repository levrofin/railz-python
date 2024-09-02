from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SummaryStatisticsData")


@_attrs_define
class SummaryStatisticsData:
    """
    Attributes:
        min_ (float):  Example: 301.5.
        max_ (float):  Example: 22012.5.
        mean (float):  Example: 6279.7.
        median (float):  Example: 3739.89.
        sdev (float):  Example: 21764.54.
        quantile5 (float):  Example: 301.5.
        quantile25 (float):  Example: 301.5.
        quantile75 (float):  Example: 6710.61.
        quantile95 (float):  Example: 7649.75.
    """

    min_: float
    max_: float
    mean: float
    median: float
    sdev: float
    quantile5: float
    quantile25: float
    quantile75: float
    quantile95: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_

        max_ = self.max_

        mean = self.mean

        median = self.median

        sdev = self.sdev

        quantile5 = self.quantile5

        quantile25 = self.quantile25

        quantile75 = self.quantile75

        quantile95 = self.quantile95

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "min**": min_,
                "max**": max_,
                "mean**": mean,
                "median**": median,
                "sdev**": sdev,
                "quantile5**": quantile5,
                "quantile25**": quantile25,
                "quantile75**": quantile75,
                "quantile95**": quantile95,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("min**")

        max_ = d.pop("max**")

        mean = d.pop("mean**")

        median = d.pop("median**")

        sdev = d.pop("sdev**")

        quantile5 = d.pop("quantile5**")

        quantile25 = d.pop("quantile25**")

        quantile75 = d.pop("quantile75**")

        quantile95 = d.pop("quantile95**")

        summary_statistics_data = cls(
            min_=min_,
            max_=max_,
            mean=mean,
            median=median,
            sdev=sdev,
            quantile5=quantile5,
            quantile25=quantile25,
            quantile75=quantile75,
            quantile95=quantile95,
        )

        summary_statistics_data.additional_properties = d
        return summary_statistics_data

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
