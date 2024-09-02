from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.balance_sheets_data_section import BalanceSheetsDataSection
from ..models.balance_sheets_data_sub_section import BalanceSheetsDataSubSection
from ..types import UNSET, Unset

T = TypeVar("T", bound="BalanceSheetsData")


@_attrs_define
class BalanceSheetsData:
    """
    Attributes:
        section (BalanceSheetsDataSection):  Example: Assets.
        sub_section (BalanceSheetsDataSubSection):  Example: Current Assets.
        fully_qualified_name (str): Full name of the account and parent account(s), colon separated. Example: Expenses :
            Transportation : Car Mileage.
        depth (float): The sub account depth, based on it's account hierarchy level. E.g. top parent account would have
            a depth of 1. Example: 3.
        account (str):  Example: Checking.
        value (float):  Example: 990.
        group (Union[Unset, str]):  Example: Cash And Cash Equivalents.
        sub_group (Union[Unset, str]):  Example: Utilities.
        account_id (Union[Unset, str]):  Example: 3928.
        sub_account_id (Union[Unset, str]):  Example: 231.
        sub_account (Union[Unset, str]):  Example: Checking.
    """

    section: BalanceSheetsDataSection
    sub_section: BalanceSheetsDataSubSection
    fully_qualified_name: str
    depth: float
    account: str
    value: float
    group: Union[Unset, str] = UNSET
    sub_group: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    sub_account_id: Union[Unset, str] = UNSET
    sub_account: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        section = self.section

        sub_section = self.sub_section

        fully_qualified_name = self.fully_qualified_name

        depth = self.depth

        account = self.account

        value = self.value

        group = self.group

        sub_group = self.sub_group

        account_id = self.account_id

        sub_account_id = self.sub_account_id

        sub_account = self.sub_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "section": section,
                "subSection": sub_section,
                "fullyQualifiedName": fully_qualified_name,
                "depth": depth,
                "account": account,
                "value": value,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        section = d.pop("section")

        sub_section = d.pop("subSection")

        fully_qualified_name = d.pop("fullyQualifiedName")

        depth = d.pop("depth")

        account = d.pop("account")

        value = d.pop("value")

        group = d.pop("group", UNSET)

        sub_group = d.pop("subGroup", UNSET)

        account_id = d.pop("accountId", UNSET)

        sub_account_id = d.pop("subAccountId", UNSET)

        sub_account = d.pop("subAccount", UNSET)

        balance_sheets_data = cls(
            section=section,
            sub_section=sub_section,
            fully_qualified_name=fully_qualified_name,
            depth=depth,
            account=account,
            value=value,
            group=group,
            sub_group=sub_group,
            account_id=account_id,
            sub_account_id=sub_account_id,
            sub_account=sub_account,
        )

        balance_sheets_data.additional_properties = d
        return balance_sheets_data

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
