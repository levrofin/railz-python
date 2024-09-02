from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.basic_start_end_date_report_meta_data import BasicStartEndDateReportMetaData
    from ..models.get_estimate_data import GetEstimateData
    from ..models.pagination_meta_data import PaginationMetaData


T = TypeVar("T", bound="GetEstimateResponseDto")


@_attrs_define
class GetEstimateResponseDto:
    """
    Attributes:
        count (float):  Example: 1.
        meta (BasicStartEndDateReportMetaData):
        pagination (PaginationMetaData):
        data (List['GetEstimateData']):
    """

    count: float
    meta: "BasicStartEndDateReportMetaData"
    pagination: "PaginationMetaData"
    data: List["GetEstimateData"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

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
                "count": count,
                "meta": meta,
                "pagination": pagination,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.basic_start_end_date_report_meta_data import BasicStartEndDateReportMetaData
        from ..models.get_estimate_data import GetEstimateData
        from ..models.pagination_meta_data import PaginationMetaData

        d = src_dict.copy()
        count = d.pop("count")

        meta = BasicStartEndDateReportMetaData.from_dict(d.pop("meta"))

        pagination = PaginationMetaData.from_dict(d.pop("pagination"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetEstimateData.from_dict(data_item_data)

            data.append(data_item)

        get_estimate_response_dto = cls(
            count=count,
            meta=meta,
            pagination=pagination,
            data=data,
        )

        get_estimate_response_dto.additional_properties = d
        return get_estimate_response_dto

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
