import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_parent_ref import AccountParentRef
    from ..models.subsidiary_ref import SubsidiaryRef
    from ..models.tax_rate_object_ref_response import TaxRateObjectRefResponse


T = TypeVar("T", bound="GetChartOfAccountsDataV2")


@_attrs_define
class GetChartOfAccountsDataV2:
    """
    Attributes:
        id (str):  Example: 1.
        is_active (bool):  Example: True.
        section (str):  Example: Assets.
        sub_section (str):  Example: Current Assets.
        nominal_code (Union[Unset, str]):  Example: 200.
        name (Union[Unset, str]):  Example: Bank Account.
        description (Union[Unset, str]):  Example: Account description..
        group (Union[Unset, str]):  Example: Cash And Cash Equivalents.
        sub_group (Union[Unset, str]):  Example: Checking.
        classification (Union[Unset, str]):  Example: Asset.
        fully_qualified_name (Union[Unset, str]):  Example: Expenses : Transportation : Car Mileage.
        depth (Union[Unset, float]):  Example: 3.
        current_balance (Union[Unset, float]):
        sub_type (Union[Unset, str]):  Example: cash&Bank.
        is_bank_account (Union[Unset, bool]):  Example: True.
        is_sub_account (Union[Unset, bool]):  Example: True.
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        parent_ref (Union[Unset, AccountParentRef]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
        account_uuid (Union[Unset, str]):  Example: 6f436c63-308f-4ccd-8c56-a445c2948640.
        type (Union[Unset, str]):  Example: Accounts Receivable.
        currency (Union[Unset, str]):  Example: USD.
        is_posting (Union[Unset, bool]):  Example: True.
        tax_rate_ref (Union[Unset, TaxRateObjectRefResponse]):
        bank_account_number (Union[Unset, str]):  Example: 11200.
        payments_enabled (Union[Unset, bool]):  Example: True.
    """

    id: str
    is_active: bool
    section: str
    sub_section: str
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
    account_uuid: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    is_posting: Union[Unset, bool] = UNSET
    tax_rate_ref: Union[Unset, "TaxRateObjectRefResponse"] = UNSET
    bank_account_number: Union[Unset, str] = UNSET
    payments_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        is_active = self.is_active

        section = self.section

        sub_section = self.sub_section

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

        account_uuid = self.account_uuid

        type = self.type

        currency = self.currency

        is_posting = self.is_posting

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        bank_account_number = self.bank_account_number

        payments_enabled = self.payments_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isActive": is_active,
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
        if account_uuid is not UNSET:
            field_dict["accountUuid"] = account_uuid
        if type is not UNSET:
            field_dict["type"] = type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if is_posting is not UNSET:
            field_dict["isPosting"] = is_posting
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if bank_account_number is not UNSET:
            field_dict["bankAccountNumber"] = bank_account_number
        if payments_enabled is not UNSET:
            field_dict["paymentsEnabled"] = payments_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_parent_ref import AccountParentRef
        from ..models.subsidiary_ref import SubsidiaryRef
        from ..models.tax_rate_object_ref_response import TaxRateObjectRefResponse

        d = src_dict.copy()
        id = d.pop("id")

        is_active = d.pop("isActive")

        section = d.pop("section")

        sub_section = d.pop("subSection")

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

        account_uuid = d.pop("accountUuid", UNSET)

        type = d.pop("type", UNSET)

        currency = d.pop("currency", UNSET)

        is_posting = d.pop("isPosting", UNSET)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, TaxRateObjectRefResponse]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = TaxRateObjectRefResponse.from_dict(_tax_rate_ref)

        bank_account_number = d.pop("bankAccountNumber", UNSET)

        payments_enabled = d.pop("paymentsEnabled", UNSET)

        get_chart_of_accounts_data_v2 = cls(
            id=id,
            is_active=is_active,
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
            account_uuid=account_uuid,
            type=type,
            currency=currency,
            is_posting=is_posting,
            tax_rate_ref=tax_rate_ref,
            bank_account_number=bank_account_number,
            payments_enabled=payments_enabled,
        )

        get_chart_of_accounts_data_v2.additional_properties = d
        return get_chart_of_accounts_data_v2

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
