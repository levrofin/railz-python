from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_object_dto import MetadataObjectDto


T = TypeVar("T", bound="UpdateBusinessDtoV2")


@_attrs_define
class UpdateBusinessDtoV2:
    """
    Attributes:
        business_name (Union[Unset, str]):  Example: Railz.
        metadata (Union[Unset, List['MetadataObjectDto']]):
    """

    business_name: Union[Unset, str] = UNSET
    metadata: Union[Unset, List["MetadataObjectDto"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_name = self.business_name

        metadata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = []
            for metadata_item_data in self.metadata:
                metadata_item = metadata_item_data.to_dict()
                metadata.append(metadata_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metadata_object_dto import MetadataObjectDto

        d = src_dict.copy()
        business_name = d.pop("businessName", UNSET)

        metadata = []
        _metadata = d.pop("metadata", UNSET)
        for metadata_item_data in _metadata or []:
            metadata_item = MetadataObjectDto.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        update_business_dto_v2 = cls(
            business_name=business_name,
            metadata=metadata,
        )

        update_business_dto_v2.additional_properties = d
        return update_business_dto_v2

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
