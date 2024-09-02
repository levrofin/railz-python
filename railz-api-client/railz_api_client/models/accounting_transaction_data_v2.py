import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.accounting_transaction_data_v2_section import AccountingTransactionDataV2Section
from ..models.accounting_transaction_data_v2_sub_section import AccountingTransactionDataV2SubSection
from ..models.accounting_transaction_data_v2_type import AccountingTransactionDataV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accounting_transaction_account_ref_v2 import AccountingTransactionAccountRefV2
    from ..models.accounting_transaction_entity_ref_v2 import AccountingTransactionEntityRefV2
    from ..models.accounting_transaction_tracking_category_ref_v2 import AccountingTransactionTrackingCategoryRefV2


T = TypeVar("T", bound="AccountingTransactionDataV2")


@_attrs_define
class AccountingTransactionDataV2:
    """
    Attributes:
        posted_date (datetime.date):  Example: 2020-11-25.
        type (AccountingTransactionDataV2Type):  Example: invoice.
        section (AccountingTransactionDataV2Section):  Example: Assets.
        sub_section (AccountingTransactionDataV2SubSection):  Example: Current Assets.
        is_reconciled (Union[Unset, bool]):  Example: True.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        is_split_transaction (Union[Unset, bool]):  Example: True.
        parent_transaction_id (Union[Unset, str]):  Example: 1043.
        sub_total (Union[Unset, float]):  Example: 300.5.
        tax_amount (Union[Unset, float]):  Example: 10.5.
        total_amount (Union[Unset, float]):  Example: 311.
        memo (Union[Unset, str]):  Example: Transaction reference.
        source_modified_date (Union[Unset, datetime.date]):  Example: 2021-03-09T10:18:29.985Z.
        id (Union[Unset, str]):  Example: 1045.
        is_posting (Union[Unset, bool]):  Example: True.
        source_id (Union[Unset, str]):  Example: INV-001.
        entity_ref (Union[Unset, AccountingTransactionEntityRefV2]):
        group (Union[Unset, str]):  Example: Cash And Cash Equivalents.
        sub_group (Union[Unset, str]):  Example: Cash And Cash Equivalents.
        tracking_category_refs (Union[Unset, List['AccountingTransactionTrackingCategoryRefV2']]):
        account_ref (Union[Unset, AccountingTransactionAccountRefV2]):
        currency (Union[Unset, str]):  Example: USD.
    """

    posted_date: datetime.date
    type: AccountingTransactionDataV2Type
    section: AccountingTransactionDataV2Section
    sub_section: AccountingTransactionDataV2SubSection
    is_reconciled: Union[Unset, bool] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    is_split_transaction: Union[Unset, bool] = UNSET
    parent_transaction_id: Union[Unset, str] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.date] = UNSET
    id: Union[Unset, str] = UNSET
    is_posting: Union[Unset, bool] = UNSET
    source_id: Union[Unset, str] = UNSET
    entity_ref: Union[Unset, "AccountingTransactionEntityRefV2"] = UNSET
    group: Union[Unset, str] = UNSET
    sub_group: Union[Unset, str] = UNSET
    tracking_category_refs: Union[Unset, List["AccountingTransactionTrackingCategoryRefV2"]] = UNSET
    account_ref: Union[Unset, "AccountingTransactionAccountRefV2"] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date = self.posted_date.isoformat()

        type = self.type

        section = self.section

        sub_section = self.sub_section

        is_reconciled = self.is_reconciled

        currency_rate = self.currency_rate

        is_split_transaction = self.is_split_transaction

        parent_transaction_id = self.parent_transaction_id

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        total_amount = self.total_amount

        memo = self.memo

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        id = self.id

        is_posting = self.is_posting

        source_id = self.source_id

        entity_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

        group = self.group

        sub_group = self.sub_group

        tracking_category_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            tracking_category_refs = []
            for tracking_category_refs_item_data in self.tracking_category_refs:
                tracking_category_refs_item = tracking_category_refs_item_data.to_dict()
                tracking_category_refs.append(tracking_category_refs_item)

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "postedDate": posted_date,
                "type": type,
                "section": section,
                "subSection": sub_section,
            }
        )
        if is_reconciled is not UNSET:
            field_dict["isReconciled"] = is_reconciled
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if is_split_transaction is not UNSET:
            field_dict["isSplitTransaction"] = is_split_transaction
        if parent_transaction_id is not UNSET:
            field_dict["parentTransactionId"] = parent_transaction_id
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if memo is not UNSET:
            field_dict["memo"] = memo
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if id is not UNSET:
            field_dict["id"] = id
        if is_posting is not UNSET:
            field_dict["isPosting"] = is_posting
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref
        if group is not UNSET:
            field_dict["group"] = group
        if sub_group is not UNSET:
            field_dict["subGroup"] = sub_group
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.accounting_transaction_account_ref_v2 import AccountingTransactionAccountRefV2
        from ..models.accounting_transaction_entity_ref_v2 import AccountingTransactionEntityRefV2
        from ..models.accounting_transaction_tracking_category_ref_v2 import AccountingTransactionTrackingCategoryRefV2

        d = src_dict.copy()
        posted_date = isoparse(d.pop("postedDate")).date()

        type = d.pop("type")

        section = d.pop("section")

        sub_section = d.pop("subSection")

        is_reconciled = d.pop("isReconciled", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        is_split_transaction = d.pop("isSplitTransaction", UNSET)

        parent_transaction_id = d.pop("parentTransactionId", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        memo = d.pop("memo", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.date]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date).date()

        id = d.pop("id", UNSET)

        is_posting = d.pop("isPosting", UNSET)

        source_id = d.pop("sourceId", UNSET)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: Union[Unset, AccountingTransactionEntityRefV2]
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = AccountingTransactionEntityRefV2.from_dict(_entity_ref)

        group = d.pop("group", UNSET)

        sub_group = d.pop("subGroup", UNSET)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = AccountingTransactionTrackingCategoryRefV2.from_dict(
                tracking_category_refs_item_data
            )

            tracking_category_refs.append(tracking_category_refs_item)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, AccountingTransactionAccountRefV2]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = AccountingTransactionAccountRefV2.from_dict(_account_ref)

        currency = d.pop("currency", UNSET)

        accounting_transaction_data_v2 = cls(
            posted_date=posted_date,
            type=type,
            section=section,
            sub_section=sub_section,
            is_reconciled=is_reconciled,
            currency_rate=currency_rate,
            is_split_transaction=is_split_transaction,
            parent_transaction_id=parent_transaction_id,
            sub_total=sub_total,
            tax_amount=tax_amount,
            total_amount=total_amount,
            memo=memo,
            source_modified_date=source_modified_date,
            id=id,
            is_posting=is_posting,
            source_id=source_id,
            entity_ref=entity_ref,
            group=group,
            sub_group=sub_group,
            tracking_category_refs=tracking_category_refs,
            account_ref=account_ref,
            currency=currency,
        )

        accounting_transaction_data_v2.additional_properties = d
        return accounting_transaction_data_v2

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
