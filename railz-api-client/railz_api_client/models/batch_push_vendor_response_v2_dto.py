from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_push_vendor_response_v2_dto_service_name import (
    BatchPushVendorResponseV2DtoServiceName,
    check_batch_push_vendor_response_v2_dto_service_name,
)

if TYPE_CHECKING:
    from ..models.push_vendor_individual_response_v2_dto import PushVendorIndividualResponseV2Dto


T = TypeVar("T", bound="BatchPushVendorResponseV2Dto")


@_attrs_define
class BatchPushVendorResponseV2Dto:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (str):  Example: Railz.
        service_name (BatchPushVendorResponseV2DtoServiceName):  Example: xero.
        batch_id (str):  Example: 60473b57f0cdd1683ca71f60.
        batch (List['PushVendorIndividualResponseV2Dto']):
    """

    connection_uuid: str
    business_name: str
    service_name: BatchPushVendorResponseV2DtoServiceName
    batch_id: str
    batch: List["PushVendorIndividualResponseV2Dto"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        business_name = self.business_name

        service_name: str = self.service_name

        batch_id = self.batch_id

        batch = []
        for batch_item_data in self.batch:
            batch_item = batch_item_data.to_dict()
            batch.append(batch_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "businessName": business_name,
                "serviceName": service_name,
                "batchId": batch_id,
                "batch": batch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_vendor_individual_response_v2_dto import PushVendorIndividualResponseV2Dto

        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName")

        service_name = check_batch_push_vendor_response_v2_dto_service_name(d.pop("serviceName"))

        batch_id = d.pop("batchId")

        batch = []
        _batch = d.pop("batch")
        for batch_item_data in _batch:
            batch_item = PushVendorIndividualResponseV2Dto.from_dict(batch_item_data)

            batch.append(batch_item)

        batch_push_vendor_response_v2_dto = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
            batch_id=batch_id,
            batch=batch,
        )

        batch_push_vendor_response_v2_dto.additional_properties = d
        return batch_push_vendor_response_v2_dto

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
