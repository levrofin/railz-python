from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_tracking_categories_v2_status import (
    PushTrackingCategoriesV2Status,
    check_push_tracking_categories_v2_status,
)
from ..models.push_tracking_categories_v2_type import (
    PushTrackingCategoriesV2Type,
    check_push_tracking_categories_v2_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parent_ref_dto_v2 import ParentRefDtoV2
    from ..models.push_tracking_categories_v2_pass_through import PushTrackingCategoriesV2PassThrough
    from ..models.subsidiary_ref_v2_dto import SubsidiaryRefV2Dto


T = TypeVar("T", bound="PushTrackingCategoriesV2")


@_attrs_define
class PushTrackingCategoriesV2:
    """
    Attributes:
        name (str):  Example: Region.
        id (Union[Unset, str]):  Example: 1.
        parent_ref (Union[Unset, ParentRefDtoV2]):
        type (Union[Unset, PushTrackingCategoriesV2Type]):  Example: class.
        is_editable (Union[Unset, bool]):  Example: true.
        has_children (Union[Unset, bool]):
        status (Union[Unset, PushTrackingCategoriesV2Status]):  Example: active.
        subsidiary_refs (Union[Unset, List['SubsidiaryRefV2Dto']]):
        pass_through (Union[Unset, PushTrackingCategoriesV2PassThrough]):  Example: {'CustomField': [{'DefinitionId':
            '1', 'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    name: str
    id: Union[Unset, str] = UNSET
    parent_ref: Union[Unset, "ParentRefDtoV2"] = UNSET
    type: Union[Unset, PushTrackingCategoriesV2Type] = UNSET
    is_editable: Union[Unset, bool] = UNSET
    has_children: Union[Unset, bool] = UNSET
    status: Union[Unset, PushTrackingCategoriesV2Status] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefV2Dto"]] = UNSET
    pass_through: Union[Unset, "PushTrackingCategoriesV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        id = self.id

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        is_editable = self.is_editable

        has_children = self.has_children

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if type is not UNSET:
            field_dict["type"] = type
        if is_editable is not UNSET:
            field_dict["isEditable"] = is_editable
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if status is not UNSET:
            field_dict["status"] = status
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parent_ref_dto_v2 import ParentRefDtoV2
        from ..models.push_tracking_categories_v2_pass_through import PushTrackingCategoriesV2PassThrough
        from ..models.subsidiary_ref_v2_dto import SubsidiaryRefV2Dto

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, ParentRefDtoV2]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = ParentRefDtoV2.from_dict(_parent_ref)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PushTrackingCategoriesV2Type]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_push_tracking_categories_v2_type(_type)

        is_editable = d.pop("isEditable", UNSET)

        has_children = d.pop("hasChildren", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PushTrackingCategoriesV2Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_push_tracking_categories_v2_status(_status)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefV2Dto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushTrackingCategoriesV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushTrackingCategoriesV2PassThrough.from_dict(_pass_through)

        push_tracking_categories_v2 = cls(
            name=name,
            id=id,
            parent_ref=parent_ref,
            type=type,
            is_editable=is_editable,
            has_children=has_children,
            status=status,
            subsidiary_refs=subsidiary_refs,
            pass_through=pass_through,
        )

        push_tracking_categories_v2.additional_properties = d
        return push_tracking_categories_v2

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
