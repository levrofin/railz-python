from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reconcilation_account_ref_section import (
    ReconcilationAccountRefSection,
    check_reconcilation_account_ref_section,
)
from ..models.reconcilation_account_ref_sub_section import (
    ReconcilationAccountRefSubSection,
    check_reconcilation_account_ref_sub_section,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconcilationAccountRef")


@_attrs_define
class ReconcilationAccountRef:
    """
    Attributes:
        id (str):  Example: 1334.
        name (str):  Example: Account Receivable.
        section (Union[Unset, ReconcilationAccountRefSection]):  Example: Assets.
        sub_section (Union[Unset, ReconcilationAccountRefSubSection]):  Example: Current Assets.
        group (Union[Unset, str]):  Example: Cash And Cash Equivalents.
        sub_group (Union[Unset, str]):  Example: Cash And Cash Equivalents.
    """

    id: str
    name: str
    section: Union[Unset, ReconcilationAccountRefSection] = UNSET
    sub_section: Union[Unset, ReconcilationAccountRefSubSection] = UNSET
    group: Union[Unset, str] = UNSET
    sub_group: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        section: Union[Unset, str] = UNSET
        if not isinstance(self.section, Unset):
            section = self.section

        sub_section: Union[Unset, str] = UNSET
        if not isinstance(self.sub_section, Unset):
            sub_section = self.sub_section

        group = self.group

        sub_group = self.sub_group

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if section is not UNSET:
            field_dict["section"] = section
        if sub_section is not UNSET:
            field_dict["subSection"] = sub_section
        if group is not UNSET:
            field_dict["group"] = group
        if sub_group is not UNSET:
            field_dict["subGroup"] = sub_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        _section = d.pop("section", UNSET)
        section: Union[Unset, ReconcilationAccountRefSection]
        if isinstance(_section, Unset):
            section = UNSET
        else:
            section = check_reconcilation_account_ref_section(_section)

        _sub_section = d.pop("subSection", UNSET)
        sub_section: Union[Unset, ReconcilationAccountRefSubSection]
        if isinstance(_sub_section, Unset):
            sub_section = UNSET
        else:
            sub_section = check_reconcilation_account_ref_sub_section(_sub_section)

        group = d.pop("group", UNSET)

        sub_group = d.pop("subGroup", UNSET)

        reconcilation_account_ref = cls(
            id=id,
            name=name,
            section=section,
            sub_section=sub_section,
            group=group,
            sub_group=sub_group,
        )

        reconcilation_account_ref.additional_properties = d
        return reconcilation_account_ref

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
