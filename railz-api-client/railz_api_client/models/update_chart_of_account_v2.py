from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_chart_of_account_v2_classification import (
    UpdateChartOfAccountV2Classification,
    check_update_chart_of_account_v2_classification,
)
from ..models.update_chart_of_account_v2_type import UpdateChartOfAccountV2Type, check_update_chart_of_account_v2_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parent_ref_dto_v2 import ParentRefDtoV2
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto
    from ..models.tax_rate_ref_dto import TaxRateRefDto
    from ..models.update_chart_of_account_v2_pass_through import UpdateChartOfAccountV2PassThrough


T = TypeVar("T", bound="UpdateChartOfAccountV2")


@_attrs_define
class UpdateChartOfAccountV2:
    """
    Attributes:
        nominal_code (Union[Unset, str]):  Example: SALES001.
        name (Union[Unset, str]):  Example: Consulting Income.
        description (Union[Unset, str]):  Example: Sales account..
        classification (Union[Unset, UpdateChartOfAccountV2Classification]):  Example: asset.
        currency (Union[Unset, str]):  Example: CAD.
        type (Union[Unset, UpdateChartOfAccountV2Type]):  Example: currentAsset.
        bank_account_number (Union[Unset, str]):  Example: 11200.
        tax_rate_ref (Union[Unset, TaxRateRefDto]):
        parent_ref (Union[Unset, ParentRefDtoV2]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        pass_through (Union[Unset, UpdateChartOfAccountV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    nominal_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    classification: Union[Unset, UpdateChartOfAccountV2Classification] = UNSET
    currency: Union[Unset, str] = UNSET
    type: Union[Unset, UpdateChartOfAccountV2Type] = UNSET
    bank_account_number: Union[Unset, str] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateRefDto"] = UNSET
    parent_ref: Union[Unset, "ParentRefDtoV2"] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    pass_through: Union[Unset, "UpdateChartOfAccountV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nominal_code = self.nominal_code

        name = self.name

        description = self.description

        classification: Union[Unset, str] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification

        currency = self.currency

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        bank_account_number = self.bank_account_number

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nominal_code is not UNSET:
            field_dict["nominalCode"] = nominal_code
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if classification is not UNSET:
            field_dict["classification"] = classification
        if currency is not UNSET:
            field_dict["currency"] = currency
        if type is not UNSET:
            field_dict["type"] = type
        if bank_account_number is not UNSET:
            field_dict["bankAccountNumber"] = bank_account_number
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parent_ref_dto_v2 import ParentRefDtoV2
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto
        from ..models.tax_rate_ref_dto import TaxRateRefDto
        from ..models.update_chart_of_account_v2_pass_through import UpdateChartOfAccountV2PassThrough

        d = src_dict.copy()
        nominal_code = d.pop("nominalCode", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, UpdateChartOfAccountV2Classification]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = check_update_chart_of_account_v2_classification(_classification)

        currency = d.pop("currency", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, UpdateChartOfAccountV2Type]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_update_chart_of_account_v2_type(_type)

        bank_account_number = d.pop("bankAccountNumber", UNSET)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateRefDto]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateRefDto.from_dict(_tax_rate_ref)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, ParentRefDtoV2]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = ParentRefDtoV2.from_dict(_parent_ref)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, UpdateChartOfAccountV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = UpdateChartOfAccountV2PassThrough.from_dict(_pass_through)

        update_chart_of_account_v2 = cls(
            nominal_code=nominal_code,
            name=name,
            description=description,
            classification=classification,
            currency=currency,
            type=type,
            bank_account_number=bank_account_number,
            tax_rate_ref=tax_rate_ref,
            parent_ref=parent_ref,
            subsidiary_refs=subsidiary_refs,
            pass_through=pass_through,
        )

        update_chart_of_account_v2.additional_properties = d
        return update_chart_of_account_v2

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
