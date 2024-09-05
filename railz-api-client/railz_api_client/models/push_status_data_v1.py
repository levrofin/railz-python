import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.push_status_data_v1_service_name import (
    PushStatusDataV1ServiceName,
    check_push_status_data_v1_service_name,
)
from ..models.push_status_data_v1_status import PushStatusDataV1Status, check_push_status_data_v1_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_id import ObjectId
    from ..models.validation import Validation


T = TypeVar("T", bound="PushStatusDataV1")


@_attrs_define
class PushStatusDataV1:
    """
    Attributes:
        service_name (PushStatusDataV1ServiceName):  Example: quickbooks.
        data_type (str):  Example: balanceSheet.
        requested_on (datetime.datetime):  Example: 2021-03-17T07:58:39.781Z.
        completed_on (datetime.datetime):  Example: 2021-03-17T07:58:39.781Z.
        status (PushStatusDataV1Status):  Example: success.
        response_code (float):  Example: 200.
        push_communication_id (str):  Example: 60473b57f0cdd1683ca71f60.
        validation (Union[Unset, Validation]):
        batch_id (Union[Unset, ObjectId]):
        source_object_id (Union[Unset, str]):  Example: 144.
        source_object_ids (Union[Unset, List[str]]):  Example: ['144', '154'].
    """

    service_name: PushStatusDataV1ServiceName
    data_type: str
    requested_on: datetime.datetime
    completed_on: datetime.datetime
    status: PushStatusDataV1Status
    response_code: float
    push_communication_id: str
    validation: Union[Unset, "Validation"] = UNSET
    batch_id: Union[Unset, "ObjectId"] = UNSET
    source_object_id: Union[Unset, str] = UNSET
    source_object_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_name: str = self.service_name

        data_type = self.data_type

        requested_on = self.requested_on.isoformat()

        completed_on = self.completed_on.isoformat()

        status: str = self.status

        response_code = self.response_code

        push_communication_id = self.push_communication_id

        validation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.to_dict()

        batch_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.batch_id, Unset):
            batch_id = self.batch_id.to_dict()

        source_object_id = self.source_object_id

        source_object_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.source_object_ids, Unset):
            source_object_ids = self.source_object_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceName": service_name,
                "dataType": data_type,
                "requestedOn": requested_on,
                "completedOn": completed_on,
                "status": status,
                "responseCode": response_code,
                "pushCommunicationId": push_communication_id,
            }
        )
        if validation is not UNSET:
            field_dict["validation"] = validation
        if batch_id is not UNSET:
            field_dict["batchId"] = batch_id
        if source_object_id is not UNSET:
            field_dict["sourceObjectId"] = source_object_id
        if source_object_ids is not UNSET:
            field_dict["sourceObjectIds"] = source_object_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.object_id import ObjectId
        from ..models.validation import Validation

        d = src_dict.copy()
        service_name = check_push_status_data_v1_service_name(d.pop("serviceName"))

        data_type = d.pop("dataType")

        requested_on = isoparse(d.pop("requestedOn"))

        completed_on = isoparse(d.pop("completedOn"))

        status = check_push_status_data_v1_status(d.pop("status"))

        response_code = d.pop("responseCode")

        push_communication_id = d.pop("pushCommunicationId")

        _validation = d.pop("validation", UNSET)
        validation: Union[Unset, Validation]
        if isinstance(_validation, Unset):
            validation = UNSET
        else:
            validation = Validation.from_dict(_validation)

        _batch_id = d.pop("batchId", UNSET)
        batch_id: Union[Unset, ObjectId]
        if isinstance(_batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = ObjectId.from_dict(_batch_id)

        source_object_id = d.pop("sourceObjectId", UNSET)

        source_object_ids = cast(List[str], d.pop("sourceObjectIds", UNSET))

        push_status_data_v1 = cls(
            service_name=service_name,
            data_type=data_type,
            requested_on=requested_on,
            completed_on=completed_on,
            status=status,
            response_code=response_code,
            push_communication_id=push_communication_id,
            validation=validation,
            batch_id=batch_id,
            source_object_id=source_object_id,
            source_object_ids=source_object_ids,
        )

        push_status_data_v1.additional_properties = d
        return push_status_data_v1

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
