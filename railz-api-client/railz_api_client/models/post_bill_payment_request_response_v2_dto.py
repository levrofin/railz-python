import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_bill_payment_request_response_v2_dto_service_name import (
    PostBillPaymentRequestResponseV2DtoServiceName,
    check_post_bill_payment_request_response_v2_dto_service_name,
)
from ..models.post_bill_payment_request_response_v2_dto_status import (
    PostBillPaymentRequestResponseV2DtoStatus,
    check_post_bill_payment_request_response_v2_dto_status,
)

if TYPE_CHECKING:
    from ..models.post_bill_payment_request_v2 import PostBillPaymentRequestV2


T = TypeVar("T", bound="PostBillPaymentRequestResponseV2Dto")


@_attrs_define
class PostBillPaymentRequestResponseV2Dto:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (str):  Example: Railz.
        service_name (PostBillPaymentRequestResponseV2DtoServiceName):  Example: xero.
        push_communication_id (str):  Example: 60473b57f0cdd1683ca71f60.
        requested_on (datetime.datetime):  Example: 2021-03-09T08:15:22.035Z.
        status (PostBillPaymentRequestResponseV2DtoStatus):  Example: pending.
        data (PostBillPaymentRequestV2):
    """

    connection_uuid: str
    business_name: str
    service_name: PostBillPaymentRequestResponseV2DtoServiceName
    push_communication_id: str
    requested_on: datetime.datetime
    status: PostBillPaymentRequestResponseV2DtoStatus
    data: "PostBillPaymentRequestV2"
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
        from ..models.post_bill_payment_request_v2 import PostBillPaymentRequestV2

        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName")

        service_name = check_post_bill_payment_request_response_v2_dto_service_name(d.pop("serviceName"))

        push_communication_id = d.pop("pushCommunicationId")

        requested_on = isoparse(d.pop("requestedOn"))

        status = check_post_bill_payment_request_response_v2_dto_status(d.pop("status"))

        data = PostBillPaymentRequestV2.from_dict(d.pop("data"))

        post_bill_payment_request_response_v2_dto = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
            push_communication_id=push_communication_id,
            requested_on=requested_on,
            status=status,
            data=data,
        )

        post_bill_payment_request_response_v2_dto.additional_properties = d
        return post_bill_payment_request_response_v2_dto

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