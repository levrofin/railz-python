from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.credit_ratings_data import CreditRatingsData
    from ..models.credit_ratings_report_meta_data import CreditRatingsReportMetaData


T = TypeVar("T", bound="CreditRatingsReport")


@_attrs_define
class CreditRatingsReport:
    """
    Attributes:
        meta (CreditRatingsReportMetaData):
        data (CreditRatingsData):
    """

    meta: "CreditRatingsReportMetaData"
    data: "CreditRatingsData"
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
        from ..models.credit_ratings_data import CreditRatingsData
        from ..models.credit_ratings_report_meta_data import CreditRatingsReportMetaData

        d = src_dict.copy()
        meta = CreditRatingsReportMetaData.from_dict(d.pop("meta"))

        data = CreditRatingsData.from_dict(d.pop("data"))

        credit_ratings_report = cls(
            meta=meta,
            data=data,
        )

        credit_ratings_report.additional_properties = d
        return credit_ratings_report

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
