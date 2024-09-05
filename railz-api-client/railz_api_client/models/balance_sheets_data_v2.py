from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.balance_sheets_data_v2_section import BalanceSheetsDataV2Section, check_balance_sheets_data_v2_section
from ..models.balance_sheets_data_v2_sub_section import (
    BalanceSheetsDataV2SubSection,
    check_balance_sheets_data_v2_sub_section,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BalanceSheetsDataV2")


@_attrs_define
class BalanceSheetsDataV2:
    """
    Attributes:
        section (BalanceSheetsDataV2Section):  Example: Assets.
        sub_section (BalanceSheetsDataV2SubSection):  Example: Current Assets.
        depth (float): The sub account depth, based on it's account hierarchy level. E.g. top parent account would have
            a depth of 1. Example: 3.
        value (float):  Example: 990.
        fully_qualified_name (Union[Unset, str]): Full name of the account and parent account(s), colon separated.
            Example: Expenses : Transportation : Car Mileage.
        group (Union[Unset, str]):  Example: Cash And Cash Equivalents.
        sub_group (Union[Unset, str]):  Example: Utilities.
        account_id (Union[Unset, str]):  Example: 3928.
        sub_account_id (Union[Unset, str]):  Example: 231.
        account (Union[Unset, str]):  Example: Checking.
        sub_account (Union[Unset, str]):  Example: Checking.
        classification (Union[Unset, str]):  Example: Assets.
        type (Union[Unset, str]):  Example: Fixed Assets.
        sub_type (Union[Unset, str]):  Example: Fixed Assets.
    """

    section: BalanceSheetsDataV2Section
    sub_section: BalanceSheetsDataV2SubSection
    depth: float
    value: float
    fully_qualified_name: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    sub_group: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    sub_account_id: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    sub_account: Union[Unset, str] = UNSET
    classification: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    sub_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        section: str = self.section

        sub_section: str = self.sub_section

        depth = self.depth

        value = self.value

        fully_qualified_name = self.fully_qualified_name

        group = self.group

        sub_group = self.sub_group

        account_id = self.account_id

        sub_account_id = self.sub_account_id

        account = self.account

        sub_account = self.sub_account

        classification = self.classification

        type = self.type

        sub_type = self.sub_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "section": section,
                "subSection": sub_section,
                "depth": depth,
                "value": value,
            }
        )
        if fully_qualified_name is not UNSET:
            field_dict["fullyQualifiedName"] = fully_qualified_name
        if group is not UNSET:
            field_dict["group"] = group
        if sub_group is not UNSET:
            field_dict["subGroup"] = sub_group
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if sub_account_id is not UNSET:
            field_dict["subAccountId"] = sub_account_id
        if account is not UNSET:
            field_dict["account"] = account
        if sub_account is not UNSET:
            field_dict["subAccount"] = sub_account
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
        section = check_balance_sheets_data_v2_section(d.pop("section"))

        sub_section = check_balance_sheets_data_v2_sub_section(d.pop("subSection"))

        depth = d.pop("depth")

        value = d.pop("value")

        fully_qualified_name = d.pop("fullyQualifiedName", UNSET)

        group = d.pop("group", UNSET)

        sub_group = d.pop("subGroup", UNSET)

        account_id = d.pop("accountId", UNSET)

        sub_account_id = d.pop("subAccountId", UNSET)

        account = d.pop("account", UNSET)

        sub_account = d.pop("subAccount", UNSET)

        classification = d.pop("classification", UNSET)

        type = d.pop("type", UNSET)

        sub_type = d.pop("subType", UNSET)

        balance_sheets_data_v2 = cls(
            section=section,
            sub_section=sub_section,
            depth=depth,
            value=value,
            fully_qualified_name=fully_qualified_name,
            group=group,
            sub_group=sub_group,
            account_id=account_id,
            sub_account_id=sub_account_id,
            account=account,
            sub_account=sub_account,
            classification=classification,
            type=type,
            sub_type=sub_type,
        )

        balance_sheets_data_v2.additional_properties = d
        return balance_sheets_data_v2

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
