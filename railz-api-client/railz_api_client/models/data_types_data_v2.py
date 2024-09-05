from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_types_data_v2_accounting_method import (
    DataTypesDataV2AccountingMethod,
    check_data_types_data_v2_accounting_method,
)
from ..models.data_types_data_v2_action_item import DataTypesDataV2ActionItem, check_data_types_data_v2_action_item
from ..models.data_types_data_v2_name import DataTypesDataV2Name, check_data_types_data_v2_name
from ..models.data_types_data_v2_report_type import DataTypesDataV2ReportType, check_data_types_data_v2_report_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataTypesDataV2")


@_attrs_define
class DataTypesDataV2:
    """
    Attributes:
        name (DataTypesDataV2Name):
        action (List[DataTypesDataV2ActionItem]):
        report_type (DataTypesDataV2ReportType):
        description (Union[Unset, str]):  Example: AP Aging.
        accounting_method (Union[Unset, DataTypesDataV2AccountingMethod]):
    """

    name: DataTypesDataV2Name
    action: List[DataTypesDataV2ActionItem]
    report_type: DataTypesDataV2ReportType
    description: Union[Unset, str] = UNSET
    accounting_method: Union[Unset, DataTypesDataV2AccountingMethod] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: str = self.name

        action = []
        for action_item_data in self.action:
            action_item: str = action_item_data
            action.append(action_item)

        report_type: str = self.report_type

        description = self.description

        accounting_method: Union[Unset, str] = UNSET
        if not isinstance(self.accounting_method, Unset):
            accounting_method = self.accounting_method

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "action": action,
                "reportType": report_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if accounting_method is not UNSET:
            field_dict["accountingMethod"] = accounting_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = check_data_types_data_v2_name(d.pop("name"))

        action = []
        _action = d.pop("action")
        for action_item_data in _action:
            action_item = check_data_types_data_v2_action_item(action_item_data)

            action.append(action_item)

        report_type = check_data_types_data_v2_report_type(d.pop("reportType"))

        description = d.pop("description", UNSET)

        _accounting_method = d.pop("accountingMethod", UNSET)
        accounting_method: Union[Unset, DataTypesDataV2AccountingMethod]
        if isinstance(_accounting_method, Unset):
            accounting_method = UNSET
        else:
            accounting_method = check_data_types_data_v2_accounting_method(_accounting_method)

        data_types_data_v2 = cls(
            name=name,
            action=action,
            report_type=report_type,
            description=description,
            accounting_method=accounting_method,
        )

        data_types_data_v2.additional_properties = d
        return data_types_data_v2

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
