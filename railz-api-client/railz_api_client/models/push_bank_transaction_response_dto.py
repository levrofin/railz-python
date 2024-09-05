from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_bank_transaction_response_dto_service_name import (
    PushBankTransactionResponseDtoServiceName,
    check_push_bank_transaction_response_dto_service_name,
)

if TYPE_CHECKING:
    from ..models.push_bank_transaction import PushBankTransaction


T = TypeVar("T", bound="PushBankTransactionResponseDto")


@_attrs_define
class PushBankTransactionResponseDto:
    """
    Attributes:
        business_name (str):  Example: Railz.
        service_name (PushBankTransactionResponseDtoServiceName):  Example: xero.
        data (PushBankTransaction):
    """

    business_name: str
    service_name: PushBankTransactionResponseDtoServiceName
    data: "PushBankTransaction"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_name = self.business_name

        service_name: str = self.service_name

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "businessName": business_name,
                "serviceName": service_name,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.push_bank_transaction import PushBankTransaction

        d = src_dict.copy()
        business_name = d.pop("businessName")

        service_name = check_push_bank_transaction_response_dto_service_name(d.pop("serviceName"))

        data = PushBankTransaction.from_dict(d.pop("data"))

        push_bank_transaction_response_dto = cls(
            business_name=business_name,
            service_name=service_name,
            data=data,
        )

        push_bank_transaction_response_dto.additional_properties = d
        return push_bank_transaction_response_dto

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
