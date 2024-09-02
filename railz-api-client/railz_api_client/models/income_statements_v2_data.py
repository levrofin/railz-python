from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.income_statements_v2_data_section import IncomeStatementsV2DataSection
from ..models.income_statements_v2_data_sub_section import IncomeStatementsV2DataSubSection
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncomeStatementsV2Data")


@_attrs_define
class IncomeStatementsV2Data:
    """
    Attributes:
        section (IncomeStatementsV2DataSection):  Example: Expenses.
        sub_section (IncomeStatementsV2DataSubSection):  Example: Operating Expenses.
        account (str):  Example: Travel.
        value (float):  Example: 490.
        depth (float): The sub account depth, based on it's account hierarchy level. E.g. top parent account would have
            a depth of 1. Example: 3.
        group (Union[Unset, str]):  Example: Office General Administrative Expenses.
        sub_group (Union[Unset, str]):  Example: Office Supplies & Software.
        account_id (Union[Unset, str]):  Example: 3928.
        sub_account_id (Union[Unset, str]):  Example: 231.
        sub_account (Union[Unset, str]):  Example: National.
        fully_qualified_name (Union[Unset, str]): Full name of the account and parent account(s), colon separated.
            Example: Expenses : Transportation : Car Mileage.
        classification (Union[Unset, str]):  Example: Assets.
        type (Union[Unset, str]):  Example: Fixed Assets.
        sub_type (Union[Unset, str]):  Example: Fixed Assets.
    """

    section: IncomeStatementsV2DataSection
    sub_section: IncomeStatementsV2DataSubSection
    account: str
    value: float
    depth: float
    group: Union[Unset, str] = UNSET
    sub_group: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    sub_account_id: Union[Unset, str] = UNSET
    sub_account: Union[Unset, str] = UNSET
    fully_qualified_name: Union[Unset, str] = UNSET
    classification: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    sub_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        section = self.section

        sub_section = self.sub_section

        account = self.account

        value = self.value

        depth = self.depth

        group = self.group

        sub_group = self.sub_group

        account_id = self.account_id

        sub_account_id = self.sub_account_id

        sub_account = self.sub_account

        fully_qualified_name = self.fully_qualified_name

        classification = self.classification

        type = self.type

        sub_type = self.sub_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "section": section,
                "subSection": sub_section,
                "account": account,
                "value": value,
                "depth": depth,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if sub_group is not UNSET:
            field_dict["subGroup"] = sub_group
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if sub_account_id is not UNSET:
            field_dict["subAccountId"] = sub_account_id
        if sub_account is not UNSET:
            field_dict["subAccount"] = sub_account
        if fully_qualified_name is not UNSET:
            field_dict["fullyQualifiedName"] = fully_qualified_name
        if classification is not UNSET:
            field_dict["classification"] = classification
        if type is not UNSET:
            field_dict["type"] = type
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        section = d.pop("section")

        sub_section = d.pop("subSection")

        account = d.pop("account")

        value = d.pop("value")

        depth = d.pop("depth")

        group = d.pop("group", UNSET)

        sub_group = d.pop("subGroup", UNSET)

        account_id = d.pop("accountId", UNSET)

        sub_account_id = d.pop("subAccountId", UNSET)

        sub_account = d.pop("subAccount", UNSET)

        fully_qualified_name = d.pop("fullyQualifiedName", UNSET)

        classification = d.pop("classification", UNSET)

        type = d.pop("type", UNSET)

        sub_type = d.pop("subType", UNSET)

        income_statements_v2_data = cls(
            section=section,
            sub_section=sub_section,
            account=account,
            value=value,
            depth=depth,
            group=group,
            sub_group=sub_group,
            account_id=account_id,
            sub_account_id=sub_account_id,
            sub_account=sub_account,
            fully_qualified_name=fully_qualified_name,
            classification=classification,
            type=type,
            sub_type=sub_type,
        )

        income_statements_v2_data.additional_properties = d
        return income_statements_v2_data

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
