from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.basic_start_end_date_report_meta_data_v2 import BasicStartEndDateReportMetaDataV2
    from ..models.get_dispute_data import GetDisputeData
    from ..models.pagination_meta_data import PaginationMetaData


T = TypeVar("T", bound="GetDisputeResponseV2Dto")


@_attrs_define
class GetDisputeResponseV2Dto:
    """
    Attributes:
        count (float):  Example: 1.
        pagination (PaginationMetaData):
        data (List['GetDisputeData']):
        meta (BasicStartEndDateReportMetaDataV2):
    """

    count: float
    pagination: "PaginationMetaData"
    data: List["GetDisputeData"]
    meta: "BasicStartEndDateReportMetaDataV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        pagination = self.pagination.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "pagination": pagination,
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.basic_start_end_date_report_meta_data_v2 import BasicStartEndDateReportMetaDataV2
        from ..models.get_dispute_data import GetDisputeData
        from ..models.pagination_meta_data import PaginationMetaData

        d = src_dict.copy()
        count = d.pop("count")

        pagination = PaginationMetaData.from_dict(d.pop("pagination"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetDisputeData.from_dict(data_item_data)

            data.append(data_item)

        meta = BasicStartEndDateReportMetaDataV2.from_dict(d.pop("meta"))

        get_dispute_response_v2_dto = cls(
            count=count,
            pagination=pagination,
            data=data,
            meta=meta,
        )

        get_dispute_response_v2_dto.additional_properties = d
        return get_dispute_response_v2_dto

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
