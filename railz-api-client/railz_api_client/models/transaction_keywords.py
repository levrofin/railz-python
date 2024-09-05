from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_keywords_type import TransactionKeywordsType, check_transaction_keywords_type

T = TypeVar("T", bound="TransactionKeywords")


@_attrs_define
class TransactionKeywords:
    """
    Attributes:
        type (TransactionKeywordsType):  Example: bill.
        count (float):  Example: 1.
    """

    type: TransactionKeywordsType
    count: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: str = self.type

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = check_transaction_keywords_type(d.pop("type"))

        count = d.pop("count")

        transaction_keywords = cls(
            type=type,
            count=count,
        )

        transaction_keywords.additional_properties = d
        return transaction_keywords

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
