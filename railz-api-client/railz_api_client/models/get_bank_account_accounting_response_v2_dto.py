from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bank_account_meta_data_v2 import BankAccountMetaDataV2
    from ..models.get_bank_account_accounting_data_v2 import GetBankAccountAccountingDataV2
    from ..models.pagination_meta_data import PaginationMetaData


T = TypeVar("T", bound="GetBankAccountAccountingResponseV2Dto")


@_attrs_define
class GetBankAccountAccountingResponseV2Dto:
    """
    Attributes:
        meta (BankAccountMetaDataV2):
        pagination (PaginationMetaData):
        data (List['GetBankAccountAccountingDataV2']):
    """

    meta: "BankAccountMetaDataV2"
    pagination: "PaginationMetaData"
    data: List["GetBankAccountAccountingDataV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        pagination = self.pagination.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "pagination": pagination,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_account_meta_data_v2 import BankAccountMetaDataV2
        from ..models.get_bank_account_accounting_data_v2 import GetBankAccountAccountingDataV2
        from ..models.pagination_meta_data import PaginationMetaData

        d = src_dict.copy()
        meta = BankAccountMetaDataV2.from_dict(d.pop("meta"))

        pagination = PaginationMetaData.from_dict(d.pop("pagination"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetBankAccountAccountingDataV2.from_dict(data_item_data)

            data.append(data_item)

        get_bank_account_accounting_response_v2_dto = cls(
            meta=meta,
            pagination=pagination,
            data=data,
        )

        get_bank_account_accounting_response_v2_dto.additional_properties = d
        return get_bank_account_accounting_response_v2_dto

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
