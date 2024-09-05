import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.push_tracking_categories_response_v2_dto_service_name import (
    PushTrackingCategoriesResponseV2DtoServiceName,
    check_push_tracking_categories_response_v2_dto_service_name,
)
from ..models.push_tracking_categories_response_v2_dto_status import (
    PushTrackingCategoriesResponseV2DtoStatus,
    check_push_tracking_categories_response_v2_dto_status,
)

if TYPE_CHECKING:
    from ..models.push_tracking_categories_v2 import PushTrackingCategoriesV2


T = TypeVar("T", bound="PushTrackingCategoriesResponseV2Dto")


@_attrs_define
class PushTrackingCategoriesResponseV2Dto:
    """
    Attributes:
        push_communication_id (str):  Example: 60473b57f0cdd1683ca71f60.
        requested_on (datetime.datetime):  Example: 2021-03-09T08:15:22.035Z.
        status (PushTrackingCategoriesResponseV2DtoStatus):  Example: pending.
        business_name (str):  Example: Railz.
        service_name (PushTrackingCategoriesResponseV2DtoServiceName):  Example: quickbooks.
        data (PushTrackingCategoriesV2):
    """

    push_communication_id: str
    requested_on: datetime.datetime
    status: PushTrackingCategoriesResponseV2DtoStatus
    business_name: str
    service_name: PushTrackingCategoriesResponseV2DtoServiceName
    data: "PushTrackingCategoriesV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        push_communication_id = self.push_communication_id

        requested_on = self.requested_on.isoformat()

        status: str = self.status

        business_name = self.business_name

        service_name: str = self.service_name

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pushCommunicationId": push_communication_id,
                "requestedOn": requested_on,
                "status": status,
                "businessName": business_name,
                "serviceName": service_name,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_tracking_categories_v2 import PushTrackingCategoriesV2

        d = src_dict.copy()
        push_communication_id = d.pop("pushCommunicationId")

        requested_on = isoparse(d.pop("requestedOn"))

        status = check_push_tracking_categories_response_v2_dto_status(d.pop("status"))

        business_name = d.pop("businessName")

        service_name = check_push_tracking_categories_response_v2_dto_service_name(d.pop("serviceName"))

        data = PushTrackingCategoriesV2.from_dict(d.pop("data"))

        push_tracking_categories_response_v2_dto = cls(
            push_communication_id=push_communication_id,
            requested_on=requested_on,
            status=status,
            business_name=business_name,
            service_name=service_name,
            data=data,
        )

        push_tracking_categories_response_v2_dto.additional_properties = d
        return push_tracking_categories_response_v2_dto

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
