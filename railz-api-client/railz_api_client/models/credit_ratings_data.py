from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_ratings_data_dbrs_rating import CreditRatingsDataDbrsRating
from ..models.credit_ratings_data_fitch_rating import CreditRatingsDataFitchRating
from ..models.credit_ratings_data_moodys_rating import CreditRatingsDataMoodysRating
from ..models.credit_ratings_data_railz_grade import CreditRatingsDataRailzGrade
from ..models.credit_ratings_data_railz_rating import CreditRatingsDataRailzRating
from ..models.credit_ratings_data_sp_rating import CreditRatingsDataSpRating

T = TypeVar("T", bound="CreditRatingsData")


@_attrs_define
class CreditRatingsData:
    """
    Attributes:
        sp_rating (CreditRatingsDataSpRating):  Example: AA+.
        moodys_rating (CreditRatingsDataMoodysRating):  Example: Aaa.
        fitch_rating (CreditRatingsDataFitchRating):  Example: AA+.
        dbrs_rating (CreditRatingsDataDbrsRating):  Example: AAA.
        railz_rating (CreditRatingsDataRailzRating):  Example: A.
        railz_grade (CreditRatingsDataRailzGrade):  Example: Excellent.
        description (str):  Example: Highest quality borrower, minimal credit risk..
    """

    sp_rating: CreditRatingsDataSpRating
    moodys_rating: CreditRatingsDataMoodysRating
    fitch_rating: CreditRatingsDataFitchRating
    dbrs_rating: CreditRatingsDataDbrsRating
    railz_rating: CreditRatingsDataRailzRating
    railz_grade: CreditRatingsDataRailzGrade
    description: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        sp_rating = d.pop("spRating")

        moodys_rating = d.pop("moodysRating")

        fitch_rating = d.pop("fitchRating")

        dbrs_rating = d.pop("dbrsRating")

        railz_rating = d.pop("railzRating")

        railz_grade = d.pop("railzGrade")

        description = d.pop("description")

        credit_ratings_data = cls(
            sp_rating=sp_rating,
            moodys_rating=moodys_rating,
            fitch_rating=fitch_rating,
            dbrs_rating=dbrs_rating,
            railz_rating=railz_rating,
            railz_grade=railz_grade,
            description=description,
        )

        credit_ratings_data.additional_properties = d
        return credit_ratings_data

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
