from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trial_balances_data_v2_section import TrialBalancesDataV2Section
from ..models.trial_balances_data_v2_sub_section import TrialBalancesDataV2SubSection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subsidiary_ref import SubsidiaryRef


T = TypeVar("T", bound="TrialBalancesDataV2")


@_attrs_define
class TrialBalancesDataV2:
    """
    Attributes:
        section (TrialBalancesDataV2Section):  Example: Expenses.
        sub_section (TrialBalancesDataV2SubSection):  Example: Operating Expenses.
        group (str):  Example: Expenses.
        sub_group (str):  Example: Utilities.
        depth (float): The sub account depth, based on it's account hierarchy level. E.g. top parent account would have
            a depth of 1. Example: 3.
        account (str):  Example: Utilities - Water.
        account_id (str):  Example: 2s4n2.
        sub_account_id (Union[Unset, str]):  Example: 203rc.
        sub_account (Union[Unset, str]):  Example: Utilities.
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        credit (Union[Unset, float]):  Example: 80.
        debit (Union[Unset, float]):
        fully_qualified_name (Union[Unset, str]):  Example: Expenses : Transportation : Car Mileage.
        currency (Union[Unset, str]):  Example: USD.
        classification (Union[Unset, str]):  Example: Asset.
        type (Union[Unset, str]):  Example: Fixed Asset.
        sub_type (Union[Unset, str]):  Example: Fixed Asset.
        ytd_credit (Union[Unset, float]):  Example: 80.
        ytd_debit (Union[Unset, float]):  Example: 80.
    """

    section: TrialBalancesDataV2Section
    sub_section: TrialBalancesDataV2SubSection
    group: str
    sub_group: str
    depth: float
    account: str
    account_id: str
    sub_account_id: Union[Unset, str] = UNSET
    sub_account: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    credit: Union[Unset, float] = UNSET
    debit: Union[Unset, float] = UNSET
    fully_qualified_name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    classification: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    sub_type: Union[Unset, str] = UNSET
    ytd_credit: Union[Unset, float] = UNSET
    ytd_debit: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        section = self.section

        sub_section = self.sub_section

        group = self.group

        sub_group = self.sub_group

        depth = self.depth

        account = self.account

        account_id = self.account_id

        sub_account_id = self.sub_account_id

        sub_account = self.sub_account

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        credit = self.credit

        debit = self.debit

        fully_qualified_name = self.fully_qualified_name

        currency = self.currency

        classification = self.classification

        type = self.type

        sub_type = self.sub_type

        ytd_credit = self.ytd_credit

        ytd_debit = self.ytd_debit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "section": section,
                "subSection": sub_section,
                "group": group,
                "subGroup": sub_group,
                "depth": depth,
                "account": account,
                "accountId": account_id,
            }
        )
        if sub_account_id is not UNSET:
            field_dict["subAccountId"] = sub_account_id
        if sub_account is not UNSET:
            field_dict["subAccount"] = sub_account
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if credit is not UNSET:
            field_dict["credit"] = credit
        if debit is not UNSET:
            field_dict["debit"] = debit
        if fully_qualified_name is not UNSET:
            field_dict["fullyQualifiedName"] = fully_qualified_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if classification is not UNSET:
            field_dict["classification"] = classification
        if type is not UNSET:
            field_dict["type"] = type
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if ytd_credit is not UNSET:
            field_dict["ytdCredit"] = ytd_credit
        if ytd_debit is not UNSET:
            field_dict["ytdDebit"] = ytd_debit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subsidiary_ref import SubsidiaryRef

        d = src_dict.copy()
        section = d.pop("section")

        sub_section = d.pop("subSection")

        group = d.pop("group")

        sub_group = d.pop("subGroup")

        depth = d.pop("depth")

        account = d.pop("account")

        account_id = d.pop("accountId")

        sub_account_id = d.pop("subAccountId", UNSET)

        sub_account = d.pop("subAccount", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRef.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        credit = d.pop("credit", UNSET)

        debit = d.pop("debit", UNSET)

        fully_qualified_name = d.pop("fullyQualifiedName", UNSET)

        currency = d.pop("currency", UNSET)

        classification = d.pop("classification", UNSET)

        type = d.pop("type", UNSET)

        sub_type = d.pop("subType", UNSET)

        ytd_credit = d.pop("ytdCredit", UNSET)

        ytd_debit = d.pop("ytdDebit", UNSET)

        trial_balances_data_v2 = cls(
            section=section,
            sub_section=sub_section,
            group=group,
            sub_group=sub_group,
            depth=depth,
            account=account,
            account_id=account_id,
            sub_account_id=sub_account_id,
            sub_account=sub_account,
            subsidiary_refs=subsidiary_refs,
            credit=credit,
            debit=debit,
            fully_qualified_name=fully_qualified_name,
            currency=currency,
            classification=classification,
            type=type,
            sub_type=sub_type,
            ytd_credit=ytd_credit,
            ytd_debit=ytd_debit,
        )

        trial_balances_data_v2.additional_properties = d
        return trial_balances_data_v2

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
