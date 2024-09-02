from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_account_ref_type_entity_ref_type_0 import ServiceAccountRefTypeEntityRefType0


T = TypeVar("T", bound="ServiceAccountRefType")


@_attrs_define
class ServiceAccountRefType:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 12345.
        entity_ref (Union['ServiceAccountRefTypeEntityRefType0', None, Unset]):  Example: {'id': '100'}.
    """

    id: Union[Unset, str] = UNSET
    entity_ref: Union["ServiceAccountRefTypeEntityRefType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.service_account_ref_type_entity_ref_type_0 import ServiceAccountRefTypeEntityRefType0

        id = self.id

        entity_ref: Union[Dict[str, Any], None, Unset]
        if isinstance(self.entity_ref, Unset):
            entity_ref = UNSET
        elif isinstance(self.entity_ref, ServiceAccountRefTypeEntityRefType0):
            entity_ref = self.entity_ref.to_dict()
        else:
            entity_ref = self.entity_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_account_ref_type_entity_ref_type_0 import ServiceAccountRefTypeEntityRefType0

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        def _parse_entity_ref(data: object) -> Union["ServiceAccountRefTypeEntityRefType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_ref_type_0 = ServiceAccountRefTypeEntityRefType0.from_dict(data)

                return entity_ref_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ServiceAccountRefTypeEntityRefType0", None, Unset], data)

        entity_ref = _parse_entity_ref(d.pop("entityRef", UNSET))

        service_account_ref_type = cls(
            id=id,
            entity_ref=entity_ref,
        )

        service_account_ref_type.additional_properties = d
        return service_account_ref_type

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
