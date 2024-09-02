import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialBenchmarkingsReportMetaData")


@_attrs_define
class FinancialBenchmarkingsReportMetaData:
    """
    Attributes:
        number_of_businesses (float):  Example: 282.
        created_at (datetime.datetime):  Example: 2020-11-30T01:02:03Z.
        industry_code (Union[Unset, str]):  Example: 54.
        time_in_business (Union[Unset, int]):  Example: 5.
        region (Union[Unset, str]):  Example: CA.
    """

    number_of_businesses: float
    created_at: datetime.datetime
    industry_code: Union[Unset, str] = UNSET
    time_in_business: Union[Unset, int] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number_of_businesses = self.number_of_businesses

        created_at = self.created_at.isoformat()

        industry_code = self.industry_code

        time_in_business = self.time_in_business

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numberOfBusinesses": number_of_businesses,
                "createdAt": created_at,
            }
        )
        if industry_code is not UNSET:
            field_dict["industryCode"] = industry_code
        if time_in_business is not UNSET:
            field_dict["timeInBusiness"] = time_in_business
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number_of_businesses = d.pop("numberOfBusinesses")

        created_at = isoparse(d.pop("createdAt"))

        industry_code = d.pop("industryCode", UNSET)

        time_in_business = d.pop("timeInBusiness", UNSET)

        region = d.pop("region", UNSET)

        financial_benchmarkings_report_meta_data = cls(
            number_of_businesses=number_of_businesses,
            created_at=created_at,
            industry_code=industry_code,
            time_in_business=time_in_business,
            region=region,
        )

        financial_benchmarkings_report_meta_data.additional_properties = d
        return financial_benchmarkings_report_meta_data

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
