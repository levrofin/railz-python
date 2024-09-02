import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_payment_method_data_status import GetPaymentMethodDataStatus
from ..models.get_payment_method_data_type import GetPaymentMethodDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPaymentMethodData")


@_attrs_define
class GetPaymentMethodData:
    """
    Attributes:
        id (str):  Example: 1.
        name (str):  Example: Harmonized sales tax.
        type (GetPaymentMethodDataType):  Example: creditCard.
        status (Union[Unset, GetPaymentMethodDataStatus]):
        source_modified_date (Union[Unset, datetime.datetime]):  Example: 2021-03-10T11:26:06.619Z.
    """

    id: str
    name: str
    type: GetPaymentMethodDataType
    status: Union[Unset, GetPaymentMethodDataStatus] = UNSET
    source_modified_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        type = self.type

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        source_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = d.pop("type")

        _status = d.pop("status", UNSET)
        status: Union[Unset, GetPaymentMethodDataStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = _status

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        get_payment_method_data = cls(
            id=id,
            name=name,
            type=type,
            status=status,
            source_modified_date=source_modified_date,
        )

        get_payment_method_data.additional_properties = d
        return get_payment_method_data

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
