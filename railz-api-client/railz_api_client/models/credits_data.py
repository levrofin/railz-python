from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credits_data_dbrs_rating import CreditsDataDbrsRating
from ..models.credits_data_fitch_rating import CreditsDataFitchRating
from ..models.credits_data_moodys_rating import CreditsDataMoodysRating
from ..models.credits_data_railz_grade import CreditsDataRailzGrade
from ..models.credits_data_railz_rating import CreditsDataRailzRating
from ..models.credits_data_sp_rating import CreditsDataSpRating

T = TypeVar("T", bound="CreditsData")


@_attrs_define
class CreditsData:
    """
    Attributes:
        score_pit (float):  Example: 800.
        score12m (float):  Example: 800.
        score24m (float):  Example: 800.
        score36m (float):  Example: 800.
        sp_rating (CreditsDataSpRating):  Example: AA+.
        moodys_rating (CreditsDataMoodysRating):  Example: Aaa.
        fitch_rating (CreditsDataFitchRating):  Example: AA+.
        dbrs_rating (CreditsDataDbrsRating):  Example: AAA.
        railz_rating (CreditsDataRailzRating):  Example: A.
        railz_grade (CreditsDataRailzGrade):  Example: Excellent.
        description (str):  Example: Highest quality borrower, minimal credit risk..
    """

    score_pit: float
    score12m: float
    score24m: float
    score36m: float
    sp_rating: CreditsDataSpRating
    moodys_rating: CreditsDataMoodysRating
    fitch_rating: CreditsDataFitchRating
    dbrs_rating: CreditsDataDbrsRating
    railz_rating: CreditsDataRailzRating
    railz_grade: CreditsDataRailzGrade
    description: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        score_pit = self.score_pit

        score12m = self.score12m

        score24m = self.score24m

        score36m = self.score36m

        sp_rating = self.sp_rating

        moodys_rating = self.moodys_rating

        fitch_rating = self.fitch_rating

        dbrs_rating = self.dbrs_rating

        railz_rating = self.railz_rating

        railz_grade = self.railz_grade

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scorePit": score_pit,
                "score12m": score12m,
                "score24m": score24m,
                "score36m": score36m,
                "spRating": sp_rating,
                "moodysRating": moodys_rating,
                "fitchRating": fitch_rating,
                "dbrsRating": dbrs_rating,
                "railzRating": railz_rating,
                "railzGrade": railz_grade,
                "description": description,
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

        sp_rating = d.pop("spRating")

        moodys_rating = d.pop("moodysRating")

        fitch_rating = d.pop("fitchRating")

        dbrs_rating = d.pop("dbrsRating")

        railz_rating = d.pop("railzRating")

        railz_grade = d.pop("railzGrade")

        description = d.pop("description")

        credits_data = cls(
            score_pit=score_pit,
            score12m=score12m,
            score24m=score24m,
            score36m=score36m,
            sp_rating=sp_rating,
            moodys_rating=moodys_rating,
            fitch_rating=fitch_rating,
            dbrs_rating=dbrs_rating,
            railz_rating=railz_rating,
            railz_grade=railz_grade,
            description=description,
        )

        credits_data.additional_properties = d
        return credits_data

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
