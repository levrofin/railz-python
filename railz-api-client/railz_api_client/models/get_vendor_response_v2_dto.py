from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_vendor_data_v2 import GetVendorDataV2
    from ..models.list_report_meta_data_v2 import ListReportMetaDataV2
    from ..models.pagination_meta_data import PaginationMetaData


T = TypeVar("T", bound="GetVendorResponseV2Dto")


@_attrs_define
class GetVendorResponseV2Dto:
    """
    Attributes:
        pagination (PaginationMetaData):
        meta (ListReportMetaDataV2):
        data (List['GetVendorDataV2']):
    """

    pagination: "PaginationMetaData"
    meta: "ListReportMetaDataV2"
    data: List["GetVendorDataV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination = self.pagination.to_dict()

        meta = self.meta.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "meta": meta,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_vendor_data_v2 import GetVendorDataV2
        from ..models.list_report_meta_data_v2 import ListReportMetaDataV2
        from ..models.pagination_meta_data import PaginationMetaData

        d = src_dict.copy()
        pagination = PaginationMetaData.from_dict(d.pop("pagination"))

        meta = ListReportMetaDataV2.from_dict(d.pop("meta"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetVendorDataV2.from_dict(data_item_data)

            data.append(data_item)

        get_vendor_response_v2_dto = cls(
            pagination=pagination,
            meta=meta,
            data=data,
        )

        get_vendor_response_v2_dto.additional_properties = d
        return get_vendor_response_v2_dto

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
