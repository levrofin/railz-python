from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trial_balances_data_v1_section import TrialBalancesDataV1Section
from ..models.trial_balances_data_v1_sub_section import TrialBalancesDataV1SubSection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_ref import CurrencyRef
    from ..models.subsidiary_ref import SubsidiaryRef


T = TypeVar("T", bound="TrialBalancesDataV1")


@_attrs_define
class TrialBalancesDataV1:
    """
    Attributes:
        section (TrialBalancesDataV1Section):  Example: Expenses.
        sub_section (TrialBalancesDataV1SubSection):  Example: Operating Expenses.
        group (str):  Example: Expenses.
        sub_group (str):  Example: Utilities.
        depth (float): The sub account depth, based on it's account hierarchy level. E.g. top parent account would have
            a depth of 1. Example: 3.
        account (str):  Example: Utilities - Water.
        fully_qualified_name (str): Full name of the account and parent account(s), colon separated. Example: Expenses :
            Transportation : Car Mileage.
        sub_account_id (Union[Unset, str]):  Example: 203rc.
        sub_account (Union[Unset, str]):  Example: Utilities.
        subsidiary_refs (Union[Unset, List['SubsidiaryRef']]):
        credit (Union[Unset, float]):  Example: 80.
        debit (Union[Unset, float]):
        account_id (Union[Unset, str]):  Example: 2s4n2.
        ytd_credit (Union[Unset, float]):  Example: 80.
        ytd_debit (Union[Unset, float]):
        currency_ref (Union[Unset, CurrencyRef]):
    """

    section: TrialBalancesDataV1Section
    sub_section: TrialBalancesDataV1SubSection
    group: str
    sub_group: str
    depth: float
    account: str
    fully_qualified_name: str
    sub_account_id: Union[Unset, str] = UNSET
    sub_account: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRef"]] = UNSET
    credit: Union[Unset, float] = UNSET
    debit: Union[Unset, float] = UNSET
    account_id: Union[Unset, str] = UNSET
    ytd_credit: Union[Unset, float] = UNSET
    ytd_debit: Union[Unset, float] = UNSET
    currency_ref: Union[Unset, "CurrencyRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        section = self.section

        sub_section = self.sub_section

        group = self.group

        sub_group = self.sub_group

        depth = self.depth

        account = self.account

        fully_qualified_name = self.fully_qualified_name

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

        account_id = self.account_id

        ytd_credit = self.ytd_credit

        ytd_debit = self.ytd_debit

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

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
                "fullyQualifiedName": fully_qualified_name,
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
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if ytd_credit is not UNSET:
            field_dict["ytdCredit"] = ytd_credit
        if ytd_debit is not UNSET:
            field_dict["ytdDebit"] = ytd_debit
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency_ref import CurrencyRef
        from ..models.subsidiary_ref import SubsidiaryRef

        d = src_dict.copy()
        section = d.pop("section")

        sub_section = d.pop("subSection")

        group = d.pop("group")

        sub_group = d.pop("subGroup")

        depth = d.pop("depth")

        account = d.pop("account")

        fully_qualified_name = d.pop("fullyQualifiedName")

        sub_account_id = d.pop("subAccountId", UNSET)

        sub_account = d.pop("subAccount", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRef.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        credit = d.pop("credit", UNSET)

        debit = d.pop("debit", UNSET)

        account_id = d.pop("accountId", UNSET)

        ytd_credit = d.pop("ytdCredit", UNSET)

        ytd_debit = d.pop("ytdDebit", UNSET)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CurrencyRef.from_dict(_currency_ref)

        trial_balances_data_v1 = cls(
            section=section,
            sub_section=sub_section,
            group=group,
            sub_group=sub_group,
            depth=depth,
            account=account,
            fully_qualified_name=fully_qualified_name,
            sub_account_id=sub_account_id,
            sub_account=sub_account,
            subsidiary_refs=subsidiary_refs,
            credit=credit,
            debit=debit,
            account_id=account_id,
            ytd_credit=ytd_credit,
            ytd_debit=ytd_debit,
            currency_ref=currency_ref,
        )

        trial_balances_data_v1.additional_properties = d
        return trial_balances_data_v1

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
