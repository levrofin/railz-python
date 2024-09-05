import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.push_chart_of_account_v2_response_dto_service_name import (
    PushChartOfAccountV2ResponseDtoServiceName,
    check_push_chart_of_account_v2_response_dto_service_name,
)
from ..models.push_chart_of_account_v2_response_dto_status import (
    PushChartOfAccountV2ResponseDtoStatus,
    check_push_chart_of_account_v2_response_dto_status,
)

if TYPE_CHECKING:
    from ..models.push_chart_of_account_v2 import PushChartOfAccountV2


T = TypeVar("T", bound="PushChartOfAccountV2ResponseDto")


@_attrs_define
class PushChartOfAccountV2ResponseDto:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (str):  Example: Railz.
        service_name (PushChartOfAccountV2ResponseDtoServiceName):  Example: xero.
        push_communication_id (str):  Example: 60473b57f0cdd1683ca71f60.
        requested_on (datetime.datetime):  Example: 2021-03-09T08:15:22.035Z.
        status (PushChartOfAccountV2ResponseDtoStatus):  Example: pending.
        data (PushChartOfAccountV2):
    """

    connection_uuid: str
    business_name: str
    service_name: PushChartOfAccountV2ResponseDtoServiceName
    push_communication_id: str
    requested_on: datetime.datetime
    status: PushChartOfAccountV2ResponseDtoStatus
    data: "PushChartOfAccountV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        business_name = self.business_name

        service_name: str = self.service_name

        push_communication_id = self.push_communication_id

        requested_on = self.requested_on.isoformat()

        status: str = self.status

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "businessName": business_name,
                "serviceName": service_name,
                "pushCommunicationId": push_communication_id,
                "requestedOn": requested_on,
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_chart_of_account_v2 import PushChartOfAccountV2

        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName")

        service_name = check_push_chart_of_account_v2_response_dto_service_name(d.pop("serviceName"))

        push_communication_id = d.pop("pushCommunicationId")

        requested_on = isoparse(d.pop("requestedOn"))

        status = check_push_chart_of_account_v2_response_dto_status(d.pop("status"))

        data = PushChartOfAccountV2.from_dict(d.pop("data"))

        push_chart_of_account_v2_response_dto = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
            push_communication_id=push_communication_id,
            requested_on=requested_on,
            status=status,
            data=data,
        )

        push_chart_of_account_v2_response_dto.additional_properties = d
        return push_chart_of_account_v2_response_dto

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
