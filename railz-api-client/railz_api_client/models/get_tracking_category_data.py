import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_tracking_category_data_status import GetTrackingCategoryDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parent_ref import ParentRef


T = TypeVar("T", bound="GetTrackingCategoryData")


@_attrs_define
class GetTrackingCategoryData:
    """
    Attributes:
        id (str):  Example: 123.
        name (str):  Example: East Coast.
        is_editable (bool):  Example: true.
        status (GetTrackingCategoryDataStatus):  Example: active.
        parent_ref (Union[Unset, ParentRef]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-10T11:26:06.619Z.
    """

    id: str
    name: str
    is_editable: bool
    status: GetTrackingCategoryDataStatus
    parent_ref: Union[Unset, "ParentRef"] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        is_editable = self.is_editable

        status = self.status

        parent_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_ref, Unset):
            parent_ref = self.parent_ref.to_dict()

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "isEditable": is_editable,
                "status": status,
            }
        )
        if parent_ref is not UNSET:
            field_dict["parentRef"] = parent_ref
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parent_ref import ParentRef

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        is_editable = d.pop("isEditable")

        status = d.pop("status")

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

        get_tracking_category_data = cls(
            id=id,
            name=name,
            is_editable=is_editable,
            status=status,
            parent_ref=parent_ref,
            source_modified_date=source_modified_date,
        )

        get_tracking_category_data.additional_properties = d
        return get_tracking_category_data

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
