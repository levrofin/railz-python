from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_bank_transaction_response_dto_service_name import UpdateBankTransactionResponseDtoServiceName

if TYPE_CHECKING:
    from ..models.update_bank_transaction import UpdateBankTransaction


T = TypeVar("T", bound="UpdateBankTransactionResponseDto")


@_attrs_define
class UpdateBankTransactionResponseDto:
    """
    Attributes:
        connection_uuid (str):  Example: CON-396d5daa-26b2-4979-89b6-cafb2c298155.
        business_name (str):  Example: Railz.
        service_name (UpdateBankTransactionResponseDtoServiceName):  Example: xero.
        data (UpdateBankTransaction):
    """

    connection_uuid: str
    business_name: str
    service_name: UpdateBankTransactionResponseDtoServiceName
    data: "UpdateBankTransaction"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        business_name = self.business_name

        service_name = self.service_name

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "businessName": business_name,
                "serviceName": service_name,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_bank_transaction import UpdateBankTransaction

        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        business_name = d.pop("businessName")

        service_name = d.pop("serviceName")

        data = UpdateBankTransaction.from_dict(d.pop("data"))

        update_bank_transaction_response_dto = cls(
            connection_uuid=connection_uuid,
            business_name=business_name,
            service_name=service_name,
            data=data,
        )

        update_bank_transaction_response_dto.additional_properties = d
        return update_bank_transaction_response_dto

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
