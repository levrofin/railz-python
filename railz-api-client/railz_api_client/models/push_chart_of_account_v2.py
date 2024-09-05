from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_chart_of_account_v2_classification import (
    PushChartOfAccountV2Classification,
    check_push_chart_of_account_v2_classification,
)
from ..models.push_chart_of_account_v2_sub_type import (
    PushChartOfAccountV2SubType,
    check_push_chart_of_account_v2_sub_type,
)
from ..models.push_chart_of_account_v2_type import PushChartOfAccountV2Type, check_push_chart_of_account_v2_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parent_ref_dto_v2 import ParentRefDtoV2
    from ..models.push_chart_of_account_v2_pass_through import PushChartOfAccountV2PassThrough
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto
    from ..models.tax_rate_ref_dto import TaxRateRefDto


T = TypeVar("T", bound="PushChartOfAccountV2")


@_attrs_define
class PushChartOfAccountV2:
    """
    Attributes:
        name (str):  Example: Consulting Income.
        nominal_code (Union[Unset, str]):  Example: SALES001.
        description (Union[Unset, str]):  Example: Sales account..
        type (Union[Unset, PushChartOfAccountV2Type]):  Example: currentAsset.
        currency (Union[Unset, str]):  Example: CAD.
        tax_rate_ref (Union[Unset, TaxRateRefDto]):
        bank_account_number (Union[Unset, str]):  Example: 11200.
        sub_type (Union[Unset, PushChartOfAccountV2SubType]):  Example: cash&Bank.
        classification (Union[Unset, PushChartOfAccountV2Classification]):  Example: asset.
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        parent_ref (Union[Unset, ParentRefDtoV2]):
        pass_through (Union[Unset, PushChartOfAccountV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    name: str
    nominal_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type: Union[Unset, PushChartOfAccountV2Type] = UNSET
    currency: Union[Unset, str] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRefDto"] = UNSET
    bank_account_number: Union[Unset, str] = UNSET
    sub_type: Union[Unset, PushChartOfAccountV2SubType] = UNSET
    classification: Union[Unset, PushChartOfAccountV2Classification] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    parent_ref: Union[Unset, "ParentRefDtoV2"] = UNSET
    pass_through: Union[Unset, "PushChartOfAccountV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        nominal_code = self.nominal_code

        description = self.description

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        currency = self.currency

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        bank_account_number = self.bank_account_number

        sub_type: Union[Unset, str] = UNSET
        if not isinstance(self.sub_type, Unset):
            sub_type = self.sub_type

        classification: Union[Unset, str] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if nominal_code is not UNSET:
            field_dict["nominalCode"] = nominal_code
        if description is not UNSET:
            field_dict["description"] = description
        if type is not UNSET:
            field_dict["type"] = type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if bank_account_number is not UNSET:
            field_dict["bankAccountNumber"] = bank_account_number
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if classification is not UNSET:
            field_dict["classification"] = classification
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parent_ref_dto_v2 import ParentRefDtoV2
        from ..models.push_chart_of_account_v2_pass_through import PushChartOfAccountV2PassThrough
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto
        from ..models.tax_rate_ref_dto import TaxRateRefDto

        d = src_dict.copy()
        name = d.pop("name")

        nominal_code = d.pop("nominalCode", UNSET)

        description = d.pop("description", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PushChartOfAccountV2Type]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_push_chart_of_account_v2_type(_type)

        currency = d.pop("currency", UNSET)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRefDto]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRefDto.from_dict(_tax_rate_ref)

        bank_account_number = d.pop("bankAccountNumber", UNSET)

        _sub_type = d.pop("subType", UNSET)
        sub_type: Union[Unset, PushChartOfAccountV2SubType]
        if isinstance(_sub_type, Unset):
            sub_type = UNSET
        else:
            sub_type = check_push_chart_of_account_v2_sub_type(_sub_type)

        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, PushChartOfAccountV2Classification]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = check_push_chart_of_account_v2_classification(_classification)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, ParentRefDtoV2]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = ParentRefDtoV2.from_dict(_parent_ref)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushChartOfAccountV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushChartOfAccountV2PassThrough.from_dict(_pass_through)

        push_chart_of_account_v2 = cls(
            name=name,
            nominal_code=nominal_code,
            description=description,
            type=type,
            currency=currency,
            tax_rate_ref=tax_rate_ref,
            bank_account_number=bank_account_number,
            sub_type=sub_type,
            classification=classification,
            subsidiary_refs=subsidiary_refs,
            parent_ref=parent_ref,
            pass_through=pass_through,
        )

        push_chart_of_account_v2.additional_properties = d
        return push_chart_of_account_v2

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
