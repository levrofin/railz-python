from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bank_account_meta_data import BankAccountMetaData
    from ..models.get_bank_account_data import GetBankAccountData
    from ..models.pagination_meta_data import PaginationMetaData


T = TypeVar("T", bound="GetBankAccountResponseDto")


@_attrs_define
class GetBankAccountResponseDto:
    """
    Attributes:
        pagination (PaginationMetaData):
        data (List['GetBankAccountData']):
        meta (BankAccountMetaData):
        count (int):  Example: 1.
    """

    pagination: "PaginationMetaData"
    data: List["GetBankAccountData"]
    meta: "BankAccountMetaData"
    count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination = self.pagination.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "data": data,
                "meta": meta,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_account_meta_data import BankAccountMetaData
        from ..models.get_bank_account_data import GetBankAccountData
        from ..models.pagination_meta_data import PaginationMetaData

        d = src_dict.copy()
        pagination = PaginationMetaData.from_dict(d.pop("pagination"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetBankAccountData.from_dict(data_item_data)

            data.append(data_item)

        meta = BankAccountMetaData.from_dict(d.pop("meta"))

        count = d.pop("count")

        get_bank_account_response_dto = cls(
            pagination=pagination,
            data=data,
            meta=meta,
            count=count,
        )

        get_bank_account_response_dto.additional_properties = d
        return get_bank_account_response_dto

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
