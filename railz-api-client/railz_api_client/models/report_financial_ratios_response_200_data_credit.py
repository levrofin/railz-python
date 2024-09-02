from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_financial_ratios_response_200_data_credit_distance_to_default import (
        ReportFinancialRatiosResponse200DataCreditDistanceToDefault,
    )
    from ..models.report_financial_ratios_response_200_data_credit_liquidation_value import (
        ReportFinancialRatiosResponse200DataCreditLiquidationValue,
    )
    from ..models.report_financial_ratios_response_200_data_credit_probability_of_default import (
        ReportFinancialRatiosResponse200DataCreditProbabilityOfDefault,
    )


T = TypeVar("T", bound="ReportFinancialRatiosResponse200DataCredit")


@_attrs_define
class ReportFinancialRatiosResponse200DataCredit:
    """
    Attributes:
        distance_to_default (Union[Unset, ReportFinancialRatiosResponse200DataCreditDistanceToDefault]):
        probability_of_default (Union[Unset, ReportFinancialRatiosResponse200DataCreditProbabilityOfDefault]):
        liquidation_value (Union[Unset, ReportFinancialRatiosResponse200DataCreditLiquidationValue]):
    """

    distance_to_default: Union[Unset, "ReportFinancialRatiosResponse200DataCreditDistanceToDefault"] = UNSET
    probability_of_default: Union[Unset, "ReportFinancialRatiosResponse200DataCreditProbabilityOfDefault"] = UNSET
    liquidation_value: Union[Unset, "ReportFinancialRatiosResponse200DataCreditLiquidationValue"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        distance_to_default: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.distance_to_default, Unset):
            distance_to_default = self.distance_to_default.to_dict()

        probability_of_default: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.probability_of_default, Unset):
            probability_of_default = self.probability_of_default.to_dict()

        liquidation_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.liquidation_value, Unset):
            liquidation_value = self.liquidation_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distance_to_default is not UNSET:
            field_dict["distanceToDefault"] = distance_to_default
        if probability_of_default is not UNSET:
            field_dict["probabilityOfDefault"] = probability_of_default
        if liquidation_value is not UNSET:
            field_dict["liquidationValue"] = liquidation_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_financial_ratios_response_200_data_credit_distance_to_default import (
            ReportFinancialRatiosResponse200DataCreditDistanceToDefault,
        )
        from ..models.report_financial_ratios_response_200_data_credit_liquidation_value import (
            ReportFinancialRatiosResponse200DataCreditLiquidationValue,
        )
        from ..models.report_financial_ratios_response_200_data_credit_probability_of_default import (
            ReportFinancialRatiosResponse200DataCreditProbabilityOfDefault,
        )

        d = src_dict.copy()
        _distance_to_default = d.pop("distanceToDefault", UNSET)
        distance_to_default: Union[Unset, ReportFinancialRatiosResponse200DataCreditDistanceToDefault]
        if isinstance(_distance_to_default, Unset):
            distance_to_default = UNSET
        else:
            distance_to_default = ReportFinancialRatiosResponse200DataCreditDistanceToDefault.from_dict(
                _distance_to_default
            )

        _probability_of_default = d.pop("probabilityOfDefault", UNSET)
        probability_of_default: Union[Unset, ReportFinancialRatiosResponse200DataCreditProbabilityOfDefault]
        if isinstance(_probability_of_default, Unset):
            probability_of_default = UNSET
        else:
            probability_of_default = ReportFinancialRatiosResponse200DataCreditProbabilityOfDefault.from_dict(
                _probability_of_default
            )

        _liquidation_value = d.pop("liquidationValue", UNSET)
        liquidation_value: Union[Unset, ReportFinancialRatiosResponse200DataCreditLiquidationValue]
        if isinstance(_liquidation_value, Unset):
            liquidation_value = UNSET
        else:
            liquidation_value = ReportFinancialRatiosResponse200DataCreditLiquidationValue.from_dict(_liquidation_value)

        report_financial_ratios_response_200_data_credit = cls(
            distance_to_default=distance_to_default,
            probability_of_default=probability_of_default,
            liquidation_value=liquidation_value,
        )

        report_financial_ratios_response_200_data_credit.additional_properties = d
        return report_financial_ratios_response_200_data_credit

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
