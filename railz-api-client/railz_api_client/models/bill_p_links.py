from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bill_p_links_type import BillPLinksType, check_bill_p_links_type

T = TypeVar("T", bound="BillPLinks")


@_attrs_define
class BillPLinks:
    """
    Attributes:
        type (BillPLinksType):
        id (str):  Example: 123.
    """

    type: BillPLinksType
    id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: str = self.type

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = check_bill_p_links_type(d.pop("type"))

        id = d.pop("id")

        bill_p_links = cls(
            type=type,
            id=id,
        )

        bill_p_links.additional_properties = d
        return bill_p_links

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
