from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_chart_of_account_v1_classification import (
    PushChartOfAccountV1Classification,
    check_push_chart_of_account_v1_classification,
)
from ..models.push_chart_of_account_v1_type import PushChartOfAccountV1Type, check_push_chart_of_account_v1_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="PushChartOfAccountV1")


@_attrs_define
class PushChartOfAccountV1:
    """
    Attributes:
        name (str):  Example: Consulting Income.
        type (PushChartOfAccountV1Type):  Example: currentAsset.
        nominal_code (Union[Unset, str]):  Example: SALES001.
        description (Union[Unset, str]):  Example: Sales account..
        currency (Union[Unset, str]):  Example: CAD.
        tax_ref (Union[Unset, str]):  Example: 12.
        classification (Union[Unset, PushChartOfAccountV1Classification]):  Example: asset.
        subsidiary_refs (Union[Unset, List[str]]):  Example: ['1', '2'].
    """

    name: str
    type: PushChartOfAccountV1Type
    nominal_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    tax_ref: Union[Unset, str] = UNSET
    classification: Union[Unset, PushChartOfAccountV1Classification] = UNSET
    subsidiary_refs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type: str = self.type

        nominal_code = self.nominal_code

        description = self.description

        currency = self.currency

        tax_ref = self.tax_ref

        classification: Union[Unset, str] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification

        subsidiary_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = self.subsidiary_refs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if nominal_code is not UNSET:
            field_dict["nominalCode"] = nominal_code
        if description is not UNSET:
            field_dict["description"] = description
        if currency is not UNSET:
            field_dict["currency"] = currency
        if tax_ref is not UNSET:
            field_dict["taxRef"] = tax_ref
        if classification is not UNSET:
            field_dict["classification"] = classification
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = check_push_chart_of_account_v1_type(d.pop("type"))

        nominal_code = d.pop("nominalCode", UNSET)

        description = d.pop("description", UNSET)

        currency = d.pop("currency", UNSET)

        tax_ref = d.pop("taxRef", UNSET)

        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, PushChartOfAccountV1Classification]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = check_push_chart_of_account_v1_classification(_classification)

        subsidiary_refs = cast(List[str], d.pop("subsidiaryRefs", UNSET))

        push_chart_of_account_v1 = cls(
            name=name,
            type=type,
            nominal_code=nominal_code,
            description=description,
            currency=currency,
            tax_ref=tax_ref,
            classification=classification,
            subsidiary_refs=subsidiary_refs,
        )

        push_chart_of_account_v1.additional_properties = d
        return push_chart_of_account_v1

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
