from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MetaPageData")


@_attrs_define
class MetaPageData:
    """
    Attributes:
        count (float):  Example: 1.
        offset (float):  Example: 1.
        limit (float):  Example: 1.
        current_page (float):  Example: 1.
        total_pages (float):  Example: 1.
    """

    count: float
    offset: float
    limit: float
    current_page: float
    total_pages: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        offset = self.offset

        limit = self.limit

        current_page = self.current_page

        total_pages = self.total_pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "offset": offset,
                "limit": limit,
                "currentPage": current_page,
                "totalPages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count")

        offset = d.pop("offset")

        limit = d.pop("limit")

        current_page = d.pop("currentPage")

        total_pages = d.pop("totalPages")

        meta_page_data = cls(
            count=count,
            offset=offset,
            limit=limit,
            current_page=current_page,
            total_pages=total_pages,
        )

        meta_page_data.additional_properties = d
        return meta_page_data

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
