import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_deposit_v2_data_status import GetDepositV2DataStatus, check_get_deposit_v2_data_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_account_ref_v2_dto import BankAccountRefV2Dto
    from ..models.deposit_line_v2_items import DepositLineV2Items


T = TypeVar("T", bound="GetDepositV2Data")


@_attrs_define
class GetDepositV2Data:
    """
    Attributes:
        id (str):  Example: 1.
        posted_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        lines (List['DepositLineV2Items']):
        total_amount (float):  Example: 322.
        status (GetDepositV2DataStatus):
        currency (Union[Unset, str]):  Example: USD.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        bank_account_ref (Union[Unset, BankAccountRefV2Dto]):
        sub_total (Union[Unset, float]):  Example: 301.5.
        tax_amount (Union[Unset, float]):  Example: 20.5.
        memo (Union[Unset, str]):  Example: Example bill memo..
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-09T10:18:29.985Z.
    """

    id: str
    posted_date: datetime.datetime
    lines: List["DepositLineV2Items"]
    total_amount: float
    status: GetDepositV2DataStatus
    currency: Union[Unset, str] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    bank_account_ref: Union[Unset, "BankAccountRefV2Dto"] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        posted_date = self.posted_date.isoformat()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        total_amount = self.total_amount

        status: str = self.status

        currency = self.currency

        currency_rate = self.currency_rate

        bank_account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bank_account_ref, Unset):
            bank_account_ref = self.bank_account_ref.to_dict()

        sub_total = self.sub_total

        tax_amount = self.tax_amount

        memo = self.memo

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "postedDate": posted_date,
                "lines": lines,
                "totalAmount": total_amount,
                "status": status,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if bank_account_ref is not UNSET:
            field_dict["bankAccountRef"] = bank_account_ref
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if memo is not UNSET:
            field_dict["memo"] = memo
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_account_ref_v2_dto import BankAccountRefV2Dto
        from ..models.deposit_line_v2_items import DepositLineV2Items

        d = src_dict.copy()
        id = d.pop("id")

        posted_date = isoparse(d.pop("postedDate"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = DepositLineV2Items.from_dict(lines_item_data)

            lines.append(lines_item)

        total_amount = d.pop("totalAmount")

        status = check_get_deposit_v2_data_status(d.pop("status"))

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        _bank_account_ref = d.pop("bankAccountRef", UNSET)
        bank_account_ref: Union[Unset, BankAccountRefV2Dto]
        if isinstance(_bank_account_ref, Unset):
            bank_account_ref = UNSET
        else:
            bank_account_ref = BankAccountRefV2Dto.from_dict(_bank_account_ref)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        memo = d.pop("memo", UNSET)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_deposit_v2_data = cls(
            id=id,
            posted_date=posted_date,
            lines=lines,
            total_amount=total_amount,
            status=status,
            currency=currency,
            currency_rate=currency_rate,
            bank_account_ref=bank_account_ref,
            sub_total=sub_total,
            tax_amount=tax_amount,
            memo=memo,
            source_modified_date=source_modified_date,
        )

        get_deposit_v2_data.additional_properties = d
        return get_deposit_v2_data

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
