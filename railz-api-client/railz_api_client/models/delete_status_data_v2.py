import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.delete_status_data_v2_service_name import (
    DeleteStatusDataV2ServiceName,
    check_delete_status_data_v2_service_name,
)
from ..models.delete_status_data_v2_status import DeleteStatusDataV2Status, check_delete_status_data_v2_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation import Validation


T = TypeVar("T", bound="DeleteStatusDataV2")


@_attrs_define
class DeleteStatusDataV2:
    """
    Attributes:
        service_name (DeleteStatusDataV2ServiceName):  Example: quickbooks.
        data_type (str):  Example: balanceSheet.
        requested_on (datetime.datetime):  Example: 2021-03-17T07:58:39.781Z.
        completed_on (datetime.datetime):  Example: 2021-03-17T07:58:39.781Z.
        status (DeleteStatusDataV2Status):  Example: success.
        response_code (float):  Example: 200.
        validation (Union[Unset, Validation]):
        delete_communication_id (Union[Unset, str]):
    """

    service_name: DeleteStatusDataV2ServiceName
    data_type: str
    requested_on: datetime.datetime
    completed_on: datetime.datetime
    status: DeleteStatusDataV2Status
    response_code: float
    validation: Union[Unset, "Validation"] = UNSET
    delete_communication_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_name: str = self.service_name

        data_type = self.data_type

        requested_on = self.requested_on.isoformat()

        completed_on = self.completed_on.isoformat()

        status: str = self.status

        response_code = self.response_code

        validation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.to_dict()

        delete_communication_id = self.delete_communication_id

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
            }
        )
        if validation is not UNSET:
            field_dict["validation"] = validation
        if delete_communication_id is not UNSET:
            field_dict["deleteCommunicationId"] = delete_communication_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validation import Validation

        d = src_dict.copy()
        service_name = check_delete_status_data_v2_service_name(d.pop("serviceName"))

        data_type = d.pop("dataType")

        requested_on = isoparse(d.pop("requestedOn"))

        completed_on = isoparse(d.pop("completedOn"))

        status = check_delete_status_data_v2_status(d.pop("status"))

        response_code = d.pop("responseCode")

        _validation = d.pop("validation", UNSET)
        validation: Union[Unset, Validation]
        if isinstance(_validation, Unset):
            validation = UNSET
        else:
            validation = Validation.from_dict(_validation)

        delete_communication_id = d.pop("deleteCommunicationId", UNSET)

        delete_status_data_v2 = cls(
            service_name=service_name,
            data_type=data_type,
            requested_on=requested_on,
            completed_on=completed_on,
            status=status,
            response_code=response_code,
            validation=validation,
            delete_communication_id=delete_communication_id,
        )

        delete_status_data_v2.additional_properties = d
        return delete_status_data_v2

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
