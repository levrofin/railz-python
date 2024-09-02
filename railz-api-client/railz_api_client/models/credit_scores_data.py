from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreditScoresData")


@_attrs_define
class CreditScoresData:
    """
    Attributes:
        score_pit (float):  Example: 800.
        score12m (float):  Example: 800.
        score24m (float):  Example: 800.
        score36m (float):  Example: 800.
    """

    score_pit: float
    score12m: float
    score24m: float
    score36m: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        score_pit = self.score_pit

        score12m = self.score12m

        score24m = self.score24m

        score36m = self.score36m

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scorePit": score_pit,
                "score12m": score12m,
                "score24m": score24m,
                "score36m": score36m,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        score_pit = d.pop("scorePit")

        score12m = d.pop("score12m")

        score24m = d.pop("score24m")

        score36m = d.pop("score36m")

        credit_scores_data = cls(
            score_pit=score_pit,
            score12m=score12m,
            score24m=score24m,
            score36m=score36m,
        )

        credit_scores_data.additional_properties = d
        return credit_scores_data

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
