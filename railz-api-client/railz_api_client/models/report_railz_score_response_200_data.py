from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportRailzScoreResponse200Data")


@_attrs_define
class ReportRailzScoreResponse200Data:
    """
    Attributes:
        score (Union[Unset, int]): A standard point in time credit score based on a 1-year probability of default in the
            range of 300-850. Example: 800.
        rating (Union[Unset, str]): Railz credit rating Example: Excellent.
        last_updated (Union[Unset, str]): Last synchronization date Example: 2020-12-31.
    """

    score: Union[Unset, int] = UNSET
    rating: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        score = self.score

        rating = self.rating

        last_updated = self.last_updated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if rating is not UNSET:
            field_dict["rating"] = rating
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        score = d.pop("score", UNSET)

        rating = d.pop("rating", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        report_railz_score_response_200_data = cls(
            score=score,
            rating=rating,
            last_updated=last_updated,
        )

        report_railz_score_response_200_data.additional_properties = d
        return report_railz_score_response_200_data

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
