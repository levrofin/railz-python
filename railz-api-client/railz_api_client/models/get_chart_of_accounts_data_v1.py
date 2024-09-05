import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_chart_of_accounts_data_v1_section import (
    GetChartOfAccountsDataV1Section,
    check_get_chart_of_accounts_data_v1_section,
)
from ..models.get_chart_of_accounts_data_v1_sub_section import (
    GetChartOfAccountsDataV1SubSection,
    check_get_chart_of_accounts_data_v1_sub_section,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_parent_ref import AccountParentRef
    from ..models.currency_ref import CurrencyRef
    from ..models.subsidiary_ref import SubsidiaryRef


T = TypeVar("T", bound="GetChartOfAccountsDataV1")


@_attrs_define
class GetChartOfAccountsDataV1:
    """
    Attributes:
        id (str):  Example: 1.
        is_active (bool):  Example: True.
        type (str):  Example: Accounts Receivable.
        section (GetChartOfAccountsDataV1Section):
        sub_section (GetChartOfAccountsDataV1SubSection):
        nominal_code (Union[Unset, str]):  Example: 200.
        name (Union[Unset, str]):  Example: Bank Account.
        description (Union[Unset, str]):  Example: Account description..
        group (Union[Unset, str]):  Example: Cash And Cash Equivalents.
        sub_group (Union[Unset, str]):  Example: Checking.
        classification (Union[Unset, str]):  Example: Asset.
        fully_qualified_name (Union[Unset, str]):  Example: Expenses : Transportation : Car Mileage.
        depth (Union[Unset, float]):  Example: 3.
        current_balance (Union[Unset, float]):
        sub_type (Union[Unset, str]):  Example: Accounts Receivable.
        is_bank_account (Union[Unset, bool]):  Example: True.
        is_sub_account (Union[Unset, bool]):  Example: True.
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        parent_ref (Union[Unset, AccountParentRef]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        currency_ref (Union[Unset, CurrencyRef]):
    """

    id: str
    is_active: bool
    type: str
    section: GetChartOfAccountsDataV1Section
    sub_section: GetChartOfAccountsDataV1SubSection
    nominal_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    sub_group: Union[Unset, str] = UNSET
    classification: Union[Unset, str] = UNSET
    fully_qualified_name: Union[Unset, str] = UNSET
    depth: Union[Unset, float] = UNSET
    current_balance: Union[Unset, float] = UNSET
    sub_type: Union[Unset, str] = UNSET
    is_bank_account: Union[Unset, bool] = UNSET
    is_sub_account: Union[Unset, bool] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    parent_ref: Union[Unset, "AccountParentRef"] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    currency_ref: Union[Unset, "CurrencyRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        is_active = self.is_active

        type = self.type

        section: str = self.section

        sub_section: str = self.sub_section

        nominal_code = self.nominal_code

        name = self.name

        description = self.description

        group = self.group

        sub_group = self.sub_group

        classification = self.classification

        fully_qualified_name = self.fully_qualified_name

        depth = self.depth

        current_balance = self.current_balance

        sub_type = self.sub_type

        is_bank_account = self.is_bank_account

        is_sub_account = self.is_sub_account

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isActive": is_active,
                "type": type,
                "section": section,
                "subSection": sub_section,
            }
        )
        if nominal_code is not UNSET:
            field_dict["nominalCode"] = nominal_code
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if group is not UNSET:
            field_dict["group"] = group
        if sub_group is not UNSET:
            field_dict["subGroup"] = sub_group
        if classification is not UNSET:
            field_dict["classification"] = classification
        if fully_qualified_name is not UNSET:
            field_dict["fullyQualifiedName"] = fully_qualified_name
        if depth is not UNSET:
            field_dict["depth"] = depth
        if current_balance is not UNSET:
            field_dict["currentBalance"] = current_balance
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if is_bank_account is not UNSET:
            field_dict["isBankAccount"] = is_bank_account
        if is_sub_account is not UNSET:
            field_dict["isSubAccount"] = is_sub_account
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_parent_ref import AccountParentRef
        from ..models.currency_ref import CurrencyRef
        from ..models.subsidiary_ref import SubsidiaryRef

        d = src_dict.copy()
        id = d.pop("id")

        is_active = d.pop("isActive")

        type = d.pop("type")

        section = check_get_chart_of_accounts_data_v1_section(d.pop("section"))

        sub_section = check_get_chart_of_accounts_data_v1_sub_section(d.pop("subSection"))

        nominal_code = d.pop("nominalCode", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        group = d.pop("group", UNSET)

        sub_group = d.pop("subGroup", UNSET)

        classification = d.pop("classification", UNSET)

        fully_qualified_name = d.pop("fullyQualifiedName", UNSET)

        depth = d.pop("depth", UNSET)

        current_balance = d.pop("currentBalance", UNSET)

        sub_type = d.pop("subType", UNSET)

        is_bank_account = d.pop("isBankAccount", UNSET)

        is_sub_account = d.pop("isSubAccount", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRef.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, AccountParentRef]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = AccountParentRef.from_dict(_parent_ref)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CurrencyRef.from_dict(_currency_ref)

        get_chart_of_accounts_data_v1 = cls(
            id=id,
            is_active=is_active,
            type=type,
            section=section,
            sub_section=sub_section,
            nominal_code=nominal_code,
            name=name,
            description=description,
            group=group,
            sub_group=sub_group,
            classification=classification,
            fully_qualified_name=fully_qualified_name,
            depth=depth,
            current_balance=current_balance,
            sub_type=sub_type,
            is_bank_account=is_bank_account,
            is_sub_account=is_sub_account,
            subsidiary_refs=subsidiary_refs,
            parent_ref=parent_ref,
            source_modified_date=source_modified_date,
            currency_ref=currency_ref,
        )

        get_chart_of_accounts_data_v1.additional_properties = d
        return get_chart_of_accounts_data_v1

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
