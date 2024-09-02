from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProbabilityOfDefaultData")


@_attrs_define
class ProbabilityOfDefaultData:
    """
    Attributes:
        markov_pd (Union[Unset, float]):  Example: 0.659176337.
        merton_pd (Union[Unset, float]):  Example: 0.659176337.
        wilcox_pd (Union[Unset, float]):  Example: 0.659176337.
        altman_z_score_pd (Union[Unset, float]):  Example: 0.659176337.
        aggregate_pd (Union[Unset, float]):  Example: 0.659176337.
        logit_pd (Union[Unset, float]):  Example: 0.659176337.
    """

    markov_pd: Union[Unset, float] = UNSET
    merton_pd: Union[Unset, float] = UNSET
    wilcox_pd: Union[Unset, float] = UNSET
    altman_z_score_pd: Union[Unset, float] = UNSET
    aggregate_pd: Union[Unset, float] = UNSET
    logit_pd: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        markov_pd = self.markov_pd

        merton_pd = self.merton_pd

        wilcox_pd = self.wilcox_pd

        altman_z_score_pd = self.altman_z_score_pd

        aggregate_pd = self.aggregate_pd

        logit_pd = self.logit_pd

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if markov_pd is not UNSET:
            field_dict["markovPD"] = markov_pd
        if merton_pd is not UNSET:
            field_dict["mertonPD"] = merton_pd
        if wilcox_pd is not UNSET:
            field_dict["wilcoxPD"] = wilcox_pd
        if altman_z_score_pd is not UNSET:
            field_dict["altmanZScorePD"] = altman_z_score_pd
        if aggregate_pd is not UNSET:
            field_dict["aggregatePD"] = aggregate_pd
        if logit_pd is not UNSET:
            field_dict["logitPD"] = logit_pd

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        markov_pd = d.pop("markovPD", UNSET)

        merton_pd = d.pop("mertonPD", UNSET)

        wilcox_pd = d.pop("wilcoxPD", UNSET)

        altman_z_score_pd = d.pop("altmanZScorePD", UNSET)

        aggregate_pd = d.pop("aggregatePD", UNSET)

        logit_pd = d.pop("logitPD", UNSET)

        probability_of_default_data = cls(
            markov_pd=markov_pd,
            merton_pd=merton_pd,
            wilcox_pd=wilcox_pd,
            altman_z_score_pd=altman_z_score_pd,
            aggregate_pd=aggregate_pd,
            logit_pd=logit_pd,
        )

        probability_of_default_data.additional_properties = d
        return probability_of_default_data

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
