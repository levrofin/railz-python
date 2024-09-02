from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report import Report


T = TypeVar("T", bound="DataType")


@_attrs_define
class DataType:
    """
    Attributes:
        data_type (str):  Example: BalanceSheet.
        reports (List['Report']):
        last_sync_date (Union[Unset, str]):  Example: 2021-04-01T00:31:00Z.
        last_updated_date (Union[Unset, str]):  Example: 2021-04-01T00:31:00Z.
    """

    data_type: str
    reports: List["Report"]
    last_sync_date: Union[Unset, str] = UNSET
    last_updated_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_type = self.data_type

        reports = []
        for reports_item_data in self.reports:
            reports_item = reports_item_data.to_dict()
            reports.append(reports_item)

        last_sync_date = self.last_sync_date

        last_updated_date = self.last_updated_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataType": data_type,
                "reports": reports,
            }
        )
        if last_sync_date is not UNSET:
            field_dict["lastSyncDate"] = last_sync_date
        if last_updated_date is not UNSET:
            field_dict["lastUpdatedDate"] = last_updated_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report import Report

        d = src_dict.copy()
        data_type = d.pop("dataType")

        reports = []
        _reports = d.pop("reports")
        for reports_item_data in _reports:
            reports_item = Report.from_dict(reports_item_data)

            reports.append(reports_item)

        last_sync_date = d.pop("lastSyncDate", UNSET)

        last_updated_date = d.pop("lastUpdatedDate", UNSET)

        data_type = cls(
            data_type=data_type,
            reports=reports,
            last_sync_date=last_sync_date,
            last_updated_date=last_updated_date,
        )

        data_type.additional_properties = d
        return data_type

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
