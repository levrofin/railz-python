import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_tracking_category_data_v2_status import GetTrackingCategoryDataV2Status
from ..models.get_tracking_category_data_v2_type import GetTrackingCategoryDataV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parent_ref import ParentRef
    from ..models.subsidiary_ref_response import SubsidiaryRefResponse


T = TypeVar("T", bound="GetTrackingCategoryDataV2")


@_attrs_define
class GetTrackingCategoryDataV2:
    """
    Attributes:
        id (str):  Example: 123.
        name (str):  Example: East Coast.
        status (GetTrackingCategoryDataV2Status):  Example: active.
        type (GetTrackingCategoryDataV2Type):  Example: class.
        is_editable (Union[Unset, bool]):  Example: true.
        parent_ref (Union[Unset, ParentRef]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-10T11:26:06.619Z.
        has_children (Union[Unset, bool]):
        subsidiary_refs (Union[Unset, List['SubsidiaryRefResponse']]):
    """

    id: str
    name: str
    status: GetTrackingCategoryDataV2Status
    type: GetTrackingCategoryDataV2Type
    is_editable: Union[Unset, bool] = UNSET
    parent_ref: Union[Unset, "ParentRef"] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    has_children: Union[Unset, bool] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefResponse"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        type = self.type

        is_editable = self.is_editable

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        has_children = self.has_children

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "type": type,
            }
        )
        if is_editable is not UNSET:
            field_dict["isEditable"] = is_editable
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parent_ref import ParentRef
        from ..models.subsidiary_ref_response import SubsidiaryRefResponse

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = d.pop("status")

        type = d.pop("type")

        is_editable = d.pop("isEditable", UNSET)

        _parent_ref = d.pop("parentRef", UNSET)
        parent_ref: Union[Unset, ParentRef]
        if isinstance(_parent_ref, Unset):
            parent_ref = UNSET
        else:
            parent_ref = ParentRef.from_dict(_parent_ref)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        has_children = d.pop("hasChildren", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefResponse.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        get_tracking_category_data_v2 = cls(
            id=id,
            name=name,
            status=status,
            type=type,
            is_editable=is_editable,
            parent_ref=parent_ref,
            source_modified_date=source_modified_date,
            has_children=has_children,
            subsidiary_refs=subsidiary_refs,
        )

        get_tracking_category_data_v2.additional_properties = d
        return get_tracking_category_data_v2

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
